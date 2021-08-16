import simplegui, random

WIDTH = 500 #set width of canvas
HEIGHT = 500 #set height of canvas
radius = 50
sizeMovement = 'shrink'
iterations = 0

#function that changes the size of the circle and drawing the circle 
def draw(canvas):
    global radius, sizeMovement, iterations
    iterations += 1
    if radius > 10 and sizeMovement == 'shrink' and iterations % 5 == 0:
        radius -= 1
    if radius < 50 and sizeMovement == 'expand' and iterations % 5 == 0:
        radius += 1
    if radius == 10:
        sizeMovement = 'expand'
    if radius == 50:
        sizeMovement = 'shrink'
    canvas.draw_circle((WIDTH/2, HEIGHT/2), radius, 1, "Pink", "Pink")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame('Shrink_Expand', WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# Start the frame animation 
frame.start()
