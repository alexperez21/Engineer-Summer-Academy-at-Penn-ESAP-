# Question 1
"""

def print_fancybox(n):
  print("-" * 16)
  for l in range(n-1):
    print("|\\/\\/\\/\\/\\/\\/\\/|")
  print("-" * 16)

print_fancybox(8)

"""#Question 2"""

def print_pyramid(n):
  whitespace = int(((n* 2)-2)/2)
  print((" " *whitespace) + "/\\")
  for i in range(1, 3):
    print((" " * (whitespace-i)) + "/" * 1 + i * "*=" + "\\ ")
  print("-" *6)

print_pyramid(3)

def print_pyramid(n):
  whitespace = int(((n* 6)-6)/6)
  print((" " *whitespace) + "/\\")
  for i in range(1, 6):
    print((" " * (whitespace-i)) + "/" * 1 + i * "*=" + "\\ ")
  print("-" *12)
print_pyramid(6)

"""# Question 3"""

# this is what defines the step size of the rocket. this gives the correct
# amount of dashes, slashes, etc. 
n = 5
def draw(n):
	print("----------------")
 #Dana the G fr
	for i in range(0, 2 * int(n) - 2):
		print("|\/\/\/\/\/\/\/|")
	print("----------------")

def draw(n):
	for i in range(1, n + 1):
		print(" "*(n - i) + "/" + "*="*(i - 1) + "\\")
	print("-" * (2 * n))

def print_rocketship1():

	for i in range(1, 6):
		print(" "*(6 - i) + '/' * i + "**" + "\\" * i)
#this is the top of the body with the rhombus design
	print("+=*=*=*=*=*=*+")
	for i in range(1, 4):
		print("|" + ("." * (3 - i) + "/\\" * i + "." * (3 - i)) * 2 + "|")
	for i in range(3, 0, -1):
		print("|" + ("." * (3 - i) + "\\/" * i + "." * (3 - i)) * 2 + "|") 
#this is the middle border witht the triangle facing down it's flipped! 
	print("+=*=*=*=*=*=*+")
	for i in range(1, 4):
		print("|" + ("." * (i - 1) + "\\/" * (4 - i) + "." * (i - 1)) * 2 + "|")
	for i in range(3, 0, -1):
		print("|" + ("." * (i - 1) + "/\\" * (4 - i) + "." * (i - 1)) * 2 + "|")

#this is the bottom border with the cone. 
	print("+=*=*=*=*=*=*+")
	for i in range(1, 6):
		print(" " * (6 - i) + '/' * i + "**" + "\\" * i)

def cone(n):
	for i in range(1, n * 2):
		print(" " * (n * 2 - i) + '/' * i + "**" + "\\" * i)

def top_box(n):
	for i in range(1, n + 1):
		print("|" + ("." * (n - i) + "/\\" * i + "." * (n - i)) * 2 + "|")

def down_box(n):
	for i in range(1, n + 1):
		print("|" + ("." * (i - 1) + "\\/" * (n + 1 - i) + "." * (i - 1)) * 2+ "|")

def border(n):
	print("+" + "=*" * (2 * n) + "+")

def print_rocketship2(n):
	cone(n)
	border(n)
	top_box(n)
	down_box(n)
	border(n)
	down_box(n)
	top_box(n)
	border(n)
	cone(n)

print_rocketship2(n)
