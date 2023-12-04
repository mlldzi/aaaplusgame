import math


class Bullet:
    def __init__(self, x, y, speed, radius):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius

    def move(self, player_x, player_y):
        dx = player_x - self.x
        dy = player_y - self.y
        distance_to_player = math.sqrt(dx ** 2 + dy ** 2)
        if distance_to_player > 1:
            direction_x = dx / distance_to_player
            direction_y = dy / distance_to_player
            if distance_to_player > self.speed:
                self.x += direction_x * self.speed
                self.y += direction_y * self.speed
            else:
                self.x = player_x
                self.y = player_y