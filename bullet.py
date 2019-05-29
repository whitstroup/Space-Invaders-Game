from game_object import GameObject

class Bullet(GameObject):
    def __init__(self, xcor, ycor, bullet_img):
        super().__init__(bullet_img, xcor - bullet_img.get_width() / 2, ycor, -1, 10)
    def show(self, game_display):
        self.ycor -= self.speed
        super().show(game_display)
    @staticmethod
    def show_all_bullets(game_display, bullets):
        for bullet in bullets:
            bullet.show(game_display)
