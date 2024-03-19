from turtle import Turtle
import unittest
import sys, os
import pygame
from unittest.mock import MagicMock

sys.path.insert(1, os.path.abspath('.'))
sys.path.append('../source')

from display import *
import global_var
from chromedino import *

class TestInstructions(unittest.TestCase):

    def Test_testing():
        global_var.audio

    def test_exit_key(self):
        global_var.test_instructions = True
        global_var.start_flag = False
        menu(0)
        self.assertEqual(global_var.start_flag, True)
        global_var.test_instructions = False

    def test_pause_to_instructions(self):
        global_var.test_instructions = True
        global_var.test_pause = True
        menu(0)
        self.assertEqual(global_var.instructions_flag, False)
        global_var.test_instructions = False
    
    def test_press_how_to_play(self):
        global_var.start_flag = True
        if (global_var.start_flag and pygame.event.Event(pygame.MOUSEBUTTONDOWN)):
            pass

    
        
    
        


    def test_instruction_body(self):
        pass
    


  

if __name__ == '__main__':
    
    unittest.main()


'''
def key_mock(key):
def helper():
tmp = [0] * 100
tmp[key] = 1
global_var.instructions_flag = True
return helper

pygame.key.get_pressed = key_mock(pygame.K_b)

#chromedino.menu(1)
if (global_var.instructions_flag and pygame.event.Event(pygame.MOUSEBUTTONDOWN, {"key":pygame.K_b})):

self.assertFalse(global_var.instructions_flag)
self.assertTrue(global_var.start_flag)
'''