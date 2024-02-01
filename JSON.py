import json

class JSON():

  def __init__(self, path):
    self.path = path
    with open(self.path, "r") as f:
      self.data = json.load(f)
      f.close()
  
  def save(self):
    with open(self.path, 'w') as file:
      json.dump(self.data, file)
      file.truncate()
      file.close()