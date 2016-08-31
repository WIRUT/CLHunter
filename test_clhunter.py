import clhunter
import unittest

class TestAreaBoundChecker(unittest.TestCase):

    coords= [ 
            [49.2652, -123.137984], 
            [49.279425, -123.097472] 
            ]

    def test_bound_checker_true(self):
        aoi = [49.271829, -123.12164]
        self.assertEqual(clhunter.area_bound_checker(aoi, self.coords), True)

    def test_bound_checker_false(self):
        aoi = [49.231829, -123.92164]
        self.assertEqual(clhunter.area_bound_checker(aoi,self.coords), False)

    def test_empty_aoi(self):
        aoi = []
        self.assertEqual(clhunter.area_bound_checker(aoi,self.coords), False)

    def test_one_aoi(self):
        aoi = [0]
        self.assertEqual(clhunter.area_bound_checker(aoi,self.coords), False)


class TestInAreaOfInterest(unittest.TestCase):

    def test_in_aoi(self):
        aoi = [49.26938671, -123.1148529053]
        self.assertEqual(clhunter.in_area_of_interest(aoi),(True,'False_Creek'))

    def test_empty_aoi(self):
        aoi = []
        self.assertEqual(clhunter.in_area_of_interest(aoi),(False, None))

# class TestInAOIMethods(unittest.TestCase):
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #                 s.split(2)

if __name__ == '__main__':
    unittest.main()
