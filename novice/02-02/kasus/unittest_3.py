import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
    
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(WidgetTestCase('test_default_widget_size'))
        suite.addTest(WidgetTestCase('test_widget_resize'))
        return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # runner.run(suite())