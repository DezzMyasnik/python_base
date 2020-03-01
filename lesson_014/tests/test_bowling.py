# -*- coding: utf-8 -*-
import unittest

from bowling import ScoreCounter


class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.score = ScoreCounter()

    def tearDown(self):
        pass

    def test_result(self):
        self.gemeresult = 'XXXXXXXXXX'
        self.assertEqual(self.score.get_score(self.gemeresult),200)

    def test_length(self):
        self.gemeresult = 'XXXXXXXXX'
        self.assertRaises(ValueError,self.score.get_score,self.gemeresult)

    def test_str(self):
        self.gemeresult = '27XXXXXXXX4/'
        self.assertRaises(ValueError,self.score.get_score,self.gemeresult)



if __name__ == '__main__':
    unittest.main()

