# -*- coding: utf-8 -*-

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
            if(rmv != self.select and any(x in tmp for x in self.prizes)):
                self.doors.remove(rmv)

    def switch_door(self):
        old = self.select
        while(old == self.select):
            self.select = self.pick_door()

    def check_win(self):
        return self.select in self.prizes

    def print_verbose(self, key, value):
        v_format = "{:33s} : {}"
        print(v_format.format(key, value))

    def start(self, switch=False, verbose=False):
        self.select_door()

        if verbose:
            self.print_verbose("Doors", self.doors)
            self.print_verbose("Prizes", self.prizes)
            self.print_verbose("Contestant's Selection", self.select)

        self.remove_doors()

        if verbose:
            self.print_verbose("Remaining Doors", self.doors)

        if(switch):
            self.switch_door()
            if verbose:
                self.print_verbose(
                    "Contestant's Switched Selection", self.select)

        if verbose:
            print()

        return self.check_win()


class Simulation:
    def __init__(self, doors=3, trials=10**5, prizes=1, limit=2):
        err1 = "Number of doors must be greater than number of prizes"
        assert doors > prizes, err1

        err2 = "The minimal number of limits is equal to the number of prizes"
        err3 = " and less than number of doors"
        assert limit >= prizes and limit < doors, err2+err3

        self.doors = doors
        self.trials = trials
        self.prizes = prizes
        self.limit = limit

    def start(self, switch=False, verbose=False):
        wins = 0
        for x in range(self.trials):
            m = MontyHall(self.doors, self.prizes, self.limit)
            if(m.start(switch, verbose)):
                wins += 1
        return self._print(switch, wins)

    def _print(self, switch, wins):
        out_format = " {:15s}: {:3.2f}℅ with {} wins of {} trials"

        ss = "Switching" if(switch) else "Not Switching"
        perc = wins / self.trials * 100
        out = out_format.format(ss, perc, wins, self.trials)
        line = "="*(len(out)+1)
        return "\n".join([line, out, line, "\n"])


if __name__ == "__main__":
    number_of_trials = 10000
    number_of_doors = 5
    number_of_prizes = 1
    number_of_limits = 2
    is_verbose = False

    # s = Simulation()  # default arguments value
    s = Simulation(doors=number_of_doors, trials=number_of_trials,
                   prizes=number_of_prizes, limit=number_of_limits)
    res = [s.start(switch=True, verbose=is_verbose),
           s.start(switch=False, verbose=is_verbose)]
    print("\n".join(res))
