import os
import turtle

import constants
from frame import Frame
from capybaraStateManager import CapybaraStateManager
from capybara import Capybara

turtle.Screen().setup(constants.width, constants.height-100)
turtle.screensize(360, 360)

if __name__ == '__main__':
    for picture in os.listdir("assets"):
        if picture.endswith(".gif"):
            turtle.register_shape("assets/" + picture)
    window = turtle.Screen()
    window.bgpic("assets/bg.gif")
    window.title("Capybara")
    mainFrame = Frame(CapybaraStateManager(Capybara()))
    mainFrame.run()
