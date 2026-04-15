
class ScoreManager:

    def __init__(self):
        self.health = 3
        self.score = 0

    def increment(self, amount=1):
        self.score += amount
    
    def decrement(self, amount=1):
        self.score -= amount

    def damage(self):
        self.health -= 1
