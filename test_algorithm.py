import unittest
from algorithm import search

class TestSearch(unittest.TestCase):
  def setUp(self):
    self.array = [10, 5, 20, 30, 1, 4]

  def test_successful(self):
    self.assertTrue(search(self.array, 20, 14))

  def test_failed(self):
    self.assertFalse(search(self.array, 100, 200))

  def test_emptyArray(self):
    self.assertFalse(search([], 10, 20))

  def test_whenArrayIsNone(self):
    self.assertFalse(search([None], 10, 20))


  def test_searchingNoneFailed(self):
    self.assertFalse(search(self.array, None, None))

  def test_searchingNoneSuccessful(self):
    self.assertTrue(search([None], None, None))


if __name__ == '__main__':
    unittest.main()
