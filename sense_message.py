from sense_hat import SenseHat
sense = SenseHat()

blue = (0,0,255)
red = (255,0,0)
yellow = (255, 255, 0)
green = (0,255,0)
white = (255,255,255)

sense.clear()

sense.show_message("Hello", text_colour = white, back_colour = blue, scroll_speed = .1)

sense.clear()