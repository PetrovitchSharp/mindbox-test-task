import unittest
from functions import get_members_count, get_members_count_from_zero


class TestMethods(unittest.TestCase):
    '''
    Class with simple tests of functions
    '''

    def test_get_members_count(self):
        '''
        Test of the get_members_count function
        '''
        self.assertDictEqual(
            get_members_count(20, 5),
            {
                5: 3,
                6: 3,
                7: 2,
                8: 2,
                9: 2,
                1: 1,
                2: 2,
                3: 2,
                4: 2,
                10: 1
            }
        )

    def test_get_members_count_from_zero(self):
        '''
        Test of the get_members_count_from_zero function
        '''
        self.assertDictEqual(
            get_members_count_from_zero(20),
            {
                0: 1,
                1: 2,
                2: 2,
                3: 2,
                4: 2,
                5: 2,
                6: 2,
                7: 2,
                8: 2,
                9: 2,
                10: 1
            }
        )


if __name__ == '__main__':
    unittest.main()
