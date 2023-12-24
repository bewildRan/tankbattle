

import random
import pygame
import traceback
import sys

# 'a' - left
# 'd' - right
# 'w' - goForth/attack
# 's' - goBack
# '2' - goForth2
# 'x' - goBack2
# space - doNothing

class AI:
    
    def __init__(self):
        pass
    def turn(self):
        try:
            print("waiting for input...")
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w: 
                            if self.robot.lookInFront() is "bot":
                                self.robot.attack()
                                print("Attack")
                            else:
                                self.robot.goForth()
                                print("goForth")
                            return
                        elif event.key == pygame.K_s:
                            self.robot.goBack()
                            print("goBack")
                            return
                        elif event.key == pygame.K_a:
                            self.robot.turnLeft()
                            print("Left")
                            return
                        elif event.key == pygame.K_d:
                            self.robot.turnRight()
                            print("Right")
                            return
                        elif event.key == pygame.K_2:
                            self.robot.goForth2()
                            print("Forth2")
                            return
                        elif event.key == pygame.K_x:
                            self.robot.goBack2()
                            print("Back2")
                            return
                        elif event.key == pygame.K_SPACE:
                            self.robot.doNothing()
                            print("Do nothing")
                            return
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
        
        except:
            traceback.print_exc()
            input()
