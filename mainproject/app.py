documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "invoice", "number": "11-2", "": "Конюх Игорев"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def number_by_name(numbers):
  unser_input = input('Введите необходимый номер документа')
  usercount = 0
  for number in numbers:
    if number['number'] == str(unser_input):
      print('Владелец документа:', number['name'])
      usercount = 1
  if usercount == 0:
    print('Запрошен несуществующий документ')

def shelf_number(shelfs):
  unser_input = input('Введите необходимый номер документа')
  doccount = 0
  for key_shelf , docnumber in shelfs.items():
    for docnum in docnumber:
      if docnum == str(unser_input):
        print('Номер полки нахождения документа:', key_shelf)
        doccount = 1
  if doccount == 0:
    print('Запрошен несуществующий документ')

def list_docs(docs):
  data = []
  for allinf in docs:
    for values in allinf.values():
      data.append(values)
  print(data)

def add_documents(docs, shelfs):
  document_type = input('Введите тип документа ')
  document_number = input('Введите номер документа ')
  document_owner = input('Введите фамилию и имя владельца документа ')
  shelf_nmbr = input('Введите номер полки документа ')
  key_shelf_list = []
  new_documents_dict = {}
  for key_shelf in shelfs.keys():
    key_shelf_list.append(key_shelf)
  if shelf_nmbr not in key_shelf_list:
      print('Введен несуществующий номер полки')
  else:
    new_documents_dict['type'] = document_type
    new_documents_dict['number'] = document_number
    new_documents_dict['name'] = document_owner
    documents.append(new_documents_dict)
    directories[shelf_nmbr].append(document_number)
    print(documents)
    print(directories)

def delete_documents(docs, shelfs):
  document_number = input('Введите номер удаляемого документа ')
  for index in range(len(docs)):
    if docs[index]["number"] == document_number:
      del docs[index]
      print(docs)
      break
  temp = []
  for value in shelfs.values():
    for val in value:
      temp.append(val)
  if document_number not in temp:      
    print('Номер документа не существует')
  for value in shelfs.values():
    for indexes in range(len(value)):
      if value[indexes] == document_number:
        del value[indexes]
        print(value)
        break

def move_documents(shelfs):
  user_docnmun = input('Введите номер перемещаемого документа ')
  user_shelfnum = input('Введите номер полки для перемещения ')
  for value in shelfs.values():
    if user_docnmun in value:
      value.remove(user_docnmun)
      for shelf_num in shelfs.keys():
        if user_shelfnum in shelf_num:
          shelfs[user_shelfnum].append(user_docnmun)
        break
      shelfs[user_shelfnum] = [user_docnmun]
      break  
    else:
      print('Номер документа не существует')
      break

def add_shelf(shelfs):
  user_shelfnum = input('Введите номер новой полки ')
  for shelf_num in shelfs.keys():
    if user_shelfnum not in shelf_num:
      shelfs.setdefault(user_shelfnum, [])
      break
    else:
      print('Номер полки уже существует')
      break

def get_name(docs):
    for doc_dict in docs:
      try:
        print(doc_dict['name'])
      except KeyError:
        print(f'Отсутствует поле "name" в документе {doc_dict.values()}')
        continue


def main():
  print('p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит\n'
  's – (shelf) – команда, которая спросит номер документа и выведет номер полки, на которой он находится\n'
  'l– (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Пупкин"\n'
  'a – (add) – команда, добавляющая новый документ в каталог\n'
  'q - (quit) - выход из программы\n'
  'd - (delete) - команда удаления документа из каталога и перечня полок\n'
  'm - (move) - команда для перемещения документа на другую полку\n'
  'as - (add shelf) – команда, для создания новой полки\n'
  'n - (name – команда, для вывода всех ФИО пользователей')
  while True:
    user_input = input('Введите команду ')
    if user_input == 'p':
      number_by_name(documents)
    elif user_input == 's':
      shelf_number(directories)
    elif user_input == 'l':
      list_docs(documents)
    elif user_input == 'a':
      add_documents(documents, directories)
    elif user_input == 'd':
      delete_documents(documents, directories)
    elif user_input == 'm':
      move_documents(directories)
    elif user_input == 'as':
      add_shelf(directories)
    elif user_input == 'n':
      get_name(documents)
    elif user_input == 'q':
      break

if __name__ == "__main__":
  main()