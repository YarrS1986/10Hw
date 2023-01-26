# Прикрутить бота к задачам с предыдущего семинара:

# Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в неё систему логирования


from telebot import TeleBot, types
from operations_rational import *
import calculatortype as ty
import operations_complex as opCom

# import os

TOKEN = '5821631445:AAEvOxCwZZAfQxdw_wefomMQ5BWFNhSQQlU'

bot = TeleBot(TOKEN)


# @bot.message_handler(content_types=['document'])
# def answer(msg: types.Message):
#     filename = msg.document.file_name
#     with open(filename, 'wb') as file:
#         file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
#     bot.send_message(chat_id=msg.from_user.id, text='Вывожу логи')

    # Можете раскомментировать, если потребуется затем удалять файл после обработки,
    # чтобы не тратить память.
    # Не забудьте импортировать os
    # os.remove(filename)


@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=f'What numbers are you going to work with? (Complex/Rational): \n')

# @bot.message_handler(commands=['log'])
# def answer(msg: types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text='Вывожу лог')

@bot.message_handler()
def answer(msg: types.Message):
    text = msg.text.lower()
    if text == 'Rational':
        bot.register_next_step_handler(msg, mainterminal)
        # bot.send_message(chat_id=msg.from_user.id, text=f'you choose Rational! \n')


    # if text == '+':
    #
    #     bot.send_message(chat_id=msg.from_user.id, text='Введите слагаемые')
    # elif text == '-':
    #     bot.register_next_step_handler(msg, answer2)




    elif text == 'Complex':
        bot.send_message(chat_id=msg.from_user.id, text=f'you choose Complex! \n')
        '''
        repeat = True
        while repeat == True:
            operands = opCom.Insert_Numbers()
            if operands[2] == "+":
                opCom.record_in_file(
                    opCom.Addition(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]),
                                   opCom.Take_Imaginary_Part(operands[0]),
                                   opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]),
                                   opCom.Take_Imaginary_Part(operands[1])))
            elif operands[2] == "-":
                opCom.record_in_file(
                    opCom.Deduction(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]),
                                    opCom.Take_Imaginary_Part(operands[0]),
                                    opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]),
                                    opCom.Take_Imaginary_Part(operands[1])))
            elif operands[2] == "*":
                opCom.record_in_file(
                    opCom.Multiply(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]),
                                   opCom.Take_Imaginary_Part(operands[0]),
                                   opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]),
                                   opCom.Take_Imaginary_Part(operands[1])))
            else:
                opCom.record_in_file(
                    opCom.division(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]),
                                   opCom.Take_Imaginary_Part(operands[0]),
                                   opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]),
                                   opCom.Take_Imaginary_Part(operands[1])))
            repeat = opCom.Repeat_Or_No()
'''



    '''
    if text == '+':
        bot.register_next_step_handler(msg, answer1)
        bot.send_message(chat_id=msg.from_user.id, text='Введите слагаемые')
    elif text == '-':
        bot.register_next_step_handler(msg, answer2)
        bot.send_message(chat_id=msg.from_user.id, text='Введите уменьшаемое и вычитаемое')
    else:
        bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text +
                                                        ', а должны были арифметическое действие')
    '''

def answer1(msg):
    a, b = map(int, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')
    bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')


def answer2(msg):
    a, b = map(int, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {a - b}')
    bot.send_message(chat_id=msg.from_user.id, text='Введите арифметическую операцию')


bot.polling()


"""
___________________________________________________________
import operations_rational as op
import calculatortype as ty
import operations_complex as opCom

type = ty.type()

while type == 'rational':
    op.mainterminal()

if type == 'complex':
    repeat = True
    while repeat == True:
        operands = opCom.Insert_Numbers()
        if operands[2] == "+":
            opCom.record_in_file(opCom.Addition(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]),
                                                opCom.Take_Imaginary_Part(operands[0]),
                                                opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]),
                                                opCom.Take_Imaginary_Part(operands[1])))
        elif operands[2] == "-":
            opCom.record_in_file(opCom.Deduction(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]),
                                                 opCom.Take_Imaginary_Part(operands[0]),
                                                 opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]),
                                                 opCom.Take_Imaginary_Part(operands[1])))
        elif operands[2] == "*":
            opCom.record_in_file(opCom.Multiply(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]),
                                                opCom.Take_Imaginary_Part(operands[0]),
                                                opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]),
                                                opCom.Take_Imaginary_Part(operands[1])))
        else:
            opCom.record_in_file(opCom.division(opCom.Take_Rational_Part(operands[0]), opCom.Take_Symbol(operands[0]),
                                                opCom.Take_Imaginary_Part(operands[0]),
                                                opCom.Take_Rational_Part(operands[1]), opCom.Take_Symbol(operands[1]),
                                                opCom.Take_Imaginary_Part(operands[1])))
        repeat = opCom.Repeat_Or_No()


"""