# import database module
import os, csv
import sys

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


key_person = ['ID', 'first', 'last', 'type']
key_login = ['ID', 'username', 'password', 'role']
key_student = ['ID', 'role', 'pro_id']
key_faculty = ['ID', 'pro_id']
key_project = ['proName', 'proID', 'lead_ID', 'member1_id', 'member2_id', 'advisor', 'status']
key_pend_member = ['proName', 'proID', 'to_be_member', 'status']
key_pend_advisor = ['proName', 'proID', 'to_be_advisor', 'status']
key_pend_send = ['proID', 'proName', 'advisor', 'status']
key_pend_approve = ['proID', 'proName', 'faculty', 'status']
all_key = [key_person, key_login, key_student, key_faculty, key_project, key_pend_member, key_pend_advisor, key_pend_send, key_pend_approve]
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
    my_DB.insert(login)
    student_list = []
    # for i in login.table:
    #     if i['role'] == 'student':
    #         student_list.append(i)
    student_table = database.Table('student', read_file('student.csv'))
    my_DB.insert(student_table)
    # faculty_list = []
    # for i in login.table:
    #     if i['role'] == 'faculty':
    #         faculty_list.append(i)
    faculty_table = database.Table('faculty', read_file('faculty.csv'))
    my_DB.insert(faculty_table)
    project_table = database.Table('project', read_file('project.csv'))
    my_DB.insert(project_table)
    pending_table_member = database.Table('pending_member', read_file('pending_member.csv'))
    pending_table_advisor = database.Table('pending_advisor', read_file('pending_advisor.csv'))
    pending_send_project = database.Table('pending_project', read_file('pending_project.csv'))
    pending_approve_project = database.Table('approve_project', read_file('approve_project.csv'))
    my_DB.insert(pending_table_member)
    my_DB.insert(pending_table_advisor)
    my_DB.insert(pending_send_project)
    my_DB.insert(pending_approve_project)




# define a function called login

