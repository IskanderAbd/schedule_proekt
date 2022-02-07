# print(10+25)
# print('hello' + 'world')

# class GrandPa:
#     def get_info(self):
#         print('hello, is GrandPa class')


# class Parent(GrandPa):
#     def get_info(self):
#         print('hello, is Parent class')

# class Child(Parent):
#     def get_info(self):
#         print('hello, is Child class')

# obj_grand = GrandPa()
# obj_parent = Parent()
# obj_child = Child()

# obj_grand.get_info()
# obj_parent.get_info()
# obj_child.get_info()


# class A:

#     def hello(self):
#         raise NotImplementedError

# class B(A):
#     def hello(self):

#         print('hello, world')

# obj_b = B()
# obj_b.hello()

# class Worker:
#     def get_salary(self):
#         raise NotImplementedError()

# class ITSphere(Worker):
#     def __init__(self, salary):
#         self.salary = salary
#     def get_salary(self):
#         print(f'Salary is: {self.salary}')
        

# class HRDepartment(Worker):
#     pass

# class Driver(Worker):
#     pass

# # obj_it = ITSphere(1500)
# # obj_it.get_salary()
# obj_hr = HRDepartment()
# obj_hr.get_salary()


# class King:

#     @staticmethod
#     def move():
#         print('Ya hoju na odnu kletku v lubuu storonu')
    
# class Queen:
#      @staticmethod
#      def move():
#          print('ya hoju kak queen')

# class Horse:

#     @staticmethod
#     def move():
#         print('ya hoju bukvoi G')

# figure_1 = King()
# figure_2 = Queen()
# figure_3 = Horse()
# for figure in [figure_1, figure_2, figure_3]:
#     figure.move()

# ------------------


from abc import ABC, abstractmethod
from cmath import pi

class Pizza(ABC):
    def __init__(self, pizza, cost):
        self.pizza = pizza
        self.cost = cost
    
    @abstractmethod
    def add_extra(self, ingridient):
        self.ingridient = ingridient
        print(f'{self.pizza} with extra {self.ingridient} costs {self.cost}')

# obj_1 = Pizza('chilling', 1500)

class DodoPizza(Pizza):
    def add_extra(self, *ingridient):
        self.cost += 50 * len(ingridient)
        return super().add_extra(ingridient)
    @staticmethod
    def late(time):
        if time >= 5:
            print('You get free pizza card!!!')

class PapaJohns(Pizza):
    def add_extra(self, *ingridient):
        self.cost += 70 * len(ingridient)
        return super().add_extra(ingridient)

    def late(self, time):
        if time >= 100:
            print(f'this pizza is free')
        
        else:
            self.cost = self.cost - (self.cost * time /100)

# pizza_1 = DodoPizza('Peperoni', 500)
# pizza_1.add_extra('cheese', 'sauce', 'pepperoni')
# pizza_1.late(6)

pizza_2 = PapaJohns('marrgarita', 400)
pizza_2.add_extra('tomatos', 'bazil')
pizza_2.late(20)
print(pizza_2.cost)