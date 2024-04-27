from htmlnode import HTMLnode

class Leafnode(HTMLnode):
  def __init__(self, value = None, tag = None,  props= None):
    if value is None:
      raise ValueError("missing a value")
    super().__init__(tag, value,None, props)

  def to_html(self):
    if self.tag is None:
      return self.value
    


  