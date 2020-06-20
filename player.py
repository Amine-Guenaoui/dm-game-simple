
class Player:

    def __init__(self, green_points, red_points, level):
        self.green_points = green_points  # guessed right points
        self.red_points = red_points  # guessed wrong points
        self.level = level  # his grade or level

        print("player score initialized")

    def get_score():
        return green_points - red_points

    def promote():
        level += 1

    def get_level():
        return level

    def add_greenpoints(n):
        self.green_points += n

    def add_redpoints(n):
        self.red_points += n
