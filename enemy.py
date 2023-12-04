import math


class Enemy:
    def __init__(self, x, y, size, speed, center_x, center_y):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.center_x = center_x
        self.center_y = center_y

    def move(self):
        dx = self.center_x - self.x
        dy = self.center_y - self.y
        distance_to_center = math.sqrt(dx ** 2 + dy ** 2)
        if distance_to_center > 1:
            direction_x = dx / distance_to_center
            direction_y = dy / distance_to_center
            self.x += direction_x * self.speed
            self.y += direction_y * self.speed

    def collides_with(self, player_x, player_y, player_size):
        distance = math.sqrt((self.x - player_x) ** 2 + (self.y - player_y) ** 2)
        if distance < (self.size + player_size) / 2:
            return True
        return False
