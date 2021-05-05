def calc(items):
  # Check if the input is actually a list and if so, check that the list isn't empty.
  if not isinstance(items, list) or len(items) == 0:
    return None
  # CHeck that all of the numbers in the list are actually numbers.
  for item in items:
    if not isinstance(item, (int, float, complex)):
      return None
  return sum(items) / len(items)