import pandas as pd
df=pd.read_excel('employee.xlsx')
# mask=df['usernumber']==20025617
# dept=df[mask]['dept']
# num=df[mask]['usernumber']

def get_userdata(key):
    num = 22222222
    df = pd.read_excel('employee.xlsx')
    mask = df['usernumber'] == num
    if key == "name":
        name = df[mask]['name'].values[0]

        return name
    if key == "dept":
        dept = df[mask]['dept'].values[0]
        return dept
    dept = df[mask]['dept']
    num = df[mask]['usernumber']
name=get_userdata("name")


mask = df['name'] == "李哲宇"
dept = df[mask]['dept'].values[0]
num = df[mask]['usernumber'].values[0]
print(dept)
print(num)