class Settings():

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Параметры снаряда
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Настройки пришельцев
        self.alien_speed = 0.8
        self.fleet_drop_speed = 15
        # fleet_direction = 1  Вправо, -1 Влево
        self.fleet_direction = 1
