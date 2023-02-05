from drawingpanel import *
import math
#from the htree.py file
W = 800
H = 500
panel = DrawingPanel(W, H)
canvas = panel.canvas

def sierpinski(n, x, y, size):
#whole triangle
	if n == 0:	
		first_tri(x, y, size)
#first triangle with multiple triangles
	elif n == 1:
		sierpinski(n - 1, x, y, size)
		draw_tri(x, y, size / 2)
#for any triangles after n=1, i.e. 2, 3, 4, 5, .....
	else:
		# the recursion
		#eq tri = sqrt3/4 so the math shows that for the sides to be equal. completely forgot basic trig lol
		x0 = x - size / 4
		y0 = y + size / (4*math.sqrt(3))
		x1 = x + size / 4
		y1 = y + size / (4*math.sqrt(3))
		x2 = x
		y2 = y - size/(2*math.sqrt(3))
        #calling my sides
		sierpinski(n-1, x0, y0, size / 2)
		sierpinski(n-1, x1, y1, size / 2)
		sierpinski(n-1, x2, y2, size / 2)


def first_tri(x, y, size):
	canvas = panel.canvas
	canvas.create_line(x - size / 2, y + size*(math.sqrt(3)/6), x + size / 2, y + size*(math.sqrt(3)/6),fill = 'gold')
	canvas.create_line(x - size / 2, y + size*(math.sqrt(3)/6), x , y - size/math.sqrt(3),fill = 'gold')
	canvas.create_line(x + size / 2, y + size*(math.sqrt(3)/6), x, y - size/math.sqrt(3),fill = 'gold')

def draw_tri(x, y, size):
	side = 0
	canvas = panel.canvas
	side1_draw = canvas.create_line(x - size / 2, y - size*(math.sqrt(3)/6), x + size / 2, y - size*(math.sqrt(3)/6), fill = 'gold')
	side2_draw = canvas.create_line(x - size / 2, y - size*(math.sqrt(3)/6), x , y + size/math.sqrt(3),fill = 'gold')
	side3_draw = canvas.create_line(x + size / 2, y - size*(math.sqrt(3)/6), x, y + size/math.sqrt(3),fill = 'gold')

	side1_draw
	side2_draw
	side3_draw

#N is the scaling size of the triangle. Use 0-6. 
n = 0
def main():
	sierpinski(n, W/2, H*0.6, W*0.6)
main()
