import sys
from os.path import dirname, abspath, join
path = abspath(join(dirname(__file__), '..', '..', 'server'))
sys.path.append(path)

import unittest
from service.poi_score_utils import update_bool_average, update_average

POI_DETAIL_RESPONSE = {"id": "detail"}
POI_LIST_RESPONSE = [POI_DETAIL_RESPONSE]

VALUES = [-1, 1, 1, 1, -1, 1, 1]
NUMBER_OF_VALUES = len(VALUES)
CURRENT_VALUE = sum(VALUES) / NUMBER_OF_VALUES
print("Current Value: %s" % CURRENT_VALUE)
EXPECTED_POSITIVE_VALUE: float
EXPECTED_NEGATIVE_VALUE: float

def define_expected_positive_score():
    global EXPECTED_POSITIVE_VALUE
    values = VALUES.copy()
    values.append(1)
    n = len(values)
    EXPECTED_POSITIVE_VALUE = sum(values) / n
    print("Expected +1 score average: %s" % EXPECTED_POSITIVE_VALUE)

def define_expected_negative_score():
    global EXPECTED_NEGATIVE_VALUE
    values = VALUES.copy()
    values.append(-1)
    n = len(values)
    EXPECTED_NEGATIVE_VALUE = sum(values) / n
    print("Expected -1 score average: %s" % EXPECTED_NEGATIVE_VALUE)

define_expected_positive_score()
define_expected_negative_score()

class UpdateAverageTest(unittest.TestCase):

    def test_that_positive_score_average_updates(self):
        result = update_average(CURRENT_VALUE, NUMBER_OF_VALUES, 1)
        self.assertEqual(result, EXPECTED_POSITIVE_VALUE)

    def test_that_positive_bool_converts_to_number(self):
        result = update_bool_average(CURRENT_VALUE, NUMBER_OF_VALUES, True, 1)
        self.assertEqual(result, EXPECTED_POSITIVE_VALUE)

    def test_that_negative_score_average_updates(self):
        result = update_average(CURRENT_VALUE, NUMBER_OF_VALUES, -1)
        self.assertEqual(result, EXPECTED_NEGATIVE_VALUE)

    def test_that_negative_bool_converts_to_number(self):
        result = update_bool_average(CURRENT_VALUE, NUMBER_OF_VALUES, True, -1)
        self.assertEqual(result, EXPECTED_NEGATIVE_VALUE)

if __name__ == '__main__':
    unittest.main()
