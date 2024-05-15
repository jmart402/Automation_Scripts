import os


commands = [
    'date',
    'uptime',
    'uname -a'
]


print("The current date and other information about my system.\n")


for command in commands:
    os.system(command)
