from os import system,name,remove
import sys
from time import sleep
import string

class term_updater():
    def __init__(self):
        self.o_std = ''
        open("term-content","w")

    def init_updater(self):
        self.o_std = sys.stdout
        f = open("term-content","a")
        sys.stdout = f


    def update_terminal(self,string,line_index):


        #assign stdout
        self.reasign_stdout()

        #replace line
        with open("term-content","r") as f:
            content = f.read().split('\n')
            content[line_index] = string
            i = 0
            for line in content:
                if line == "":
                    content.pop(i)
                else:
                    content[i] = str(line).strip('\n')
                    i +=1


            #assign stdout
            self.init_updater()

            #rewrite new content
            with open("term-content","w") as f:
                for line in content:
                    f.write(f"{str(line)}\n")


    def display_terminal(self):
        self.reasign_stdout()

        system('cls' if name == 'nt' else 'clear')

        with open("term-content","r") as f:
            for line in f.read().split('\n'):
                if line == "\n":
                    pass
                else:
                    print(line)


        self.init_updater()

    def reasign_stdout(self):
        sys.stdout = self.o_std

    
    def end_updater(self):
        sys.stdout = self.o_std
        remove("term-content")