import turtle
import random


class Frame:
    capybaraStateManager = None

    def __init__(self, manager):
        self.capybaraStateManager = manager

    def run(self):
        self.capybaraStateManager.manage()
