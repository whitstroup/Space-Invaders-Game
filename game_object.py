class GameObject():
    def __init__(self, image, xcor, ycor, initial_direction, initial_speed):
        self.image = image
        self.xcor = xcor
        self.ycor = ycor
        self.direction = initial_direction
        self.speed = initial_speed
        self.is_alive = True
    def show(self, game_display):
        game_display.blit(self.image, (self.xcor, self.ycor))
    def collides_with(self, foreign_object):
        if  self.xcor + self.image.get_width() > foreign_object.xcor and \
            self.xcor < foreign_object.xcor + foreign_object.image.get_width() and \
            self.ycor + self.image.get_height() > foreign_object.ycor and \
            self.ycor < foreign_object.ycor + foreign_object.image.get_height():
            return True
        else:
            return False

    