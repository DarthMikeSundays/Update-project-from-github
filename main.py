import os
import sys

class MainSingleton(object):
    _instance = None

    def __new__(cls,*args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    # the main method
    def run(self):
        self.get_input()

    def get_input(self):
        self.githubProjectName = input("What's the name of the github project?")
        self.operationToDo = input("Do you want to update a existing dir or just clone? /dir /clone")
