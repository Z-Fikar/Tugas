import random as r

class MontyHall:
	def __init__(self, doors=3):
		self.doors = [x for x in range(doors)]
		self.prize = self.pick_door()
	
	def pick_door(self):
		return r.choice(self.doors)
		
	def select_door(self):
		self.select = self.pick_door()

	def remove_doors(self):
		while(len(self.doors)>2):
			rmv = self.pick_door()
			if(rmv != self.select and rmv != self.prize):
				self.doors.remove(rmv)
				
	def switch_door(self):
		old = self.select
		while(old==self.select):
			self.select = self.pick_door()

	def check_win(self):
		return self.select==self.prize
	
	def start(self, switch=False):
		self.select_door()
		self.remove_doors()
		if(switch):
			self.switch_door()
		return self.check_win()


class Simulation:
	def __init__(self, doors=3, trials=10**5):
		self.doors = doors
		self.trials = trials
		
	def start(self, switch=False):
		wins = 0
		for x in range(self.trials):
			m = MontyHall(self.doors)
			if(m.start(switch)):
				wins += 1
		return self._print(switch, wins)
		
	def _print(self, switch, wins):
		out_format = "{:15s}: {:3.2f}℅ with {} wins of {} trials"
		
		ss = "Switching" if(switch) else "Not Switching"
		perc = wins/self.trials*100
		return out_format.format(ss, perc, wins, self.trials)
		

if __name__ == "__main__":
	d = int(input())
	t = int(input())
	s = Simulation(doors=d, trials=t)
	print(s.start(switch=True))
	print(s.start(switch=False))
