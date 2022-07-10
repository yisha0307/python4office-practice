class Person:
    def __init__(self, fname,lname):
       self.fname = fname
       self.lname = lname


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)

x = Student('yisha', 'chen', 2012)
x.welcome()