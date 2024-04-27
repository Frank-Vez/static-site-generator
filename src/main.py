from textnode import Textnode
from leafnode import Leafnode

def main():
  print(Leafnode( tag = "bold", props= "https://www.boot.dev"))
  print(Textnode("This is a text node", "bold", "https://www.boot.dev"))

main()
