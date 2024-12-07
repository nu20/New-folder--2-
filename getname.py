class Ishaan:
   __age = 18
   def __init__(self , name , grade) :
      self.__name = name
      self.__grade = grade

   def setName(self , newName) :
      self.__name = newName
 
   def setGrade(self , newGrade) :
      self.__name = newGrade

   def getName(self) :
      print(self.__name)

   def getGrade(self) :
    print(self.__grade)

obj = Ishaan("thor")
obj.getName()
obj.setName("spider man")
obj.getName()
