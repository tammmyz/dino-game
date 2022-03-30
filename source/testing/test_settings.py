import unittest

import sys, os
from unittest.mock import patch

sys.path.insert(1, os.path.abspath('.'))

from display import *

import global_var
from chromedino import menu

class TestInstructions(unittest.TestCase):

    # Tests if default settings is audio on
    def test_default_audio(self):
        self.assertTrue(global_var.audio)

    def test_default_theme(self):
        self.assertEqual(global_var.theme, 'default')

    # @patch("builtins.input", return_value="e")
    # def test_settings_pg(self):
    #
    #     self.assertEqual()




if __name__ == '__main__':
    unittest.main()