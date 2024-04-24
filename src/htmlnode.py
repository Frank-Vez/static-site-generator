class HTMLnode:

  def __init__(self, tag = None ,  value = None, children = None, props = None):
    self.tag = tag 
    self.value = value 
    self.children = children 
    self.props = props
  
  def to_html(self):
    raise NotImplementedError
  
  def props_to_html(self):
    parameters =""
    for key,value in self.props.items():
     parameters += " " + key + '="' + value + '"'
    return parameters
  
  def __repr__(self):
        return f"HTMLnode({self.tag}, {self.value}, children: {self.children}, {self.props})"



