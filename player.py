
class Player:

    def __init__(self, green_points, red_points, level):
        self.green_points = green_points  # guessed right points
        self.red_points = red_points  # guessed wrong points
        self.level = level  # his grade or level

        print("player score initialized")

    def get_score(self):
        return self.green_points - self.red_points

    def promote(self):
        if self.green_points - self.red_points > 0:
            self.level += 1
            return True
        return False

    def get_level(self):
        return self.level

    def add_greenpoints(self, n):
        self.green_points += n

    def add_redpoints(self, n):
        self.red_points += n

    def get_greenPoints(self):
        return self.green_points

    def get_redPoints(self):
        return self.red_points
