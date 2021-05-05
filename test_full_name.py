import unittest
import full_name

class Tester(unittest.TestCase):
  # Test for a case of a mix between integers/floats/complex numbers.
  def test_name(self):
    result = full_name.generate("Chris", "Miraflor")
    self.assertEqual(result, "Chris Miraflor")
  
  # Test for a case with non-string inputs.
  def test_nums(self):
    with self.assertRaises(TypeError):
      full_name.generate(1234, 5678)
  
  # Test for a case with too few inputs.
  def test_few_inputs(self):
    with self.assertRaises(TypeError):
      full_name.generate("Full Name")

if __name__ == '__main__':
  unittest.main()