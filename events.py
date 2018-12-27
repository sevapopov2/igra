import random
class randomevent:
    @staticmethod
    def instrumentbreak():
        if random.random() > 0.9:
            return True

        else:
            return False