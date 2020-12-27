from tkinter import *
from tkinter import messagebox
import os


def check_button():
    get_check_data = check_var.get()

    if get_check_data == True:
        password.config(show='')
        test_password.config(show='')

    elif get_check_data == False:
        password.config(show='*')
        test_password.config(show='*')


def check_button2():
    get_check_data = check_var2.get()

    if get_check_data == True:
        password2.config(show='')

    elif get_check_data == False:
        password2.config(show='*')


def main_program():
    print('do the main thingy...')


def get_inputted_data():
    inputted_name = name_var.get()
    inputted_password = password_var.get()
    inputted_two_pass = two_password_var.get()

    if len(inputted_password) != 0 and len(inputted_two_pass) != 0 and len(inputted_name) != 0:

        if inputted_password == inputted_two_pass:

            with open('user_details.txt', 'a') as data:
                data = open('user_details.txt', 'r')
                is_empty = data.read(1)

                if not is_empty:
                    data.close()
                    data2 = open('user_details.txt', 'a')
                    data2.write(inputted_name + ',' + inputted_password)
                    data2.close()
                    success_label = Label(root2, text='Signed in successfully!', fg='green')
                    success_label.pack(side=TOP)
                    name.delete(0, END)
                    password.delete(0, END)
                    test_password.delete(0, END)

                else:
                    data.close()
                    exists = False
                    data_check2 = open('user_details.txt', 'r')
                    for i in data_check2:
                        usse2, passw2 = i.split(',')
                        passw2 = passw2.strip()

                        if usse2 == inputted_name and passw2 == inputted_password:
                            exists = True
                            break
                    data_check2.close()

                    already_exists = Label(root2, text='User already signed in!', fg='red')
                    already_exists.pack(side=TOP)

                    if exists == True:
                        name.delete(0, END)
                        password.delete(0, END)
                        test_password.delete(0, END)

                    elif exists == False:
                        already_exists.destroy()
                        data2 = open('user_details.txt', 'a')
                        data2.write('\n' + inputted_name + ',' + inputted_password)
                        data2.close()
                        success_label = Label(root2, text='Signed in successfully!', fg='green')
                        success_label.pack(side=TOP)
                        name.delete(0, END)
                        password.delete(0, END)
                        test_password.delete(0, END)

        elif inputted_password != inputted_two_pass:
            messagebox.showerror('ERROR', 'Password do not match, try again!')

            root2.destroy()
            root2.update()
            sign_in()

            name.insert(0, inputted_name)
            password.insert(0, inputted_password)
            test_password.insert(0, inputted_two_pass)

    elif len(inputted_name) == 0 and len(inputted_password) == 0 and len(inputted_two_pass) == 0:
        messagebox.showerror('ERROR', 'All fields are empty!')

        root2.destroy()
        root2.update()
        sign_in()

    elif len(inputted_password) == 0 or len(inputted_two_pass) == 0:
        messagebox.showerror('ERROR', 'Password field is empty!')

        root2.destroy()
        root2.update()
        sign_in()

        name.insert(0, inputted_name)

    elif len(inputted_name) == 0:
        messagebox.showerror('ERROR', 'Name field is empty!')

        root2.destroy()
        root2.update()
        sign_in()

        password.insert(0, inputted_password)
        test_password.insert(0, inputted_two_pass)


def log_in_check():
    global inputted_name2
    global inputted_password2

    inputted_name2 = name_var2.get()
    inputted_password2 = password_var2.get()

    if len(inputted_name2) != 0 and len(inputted_password2) != 0:
        success = False
        data = open('user_details.txt', 'r')

        for i in data:
            usse, passw = i.split(',')
            passw = passw.strip()

            if usse == inputted_name2 and passw == inputted_password2:
                success = True
                break
        data.close()

        if success == True:
            successLabel = Label(root3, text='Signed in successfully', fg='green')
            successLabel.pack(side=TOP)
            name2.delete(0, END)
            password2.delete(0, END)
            main_program()

        else:
            messagebox.showerror('ERROR', 'Incorrect username or password!')

            root3.destroy()
            root3.update()
            log_in()

            name2.insert(0, inputted_name2)
            password2.insert(0, inputted_password2)

    elif len(inputted_name2) == 0:
        messagebox.showerror('ERROR', 'Name field is empty!')

        root3.destroy()
        root3.update()
        log_in()

        password2.insert(0, inputted_password2)

    elif len(inputted_password2) == 0:
        messagebox.showerror('ERROR', 'Name field is empty!')

        root3.destroy()
        root3.update()
        log_in()

        name2.insert(0, inputted_name2)


