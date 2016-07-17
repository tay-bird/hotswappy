import unittest

import plugins
from hotswappy import Controller
from hotswappy import Plugin


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.ctrl = Controller(plugins)
        self.ctrl.load('P1')

    def test_param_revert(self):
        self.ctrl.plugins['P1'].test_field = "test"
        self.ctrl.hotswap()
        
        with self.assertRaises(AttributeError):
            self.ctrl.plugins['P1'].test_field


if __name__ == '__main__':
    unittest.main()
