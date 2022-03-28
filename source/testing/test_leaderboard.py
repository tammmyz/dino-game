import unittest
import pygame
import sys, os
sys.path.insert(1, os.path.abspath('.'))
from display import *
from chromedino import *

##assumes you're on the restart page

class TestLeaderboard(unittest.TestCase):
    
    def test_upper(self):
        menu(1,0)
        mouse_pos = pygame.mouse.get_pos() 
        # global_var.restart_flag == True
        print("inside assert")
        self.assertEqual(global_var.leaderboard_flag, True)
       
            



if __name__ == '__main__':
    unittest.main()

