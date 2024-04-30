import telebot
from telebot import types
from phisics_formuls import *

bot = telebot.TeleBot('7078700379:AAGxduJl5LYrHd9vr2aChqmUe0Jk2H_gS9o')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('Формулы', callback_data='formuls')
    markup.add(btn)
    bot.send_message(message.chat.id,
                     f'Привет, {message.from_user.first_name}!'
                     f'\nЕсли хочешь решить арифметический пример, просто напиши его.'
                     f'\nА если хочешь найти формулу, нажми на кнопку ниже)',
                     reply_markup=markup)


@bot.message_handler()
def solve(message):
    try:
        example = ''.join(message.text.replace(':', '/').split())
        ansver = eval(example)
    except Exception:
        bot.send_message(message.chat.id, 'Это не пример)')
        return
    bot.send_message(message.chat.id, f'{example} = <b>{round(ansver, 4)}</b>', parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_formuls(call):
    if call.data == 'formuls':
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('МЕХАНИКА', callback_data='meh')
        btn2 = types.InlineKeyboardButton('ТЕРМОДИНАМИКА', callback_data='term')
        btn3 = types.InlineKeyboardButton('ЭЛЕКТРОДИНАМИКА', callback_data='electro')
        btn4 = types.InlineKeyboardButton('КВАНТОВАЯ ФИЗИКА', callback_data='quant')
        btn5 = types.InlineKeyboardButton('ВСЁ!', callback_data='all')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(call.message.chat.id, 'Какой раздел физики вас интересует?',
                         reply_markup=markup)
    elif call.data == 'meh':
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('КИНЕМАТИКА', callback_data='kin')
        btn2 = types.InlineKeyboardButton('ЗАКОНЫ СОХРАНЕНИЯ', callback_data='zs')
        btn3 = types.InlineKeyboardButton('КОЛЕБАНИЯ', callback_data='koleb')
        markup.add(btn1, btn2, btn3)
        bot.send_message(call.message.chat.id, 'Какой раздел механики вас интересует?',
                         reply_markup=markup)
    elif call.data == 'term':
        bot.send_message(call.message.chat.id, term)
    elif call.data == 'electro':
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('ЭЛЕКТРИЧЕСКОЕ ПОЛЕ', callback_data='e_pole')
        btn2 = types.InlineKeyboardButton('ЗАКОНЫ ТОКА', callback_data='tok')
        btn3 = types.InlineKeyboardButton('МАГНИТНОЕ ПОЛЕ', callback_data='m_pole')
        markup.add(btn1, btn2, btn3)
        bot.send_message(call.message.chat.id, 'Какой раздел электродинамики вас интересует?',
                         reply_markup=markup)
    elif call.data == 'quant':
        bot.send_message(call.message.chat.id, quant)

    elif call.data == 'kin':
        bot.send_message(call.message.chat.id, meh[0])
    elif call.data == 'zs':
        bot.send_message(call.message.chat.id, meh[1])
    elif call.data == 'koleb':
        bot.send_message(call.message.chat.id, meh[2])

    elif call.data == 'e_pole':
        bot.send_message(call.message.chat.id, electro[0])
    elif call.data == 'tok':
        bot.send_message(call.message.chat.id, electro[1])
    elif call.data == 'm_pole':
        bot.send_message(call.message.chat.id, electro[2])

    elif call.data == 'all':
        all = [kinematika, zn_sohr, volna, term, pole, tok, voln, quant]
        for i in all:
            bot.send_message(call.message.chat.id, i)


bot.infinity_polling()
