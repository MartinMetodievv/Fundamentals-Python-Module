number_of_messages = int(input())

for messages in range(number_of_messages):
    number = int(input())
    if number == 88:
        print('Hello')
    elif number == 86:
        print('How are you?')
    elif number < 88:
        print('GREAT!')
    else:
        print('Bye.')

# 4
# 88
# 86
# 2
# 105