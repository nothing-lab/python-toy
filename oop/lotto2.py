class Lotto:
    def __init__(self, numbers):
        self.numbers = numbers

    def draw(self):
        return self.numbers

    def __str__(self):
        return str(self.numbers)

# 이렇게만 만들면 될까?
# 검증은?