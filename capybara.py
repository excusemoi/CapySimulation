import turtle

import constants


class Capybara(turtle.Turtle):
    sleep = 98
    hunger = 98
    enjoy = 0
    state = constants.sleep

    def __init__(self):
        super().__init__(visible=False)
        self.speed(0)
        self.up()
        self.goto(constants.sleep_pos[0], constants.sleep_pos[1])
        self.speed(4)
        self.up()
        self.showturtle()

    def is_hungry(self):
        return self.hunger <= constants.lower_threshold

    def is_sleepy(self):
        return self.sleep <= constants.lower_threshold

    def move(self):
        self.shape(constants.run_image_path)
        self.clear()
        match self.state:
            case constants.sleep:
                self.sleep_()
            case constants.chill:
                self.chill()
            case constants.swim:
                self.swim()
            case constants.be_petted:
                self.be_petted()
            case constants.eat:
                self.eat()

    def sleep_(self):
        self.goto(constants.sleep_pos[0], constants.sleep_pos[1])
        self.shape(constants.sleep_image_path)

    def chill(self):
        self.goto(constants.run_pos[0], constants.run_pos[1])
        self.shape(constants.chill_image_path)

    def swim(self):
        self.goto(constants.swim_pos[0], constants.swim_pos[1])
        self.shape(constants.swim_image_path)

    def be_petted(self):
        self.goto(constants.be_petted_pos[0], constants.be_petted_pos[1])
        self.shape(constants.be_petted_image_path)

    def eat(self):
        self.goto(constants.eat_pos[0], constants.eat_pos[1])
        self.shape(constants.eat_image_path)


