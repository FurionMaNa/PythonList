from prettytable import PrettyTable

class Book:

    id=0
    name=""

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Author:

    id=0
    name=""

    def __init__(self, id, name):
        self.id = id
        self.name = name

class AuthorBook:

    idAuthor=[]
    idBook=0

    def __init__(self,idBook ,idAuthor ):
        self.idAuthor = idAuthor
        self.idBook = idBook

def findByAuthor(name,book,author,authorBook):
    s=True
    f=False
    id=[]
    tableBook = PrettyTable()
    tableBook.field_names = ['id', 'Название']
    for i in author:
        if(name==i.name):
            for j in authorBook:
                for l in j.idAuthor:
                    if(l==i.id):
                        for k in book:
                            if(k.id==j.idBook):
                                f=True
                                for t in id:
                                    if(t==k.id): f=False
                                if(f):
                                    s = False;
                                    tableBook.add_row([k.id, k.name])
    if(s): return  "Ничего не найдено!"
    return tableBook

def findByName(name,book):
    s=True
    tableBook = PrettyTable()
    tableBook.field_names = ['id', 'Название']
    for i in book:
        if(name==i.name):
            s=False
            tableBook.add_row([i.id, i.name])
    if(s): return  "Ничего не найдено!"
    return tableBook

book=[]
author=[]
authorId=[]
authorBook=[]
while True:
    while True:
        idBook=input("Введи id книги: ")
        nameBook=input("Введи название книги: ")
        newBook=True
        if(len(book)!=0):
            for i in book:
                if(i.id==idBook):
                    newBook=False
                    print("Такой номер уже есть!")
                    break
        if(newBook):
            book.append(Book(idBook,nameBook))
            break
    while True:
        idAuthor=input("Введи id автора: ")
        nameAuthor=input("Введи имя автора: ")
        newAuthor = True
        if (len(author) != 0):
            for i in author:
                if (i.id == idAuthor):
                    newAuthor = False
                    print("Такой номер уже есть!")
                    break
        if (newAuthor):
            author.append(Author(idAuthor,nameAuthor))
            authorId.append(idAuthor)
            exits=input("Указать ещё одного автора?(0-Да,1-Нет) ")
            if(exits=="1"):
                authorBook.append(AuthorBook(idBook,authorId))
                authorId=[]
                break
    exits=input("Указать ещё одну книгу?(0-Да,1-Нет) ")
    if(exits=="1"):
        break

tableBook = PrettyTable()
tableBook.field_names=['id','Название']
for i in book:
    tableBook.add_row([i.id,i.name])
print("Книги:")
print(tableBook)

tableAuthor = PrettyTable()
tableAuthor.field_names=['id','Имя']
for i in author:
    tableAuthor.add_row([i.id,i.name])
print("Авторы:")
print(tableAuthor)

tableAuthorBook = PrettyTable()
tableAuthorBook.field_names=['idКниги','idАвторов']
for i in authorBook:
    tableAuthorBook.add_row([i.idBook,i.idAuthor])
print("книги авторов:")
print(tableAuthorBook)

while True:
    while True:
        search=input("Найти по автору(0) или по названию(1)? ")
        if(search=="0"):
            name=input("Введи имя автора: ")
            print(findByAuthor(name,book,author,authorBook))
            break
        elif(search=="1"):
            name=input("Введи название книги: ")
            print(findByName(name,book))
            break
        else:
            print("Такого варианта нет!")

    exits = input("Искать книгу ещё раз?(0-Да,1-Нет) ")
    if (exits == "1"): break

