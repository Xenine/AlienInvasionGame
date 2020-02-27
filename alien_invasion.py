import sys
import os
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf


def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    
def run_game():
	# Инициализирует Pygame, settings и объект экрана
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	# Создание корабля, группы для хранения пуль и пришельцев
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	stats = GameStats(ai_settings)

	gf.create_fleet(ai_settings, screen, ship, aliens)

	# Запуск основного цикла игры 
	while True:
		# Отследивание событий клавиатуры и мыши
		gf.check_events(ai_settings, screen, ship, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()