def login():
    username = input('username: ')
    password = input('password: ')
    DB_login = my_DB.search('login')
    for i in DB_login.table:
        if username == i['username'] and password == i['password']:
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
    def __init__(self, ID, role='student', pro_id=None, pro_name=None):
        self.ID = ID
        self.role = role
        self.pro_id = pro_id
        self.pro_name = pro_name

    def create_project(self):
        # student = my_DB.search('student')
        print('creating...')
        self.pro_name = input('Project name: ')
        self.pro_id = str(random.randint(1000, 9999))
        project = my_DB.search('project')
        project.table.append({'proName': self.pro_name, 'proID': self.pro_id, 'lead_ID': self.ID,
                              'member1_id': None, 'member2_id': None, 'advisor': None, 'status': 'in progress'})
        self.role = 'leader'
        login_table = my_DB.search('login')
        filter_login = login_table.filter(lambda x: x['ID'] == self.ID).table[0]
        filter_login['role'] = 'leader'
        self.leader_menu()

    def student_menu(self):
        print('Choose your role')
        print('1. creating new project')
        print('2. joined other project')
        option = get_option([1, 2],  'What do you want to choose: ')
        if option == '1':
            self.create_project()
        elif option == '2':
            self.student_check_request()
        elif option == '0':
            student_table = my_DB.search('student')
            this_student = student_table.filter(lambda x: x['ID'] == self.ID)
            update_info = {'ID': self.ID, 'role': self.role, 'pro_id': self.pro_id}
            if this_student.table:
                this_student.table[0] = update_info
            else:
                student_table.table.append(update_info)
            # exit_all()

    def leader_menu(self):
        print("Let's choose your choice!")
        print('1. inviting project member')
        print('2. inviting project advisor')
        print('3. checking status')
        print('4. checking project')
        print('5. sending project')
        print('0. log out')
        choice = int(get_option([0, 1, 2, 3, 4, 5], "What do you wanna choose: "))
        if choice == 1:
            self.send_request_member()
        elif choice == 2:
            self.send_request_advisor()
        elif choice == 3:
            self.lead_check_request()
        elif choice == 4:
            self.check_project()
        elif choice == 5:
            self.send_project()
        elif choice == 0:
            student_table = my_DB.search('student')
            this_student = student_table.filter(lambda x: x['ID'] == self.ID)
            update_info = {'ID': self.ID, 'role': self.role, 'pro_id': self.pro_id}
            if this_student.table:
                this_student.table[0] = update_info
            else:
                student_table.table.append(update_info)
            # exit_all()
        self.leader_menu()

    def member_menu(self):
        print('Welcome to our project.')
        print('1. implementing the project detail')
        print('0. log out')
        choice = int(get_option([0, 1], "What do you wanna choose: "))
        if choice == 0:
            self.check_project()
        elif choice == 0:
            student_table = my_DB.search('student')
            this_student = student_table.filter(lambda x: x['ID'] == self.ID)
            update_info = {'ID': self.ID, 'role': self.role, 'pro_id': self.pro_id}
            if this_student.table:
                this_student.table[0] = update_info
            else:
                student_table.table.append(update_info)
            # exit_all()
        self.member_menu()

    def send_request_member(self):
        pending = my_DB.search('pending_member')
        pend_list = pending.filter(lambda x: x['proID'] == self.pro_id and x['status'] in ['pending', 'accept'])
        if len(pend_list.table) == 2:
            print('You have already sent this request!')
        else:
            DB_student = my_DB.search('login')
            for i in DB_student.table:
                if i['role'] == 'student':
                    print(f"{i['username']:18}{i['ID']}")
            id_invitation = input('Type ID person that you want to choose: ')

            pending.table.append(
                {'proName': self.pro_name, 'proID': self.pro_id, 'to_be_member': id_invitation, 'status': 'pending'})

    def send_request_advisor(self):
        pending = my_DB.search('pending_advisor')
        pend_list = pending.filter(lambda x: x['proID'] == self.pro_id and x['status'] in ['pending', 'accept'])
        if pend_list.table:
            print('You have already sent this request!')
        else:
            DB_advisor = my_DB.search('login')
            id_faculty = [advisor['ID'] for advisor in DB_advisor.table if advisor['role'] == 'faculty']
            for i in DB_advisor.table:
                if i['role'] == 'faculty':
                    print(f"{i['username']:18}{i['ID']}")
            id_invitation = get_option(id_faculty, 'Type ID person that you want to choose: ')

            pending.table.append(
                {'proName': self.pro_name, 'proID': self.pro_id, 'to_be_advisor': id_invitation, 'status': 'pending'})

    def lead_check_request(self):
        print('Member')
        pending = my_DB.search('pending_member')
        all_request = [row for row in pending.table if row['proID'] == self.pro_id]
        if not all_request:
            print('You have not requested anyone yet.')
        else:
            for i in all_request:
                print(f'{i["to_be_member"]:<10}{i["status"]}')

        print('Advisor')
        pending = my_DB.search('pending_advisor')
        all_request = [row for row in pending.table if row['proID'] == self.pro_id]
        if not all_request:
            print('You have not requested anyone yet.')
        else:
            for i in all_request:
                print(f'{i["to_be_advisor"]:<10}{i["status"]}')

    def student_check_request(self):
        print('pending')
        print("Let's see who inviting you???")
        pending = my_DB.search('pending_member')
        all_request = [row for row in pending.table if row['to_be_member'] == self.ID]
        all_proID = [row['proID'] for row in all_request]
        if all_request:
            for i in all_request:
                print(i['proID'], i['proName'])
            choose = get_option(all_proID, 'What project id do you want to join: ')
            this_request = [row for row in all_request if row['proID'] == choose][0]
            other_request = [row for row in all_request if row['proID'] != choose]
            for row in other_request:
                row['status'] = 'deny'
            this_request['status'] = 'accept'
            project = my_DB.search('project')
            my_project = project.filter(lambda x: x['proID'] == choose).table[0]
            if my_project['member1_id'] is None:
                my_project['member1_id'] = self.ID
            else:
                my_project['member2_id'] = self.ID
            self.role = 'member'
            login_table = my_DB.search('login')
            filter_login = login_table.filter(lambda x: x['ID'] == self.ID).table[0]
            filter_login['role'] = 'member'
            self.pro_id = this_request['proID']
            self.member_menu()
        else:
            print('There is no invitation T__T')

    def check_project(self):
        project = my_DB.search('project')
        my_project = project.filter(lambda x: x['proID'] == self.pro_id).table[0]
        print()  ##### print project detail
        print(my_project['status'])
        ans = get_option(['y','n'], 'Do u want to change your project name')
        if ans == 'y':
            name = input('What name do you want to change: ')
            my_project['proName'] = name

    def send_project(self):
        project = my_DB.search('project')
        my_project = project.filter(lambda x: x['proID'] == self.pro_id).table[0]
        pending_send = my_DB.search('pending_project')
        check_accept = pending_send.filter(lambda x: x['proID']==self.pro_id and x['status'] == 'accept')
        check_pending = pending_send.filter(lambda x: x['proID'] == self.pro_id and x['status'] == 'pending')
        if my_project['advisor'] is None:
            print("Your project do not have advisor!")
        elif check_accept.table:
            print('This project have been approve by the advisor ')
        elif check_pending.table:
            print('Already sent')
        else:
            ans = get_option(['y', 'n'], "Are this project ready to submit: ")
            if ans == 'y':
                pending_send.table.append({'proID':self.pro_id, 'proName':my_project['proName'], 'advisor':my_project['advisor'], 'status':'pending'})


