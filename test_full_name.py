import unittest
import full_name

class Tester(unittest.TestCase):
  # Test for a case of a mix between integers/floats/complex numbers.
  def test_name(self):
    result = full_name.generate("Chris", "Miraflor")
    self.assertEqual(result, "Chris Miraflor")

if __name__ == '__main__':
  unittest.main()