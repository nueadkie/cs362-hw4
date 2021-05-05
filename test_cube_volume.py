import unittest
import cube_volume

class Tester(unittest.TestCase):
  def test_int(self):
    result = cube_volume.volume(2)
    self.assertEqual(result, 8)
  
  def test_int2(self):
    result = cube_volume.volume(5)
    self.assertEqual(result, 125)
  
  def test_float(self):
    result = cube_volume.volume(1.2)
    self.assertEqual(result, 1.728)
  
  def test_float2(self):
    result = cube_volume.volume(5.0)
    self.assertEqual(result, 125.0)
  
  def test_complex(self):
    result = cube_volume.volume(1j)
    # j * j = -1
    # -1 * j = -j
    self.assertEqual(result, -1j)
  
  def test_type_error(self):
    result = cube_volume.volume("hello")
    self.assertEqual(result, None)

if __name__ == '__main__':
  unittest.main()