class Advisor:
    def __init__(self, ID, pro_id=None):
        self.ID = ID
        self.pro_id = pro_id

    def advisor_menu(self):
        print()
        print('1. check project')
        print('2. approving project')
        print('3. proposal')
        print('0 . log out')
        choice = int(get_option([0, 1, 2, 3], 'Which choice do you want to choose: '))
        if choice == 1:
            self.check_project()
        elif choice == 2:
            self.approve_project()
        elif choice == 3:
            self.check_submit()
        elif choice == 0:
            faculty_table = my_DB.search('faculty')
            this_faculty = faculty_table.filter(lambda x: x['ID'] == self.ID)
            update_info = {'ID': self.ID, 'pro_id': self.pro_id}
            if this_faculty.table:
                this_faculty.table[0] = update_info
            else:
                faculty_table.table.append(update_info)
            # exit_all()
        self.advisor_menu()

    def faculty_menu(self):
        print('Click the choice')
        print('1.checking pending request')
        print('2.approving the project')
        print('0.log out')
        choice = int(get_option([0, 1, 2], 'Which choice do you want to choose: '))
        if choice == 1:
            print("Let's see your pending request!")
            self.check_pending_status()
        elif choice == 2:
            # print("Let's see your project that you incharge")
            # project = my_DB.search('project')
            # for i in project.table:
            #     if self.ID == i['advi']:
            #         print(i['project name'], i[project])
            self.approve_project()
        elif choice == 0:
            faculty_table = my_DB.search('faculty')
            this_faculty = faculty_table.filter(lambda x: x['ID'] == self.ID)
            update_info = {'ID': self.ID, 'pro_id': self.pro_id}
            if this_faculty.table:
                this_faculty.table[0] = update_info
            else:
                faculty_table.table.append(update_info)
            # exit_all()
        self.faculty_menu()

    def check_pending_status(self):
        print('pending')
        print("Let's see who inviting you???")
        pending = my_DB.search('pending_advisor')
        all_request = [row for row in pending.table if row['to_be_advisor'] == self.ID]
        all_proID = [row['proID'] for row in all_request]
        if all_request:
            for i in all_request:
                print(i['proID'], i['proName'])
            choose = get_option(all_proID, 'What project id do you want to join: ')
            this_request = [row for row in all_request if row['proID'] == choose][0]
            other_request = [row for row in all_request if row['proID'] != choose]
            for row in other_request:
                row['status'] = 'deny'
            this_request['status'] = 'accept'
            self.pro_id = choose
            project = my_DB.search('project')
            my_project = project.filter(lambda x: x['proID'] == choose).table[0]
            my_project['advisor'] = self.ID
            login_table = my_DB.search('login')
            filter_login = login_table.filter(lambda x: x['ID'] == self.ID).table[0]
            filter_login['role'] = 'advisor'
            self.advisor_menu()
        else:
            print('There is no invitation T__T')

    def check_project(self):
        project = my_DB.search('project')
        my_project = project.filter(lambda x: x['proID'] == self.pro_id).table[0]
        print(my_project['status'])  ##### print project detail

    def check_submit(self):
        pending_send = my_DB.search('pending_project')
        my_submit = pending_send.filter(lambda x: x['advisor'] == self.ID and x['status'] == 'pending')
        if not my_submit.table:
            print('There is no submit.')
        else:
            my_submit = my_submit.table[0]
            print(f"{my_submit['proID']:<10}{my_submit['proName']}")
            option = get_option(['approve', 'deny'], 'Do you want to [approve or deny]: ')
            if option == 'deny':
                my_submit['status'] = 'deny'
            else:
                my_submit['status'] = 'approve'
                send_project = my_DB.search('approve_project')
                login_table = my_DB.search('login')
                id_faculty = [i['ID'] for i in login_table.table if i['role'] == 'faculty' or i['role'] == 'advisor']
                project = my_DB.search('project')
                print(self.pro_id)
                my_project = project.filter(lambda x: x['proID'] == self.pro_id).table[0]
                for id in id_faculty:
                    send_project.table.append({'proID':self.pro_id, 'proName':my_project['proName'], 'faculty':id, 'status':'on going'})

    def approve_project(self):
        send_project = my_DB.search('approve_project')
        my_approve = send_project.filter(lambda x: x['faculty'] == self.ID and x['status'] == 'on going')
        if not my_approve.table:
            print('There is no project to approve')
        else:
            for i in my_approve.table:
                print(f"{i['proName']:<10}{i['proID']}")
            list_id = [i['proID']for i in my_approve]
            choose = get_option(list_id, 'Which project do you want to approve: ')
            my_approve = my_approve.filter(lambda x: x['proID'] == choose).table[0]
            my_approve['status'] = 'approve'
            all_approve = send_project.filter(lambda x: x['proID'] == choose and x['status'] == 'approve')
            print(all_approve)
            if len(all_approve.table) == 3:
                project = my_DB.search('project')
                this_project = project.filter(lambda x: x['proID'] == choose).table[0]
                this_project['status'] = 'complete'
                other_approve = send_project.filter(lambda x: x['proID'] == choose and x['status'] == 'on going')
                other_id = [i['faculty'] for i in other_approve.table]
                for i in other_id:
                    send_project.table.remove({'proID':choose, 'proName':this_project['proName'], 'faculty':i, 'status':'on going'})





