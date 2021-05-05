import unittest
import avg_list

class Tester(unittest.TestCase):
  # Tests for list of all integers/floats/complex numbers.
  def test_ints(self):
    result = avg_list.calc([2, 3, 4, 5, 6])
    self.assertEqual(result, 4)
  
  def test_floats(self):
    result = avg_list.calc([1.2, 4.6, 3.1, 5.4])
    self.assertEqual(result, 3.575)
  
  def test_complexes(self):
    result = avg_list.calc([2+1j, 3+5j])
    self.assertEqual(result, 2.5+3j)

  # Test for a case of a mix between integers/floats/complex numbers.
  def test_mix(self):
    result = avg_list.calc([7, 2, 6.125, 2+1j])
    self.assertEqual(result, 4.28125+0.25j)

  # Test for the special case of an empty list
  def test_empty(self):
    result = avg_list.calc([])
    self.assertEqual(result, None)
  
  # Test for output when not given a list
  def test_wrong_type(self):
    result = avg_list.calc("hello")
    self.assertEqual(result, None)
  
  # Test for if a list member is not a number
  def test_type_error(self):
    result = avg_list.calc([2, 3, 4, 5, 6, "yes"])
    self.assertEqual(result, None)

if __name__ == '__main__':
  unittest.main()