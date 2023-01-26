import operations_rational as op
import sys
from telebot import TeleBot, types
from main import bot

@bot.message_handler()
def x(msg: types.Message):
    text = float(msg.text.replace(',', '.'))
    bot.send_message(chat_id=msg.from_user.id, text=f'Choose first float number: \n')
    return text

@bot.message_handler()
def y(msg: types.Message):
    text = float(msg.text.replace(',', '.'))
    bot.send_message(chat_id=msg.from_user.id, text=f'Choose first float number: \n')
    return text

def selectoperation():
    global operation
    operation = (input(f'Select operation: +, -, *, /: '))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Invalid syntax')

def res(firstnum, secondnum):
    if  operation == '+':
        res = firstnum + secondnum
        result = round(res, 3)
        return result
    elif operation == '-':
        res = firstnum - secondnum
        result = round(res, 3)
        return result
    elif operation == '*':
        res = firstnum * secondnum
        result = round(res, 3)
        return result
    elif operation == '/':
        res = firstnum / secondnum
        result = round(res, 3)
        return result
    else:
        print('invalid syntax')

@bot.message_handler()
def mainterminal(msg):
    # global file
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {x}, {y}')
    x = bot.register_next_step_handler(msg, op.x)

    while True:
        y = bot.register_next_step_handler(msg, op.y)



        '''
        oper = op.selectoperation()
        res = op.res(x, y)
        file = 'results.txt'
        with open('results.txt', 'a') as data:
            data.write(f'The result of {x} {oper} {y} = {res}\n')
        print(f'The result of {x} {oper} {y} = {res}\n(already written to txt file)' )
        again = input('Do you want calculate another numbers? Yes/No: ').lower()
        if again == 'yes':
            useresult = input('Do you want to use the result of the last operation? (Yes/No): ').lower()
            if useresult == 'yes':
                x = res
                continue
            elif useresult == 'no':
                break
            else:
                sys.exit()
        else:
            sys.exit()
        '''