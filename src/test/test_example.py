from unittest import TestCase


class TestStringMethods(TestCase):
  """
  String methods tests - example
  """

  def test_upper(self):
    """
    should uppercase a word
    """
    word = 'fOo'
    result = word.upper()
    expectation = 'FOO'
    self.assertEqual(result, expectation)

  def test_isupper(self):
    """
    should check if a word is uppercased
    """
    word = 'FOO'
    result = word.isupper()
    self.assertTrue(result)

    word = 'FOo'
    result = word.isupper()
    self.assertFalse(result)

    word = 'foo'
    result = word.isupper()
    self.assertFalse(result)

  def test_lower(self):
    """
    should lowercase a word
    """
    word = 'FoO'
    result = word.lower()
    expectation = 'foo'
    self.assertEqual(result, expectation)

  def test_islower(self):
    """
    should check if a word is lowecased
    """
    word = 'foo'
    result = word.islower()
    self.assertTrue(result)

    word = 'fOo'
    result = word.islower()
    self.assertFalse(result)

    word = 'FOO'
    result = word.islower()
    self.assertFalse(result)
