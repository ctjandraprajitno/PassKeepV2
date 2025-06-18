"""
Project Title: PassKeep
note for V2:
- improve password generator
- use classes so every user have their own obj
- use API to make additional feature (generate pass without keyword)
"""

#libary
import csv
import random

#lists
valid_todo = ['view', 'add', 'edit', 'exit'] #valid to do options
valid_yon = ['yes', 'y', 'no', 'n'] #valid yes or no options
valid_edit = ['password', 'platform', 'email'] #valid edit options
data = [] #empty list of current user data
all_data = [] #empty lits of all of user's data
#dictionary of letter that can be changed
replacements = {'a': '@'
                , 'b': '8'
                , 'e': '3'
                , 'g': '9'
                , 'i': '!'
                , 'l': '1'
                , 'o': '0'
                , 's': '$'
                , 't': '7'
                , 'z': '2'}

#variables
running = 1 #tracker to check if the program is running
account_num = 0 #tracker for the specific number of an account
current_acc = 0 #tracker to track specific account currently called
pw = '' #password
replaced = 0 #tracker to check if the letter is replaced

#functions
#check if input is valid and return valid input
def input_checker(user_input, valid_input):
    while user_input not in valid_input:
        user_input = input('Please enter a valid input: ').strip().lower()
    else:
        return user_input
    
#ask if user want to continue using the program
def continue_using():
    print()
    user_input = input('Is there anything else you want to do? (y/n) ').strip().lower()
    user_input = input_checker(user_input, valid_yon)
    
    if user_input == 'y' or user_input == 'yes':
        return True
    else:
        print()
        print("Thank you for using PassKeep")
        return False
        
#password generator
def pw_generator(pw, keyword):
    pw = '' #reset password 
    for letter in keyword:
        replaced = 0 #reset tracker to start replacing if valid
        for key in replacements:
            if letter == key:
                pw += replacements[key]
                replaced = 1 #changed tracker to true if the letter is replaced using replacement dict
                continue
        if not replaced:
            #randomizer to change letter to upper case or lower case
            upper_or_lower = random.randint(1, 2)
            if upper_or_lower == 1:
                pw += letter.upper()
            else:
                pw += letter.lower()
            continue
                
    return pw
        
#intro
print('Welcome to PassKeep, your personal password manager.')

