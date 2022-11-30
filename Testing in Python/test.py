import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_num = 10
        result  = main.do_stuf(test_num)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
            test_num = 'asfdasdf'
            result  = main.do_stuf(test_num)
            self.assertTrue(result, isinstance(result,ValueError))
    
    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuf(test_param)
        self.assertEqual(result, 'please enter number')
     
    
    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuf(test_param)
        self.assertEqual(result, 'please enter number')

if __name__ == '__main__': 
   unittest.main()
