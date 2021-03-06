import unittest
import avg_list

class Tester(unittest.TestCase):
  # Test for a case of a mix between integers/floats/complex numbers.
  def test_mix(self):
    result = avg_list.calc([7, 2, 6.125, 2+1j])
    self.assertEqual(result, 4.28125+0.25j)

  # Test for the special case of an empty list
  def test_empty(self):
    with self.assertRaises(ValueError):
      avg_list.calc([])
  
  # Test for if a list member is not a number
  def test_type_error(self):
    with self.assertRaises(TypeError):
      avg_list.calc([2, 3, 4, 5, 6, "yes"])

if __name__ == '__main__':
  unittest.main()