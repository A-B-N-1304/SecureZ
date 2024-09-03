
from loginpage import loginpagefunc
def loggedin():
    result = 1
    try:
        userFile = open('userlog.txt', 'r')
        userFile.close()
    except FileNotFoundError:
        result = 0

    if result == 0:

        print("blah 1")
        return False
    elif result == 1:
        userFile = open('userlog.txt', 'r')
        datInFile = userFile.readlines()
        userFile.close()
        if datInFile == []:
            return False
        else:
            return True



def login():

    print('111')

    if loggedin():
        print('done')
        return ''

    elif loggedin() == False:
        loginpagefunc()
        login()
