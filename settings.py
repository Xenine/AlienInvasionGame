class Settings():
	""" Класс для хранения настроек """

	def __init__(self):
		""" Инициализирует настройки игры """
		# Параметры экрана
		self.screen_width = 1200 
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Настройки корабля 
		self.ship_speed_factor = 0.6
		self.ship_limit = 3

		# Настройка пришельцев
		self.alien_speed_factor = 0.5
		self.fleet_drop_speed = 10
		self.fleet_direction = 1

		# Настройка пуль
		self.bullet_speed_factor = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 4