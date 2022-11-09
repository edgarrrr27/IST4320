import pyglet

# Will open a new window that is the full size of the screen, without a borders
window = pyglet.window.Window(fullscreen=True)

# Inserts text in window, setting the font name and size,
# along with the positioning based on x and y axis and placing it in the center
label = pyglet.text.Label('Dino feasting on prey',
                          font_name='Times New Roman',
                          font_size=50,
                          x=window.width//2, y=window.height//1.03,
                          anchor_x='center', anchor_y='center')

# Inserts image specified
image = pyglet.resource.image('DINOSAUR.jpg')
# Resizing image
imageWidth = 1000
imageHeight = 1000
image.width = imageWidth
image.height = imageHeight

# Sounds that will be played
roar = pyglet.resource.media('dino.mp3')
roar.play()

bird = pyglet.resource.media('bird_call.mp3')
bird.play()

# Makes the window open, text and image to be inputted
@window.event
def on_draw():
    window.clear() # for the window
    label.draw() # the text
    image.blit(475,0) # reposition image starting from the bottom left corner using the x and y axis

# runs the module
pyglet.app.run()