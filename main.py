#DONE
#Julius Inocencio
def encode(password):  # takes in a numeric password and encodes it by shifting the digits 3 numbers up
    new = ''
    for i in password:
        x = int(i) + 3  # adds 3 to current value as it loops
        if x > 9:  # if value is greater than 9, checks to see if there is a remainder
            y = x % 9  # not sure why this works, should be 9 % x [DID NOT USE IMPORT MATH]
            new += str(y-1)  # subtracts 1 from y variable to make sure it accounts for 0 and adds to 'new' string
        else:
            new += str(x)  # adds to 'new' string
    return new

def decode(encoded_password):
    # Jonathan Vargas
    e_pass = list(encoded_password)  # create a list from input passcode string
    e_list = [int(x) for x in e_pass]  # from str to int elements into a new list
    p_list = []  # create empty list to append converted numbers (old passcode list)
    for num in e_list:
        if 3 <= num <= 9:
            # if num is 3-9, just subtract 3 and add to p_list
            num1 = num - 3
            p_list.append(num1)
        elif 0 <= num <= 2:
            # if num is 0-2, convert them into new numbers
            # from 0 -> 7, 1 -> 8, 2 -> 9 then append to new list
            if num == 0:
                num1 = 7
                p_list.append(num1)
            elif num == 1:
                num1 = 8
                p_list.append(num1)
            elif num == 2:
                num1 = 9
                p_list.append(num1)
    string_list = [str(x) for x in p_list]
    old = ''.join(string_list)
    return old






if __name__ == "__main__":
    #stored_password = '' these are not needed since there are local variables that have the data stored
    #encoded_password = ''
    menu_open = True
    
    while menu_open:
        print(f'Menu\n'
              f'-------------\n'
              f'1. Encode\n'
              f'2. Decode\n'
              f'3. Quit\n')
        option = int(input('Please enter an option: '))

        if option == 1:
            stored_password = input('Please enter your password to encode: ')
            encoded_password = encode(stored_password)
            print('Your password has been encoded and stored!')
        elif option == 2:
            stored_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {stored_password}')
        elif option == 3:
            menu_open = False


