import random
import turtle

import constants
import time


class CapybaraStateManager:
    capybara = None
    hunger_turtle = turtle.Turtle()
    sleep_turtle = turtle.Turtle()
    state_turtle = turtle.Turtle()

    def __init__(self, capybara):
        self.capybara = capybara
        self.hunger_turtle.up()
        self.hunger_turtle.goto(constants.stats_pos[0]-100, constants.stats_pos[1])
        self.sleep_turtle.up()
        self.sleep_turtle.goto(constants.stats_pos[0]-100, constants.stats_pos[1]-20)
        self.state_turtle.up()
        self.state_turtle.goto(constants.stats_pos[0]-100, constants.stats_pos[1] - 40)

    def manage(self):
        while True:
            current_state = self.capybara.state
            match self.capybara.state:
                case constants.eat:
                    self.capybara.hunger += int(constants.dx_default / 2)
                    self.draw_states()
                    if self.capybara.is_sleepy() and not self.capybara.is_hungry()\
                            and self.capybara.hunger >= constants.upper_threshold:
                        self.capybara.state = constants.sleep
                    elif not self.capybara.is_sleepy() and not self.capybara.is_hungry() and self.capybara.hunger >= constants.upper_threshold:
                        self.choose_next_activity()
                case constants.sleep:
                    self.capybara.sleep += int(constants.dx_default / 2)
                    self.draw_states()
                    if self.capybara.is_hungry() and not self.capybara.is_sleepy() \
                            and self.capybara.sleep >= constants.upper_threshold:
                        self.capybara.state = constants.eat
                    elif not self.capybara.is_sleepy() and not self.capybara.is_hungry() and self.capybara.sleep >= constants.upper_threshold:
                        self.choose_next_activity()
                case constants.swim:
                    self.capybara.sleep -= constants.dx_default
                    self.capybara.hunger -= constants.dx_default
                    self.draw_states()
                    self.route_entertainment_activity()
                case constants.chill:
                    self.capybara.hunger -= constants.dx_default
                    self.draw_states()
                    self.route_entertainment_activity()
                case constants.be_petted:
                    self.capybara.sleep -= constants.dx_default
                    self.draw_states()
                    self.route_entertainment_activity()
            if current_state != self.capybara.state:
                self.capybara.move()


            time.sleep(1)


    def draw_states(self):
        self.hunger_turtle.clear()
        self.hunger_turtle.write("Hunger: " + str(self.capybara.hunger), font=('arial', 20, 'bold'))
        self.sleep_turtle.clear()
        self.sleep_turtle.write("Sleep: " + str(self.capybara.sleep), font=('arial', 20, 'bold'))
        self.state_turtle.clear()
        self.state_turtle.write("State: " + self.capybara.state, font=('arial', 20, 'bold'))

    def choose_next_activity(self):
        match self.capybara.state:
            case constants.eat | constants.sleep:
                self.capybara.state = constants.swim
            case constants.swim:
                self.capybara.state = constants.chill
            case constants.chill:
                self.capybara.state = constants.be_petted
            case constants.be_petted:
                self.capybara.state = constants.swim

    def route_entertainment_activity(self):
        if self.capybara.is_hungry():
            self.capybara.state = constants.eat
        elif self.capybara.is_sleepy():
            self.capybara.state = constants.sleep
        elif not self.capybara.is_sleepy() and not self.capybara.is_hungry():
            self.choose_next_activity()
