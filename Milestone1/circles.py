import simplegui, random
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

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_circle([50, 50], 30, 8, randCol ())
    canvas.draw_circle((30, 30), 25, 12, randCol ())
        
    #The second circle is on top. This is because the program is sequential 
    #This means that the most recently called piece of code, in this case, the circle drawn second, is the last piece of code to be called
    #As a result, the second circle is drawn last, and, therefore, on top of the first circle
    #If the first circle was drawn after the second, sequentially, then it would be drawn on top
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame('Circles', 100, 100)
frame.set_draw_handler(draw)
#creates a timer 
timer = simplegui.create_timer(500, ColourChanger)

# Start the frame animation and the timer 
frame.start()
timer.start()
