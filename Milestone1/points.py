import simplegui

WIDTH = 700 #task 2 set the width of canvas
HEIGHT = 500 #task 2 set the height of canvas

def draw(canvas):
    canvas.draw_point((0,0), "Yellow") #task 3 set point to bottom corner 0,0
    canvas.draw_point((699, 499), "Yellow") #task 3 set point to top corber 699, 499
    #if drawn at 700, 500 the point is drawn off the screen
    
frame = simplegui.create_frame("Points", WIDTH, HEIGHT)
frame.set_draw_handler(draw)


frame.start()