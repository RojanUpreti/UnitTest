import random
def run_guess(guess,answer):
	if 0<guess<11:
			if guess==answer:
				print('Rojan is a genius')
				return True
	else:
		print('Hey Rojan, I said 1-10')

if __name__=='__main__':
	answer=random.randint(1,10)
	while True:
		try:
			guess=int(input('Guess a number 1-10:'))
			if(run_guess(guess,answer)):
				break
		except ValueError:
			print('please enter a number')
			continue

	

