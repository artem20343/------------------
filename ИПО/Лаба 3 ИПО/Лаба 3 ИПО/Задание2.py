class Stars:
    def __init__(self, n):
        self.qty = '*' * n
        def __add__(self, n):
            return self.qty + '*' * n
a=Stars(3)
b = a + 5
print(b)