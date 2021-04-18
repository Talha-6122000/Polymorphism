# Polymorphism 
# Many forms
class User:
  def sign_in(self):
    print("Logged In")
class Wizard(User):
  def __init__(self,name,power):
    self.name=name
    self.power=power
  def attack(self):
    print(f'Player Name is:{self.name}')
    print(f'Attackig with Power:{self.power}')
class Archar(User):
  def __init__(self,name,power):
    self.name=name
    self.power=power
  def attack(self):
    print(f'Player Name is:{self.name}')
    print(f'Attackig with Arrows:{self.power}')

wizard=Wizard("Talha","80")
archar=Archar("Hassan",90)

# Now here come the polymorphism
def player_attack(char):
  char.attack()
player_attack(wizard)
player_attack(archar)