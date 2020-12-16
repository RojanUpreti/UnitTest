import unittest
import script


class TestGame(unittest.TestCase):
	def test_input(self):
		answer=5
		guess=5
		result=script.run_guess(answer,guess)
		self.assertTrue(result)


	def test_input_wrong_guess(self):
		answer=2
		guess=5
		result=script.run_guess(answer,guess)
		self.assertFalse(result)


	def test_input_wrong_number(self):
		result=script.run_guess(5,12)
		self.assertFalse(result)

if __name__=='__main__':
	unittest.main()