#main loop
while running:

    #ask user what to do
    print()
    todo = input('What can I help you with today? (view/add/edit) ').strip().lower()
    #check if input is valid
    todo = input_checker(todo, valid_todo)

    #if the user want to see their passwords
    if todo == "view":
        print()
        account_num = 0 #reset tracker to 0
        with open('user_data.csv', 'r') as csv_file:
            #create object to read file
            csv_reader = csv.reader(csv_file, delimiter = '|')
            #skip first line
            next(csv_reader)
            #print the data stored
            for line in csv_reader:
                account_num += 1
                print('#' + str(account_num))
                print('Platform:', line[0])
                print('Email:', line[1])
                print('Password:', line[2])
                
        if not continue_using():
            running = 0
            
    #if the user want to add a password
    elif todo == 'add':
        #ask user to input the platform
        print()
        platform = input("Which platform is this password for? (e.g., Gmail, Facebook, Twitter) ").strip().lower()
        #check if input is valid
        while not platform.isalpha():
            platform = input("Please enter a valid platform name: ").strip().lower()
    
        #ask user to input email
        gmail = input("Enter email associated with this account: ").strip().lower()
        #check if input is valid
        while "@" not in gmail or "." not in gmail:
            gmail = input("Please enter a valid gmail: ").strip().lower()
    
        #ask user if they want to use their own password or no
        print()
        use_generator = input('Do you want to use the password generator? (y/n) ').strip().lower()
        
        #check if input is valid
        use_generator = input_checker(use_generator, valid_yon)
        
        if use_generator == 'y' or use_generator == 'yes':
            keyword = input("Provide a keyword or base for your password (e.g., your pet's name, a favorite word): ").strip().lower()
            #check if input is valid
            while not keyword.isalpha():
                keyword = input("Please enter a valid keyword: ").strip().lower()

            #make the password more secure
            pw = pw_generator(pw, keyword)
        
            print('Your secure password is', pw)
    
        else:
            pw = input('Please enter password you want to save: ')

        #add data to the list called data
        data.append(platform)
        data.append(gmail)
        data.append(pw)

        #open and store data to cvs file
        with open('user_data.csv', 'a') as csv_file:
            #create object to write in file
            csv_writer = csv.writer(csv_file, delimiter = '|')
            #write the data on the file
            csv_writer.writerow(data)
            
        if not continue_using():
            running = 0
    
    #if user choose edit 
    #user can't edit multiple data at the same time because there will be a logic error in the indexing 
    #so the tradeoff is, the user need to edit the file one at a time by selecting 'edit' again
    elif todo == 'edit':
        all_data = [] #reset all data
        print()
        account_num = 0 #reset tracker to 0
        with open('user_data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = '|') #create object to read file
            next(csv_reader) #skip first line
            #print the data stored
            for line in csv_reader:
                account_num += 1
                print('#' + str(account_num))
                print('Platform:', line[0])
                print('Email:', line[1])
                print('Password:', line[2])
                all_data.append(line) #copy all current data
            
        #ask user which account to edit
        print()
        selected_account = int(input('which account do you want to edit? (enter the number of the account from 1 to ' + str(account_num) + ') '))
        
        #check if user input valid account number
        while 1 > selected_account or selected_account > account_num:
            selected_account = int(input('account number must be in between 1 and ' + str(account_num) + ': '))
        
        account_num = 0 #reset tracker to 0
        with open('user_data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = '|') #create object to read file
            next(csv_reader) #skip first line
            for line in csv_reader:
                account_num += 1 #track account currently called
                if account_num == selected_account: #check if the account called is the same as selected account
                    platform = line[0] #save selected platform
                    email = line[1] #save selected email
                    pw = line[2] #save selected password
                    #add new data to the list called data
                    data = [platform, email, pw]
                    break
                    
        print()
        edit = input('What do you want to edit? (platform/email/password) ')
        edit = input_checker(edit, valid_edit)
        
        if edit == 'platform':
            platform = input('What is the new platform? ')
            #check if input is valid
            while not platform.isalpha():
                platform = input("Please enter a valid platform name: ").strip().lower()
            #replace old with new data
            data[0] = platform
            
        if edit == 'email':
            email = input('What is the new email? ')
            #check if input is valid
            while "@" not in email or "." not in email:
                email = input("Please enter a valid email: ").strip().lower()
            #replace old with new data
            data[1] = email
                
        if edit == 'password':
            #ask user if they want to use their own password or no
            print()
            use_generator = input('Do you want to use the password generator? (y/n) ').strip().lower()
        
            #check if input is valid
            use_generator = input_checker(use_generator, valid_yon)
    
            if use_generator == 'y' or use_generator == 'yes':
                keyword = input("Provide a keyword or base for your password (e.g., your pet's name, a favorite word): ").strip().lower()
                #check if input is valid
                while not keyword.isalpha():
                    keyword = input("Please enter a valid keyword: ").strip().lower()
            
                #make password secure
                pw = pw_generator(pw, keyword)
                #print secured pw
                print('Your secure password is', pw)
                #replace old with new data
                data[2] = pw
                
            else:
                edit_pw = input('What is the new password? ')
                #replace old with new data
                data[2] = pw
        
        #update all data
        all_data[selected_account - 1] = data
        
        # Write the updated data back to the CSV file
        with open('user_data.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter='|')
            csv_writer.writerow(['Platform', 'Email', 'Password'])
            csv_writer.writerows(all_data)

        
        if not continue_using():
            running = 0