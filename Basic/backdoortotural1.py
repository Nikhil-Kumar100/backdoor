from threading import *
from time import sleep

class one(Thread):
	def run(self):
		for i in range(500):
			print("class one")
			sleep(1)	


class two(Thread):
	def run(self):
		for i in range(500):
			print("class two")
			sleep(1)

One = one()
Two = two()

One.start()
Two.start()
