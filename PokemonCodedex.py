# Write code below 💖

class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

    if self.is_caught:
      print(self.name + " has already been caught!")
    else:
      print(self.name + "hasn't been caught!")

  def speak(self):
    print(self.name + ', ' + self.name)

  def display_details(self):
    print(f"Entry Number: {self.entry}\nName: {self.name}\nType: {self.types}\nDescription: {self.description}")

pikachu = Pokemon(25, "Pikachu", "Electric", "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.", True)
charizard = Pokemon(6, "Charizard", "Fire/Flying", "Large fiery dragon", True)
treecko = Pokemon(252, "Treecko", "Grass", "Small little frog that does karate!", False)

pikachu.speak()
charizard.speak()
treecko.speak()

pikachu.display_details()
charizard.display_details()