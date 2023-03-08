#DONE
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

    #stored_password = ''
    menu_open = True
    
    while menu_open:
        print(f'Menu\n'
              f'-------------\n'
              f'1. Encode\n'
              f'2. Decode\n'
              f'3. Quit\n')
        option = int(input('Please enter an option: '))

        if option == 1:
            password = input('Please enter your password to encode: ')
            stored_password = encode(password)
            print('Your password has been encoded and stored!')
            Continue = False

        elif option == 2:
            print('In progress')

        elif option == 3:
            #print(stored_password)  #FOR TESTING PURPOSE
            menu_open = False