def sign_in():
    global root2
    root2 = Toplevel(root)
    root2.title('User module')
    root2.geometry('250x250+700+400')
    root2.resizable('false', 'false')

    label = Label(root2, text='Sign in', bg='#DF5DF3')
    label.pack(side=TOP, fill=X)

    main_frame = Frame(root2)

    global name_var
    global password_var
    global two_password_var
    name_var = StringVar()
    password_var = StringVar()
    two_password_var = StringVar()

    name_lab1 = Label(main_frame, text='Name')
    name_lab1.grid(row=0, column=0, sticky=E)
    password_lab1 = Label(main_frame, text='Password')
    password_lab1.grid(row=1, column=0, sticky=E)
    test_password_lab1 = Label(main_frame, text='Repeat password')
    test_password_lab1.grid(row=2, column=0)

    global name
    global password
    global test_password
    name = Entry(main_frame, textvariable=name_var, width=50)
    name.grid(row=0, column=1)
    name.focus()
    password = Entry(main_frame, textvariable=password_var, width=50, show='*')
    password.grid(row=1, column=1)
    test_password = Entry(main_frame, textvariable=two_password_var, width=50, show='*')
    test_password.grid(row=2, column=1)

    main_frame.pack()

    button_frame = Frame(root2)

    sign_in_button = Button(button_frame, text='Sign in', command=get_inputted_data)
    sign_in_button.grid(columnspan=2)

    button_frame.pack()

    global check_var
    check_var = BooleanVar()

    global check
    check = Checkbutton(root2, text='Show passwords', variable=check_var, command=check_button)
    check.pack()

    label_bottom = Label(root2, bg='#DF5DF3')
    label_bottom.pack(side=BOTTOM, fill=X)


def log_in():
    global root3
    root3 = Toplevel(root)
    root3.title('User module')
    root3.geometry('250x250+700+400')
    root3.resizable('false', 'false')

    label = Label(root3, text='Log in', bg='#DF5DF3')
    label.pack(side=TOP, fill=X)

    main_frame2 = Frame(root3)

    global name_var2
    global password_var2

    name_var2 = StringVar()
    password_var2 = StringVar()

    name_lab2 = Label(main_frame2, text='Name')
    name_lab2.grid(row=0, column=0, sticky=E)
    password_lab2 = Label(main_frame2, text='Password')
    password_lab2.grid(row=1, column=0, sticky=E)

    global name2
    global password2

    name2 = Entry(main_frame2, textvariable=name_var2, width=50)
    name2.grid(row=0, column=1)
    name2.focus()
    password2 = Entry(main_frame2, textvariable=password_var2, width=50, show='*')
    password2.grid(row=1, column=1)

    main_frame2.pack()

    button_frame2 = Frame(root3)

    log_in_button = Button(button_frame2, text='Log in', command=log_in_check)
    log_in_button.grid(columnspan=2)

    button_frame2.pack()

    global check_var2
    check_var2 = BooleanVar()

    global check2
    check2 = Checkbutton(root3, text='Show password', variable=check_var2, command=check_button2)
    check2.pack()

    label_bottom = Label(root3, bg='#DF5DF3')
    label_bottom.pack(side=BOTTOM, fill=X)


def main_screen():
    global root
    root = Tk()

    root.title('User module')
    root.geometry('250x250+700+400')
    root.resizable('false', 'false')

    root.protocol('WM_EXIT_BUTTON', root.destroy)

    label = Label(root, text='Sign in/log in module', bg='#DF5DF3')
    label.pack(side=TOP, fill=X)

    button1 = Button(root, text='Sign in', command=sign_in)
    button1.pack(padx=5, pady=5)
    button2 = Button(root, text='Log in', command=log_in)
    button2.pack(padx=5, pady=5)
    button3 = Button(root, text='Exit', command=root.destroy)
    button3.pack(padx=5, pady=5)

    label_bottom = Label(root, bg='#DF5DF3')
    label_bottom.pack(side=BOTTOM, fill=X)

    root.mainloop()

main_screen()

#made by lorkz






