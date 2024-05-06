import pygame
import random

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption('AimTraining')  # Ustawienie tytułu okna

# Kolory
BackgroundColor = (204, 102, 0)
CircleColor = (195, 0, 0)
BlackColor = (0, 0, 0)

# Promień okręgu
radius = 20

# Czcionka do wyświetlania tekstu
font = pygame.font.Font(None, 36)

def show_countdown(number):
    screen.fill(BackgroundColor)
    countdown_text = font.render(str(number), True, BlackColor)
    text_rect = countdown_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(countdown_text, text_rect)
    pygame.display.flip()
    pygame.time.delay(1000)  # Opóźnienie na 1 sekundę (1000 milisekund)

# Wyświetlanie odliczania na początku
for i in range(3, 0, -1):
    show_countdown(i)
show_countdown('Go!')

# Początkowa pozycja okręgu
x = random.randint(radius, screen_width - radius)
y = random.randint(radius, screen_height - radius)

# Licznik kliknięć i czasu
click_count = 0
last_click_time = pygame.time.get_ticks()
time_between_clicks = []

# Pętla gry
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.size
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if (x - mouse_x) ** 2 + (y - mouse_y) ** 2 <= radius ** 2:
                x = random.randint(radius, screen_width - radius)
                y = random.randint(radius, screen_height - radius)
                click_count += 1
                current_time = pygame.time.get_ticks()
                time_since_last_click = current_time - last_click_time
                last_click_time = current_time
                time_between_clicks.append(time_since_last_click)
                average_time = sum(time_between_clicks) / len(time_between_clicks) if time_between_clicks else 0

    # Aktualizacja ekranu
    screen.fill(BackgroundColor)
    pygame.draw.line(screen, BlackColor, (screen_width // 2, 0), (screen_width // 2, screen_height), 3)
    pygame.draw.line(screen, BlackColor, (0, screen_height // 2), (screen_width, screen_height // 2), 3)
    pygame.draw.circle(screen, CircleColor, (x, y), radius)
    count_text = font.render(f'Clicks: {click_count}', True, BlackColor)
    screen.blit(count_text, (10, 10))
    if click_count > 0:  # Display time info only if there are clicks
        time_text = font.render(f'Last Time: {time_since_last_click} ms', True, BlackColor)
        screen.blit(time_text, (screen_width - 300, 10))
        average_text = font.render(f'Avg Time: {average_time:.2f} ms', True, BlackColor)
        screen.blit(average_text, (screen_width - 300, 50))
    pygame.display.flip()

pygame.quit()
