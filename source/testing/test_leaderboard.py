import unittest
import pygame
import sys, os
sys.path.insert(1, os.path.abspath('.'))
from display import *
from chromedino import *

##assumes you're on the restart page

class TestLeaderboard(unittest.TestCase):
    
    def test_leaderboardflag(self):
        menu(1,0)
        mouse_pos = pygame.mouse.get_pos() 
        # global_var.restart_flag == True
        print("inside assert")
        self.assertEqual(global_var.leaderboard_flag, True)
       
    def test_leaderbaord_corectness(self):
        leaders = get_leaders()
        cleaders = ["Chelsea", "Anjola","Sheridan","Chelsea", "Sharon"]
        i = 0
        for leader in leaders:
            self.assertEqual(leader[0], cleaders[i])
            i += 1

'''
Sheridan 10000
Anjola 50000
Chelsea 470000
Chelsea 3444
Sharon 53
Ben 17
'''
 



if __name__ == '__main__':
    unittest.main()

