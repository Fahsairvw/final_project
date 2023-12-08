# import database module
import os, csv
import database
import random
# define a funcion called initializing
my_DB = database.Database()
# here are things to do in this function:


def read_file(file):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    # create an object to read an input csv file, persons.csv
    _list = []
    with open(os.path.join(__location__, file)) as f:
        rows = csv.DictReader(f)
        for r in rows:
            _list.append(dict(r))
    return _list


def initializing():
    persons_list = read_file('persons.csv')
    persons = database.Table('persons', persons_list)
    # print(persons)
    # add the 'persons' table into the database
    my_DB.insert(persons)
    # print(persons.table)
    # create a 'login' table
    login_list = read_file('login.csv')
    login = database.Table('login', login_list)
    print(login.table)
    my_DB.insert(login)
    student_list = []
    for i in login.table:
        if i['role'] == 'student':
            student_list.append(i)
    student_table = database.Table('student', student_list)
    my_DB.insert(student_table)
    faculty_list = []
    for i in login.table:
        if i['role'] == 'faculty':
            faculty_list.append(i)
    faculty_table = database.Table('faculty', faculty_list)
    my_DB.insert(faculty_table)
    pending_table = database.Table('pending', [])
    my_DB.insert(pending_table)
    project_table = database.Table('project', [])
    my_DB.insert(project_table)




# define a function called login

def login():
    username = input('username: ')
    password = input('password: ')
    DB_login = my_DB.search('login')
    for i in DB_login.table:
        if username == i['username'] and password == i['password']:
            print([i['ID'], i['role']])
            return [i['ID'], i['role']]
    print('Invalid')
    return None

# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None

# define a function called exit


def get_option(_list, massage):
    a = input(massage)
    while a not in str(_list):
        a = input(massage)
    return a


class Student:
    def __init__(self, username, role='student'):
        self.role = role
        self.username = username


    def create_project(self):
        login = my_DB.search('login')
        print('creating...')
        for i in login:
            if self.username == i['username']:
                i['role'] = 'leader'
        project_name = input('Project name: ')
        project_id = random.randint(1000,9999)
        return project_id, project_name



    def check_request(self):
        print('pending')

    def student_menu(self):
        print('Choose your role')
        print('1. creating new project')
        print('2. joined other project')
        option = get_option([1, 2],  'What do you want to choose: ')
        if option == '1':
            self.create_project()
        elif option == '2':
            self.check_request()
class Project:
    def __init__(self, title, leader):
        self.title = title
        self.leader = leader
        self.member1 = None
        self.member2 = None
        self.advisor = None
        self.status = 'pending'








# def exit_csv(file, table, head):
#     myFile = open(f"{file}.csv", 'w')
#     writer = csv.writer(myFile)
#     writer.writerow(head)
#     for dictionary in my_DB.search(table).table:
#         writer.writerow(dictionary.values())
#     myFile.close()
#
# def exit():
#     pass

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
   
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above
initializing()
val = login()

# exit_csv("login", my_DB.search("login").table)
# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# def role():
#     if val[1] = 'admin':
#         see and do admin related activities
    # elif val[1] = 'student':
        # see and do student related activities
    # elif val[1] = 'member':
        # see and do member related activities
    # elif val[1] = 'lead':
        # see and do lead related activities
    # elif val[1] = 'faculty':
        # see and do faculty related activities
    # elif val[1] = 'advisor':
        # see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit()
