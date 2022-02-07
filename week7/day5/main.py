# class BankAccount:
#     def __init__(self, balance):
#         self.balace = balance

#     def withdrow(self):






#  Напишите класс ToDoList для списка завершенных заданий.
#  Каждое задание (имплементируется для этого есть класс Task), он состоит возвращает стринг кот-е описывает задание и срочность (Priority) этих заданий: 1(очень низкая), 2(низкая), 3(средняя), 4(высокая), 5(очень высокая).
#  Конструктор принимает два аттрибута, по дефолту срочность будет 3.

# Есть три метода, 
#-   Put кот-й добавляет таск в конец списка ToDoList.
#-   Get который выдает самый срочный таск т.е 5, если его нет то 4. Если нет ничего то None
#-   Count выдает кол-во тасков в ToDoList, если в параметр указать Priority, должны быть посчитаны лишь те Tasks, срочность кот-х соответсвует требуемости. Как default argument вы можете взять 1; а если срочность не лежит на интервале от 1 до 5, то выдайте 0.
#Используйте обычный Python-List внутренний тип данных ToDoList, для GET используйте оператор '<'. 
#Т.е Task меньше другого Task, когда его срочность ниже. Используйте str, чтобы получить результат каждого таска, а так же общий лист. 

# class Replace(int):
#     def __init__(self, num1):
#         self.num1 = num1
        
#     def __add__(self, other):
#         return f'minus {self.num1 - other.num1}'

#     def __sub__(self, other):
#         return f'plus {self.num1 + other.num1}'
#     def __truediv__(self, other):
#         return f'multiply {self.num1 * other.num1}'
#     def __mul__(self, other):
#         return f'del {self.num1 / other.num1}'

# obj1 = Replace(10)
# obj2 = Replace(5)
# print(obj1+obj2)
# print(obj1 / obj2)
# print(obj1 * obj2)
# print(obj1 - obj2)


# Создайте класс KgToPounds с параметром kg, куда передается определенное количество килограмм, 
# а с помощью метода to_pounds() они переводятся в фунты. Закройте доступ к переменной “kg”.
# Напишите методы set_kg() - для задания нового значения килограммов,
#  get_kg() - для вывода текущего значения кг  с использованием функции property() и свойств-декораторов.


# class KgToPounds:
    
#     def init(self, kg):
#         self.__kg = kg

#     @property
#     def get_kg(self):
#         return self.__kg

#     @get_kg.setter
#     def set_kg(self, new_kg):
#         self.__kg = new_kg
#         return self.__kg

#     def to_pounds(self):
#         pounds = self.__kg * 2.2
#         return pounds

# obj = KgToPounds(20)
# # print(obj.to_pounds())
# obj.set_kg = 5
# print(obj.to_pounds())


from functools import reduce

class Task:
    def __init__(self, task, priority=3):
        self.task = task
        self.priority = priority

    def __str__(self):
        return f'i have to {self.task} and its priority level is: {self.priority}'

    
class ToDoList:
    
    
    def __init__(self):
        self.tasks = []

    def put(self, todo):
        self.tasks.append(todo)


    def get(self):
        if not (get:= [[i.task, i.priority] for i in self.tasks]):
            return None

        max_value = list(reduce(lambda x, y:x if y[1] < x[1] else y, get))
        return f'in my highest priority is to {max_value[0]}'

    def count(self, priority=0):
        self.priority = priority
        self.counts = []

        for i in self.tasks:
            if i.priority == self.priority:
                self.count.append()
                print(i)

            else:
                self.priority = 0
            
        return f'i have {len(self.counts)} tasks with {self.priority} priority level'

me = ToDoList()
task1 = Task('buy a milk')
task2 = Task('visit my parents', 4)
task3 = Task('play with my cat', 5)
task4 = Task('feed animals', 4)

me.put(task1)
me.put(task2)
me.put(task3)
me.put(task4)
print(me.get())
print(me.count(5))