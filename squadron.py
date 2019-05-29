from enemy import Enemy

class Squadron():
    def __init__(self, left_game_wall, top_game_wall, row_count, col_count, speed, enemy_img):
        self.speed = speed
        self.direction = 1
        self.create_squadron_enemies(left_game_wall, top_game_wall, row_count, col_count, enemy_img)
    def create_squadron_enemies(self,left_game_wall, top_game_wall, row_count, col_count, enemy_img):
        self.enemies = []
        for y in range(0, row_count):
            for x in range(0, col_count):
                xcor = left_game_wall + x * enemy_img.get_width() 
                ycor = top_game_wall + y * enemy_img.get_height()
                self.enemies.append(Enemy(xcor, ycor, enemy_img, self.speed))
    def show(self, game_display,):
        for enemy in self.enemies:
            enemy.show(game_display)
    def will_hit_wall(self, left_game_wall, right_game_wall):
        will_hit_wall = False
        for enemy in self.enemies:
            new_xcor = enemy.xcor + self.direction * enemy.speed
            if new_xcor < left_game_wall or new_xcor + enemy.image.get_width() > right_game_wall:
                return True
        return False
    def move_squadron_vertically(self, amount):
        for enemy in self.enemies:
            enemy.move_vertically(amount)
    def move_squadron_horizontally(self):
        for enemy in self.enemies:
            enemy.move_vertically(self.direction)

    def move(self, left_game_wall, right_game_wall):

        if self.will_hit_wall(left_game_wall, right_game_wall):
            self.direction *= -1
            for enemy in self.enemies:
                enemy.move_vertically(10)

        for enemy in self.enemies:
            enemy.move_horizontally(self.direction)
