import random as r


class MontyHall:
    def __init__(self, doors=3, prizes=1, limit=2):
        self.doors = [x for x in range(doors)]

        self.prizes = []
        while len(self.prizes) < prizes:
            tmp = self.pick_door()
            if tmp not in self.prizes:
                self.prizes.append(tmp)

        self.limit = limit

    def pick_door(self):
        return r.choice(self.doors)

    def select_door(self):
        self.select = self.pick_door()

    def remove_doors(self):
        while(len(self.doors) > self.limit):
            rmv = self.pick_door()
            tmp = [x for x in self.doors]
            tmp.remove(rmv)
            if(rmv != self.select and any(x in self.prizes for x in tmp)):
                self.doors.remove(rmv)

    def switch_door(self):
        old = self.select
        while(old == self.select):
            self.select = self.pick_door()

    def check_win(self):
        return self.select in self.prizes

    def start(self, switch=False):
        self.select_door()
        self.remove_doors()
        if(switch):
            self.switch_door()
        return self.check_win()


class Simulation:
    def __init__(self, doors=3, trials=10**5, prizes=1, limit=2):
        self.doors = doors
        self.trials = trials
        self.prizes = prizes
        self.limit = limit

    def start(self, switch=False):
        wins = 0
        for x in range(self.trials):
            m = MontyHall(self.doors, self.prizes, self.limit)
            if(m.start(switch)):
                wins += 1
        return self._print(switch, wins)

    def _print(self, switch, wins):
        out_format = "{:15s}: {:3.2f}℅ with {} wins of {} trials"

        ss = "Switching" if(switch) else "Not Switching"
        perc = wins / self.trials * 100
        return out_format.format(ss, perc, wins, self.trials)


if __name__ == "__main__":
    d = 10  # int(input())
    t = 10**5  # int(input())
    p = 1
    l = 5

    # s = Simulation()  # default arguments value
    s = Simulation(doors=d, trials=t, prizes=p, limit=l)
    print(s.start(switch=True))
    print(s.start(switch=False))
