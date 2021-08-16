import simplegui, random

iterations = 0

def randCol():
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    
    return 'rgb('+str(r)+ ',' +str(g)+ ',' +str(b)+ ')'

#drawing handler
def draw(canvas):
    global iterations
    print("No. Draws: ", iterations)
    iterations += 1
    if iterations % 60 == 0:
        frame.set_canvas_background(randCol())


frame = simplegui.create_frame(" Colours ", 400, 200)
frame.set_draw_handler(draw) 

#start frame animation
frame.start()