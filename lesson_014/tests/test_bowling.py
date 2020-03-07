# -*- coding: utf-8 -*-
import unittest

from bowling import ScoreCounter


class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.score = ScoreCounter()

    def test_result(self):  
        self.gemeresult = 'XXXXXXXXX55'
        self.assertEqual(self.score.get_score(self.gemeresult),190)
        self.gemeresult = 'XXXXXXXXX--'
        self.assertEqual(self.score.get_score(self.gemeresult), 180)
        self.gemeresult = 'XXXXXXXXX3-'
        self.assertEqual(self.score.get_score(self.gemeresult), 183)
        self.gemeresult = 'XXXXXXXXX-4'
        self.assertEqual(self.score.get_score(self.gemeresult), 184)




    def test_length(self):
        self.gemeresult = 'XXXXXXXXX'
        self.assertRaises(ValueError,self.score.get_score,self.gemeresult)

    def test_str(self):
        self.gemeresult = '27XXXXXXX4/'
        self.assertRaises(ValueError,self.score.get_score,self.gemeresult)
        self.gemeresult = '27XXXXXXXX/2'
        self.assertRaises(ValueError, self.score.get_score, self.gemeresult)
        self.gemeresult = '27XXXXXXXX/2'
        self.assertRaises(ValueError, self.score.get_score, self.gemeresult)
        self.gemeresult = '27XXXXXXXX-'
        self.assertRaises(ValueError, self.score.get_score, self.gemeresult)

if __name__ == '__main__':
    unittest.main()

