from unittest import TestCase

from my_diary.diaries import Diaries
from my_diary.diary_not_found import DiaryNotFound


class testDiaries(TestCase):
    def setUp(self) -> None:
        self.diaries = Diaries()
        self.diaries.add('tobi', '1234')

    def test_add_diary_and_find_by_username(self):
        self.assertEqual('favy', self.diaries.find_by_username('favy').get_username())

    def test_delete_diary(self):
        self.diaries.add('dee','1234')
        self.assertEqual('dee', self.diaries.find_by_username('dee').get_username())
        self.diaries.delete('dee','1234')
        self.assertRaises(DiaryNotFound, self.diaries.find_by_username,'dee')
