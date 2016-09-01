# coding: utf-8
def load_src(name, fpath):
    import os, imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))
load_src("clhousehunter", "../lib/clhousehunter.py")
import clhousehunter 
import unittest

class TestAreaBoundChecker(unittest.TestCase):
    coords= [ 
            [49.2652, -123.137984], 
            [49.279425, -123.097472] 
            ]

    def test_bound_checker_true(self):
        aoi = [49.271829, -123.12164]
        self.assertEqual(clhousehunter.area_in_bounds(aoi, self.coords), True)

    def test_bound_checker_false(self):
        aoi = [49.231829, -123.92164]
        self.assertEqual(clhousehunter.area_in_bounds(aoi,self.coords), False)

    def test_empty_aoi(self):
        aoi = []
        self.assertEqual(clhousehunter.area_in_bounds(aoi,self.coords), False)

    def test_one_aoi(self):
        aoi = [0]
        self.assertEqual(clhousehunter.area_in_bounds(aoi,self.coords), False)


class TestInAreaOfInterest(unittest.TestCase):

    def test_in_aoi(self):
        aoi = [49.26938671, -123.1148529053]
        self.assertEqual(clhousehunter.in_area_of_interest(aoi),
                (True,'False_Creek'))

    def test_empty_aoi(self):
        aoi = []
        self.assertEqual(clhousehunter.in_area_of_interest(aoi),
                (False, None))


class TestCLInfoParser(unittest.TestCase):
    area = "Coal Harbour"
    info = {'price': '$9999', 'name': 'Waterfront Penthouse for rent!', 
            'url': 'http://www.vancitylofts.com'} 
    desc = "$9999 | Waterfront Penthouse for rent! | Coal Harbour "\
             "| <http://www.vancitylofts.com>"
    desc_mia_area = "$9999 | Waterfront Penthouse for rent! | N/A "\
             "| <http://www.vancitylofts.com>"

    def test_cl_info_parser(self):
        self.assertEqual(clhousehunter.cl_info_parser(self.area, self.info), 
                self.desc)

    def test_cl_info_parser_one_empty(self):
        self.assertEqual(clhousehunter.cl_info_parser(self.area, None), None)
        self.assertEqual(clhousehunter.cl_info_parser(None, self.info), 
                self.desc_mia_area)

    def test_cl_info_parser_empty(self):
        self.assertEqual(clhousehunter.cl_info_parser(None, None), None)

if __name__ == '__main__':
    unittest.main()
