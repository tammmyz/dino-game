import unittest
import pygame

import sys, os
from unittest.mock import patch

sys.path.insert(1, os.path.abspath('.'))

from display import *
import global_var
from chromedino import *

class TestInstructions(unittest.TestCase):

    # Tests if default settings is audio on
    def test_default_audio(self):
        self.assertTrue(global_var.audio)

    def test_default_theme(self):
        self.assertEqual(global_var.theme, 'default')

    def test_no_audio(self):
        global_var.test_settings = True
        menu(1)
        self.assertEqual(global_var.audio, False)
        global_var.test_settings = False

    def test_student_theme(self):
        global_var.test_settings = True
        menu(1)
        self.assertEqual(global_var.theme, 'student')
        global_var.test_settings = False

    def test_corona_theme(self):
        global_var.test_settings = True
        menu(1)
        self.assertEqual(global_var.theme, 'corona')

if __name__ == '__main__':
    unittest.main()