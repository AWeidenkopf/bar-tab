from tkinter import Menu


class Tab:

  menu = {
    'wine': 10,
    'beer': 7,
    'soda': 3,
    'chicken': 19,
    'steak': 20,
    'pasta': 15,
    'lava-cake': 6
  }

  def __init__(self):
    self.total = 0
    self.items = []

  def add(self, item):
    self.items.append(item)
    self.total += self.menu[item]