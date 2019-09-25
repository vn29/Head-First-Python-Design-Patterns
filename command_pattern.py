#command pattern

class Remote():
  payload = 0
  state = False
  def __init__(self,commandObject,state):
    self.state = state
    self.payLoad = commandObject
  
  
  def execute(self):
    if self.state == True:
      self.payLoad.execute()
    
class LightsOn():
  def execute(self):
    print("lights are on")

lightsOnCommand = LightsOn()

remote = Remote(lightsOnCommand,True)

remote.execute()