class Admin:
    def __init__(self, ID):
        self.id = ID

    def menu(self):
        print("Let's see what you can do")
        print("1. add account")
        print("2. delete account")
        choice = int(get_option([1, 2], 'What do you want to do: '))
        if choice == 1:
            name = input('Surname: ')
            last = input('Lastname: ')
            username = name + '.' + last[0].upper()
            role = get_option(['student', 'faculty'], 'Which role do you want to be: ')
            login_table = my_DB.search('login')
            login_table.table.append({'ID': random.randint(1000000, 9999999), 'username': username,
                                      'password': random.randint(1000, 2000), 'role': role})
        elif choice == 2:
            pass







def exit_all():
    for i in range(len(my_DB.database)):
        table = my_DB.database[i]
        exit_csv(table.table_name, table.table_name, all_key[i])
    sys.exit()



def exit_csv(file, table, head):
    myFile = open(f"{file}.csv", 'w')
    writer = csv.writer(myFile)
    writer.writerow(head)
    for dictionary in my_DB.search(table).table:
        writer.writerow(dictionary.values())
    myFile.close()
#
# def exit():
#     pass

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
   
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above
initializing()



# Student(val).student_menu()
# Admin(val).menu()
# Advisor(val).menu()

# exit_csv("login", my_DB.search("login").table)
# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

def role():
    val = login()
    if val is None:
        print('Incorrect user')
        role()
    if val[1] == 'admin':
        Admin(val).menu()
    elif val[1] == 'student':
        info = student(val[0])
        if info is None:
            Student(val[0]).student_menu()
        else:
            Student(info[0], info[1], info[2], info[3]).student_menu()
    elif val[1] == 'member':
        info = student(val[0])
        if info is None:
            Student(val[0]).member_menu()
        else:
            Student(info[0], info[1], info[2]).member_menu()
    elif val[1] == 'leader':
        info = student(val[0])
        if info is None:
            Student(val[0]).leader_menu()
        else:
            Student(info[0], info[1], info[2]).leader_menu()
    elif val[1] == 'faculty':
        info = faculty(val[0])
        if info is None:
            Advisor(val[0]).faculty_menu()
        else:
            Advisor(info[0], info[1]).faculty_menu()
    elif val[1] == 'advisor':
        info = faculty(val[0])
        if info is None:
            Advisor(val[0]).advisor_menu()
        else:
            Advisor(info[0], info[1]).advisor_menu()


def student(id):
    student_table = my_DB.search('student')
    this_student = student_table.filter(lambda x: x['ID'] == id)
    if not this_student.table:
        return None
    return list(this_student.table[0].values())


def faculty(id):
    faculty_table = my_DB.search('faculty')
    this_faculty = faculty_table.filter(lambda x: x['ID'] == id)
    if not this_faculty.table:
        return None
    return list(this_faculty.table[0].values())

role()
# once everyhthing is done, make a call to the exit function

