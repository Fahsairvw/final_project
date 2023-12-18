# Final project for 2023's 219114/115 Programming I
* Starting files for part 1
  - database.py
  - project_manage.py
  - persons.csv
**For class of student**
  - project_manage.py for running all the code
  - login.csv for login 
  - approve_project.csv for checking status of the project
  - faculty.csv for checking who is the advisor for each student project
  - pending_advisor.csv for sending request asking the faculty to become a project advisor
  - pending_member.csv for sending request asking the student to become  project members
  - pending_pro.csv for sending request asking the advisor to approve the project
  - project.csv for checking the project member
  - student.csv for checking their role
  - database.py to search for the table and to append every thing in the table
  
**For class of advisor**
- project_manage.py for running all the code
- approve_project.csv for sending the project proposal to the other faculty to approve the project 
  and also suing for the other faculty to approve the project
- faculty.csv for checking all the faculty status 
- login.csv for login to their role
- pending_advisor.csv for checking their pending status to become an advisor
- pending_project.csv for approving their proposal 

**For the admin class**
- project_manage.py for running all the code
- database.py to add and delete new person/ project in login.csv and person.csv
- pending_advisor.csv, pending_member.csv, project.csv to delete the project

Another file
-TODO for telling function for each role
-proposal for telling each step for project to pass

**To compile my code** 
To begin with, the first student who log in should create the new project then become a leader.
Secondly, leader will need to request 2 members and 1 advisor for his project.
Thirdly, members and advisor choose to accept their pending request.
Moreover, leader and member checking their project proposal then send to the advisor.
Next, the project advisor will decide to approve or not.
Then, if the project is approved, the advisor sent the proposal to the other faculty 
and waiting for the approval.Finally, project will be complete after three of the faculty approve.
for more information, please read the TODO and proposal. Sorry for the short description, I have doctor appointment
which can not be postponed because my hand is bleeding.


|  Role |  Action | Method  | Class |  Completion Percentage|
|---|---|---|---|---|
| Admin  | menu and edit info | menu | Admin  | 95 % |
| leader  | create project  | create_project | Student  | 100 % |
| leader  | get project id, name  | project_info | Student  | 100 % |
| student  | menu  | student_menu | Student  | 100 % |
| leader  | menu  | leader_menu | Student  | 100 % |
| member | menu  | member_menu | Student | 100 % |
| leader  | sent member request  | send_request_member | Student | 100 % |
| leader  | sent advisor request  | send_request_advisor | Student | 100 % |
| leader  | check request  | lead_check_request | Student | 100 % |
| student  | check request  | student_check_request | Student | 100 % |
| leader  | check project  | check_project | Student | 100 % |
| leader  | sent request proposal | sent_project | Student | 100 % |
| advisor/faculty  | get project id  | project_info | Advisor | 100 % |
| advisor  | menu  | advisor_menu | Advisor | 100 % |
| faculty  | menu  | faculty_menu | Advisor | 100 % |
| faculty  | check request  | check_pending_status | Advisor | 100 % |
| faculty  | menu  | faculty_menu | Advisor | 100 % |
| advisor  | check project  | check_project | Advisor | 100 % |
| advisor  | check proposal  | check_submit | Advisor | 100 % |
| faculty  | approve project  | approve_project | Advisor | 100 % |


Missing Feature
I think my project should check more cases such as same id.
The approval should be able to add comment.
