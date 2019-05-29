from game_object import GameObject
from bullet import Bullet

class Player(GameObject):
    def __init__(self, left_game_wall,right_game_wall, bottom_game_wall, player_img):
        xcor = (right_game_wall + left_game_wall) / 2 - player_img.get_width() / 2
        ycor = bottom_game_wall - player_img.get_height()
        super().__init__(player_img, xcor, ycor, 0, 5)
        self.bullets_fired = []
        self.score = 0
    def show(self, left_game_wall, right_game_wall, game_display):
        new_xcor = self.xcor + self.speed * self.direction
        if new_xcor < left_game_wall:
            self.xcor = left_game_wall
        elif new_xcor > right_game_wall - self.image.get_width():
            self.xcor = right_game_wall - self.image.get_width()
        else:
            self.xcor = new_xcor
        super().show(game_display)
    def move_left(self):
        self.direction = - 1
    def move_right(self):
        self.direction = 1
    def stop_moving(self):
        self.direction = 0
    def shoot(self, bullet_img, shooting_sound):
        shooting_sound.play()
        new_bullet = Bullet(self.xcor + self.image.get_width() / 2, self.ycor, bullet_img)
        self.bullets_fired.append(new_bullet)
    def remove_missed_bullets(self, top_game_wall):
        for bullet in self.bullets_fired:
            if bullet.ycor < top_game_wall:
                self.bullets_fired.remove(bullet)
    def kill_enemies_colliding_with_bullets(self, squadron, game_display, kill_enemy_sound):
        for bullet in self.bullets_fired:
            for enemy in squadron.enemies:
                if bullet.collides_with(enemy):
                 kill_enemy_sound.play()
                 squadron.enemies.remove(enemy)
                 bullet.is_alive = False
                 self.score += 10
                 break
            if bullet.is_alive == False:
                self.bullets_fired.remove(bullet)
    def kill_player_if_invaded(self, squadron, bottom_game_wall):
        for enemy in squadron.enemies:
            if enemy.collides_with(self) or enemy.ycor > bottom_game_wall:
                self.is_alive = False

