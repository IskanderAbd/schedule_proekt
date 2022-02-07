# class A:
#     pass
#     # def hello(self):
#     #     print('hello im class A')

# class B:
#     def hello(self):
#         print('hello im class B')

# class C(A, B):  ----sleva na pravo
#     pass

# obj = C()
# obj.hello()

# class MomParent:
#     def mom_parents_info(self):
#         print('roditeli mamy')

# class DadParent:
#     def dad_parent_info(self):
#         print('roditeli otca')

# class Mom(MomParent):
#     def mom_info(self):
#         print('mama')
    
# class Dad(DadParent):
#     def dad_info(self):
#         print('otec')
    
# class Child(Mom, Dad):
#     def child_info(self):
#         print('rebonok')

# child = Child()
# # child.mom_parents_info()
# # child.dad_info()
# # child.child_info

# # mro() method resolution order()
# print(Child.mro())


# problema romba(diamond problem)
# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
#     pass

# obj = D()
# print(D.mro())



# class SoundMixin:
#     def sound(self):
#         print('Sound')
    
# class People(SoundMixin):
#     pass

# class Animal(SoundMixin):
#     pass

# class Car(SoundMixin):
#     pass


# obj_people = People()
# obj_animal = Animal()
# obj_car = Car()

# for obj in [obj_people, obj_animal, obj_car]:
#     obj.sound()

# class A:
#     def hello(self):
#         print('hello class A')


# class B:
#     def hello(self):
#         print('hello, class B')

# class C:
#     def hello(self):
#         print('hello, class C')

# class D(A,B,C):
#     def hello(self):
#         # super().hello()
#         # super().helloB()
#         # super(A, self).hello()
#         B.hello(self)
#         print('hello, class D')

# obj_d = D()
# obj_d.hello()


# class DataBase:

#     db = {}
   

#     def create(self, name, password):
#         self.db[name] = password
#         return self.db

#     def read(self):
#         return self.db

#     def update(self, name, new_password):
#         self.db[name]= new_password
#         return self.db

#     def delete(self, name):
#         self.db.pop(name)
#         return self.db

# obj = DataBase()
# obj.create('john', '12345')
# obj.update('john', 'new123')
# obj.delete('john')
# print(obj.read())

# class A:
#     def site(self,name):
#         self.name = name
#         if name == 'vesti.kg':
#             res = input('kod? or text?')
#             if res == 'kod':
#                 print(200)
#             elif res == 'text':
#                 print('text')



# class GetResponse:
#     def get_site_info(self, site, answ):
#         import requests
#         url = ''
#         if site =='v':
#             url = 'https://vesti.kg'
#         elif site == 'e':
#             url = 'https://enter.kg'
#         elif site == 'k':
#             url = 'https://kivano.kg'
#         response = requests.get(url)
#         if answ =='s':
#             return response.status_code

#         elif answ == 't':
#             return response.text

#     def main(self):
#         site = input('choose site from(vesti.kg(v), enter.kg(e), kivano.kg(k): ')
#         code_or_text = input('get status code(s) or text(t): ')
#         print(self.get_site_info(site, code_or_text))

# obj = GetResponse()
# obj.main()


class InstructionMixin:
    @staticmethod
    def get_info():
        print('''Класс для просмотра информации о фильмах, доступны методы:
                create_film - создание поста о фильме,
                get_all_films - получение списка всех фильмов
                filter_films - фильтрует по категории фильмы,
                search films - поиск фильмов по седержанию или заголовку!''')

class FilmBlog(InstructionMixin):
    db = [
        {'title': 'Fast&Furios2', 'body': 'Film about cars', 'category': 'action', 'author': 'Admin', 'created_on': '2022-01-28'},
        {'title': 'Harry Potter', 'body': 'Film about Harry', 'category': 'fantastic', 'author': 'Admin', 'created_on': '2022-01-28'},
        {'title': 'Marvel', 'body': 'Film about Marvel', 'category': 'adventure', 'author': 'Admin', 'created_on': '2022-01-28'}
    ]

    def __init__(self, user):
       self.user = user
       print('polzovatel inicializirovan!')
       super().get_info()

    def create_film(self):
        from datetime import datetime
        title = input('zagolovok filma: ')
        body = input('opisanie filma: ')
        category = input('janr filma: ').lower()
        film = {
           'title' : title,
           'body' : body,
           'category': category,
           'author': self.user,
           'created_on': str(datetime.date(datetime.now()))
        }
        self.db.append(film)
        print('film uspeshno dobavlen')
        FilmBlog.get_all_films(self)

    def  get_all_films(self):
        for film in self.db:
            print(film)
    def filter_films(self):
        category = input('vvedete categoriu: ')
        films = list(filter(lambda x:x['category'] == category.lower(), self.db))
        for film in films:
            print(film)
    def search_films(self):
        search = input('enter some word from title or body: ')
        films = list(filter(lambda x: search in x['title'].lower() or search.lower() in x['body'].lower(), self.db))
        for film in films:
            print(film)
user_tom  = FilmBlog('Tom')
# user_tom = 
user_tom.filter_films()
user_tom.search_films()