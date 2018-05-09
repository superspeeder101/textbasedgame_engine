import base

class Location(object):
  def __init__(self, x, y, name, game):
    self.game = game
    self.name = name
    self.pos = (x,y)
    
    
    self.game.registerLocation(self, self.name, self.pos)
    
class Event(object):
  pass

class Action(object):
  pass

class Item(object):
  pass

class Inventory(base.DataContainer):
  pass

class MainParser(base.BaseParser):
  pass

class Map(object):
  pass

class Game(base.DataContainer):
  def __init__(self, map_, stateMachine, inventory):
    self.map = map
    self.stateMachine = stateMachine
    self.inventory = inventory
    
    self.registerType("location", cls=Location, adder=self._locationAdder, remover=self._locationRemover)
    self.registerType("item", cls=Item, adder=self.inventory.addItem, remover=self.inventory.removeItem)
    self.registerType("action", cls=Action, adder=self._actionAdder, remover=self._actionRemover)
    

class StateCondition(base.Conditional):
  pass

class State(base.EnumObject):
  pass

class StateEnum(base.Enum):
  pass

class StateMachine(base.Decider):
  def __init__(self, stateEnum):
    self.optionEnum = stateEnum
    
    self.generateConditionTester()

class Scene(base.DataContainer):
  pass
