#DONE
def encode(password):
    new = ''
    for i in password:
        new += str(int(i) + 3)
    return new

def decode():
    pass


if __name__ == "__main__":

    stored_password = ''

    print(f'Menu\n'
          f'-------------\n'
          f'1. Encode\n'
          f'2. Decode\n'
          f'3. Quit\n')
    option = int(input('Please enter an option: '))
    password = input('Please enter your password to encode: ')

    Continue = True

    while Continue:
        if option == 1:
            stored_password = encode(password)
            print('Your password has been encoded and stored!')
            Continue = False
        elif option == 2:
            print('In progress')

        elif option == 3:
            Continue = False


