# Expense-Tracker

Expense Tracker is an CLI application to keep records of expenses.

Programming Language : Python Module used :
Typer,tempfile,os,shutil,date,etc

#Required : 1. Python must be installed. 2. Typer module also installed.
--\> If typer module was not installed the open any terminal and use
command - pip install typer .

#How to Use : Step 1 : Clone the Expense-Tracker.py to your system step
2 : Use Typer commands to run commands as given below.

#Commands : Usage : typer \[Module_or_Path\] run \[command\]
\[argument\]....... \[Module_or_Path\] : Expense-Tracker.py --help : Can
use after module or after command to get requird helps. *getting help of
the commands.
`<img width="957" height="343" alt="image" src="https://github.com/user-attachments/assets/64d3da3d-61ce-47a5-af08-70ef50a66762" />`{=html}
*getting helP OF the arguments for add command.
`<img width="962" height="192" alt="image" src="https://github.com/user-attachments/assets/a86e6ec3-46d4-4e14-806d-939b4e54c918" />`{=html}

Commands :\
add : To add expenses. Required arugemts - discription (use '\_' insted
of space),amount.
\*`<img width="961" height="98" alt="image" src="https://github.com/user-attachments/assets/5662abe5-0f64-4694-8823-931b82acda70" />`{=html}

update : To update exixting record. Required arguments - id,discription
(use '\_' insted of space),amount.
\*`<img width="960" height="53" alt="image" src="https://github.com/user-attachments/assets/c8be7955-cf01-40a5-9341-efdbafccd574" />`{=html}

delete : To delete existing record. Required argument - id.
\*`<img width="955" height="48" alt="image" src="https://github.com/user-attachments/assets/28ae14f4-536f-4c15-8715-9c48953df196" />`{=html}

show : To get all records. No requird argument.
\*`<img width="960" height="61" alt="image" src="https://github.com/user-attachments/assets/83cd7170-081a-471b-ba56-b1fa28373020" />`{=html}

summary : To get summary of all records. No required argument. (After
adding dummy records)
\*`<img width="963" height="46" alt="image" src="https://github.com/user-attachments/assets/a0a07b1e-466d-41b9-925b-86d6f0af9dbc" />`{=html}

monthly-summary : To get summary of perticular month. Required
argument - Month(in MM).
\*`<img width="963" height="49" alt="image" src="https://github.com/user-attachments/assets/1aa46d8a-2045-4fd1-a969-b436dc346f46" />`{=html}

export : To export records in form of '.csv' file to a specific path.
Required argument - path.
\*`<img width="960" height="49" alt="image" src="https://github.com/user-attachments/assets/833b804f-2818-4def-991e-88a562ffc8af" />`{=html}

open-csv : To open records in '.csv' file directly without exporting to
specific location. No required argument.
*`<img width="963" height="33" alt="image" src="https://github.com/user-attachments/assets/2f50763f-b699-459a-b55e-a620e7713e35" />`{=html}
*`<img width="703" height="500" alt="image" src="https://github.com/user-attachments/assets/26de5613-2656-487d-a35b-3a2199fe16c1" />`{=html}
