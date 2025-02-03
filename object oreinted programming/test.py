import Math


class Obj:
    def __init__(self, N, C):
        self.N = N
        self.C = C

    def Info(self):
        print(f"{self.C} {self.N}")

    def A(self):
        pass

    def P(self):
        pass


class C(Obj):
    def __init__(self, N, C, R):
        super().__init__(N, C)
        self.R = R

    def A(self):
        return Math.pi * self.R ** 2

    def P(self):
        return 2 * Math.pi * self.R


class R(Obj):
    def __init__(self, N, C, L, W):
        super().__init__(N, C)
        self.L = L
        self.W = W

    def A(self):
        return self.L * self.W

    def P(self):
        return 2 * (self.L + self.W)


class T(Obj):
    def __init__(self, N, C, S1, S2, S3):
        super().__init__(N, C)
        self.S1 = S1
        self.S2 = S2
        self.S3 = S3

    def A(self):
        ST = (self.S1 + self.S2 + self.S3) / 2
        return (Math.sqrt(ST * (ST - self.S1) * (ST - self.S2) * (ST - self.S3)))

    def P(self):
        return self.S1 + self.S2 + self.S3


c = C("Circle", "Red", 5)
r = R("Rectangle", "Blue", 4, 6)
t = T("Triangle", "Green", 3, 4, 5)

Sh = [c, r, t]

for S in Sh:
    S.Info()
    print(f"A: {S.A():.2f}")
    print(f"P: {S.P():.2f}")
    print()