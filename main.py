#DONE
#Julius Inocencio
def encode(password):
    new = ''
    for i in password:
        x = int(i) + 3

        if x > 9:
            y = x % 9
            new += str(y-1)
        else:
            new += str(x)
    return new

def decode():
    pass


if __name__ == "__main__":

    stored_password = ''
    encoded_password = ''
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
            print(f'The encoded password is {encoded_password}, and the original password is {stored_password}')
            #DECODE IN PROGRESS
        elif option == 3:
            menu_open = False


