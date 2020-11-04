import random




class Randombot:
    
	def __init__(self,random_num_list = []):
        self._random_num_list = random_num_list
        self._strikes = 0
        self._balls = 0

	def init_random_num_list(self):
        self.random_num_list = [str(x) for x in random.sample(range(0,10),4)]
	
	def sb_count_calculator(self,random_num_list,input_num_list):
		

		for n,nvalue in enumerate(random_num_list):
			for m,mvalue in enumerate(input_num_list):
    				if nvalue == mvalue:
				        if n == m:
					        self.strikes += 1
                        else:
		                    self.balls +=1	

	#property는 항상 setter 함수 위에 있어야함(순서중요!!)
	@property
	def random_num_list(self):
            return self._random_num_list	
	
	@random_num_list.setter
	def random_num_list(self,random_num_list):
            self._random_num_list = random_num_list

	@property
	def strikes(self):
            return self._strikes

	@strikes.setter
	def strikes(self, strikes):
		    self._strikes = strikes
	
    @property
    def balls(self):
            return self._balls

	
    @balls.setter
    def balls(self, balls):
            self._balls = balls



bot1 = Randombot()
bot1.init_random_num_list()
bot1.random_num_list
print(bot1.random_num_list)	