def generate(fname, lname):
  if isinstance(fname, str) and isinstance(lname, str):
    return fname + " " + lname
  else:
    raise TypeError("name must be comprised of strings")