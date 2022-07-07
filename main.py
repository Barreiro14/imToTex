from valToTex import ValToTex
from recognizer import Recognize
from output import init, writeIn, finish

def main():
	init()
	writeIn(ValToTex(Recognize("test.JPG")))
	finish()
	print("hasta ahora todo jevi")
	#main function

if __name__ == '__main__':
	main()
