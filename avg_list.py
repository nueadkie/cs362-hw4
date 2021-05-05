def calc(items):
  # Check if the input is actually a list and if so, check that the list isn't empty.
  if not isinstance(items, list):
    raise TypeError("cannot calculate average of non-list")
  if len(items) == 0:
    raise ValueError("cannot calculate average of empty list")
  # Check that all of the numbers in the list are actually numbers.
  for item in items:
    if not isinstance(item, (int, float, complex)):
      return TypeError("cannot calculate average of list with non-numeric value")
  return sum(items) / len(items)