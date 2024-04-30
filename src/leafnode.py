from htmlnode import HTMLnode

class Leafnode(HTMLnode):
  def __init__(self, value = None, tag = None, children = None,  props= None):
    if value is None:
      raise ValueError("missing a value")
    super().__init__(tag, value,None, props)

  def to_html(self):
    htmltag = ""
    if self.tag is None:
      htmltag = self.value
      return htmltag
    else:
      htmltag =+ f"<{self.tag}"
      if self.props != None:
        htmltag =+ f"{super().props_to_html(self)}"
      htmltag =+ f" >{self.value}</{self.tag}>"
      return htmltag
    


  