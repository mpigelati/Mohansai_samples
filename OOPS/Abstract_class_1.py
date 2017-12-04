from abc import ABC, abstractmethod

class Employee(ABC):

      @abstractmethod

      def calculate_salary(self,sal):

          pass
class Developer(Employee):

    def calculate_salary(self,sal):
        finalsalary=sal * 1.10
        return finalsalary
    def  position_1(self,position):
        #self.position=position # both way we can use this
        position = position
        return position

emp1=Developer()
print(emp1.calculate_salary(10000))
print(emp1.position_1("python_dev"))