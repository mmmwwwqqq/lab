import random

class Pupa(object):
    def __init__(self):
        self.Pupa_wallet = 0

    def do_work(self, spisok1, spisok2):
        Pupa_work = []
        count = max(len(spisok1), len(spisok2))
        for i in range(count):
            Pupa_work.append(spisok1[i] + spisok2[i])
        print('Pupa_work:', Pupa_work)
        return Pupa_work

    def take_salary(self, salary):
        self.Pupa_wallet += salary

class Lupa(object):
    def __init__(self):
        self.Lupa_wallet = 0

    def do_work(self, spisok1, spisok2):
        Lupa_work = []
        count = max(len(spisok1), len(spisok2))
        for i in range(count):
            Lupa_work.append(spisok1[i] - spisok2[i])
        print('Lupa_work:', Lupa_work)
        return Lupa_work

    def take_salary(self, salary):
        self.Lupa_wallet += salary

class Accountant(object):
    def __init__(self):
        self.salary = random.randint(1, 1000)

    def give_salary(self, pupa, lupa):
        pupa.take_salary(self.salary)
        lupa.take_salary(self.salary)

pupa = Pupa()
lupa = Lupa()
accountant = Accountant()

spisok1 = [1, 2, 3, 4, 5, 6]
spisok2 = [1, 2, 3, 4, 5, 6]

pupa.do_work(spisok1, spisok2)
lupa.do_work(spisok1, spisok2)

accountant.give_salary(pupa, lupa)

print('Pupa wallet:', pupa.Pupa_wallet)
print('Lupa wallet:', lupa.Lupa_wallet)
