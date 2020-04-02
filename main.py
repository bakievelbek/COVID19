import telebot
import COVID19Py


from telebot import types

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1254782658:AAFn9JWXKjoHm5psD36eI0WHNcexAxkn50U')

@bot.message_handler(commands=['start'])
def start(message):
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
        btn1 = types.KeyboardButton("Во всем мире🌐")
        btn2 = types.KeyboardButton("США 🇺🇸")
        btn3 = types.KeyboardButton("Китай 🇨🇳")
        btn4 = types.KeyboardButton("Корея 🇰🇷")
        btn5 = types.KeyboardButton("Узбекистан 🇺🇿")
        btn6 = types.KeyboardButton("ОАЭ 🇦🇪")
        btn7 = types.KeyboardButton("Великобритания 🇬🇧󠁧󠁢󠁥󠁮󠁧󠁿󠁧󠁢󠁥󠁮󠁧󠁿")
        btn8 = types.KeyboardButton("Испания 🇪🇸")
        btn9 = types.KeyboardButton("Италия 🇮🇹")
        btn10 = types.KeyboardButton("Германия 🇩🇪")
        btn11 = types.KeyboardButton("Франция 🇫🇷")
        btn12 = types.KeyboardButton("Турция 🇹🇷")
        btn13 = types.KeyboardButton("Украина 🇺🇦")
        btn14 = types.KeyboardButton("Беларусь 🇧🇾")
        btn15 = types.KeyboardButton("Израиль 🇮🇱")
        btn16 = types.KeyboardButton("Россия 🇷🇺")
        btn17 = types.KeyboardButton("Иран 🇮🇷")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17)
        
        
        send_mess = f"<b>Привет! {message.from_user.first_name}!</b>\nВведите страну"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text
    
    if get_message_bot == "США 🇺🇸":
        location = covid19.getLocationByCountryCode("US")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "Украина 🇺🇦":
        location = covid19.getLocationByCountryCode("UA")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "Беларусь 🇧🇾":
        location = covid19.getLocationByCountryCode("BY")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "Россия 🇷🇺":
        location = covid19.getLocationByCountryCode("RU")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "Иран 🇮🇷":
        location = covid19.getLocationByCountryCode("IR")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "Корея 🇰🇷":
        location = covid19.getLocationByCountryCode("KR")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "ОАЭ 🇦🇪":
        location = covid19.getLocationByCountryCode("AE")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "Израиль 🇮🇱":
        location = covid19.getLocationByCountryCode("IL")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "Испания 🇪🇸":
        location = covid19.getLocationByCountryCode("ES")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "Италия 🇮🇹":
        location = covid19.getLocationByCountryCode("IT")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "Китай 🇨🇳":
        location = covid19.getLocationByCountryCode("CN")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "Германия 🇩🇪":
        location = covid19.getLocationByCountryCode("DE")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "Франция 🇫🇷":
        location = covid19.getLocationByCountryCode("FR")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "Великобритания 🇬🇧󠁧󠁢󠁥󠁮󠁧󠁿󠁧󠁢󠁥󠁮󠁧󠁿":
        location = covid19.getLocationByCountryCode("GB")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "Турция 🇹🇷":
        location = covid19.getLocationByCountryCode("TR")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    elif get_message_bot == "Узбекистан 🇺🇿":
        location = covid19.getLocationByCountryCode("UZ")
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<b>Данные по стране:</b>\nНаселение страны: {location[0]['country_population']}\nПоследнее обновление: {date[0]} {time[0]} \n<b>Заболевшие : {location[0]['latest']['confirmed']}</b>\nСмертей : {location[0]['latest']['deaths']}"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру</u>\n<b>Заболевшие: </b>{location['confirmed']}\n"
        bot.send_message(message.chat.id, final_message, parse_mode='html')
    
    # if final_message == "":
    #     date = location[0]['last_updated'].split("T")
    #     time = date[1].split(".")
    #     final_message = f"<b>Последнее обновление:</b> {date[0]} {time[0]}\n"
    #                     f"<b>Заболевших: </b>{location[0]['latest']['confirmed']:,}\n"
    #                     f"<b>Смертей: </b>{location[0]['latest']['deaths']:,}"
    
    

bot.polling(none_stop=True)

        
latest = covid19.getLatest()

location = covid19.getLocationByCountryCode('US')