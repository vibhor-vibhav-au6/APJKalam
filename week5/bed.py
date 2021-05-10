class Bed:
  def __init__(self, length, breadth, year_made,has_headboard, has_posts, material):
    self.length = float(length)
    self.breadth = float(breadth)
    self.year_made = year_made
    self.has_headboard = bool(has_headboard)
    self.has_posts = bool(has_posts)
    self.material = material




