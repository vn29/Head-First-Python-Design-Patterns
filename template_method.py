
#tempate method. The algo class is inhereted by the Subclasses which each define their own methods to run at their
#respective parts of the algorithm
class Algo():
  def __init__(self):
    self.s1()
    self.s2()
    self.s3()
    self.s4()
    
  def s1(self): print("s1 abstract")
  def s2(self): raise NotImplementedError
  def s3(self): print("s3 abstract")
  def s4(self): raise NotImplementedError
    
class SubClass1(Algo):
  def s2(self):
    print("this is subclass 1 method")
    
  def s4(self):
    print("this is subclass 1 method")
    
class SubClass2(Algo):
  def s2(self):
    print("this is subclass 2 method")
    
  def s4(self):
    print("this is subclass 2 method")

    
SC1 = SubClass1()
SC2 = SubClass2()
