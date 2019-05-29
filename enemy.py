from game_object import GameObject

class Enemy(GameObject):
    def __init__(self, xcor, ycor, enemy_img, speed):
        super(). __init__(enemy_img, xcor, ycor , 1, speed)
    def move_horizontally(self, direction):
        self.xcor += self.speed * direction
    def move_vertically(self, amount):
        self.ycor += amount
    
