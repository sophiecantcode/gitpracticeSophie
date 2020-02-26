#Partner 1: Lauren Shareshian
#Partner 2: Sophie Chen
#################
assignment name: github practice 20 points, 2/26/20

from random import randint

def getNRandom(n):
	'''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
    number_list = []
    for i in range(n):
        value = randint(1,10)
        number_list.append(value)
    return number_list

def multiplyRandom(numbers):
	'''takes in a list of n numbers and returns the product of the numbers'''
    pass

def main():
	print(multiplyRandom(getNRandom(10))

if __name__ == "__main__":
	main()
