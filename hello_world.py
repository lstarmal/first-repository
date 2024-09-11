def print_hello():
	print("Hello World")

def print_KIT():
	print("Kumoh National Institute of Technology.")

def add(x, y):
	a = x + y
	return a

def sq(f):
	b = f*f
	return b

if __name__ == '__main__':
	print_KIT()
	print_hello()
	print(add(3,4))
	print(sq(6))