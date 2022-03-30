import unittest
import pygame

import sys, os
from unittest.mock import patch

sys.path.insert(1, os.path.abspath('.'))

from display import *
import global_var
from chromedino import *

# inputs are 3, n, 2
class TestInstructions(unittest.TestCase):

    # Tests if default settings is audio on
    def test_a_default_audio(self):
        print("this is the variable {} ".format(global_var.audio))
        self.assertTrue(global_var.audio)

    def test_b_no_audio(self):
        print("this is the no audio test")
        global_var.test_settings = True
        menu(1)
        self.assertEqual(global_var.audio, False)
        global_var.test_settings = False
        global_var.audio = True


    def test_c_default_press(self):
        print("this is the default press theme")
        global_var.test_settings = True
        menu(1)
        self.assertEqual(global_var.theme, 'default')
        global_var.test_settings = False
        global_var.theme = 'default'

    def test_d_default_theme(self):
        print("this is the default_theme")
        self.assertEqual(global_var.theme, 'default')

    def test_e_student_theme(self):
        print("this is the student theme")
        global_var.test_settings = True
        menu(1)
        self.assertEqual(global_var.theme, 'student')
        global_var.test_settings = False
        global_var.theme = 'default'

    def test_f_corona_theme(self):
        print("this is corona_theme")
        global_var.test_settings = True
        menu(1)
        self.assertEqual(global_var.theme, 'corona')
        global_var.test_settings = False
        global_var.theme = 'default'





    # def test_corona_theme(self):
    #     global_var.test_settings = True
    #     menu(1)
    #     self.assertEqual(global_var.theme, 'corona')
    #     global_var.test_settings = False
    #     global_var.theme = 'default'


if __name__ == '__main__':
    unittest.main()