class Matrix:
    def __init__(self, a = 1, b = 1, c = 1, d = 0):
        self.a = a # Fn
        self.b = b # Fn-1
        self.c = c # Fn-1
        self.d = d # Fn

    def __mul__(self, other):
        a = self.a * other.a + self.b * other.c
        b = self.a * other.b + self.b * other.d
        c = self.c * other.a + self.d * other.c
        d = self.c * other.b + self.d * other.d
        
        return Matrix(a, b, c, d)
    
    def __pow__(self, n):
        if n == 1:
            return Matrix()

        half = self ** (n // 2)
        return half * half * Matrix() if n % 2 else half * half
    
    def __mod__(self, other):
        return self.a % other
    
print(Matrix() ** int(input()) % 10007)
    