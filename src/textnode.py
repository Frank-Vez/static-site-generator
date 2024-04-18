class Textnode:
  def __init__(self, text, text_node, url):
    self.text = text
    self.text_node = text_node
    self.url = url
  
  def __eq__(self, other):
    if(self.text == other.text and
       self.text_node == other.text_node and
       self.url == other.url):
      return True
  
  def __repr__(self) -> str:
    return f"Textnode {self.text, self.text_node, self.url}"

