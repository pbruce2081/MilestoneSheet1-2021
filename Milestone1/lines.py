import simplegui,random

WIDTH = 800 #setting width of canvas
HEIGHT = 600 #setting height of canvas
x = 0 #setting x value
thickness = 40 #setting thickness of line
x0 = 0 #setting second x value
iterations = 0 #setting iterations for chaning colour
r = 255
g = 255
b = 255

#function that generates a random colour 
def ColourChanger():
    global r,g,b
    r0 = random.randrange (0, 256)
    g0 = random.randrange (0, 256)
    b0 = random.randrange (0, 256)
    r = r0
    g = g0
    b = b0
def randCol ():
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

#function that creates a timer to move the line
def timer():
    global x
    global x0
    
    x += 1
    if x == WIDTH + thickness / 2:
        x = 0 - WIDTH + thickness / 2
        
    x0 += 1
    if x0 == WIDTH * 2 + thickness / 2:
        x0 = thickness / 2
    
def draw(canvas):
    canvas.draw_line([WIDTH, 0], [0, HEIGHT], 1, randCol ())    # Draw diagonal
    canvas.draw_line([WIDTH, HEIGHT], [0, 0], 1, randCol ())    # Draw diagonal
    canvas.draw_line([x, HEIGHT], [x, 0], thickness, randCol ())  #Draw 1st moving line
    canvas.draw_line([x0 - WIDTH, HEIGHT], [x0 - WIDTH, 0], thickness, randCol ())   #Draw 2nd moving line

frame = simplegui.create_frame('Lines', WIDTH, HEIGHT)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1, timer)
timer0 = simplegui.create_timer(500, ColourChanger)

frame.start()
timer.start()
timer0.start()