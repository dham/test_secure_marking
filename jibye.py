class Enumerate:
    def __init__(self, n):
        self.list = [i for i in range(n)]
        self.num = n

    def append(self, n):
        self.list += [n]
        self.num += 1

    def show(self):
        print(self.list)


pj = Enumerate(10)
pj.append(67)
pj.show()
