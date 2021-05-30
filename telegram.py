import telebot
import pyautogui
API_TOKEN = '1642681006:AAGZRci1RXEwNZaAVYb9yiHv3f9-woYe4KE'

bot = telebot.TeleBot(API_TOKEN)
from telebot import types

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton("Пока")
    item2 = types.KeyboardButton("Привет")
    
    markup.add(item, item2)
    bot.send_message(message.chat.id, """\
Привет, я знаю что Игорь не очень быстро отвечает на сообщения, поэтому я его заменяю, если хочешь мне что то написать, напиши мне)\
""", reply_markup=markup)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    
    
    
    if message.chat.type == 'private':
        print(message.text)
        
        
        
        
        if message.text == 'Привет':
            
            bot.send_message(message.chat.id, 'Здорова')

        elif message.text == 'Пока':
            
            bot.send_message(message.chat.id, 'До свидания')

        elif message.text == 'Норм':
            
            bot.send_message(message.chat.id, '))')

        elif message.text == 'Красивый':
            
            bot.send_message(message.chat.id, 'Спасибо)')

        
        elif message.text == 'Я тебя люблю)':
            
            bot.send_message(message.chat.id, """\
Я знаю лол\
""")
        elif message.text == 'Игорь':
            
            bot.send_message(message.chat.id, """\
это я\
""")

        elif message.text == 'Я тебя люблю':
            
            bot.send_message(message.chat.id, """\
Я знаю лол\
""")
        elif message.text == 'Как жизнь?':
            
            bot.send_message(message.chat.id, """\
норм, у тя как?\
""")
        elif message.text == 'Как дела':
            
            bot.send_message(message.chat.id, """\
норм, у тя как?\
""")
        elif message.text == 'Ладно':
            
            bot.send_message(message.chat.id, """\
Ладно\
""")
        elif message.text == 'Ты мне нравишся':
            
            bot.send_message(message.chat.id, """\
Бывает)\
""")
        elif message.text == 'Что делаешь?':
            
            bot.send_message(message.chat.id, """\
Пишу тебе сообщение\
""")
        elif message.text == 'Спокойной)':
            
            bot.send_message(message.chat.id, """\
Я знаю лол\
""")
        elif message.text == 'Спокойной ночи)':
            
            bot.send_message(message.chat.id, """\
Cпокойной\
""")
        elif message.text == 'А ты меня?':
            bot.send_message(message.chat.id, """\
Не спрашивай\
""")
        elif message.text == 'Ок':
            bot.send_message(message.chat.id, """\
Угу\
""")
        elif message.text == 'Хорошо':
            bot.send_message(message.chat.id, """\
Угу\
""")
        elif message.text == 'Пора':
            bot.send_message(message.chat.id, """\
Да, пора\
""")
        
            
        elif message.text == 'Спокойной ночи)':
            bot.send_message(message.chat.id, """\
Спокойной)\
""")
        elif message.text == 'Скинь свою фотку':
        
        
        
            
            photo = open(r'C:\\Users\oksana\Desktop\\igor.jpg', 'rb')
            bot.send_photo(message.chat.id, photo, 'ну как?')
        elif message.text == 'Красивый':
            bot.send_message(message.chat.id, """\
))\
""")
        elif message.text == 'Чем занимаешься?':
            bot.send_message(message.chat.id, """\
Дышу)0(0))))0))))()()())))((()))00))()0))\
""")
        elif message.text == 'Что мне делать?':
            bot.send_message(message.chat.id, """\
Займись чем то полезным\
""")
        elif message.text == 'Чем мне заняться?':
            bot.send_message(message.chat.id, """\
Займись чем то полезным\
""")
        elif message.text == 'Как дела?':
            bot.send_message(message.chat.id, """\
Нормально, а у тебя?\
""")
        
        elif message.text == 'Скажи что-то умное':
            bot.send_message(message.chat.id, """\
Синусоидальность дидукционнго индуктора некоэмутируется с хромофорной эфузией аксирогентно-адиквантного фотонного триангулятора\
""")
        elif message.text == 'Ахах':
            bot.send_message(message.chat.id, """\
Хехе)\
""")
        elif message.text == 'Ты красивый':
            bot.send_message(message.chat.id, """\
Спасибо большое)))))))\
""")
        
        else:
            bot.send_message(message.chat.id, """\
))))0))(00)()()0)0(())00)((((()))()()00)))()\
""")
            
        
        
            


bot.polling()
