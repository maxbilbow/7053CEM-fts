import sys
from os.path import dirname, abspath, join
path = abspath(join(dirname(__file__), '..', '..', 'server'))
sys.path.append(path)

import unittest
from unittest.mock import MagicMock
from repository.PoiScoreRepository import PoiScoreRepository
from service.PoiScoreService import PoiScoreService

POI_DETAIL_RESPONSE = {"id": "detail"}
POI_LIST_RESPONSE = [POI_DETAIL_RESPONSE]


class PoiScoreServiceTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_repo: PoiScoreRepository = MagicMock()
        self.mock_repo.get_poi_details = MagicMock(return_value=POI_DETAIL_RESPONSE)
        self.mock_repo.get_poi_with_ids = MagicMock(return_value=POI_LIST_RESPONSE)
        self.poi_score_service = PoiScoreService(self.mock_repo)

    def test_that_get_poi_list_returns_repo_result(self):
        id_list = ["input"]
        result = self.poi_score_service.get_poi_list(id_list)
        self.assertEqual(result, POI_LIST_RESPONSE)
        self.mock_repo.get_poi_with_ids.assert_called_with(id_list)

    def test_that_get_poi_details_returns_repo_result(self):
        result = self.poi_score_service.get_poi_details("input")
        self.assertEqual(result, POI_DETAIL_RESPONSE)
        self.mock_repo.get_poi_details.assert_called_with("input")

if __name__ == '__main__':
    unittest.main()
