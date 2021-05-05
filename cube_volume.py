# Takes in an integer, float, or complex value, then calculates the volume of the cube with that side length.
# Returns None with incompatible data types for the side length.
def volume(length):
  if isinstance(length, (int, float, complex)):
    return length * length * length
  else:
    return None