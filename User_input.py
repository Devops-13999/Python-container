user_name = input("enter your name to add it into file ")
if user_name:
    with open('user_info.txt','a') as file:
        file.write(user_name +"\n")
show_info = input("enter y/n to add your name in file ")
if show_info == 'y':
    try:
        with open('user_info.txt' , 'r') as file:
            content = file.readlines()
    except Exception as e:
        print(e,type(e))
    else:
        for line in content:
            print(f'{line.rstrip()}')
