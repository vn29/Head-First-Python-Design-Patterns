# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod

#observer pattern practice

#subject class
class Subject(ABC):
  
  @abstractmethod
  def registerObserver(self):pass
  @abstractmethod  
  def removeObserver(self):pass
  @abstractmethod  
  def notifyObservers(self):pass

#WeatherData class  
class WeatherData(Subject):
  temperature= 0
  humidity=0
  pressure=0
  
  def __init__(self):
    self.observers = []
  
  def registerObserver(self,o):
    self.observers.append(o)
  
  def removeObserver(self,o):
    if length(self.observers) >=0:
      self.observers.remove(o)
  
  def notifyObservers(self):
    for e in self.observers:
      e.update(self.temperature,self.humidity,self.pressure)
      
  
  def getTemperature(self):pass
    
  def getHumidity(self):pass
    
  def getPressure(self):pass
  
  def measurementsChanged(self):
    self.notifyObservers()

  def setMeasurements(self,temperature,humidity,pressure):
    self.temperature = temperature
    self.humidity = humidity
    self.pressure = pressure
    self.measurementsChanged()
    
#observer calss   
class Observer(ABC):
  @abstractmethod
  def update(self):pass

#DisplayElement class
class DisplayElement(ABC):
  @abstractmethod
  def display(self):pass

#
class CurrentConditionsDisplay(Observer,DisplayElement):
  temperature= 0
  humidity=0
  weatherData=0
  
  def __init__(self,weatherData):
    self.weatherData = weatherData
    weatherData.registerObserver(self)
  
  
  def update(self,temperature,humidity,pressure):
    self.temperature = temperature
    self.humidity = humidity
    self.display()
  
  def display(self):
    print("current conditions: {0}F degrees and {1}% humidity".format(self.temperature,self.humidity))
    
  
  
class WeatherStation():
  def main(self):
    weatherData = WeatherData()
    
    currentDisplay = CurrentConditionsDisplay(weatherData)
    
    weatherData.setMeasurements(80,65,30.4)
    weatherData.setMeasurements(980,65,30.4)


ws = WeatherStation()

ws.main()