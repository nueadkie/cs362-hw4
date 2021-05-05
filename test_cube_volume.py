import unittest
import cube_volume

class Tester(unittest.TestCase):
  # Tests for float inputs
  def test_float(self):
    result = cube_volume.volume(5.5)
    self.assertEqual(result, 166.375)
  
  # Test for an imaginary input
  def test_complex(self):
    result = cube_volume.volume(1j)
    # j * j = -1
    # -1 * j = -j
    self.assertEqual(result, -1j)
  
  # Error-checking type errors
  def test_type_error(self):
    result = cube_volume.volume("hello")
    self.assertEqual(result, None)

if __name__ == '__main__':
  unittest.main()