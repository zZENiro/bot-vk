import vk_api
import time
import random
import pymysql as sql
import json
from gtts import gTTS
import requests

# Сообщество
token = "а вот!"
vk = vk_api.VkApi(token=token)
vk._auth_token()

# Личный токен, получать тут https://vkhost.github.io/
own_token = "token"
vk_user = vk_api.VkApi(token=own_token)
vk._auth_token()


def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color}


# Первый выбор
keyboardChoice = {
    "one_time": True,
    "buttons": [
        [get_button(label='Студент', color="primary"),
         get_button(label='Абитуриент', color="negative")]]}
keyboardChoice = json.dumps(keyboardChoice, ensure_ascii=False)

# Пробуй еще раз
keyboardAccept = {
    "one_time": True,
    "buttons": [
        [get_button(label='Все Верно.', color="primary"),
         get_button(label='В данных есть ошибка', color="negative")]]}
keyboardAccept = json.dumps(keyboardAccept, ensure_ascii=False)

# Клава выхода.
keyboardExit = {
    "one_time": True,
    "buttons": [
        [get_button(label='Выход', color="negative")]]}
keyboardExit = json.dumps(keyboardExit, ensure_ascii=False)

# Клава готовности задания.
keyboardReady = {
    "one_time": True,
    "buttons": [
        [get_button(label='Готово.', color="positive")],
        [get_button(label='Назад.', color="negative")]]}
keyboardReady = json.dumps(keyboardReady, ensure_ascii=False)

# Клава выбора заданий - объективно понимаю, что нет времени искать свою старую динамическую, поэтому гиперкод
keyboardQ = {
    "one_time": True,
    "buttons": [
        [get_button(label='Задание 1. Подписаться на сообщество.', color="secondary")],
        [get_button(label='Задание 2. Поставить лайк.', color="secondary")],
        [get_button(label='Вернуться в главное меню.', color="negative")]]}
keyboardQ = json.dumps(keyboardQ, ensure_ascii=False)

keyboardOne = {
    "one_time": True,
    "buttons": [
        [get_button(label='Задание 1. Подписаться на сообщество.', color="positive")],
        [get_button(label='Задание 2. Поставить лайк.', color="secondary")],
        [get_button(label='Вернуться в главное меню.', color="negative")]]}
keyboardOne = json.dumps(keyboardOne, ensure_ascii=False)

keyboardTwo = {
    "one_time": True,
    "buttons": [
        [get_button(label='Задание 1. Подписаться на сообщество.', color="secondary")],
        [get_button(label='Задание 2. Поставить лайк.', color="positive")],
        [get_button(label='Вернуться в главное меню.', color="negative")]]}
keyboardTwo = json.dumps(keyboardTwo, ensure_ascii=False)

keyboardDouble = {
    "one_time": True,
    "buttons": [
        [get_button(label='Задание 1. Подписаться на сообщество.', color="positive")],
        [get_button(label='Задание 2. Поставить лайк.', color="positive")],
        [get_button(label='Вернуться в главное меню.', color="negative")]]}
keyboardDouble = json.dumps(keyboardDouble, ensure_ascii=False)

keyboardAhiv = {
    "one_time": True,
    "buttons": [
        [get_button(label='Организатор', color="secondary"), get_button(label='Медиа', color="secondary")],
        [get_button(label='Участник', color="secondary"), get_button(label='Волонтёр', color="secondary")]]}
keyboardAhiv = json.dumps(keyboardAhiv, ensure_ascii=False)

keyboardAhivONE = {
    "one_time": True,
    "buttons": [
        [get_button(label='Город', color="secondary")],
        [get_button(label='Страна', color="secondary")],
        [get_button(label='Международный', color="secondary")]]}
keyboardAhivONE = json.dumps(keyboardAhivONE, ensure_ascii=False)

keyboardAhivTWO = {
    "one_time": True,
    "buttons": [
        [get_button(label='1', color="positive")],
        [get_button(label='2', color="secondary")],
        [get_button(label='3', color="negative")]]}
keyboardAhivTWO = json.dumps(keyboardAhivTWO, ensure_ascii=False)

# Главная
keyboardMain = {
    "one_time": True,
    "buttons": [
        [get_button(label='Профиль 🙄', color="secondary")],
        [get_button(label='💳 ВТБ-Профиль 💎', color="secondary")],
        [get_button(label='Задания 📒', color="secondary"),
         get_button(label='Приложить достижение.', color="positive")],
        [get_button(label='Поддержка 🔧', color="secondary")],
        [get_button(label='Больше о программе лояльности 🔎', color="primary")]]}
keyboardMain = json.dumps(keyboardMain, ensure_ascii=False)

connection = sql.connect(
    host="91.243.84.18",
    user="root",
    passwd="123456",
    database='vk_db',
    port=3308
)

q = connection.cursor()

kash_data_students = []
kash_data = []
# Подключение к бд
try:

    q.execute("SELECT * FROM Main;")
    kash_data = q.fetchall()
    print(kash_data)
    for i in kash_data:
        ka_sk = []

        for j in i:
            ka_sk.append(j)

        kash_data_students.append(ka_sk)

    print(kash_data_students)
except:
    q.execute("""
            CREATE TABLE Main
            (id int,
            Name varchar(64),
            VUZ varchar(32),
            Student_id varchar(32),
            Step int default "0",
            count_quest int default "0",
            current_quest int default "0",
            rating real);
                  """)
    connection.commit()
    q.execute("SELECT * FROM Main;")
    kash_data = q.fetchall()
    print(kash_data)

    for i in kash_data:
        ka_sk = []

        for j in i:
            ka_sk.append(j)

        kash_data_students.append(ka_sk)
#        print(kash_data_sudents)
    print(kash_data_students)

kash_person = {}

for item in kash_data_students:
    if item[0] != 0:
        kash_person[item[0]] = item

print(kash_person)

kash_ids_students = []
for item in kash_data_students:
    kash_ids_students.append(item[0])

Vuz_list = []
for item in kash_data_students:
    Vuz_list.append(str(item[2]).lower())
Vuz_list = Vuz_list
print(Vuz_list)

Student_id_list = []
for item in kash_data_students:
    Student_id_list.append(str(item[3]).lower())
print(Student_id_list)

name_list = []
for item in kash_data_students:
    name_list.append((str(item[1]).lower()).split(" ")[0])
print(name_list)
ahiv = {}
print(kash_ids_students)


def send_audio(id, text):  # Данная функция отправляет сообщение
    tts = gTTS(text=text, lang="ru", lang_check=True)
    name = "voice.ogg"
    tts.save(name)
    a = vk.method("docs.getMessagesUploadServer", {"type": "audio_message", "peer_id": id})
    b = requests.post(a['upload_url'], files={'file': open("voice.ogg", 'rb')}).json()
    c = vk.method("docs.save", {"file": b["file"]})
    d = 'doc{}_{}'.format(c['audio_message']['owner_id'], c['audio_message']['id'])
    vk.method('messages.send', {'peer_id': id, 'attachment': d, "random_id": random.randint(1, 2147483647)})


def sendphoto(user_id, msg):
    a = vk.method("photos.getMessagesUploadServer")
    pyp = '1.jpg'  # фотки\\
    b = requests.post(a['upload_url'], files={'photo': open(pyp, 'rb')}).json()
    c = vk.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
    vk.method("messages.send", {"peer_id": user_id, "random_id": random.randint(-203030, 2032303), "message": msg,
                                "attachment": f'photo{c["owner_id"]}_{c["id"]}', "keyboard": keyboardMain})


while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 1, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if id not in kash_ids_students:  # Если мы не знаем чела в вк
                text = "Привет, ты студент или аббитуриент? Нажми кнопочку и мы отправим тебя дальше, в удивительный мир ВТБ-банка."
                vk.method("messages.send", {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                            "keyboard": keyboardChoice})
                kash_ids_students.append(id)
                kash_person[id] = [id, "", "", "", 0, "", "", "", ""]
            else:
                print(kash_person[id])  # 4 = step
                if kash_person[id][4] == 0:
                    if body.lower() == 'студент':
                        text = "Укажите ВУЗ в котором вы учитесь"
                        kash_person[id][4] = 101
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647)})

                    elif body.lower() == 'абитуриент':  #
                        text = 'На данный момент функционала для абитуриентов нет('
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                   "keyboard": keyboardChoice})
                    else:
                        text = "Укажите вы студент или абитуриент"
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                   "keyboard": keyboardChoice})

                # СТУДЕНТ рабочая область
                elif kash_person[id][4] == 101:  # ВУЗ
                    if body.lower() in Vuz_list:
                        kash_vuz_antivor = []
                        k = 0
                        for item in Vuz_list:
                            if item == body.lower():
                                kash_vuz_antivor.append(k)
                            k += 1
                        print(kash_vuz_antivor)
                        text = 'Укажите номер студенческого билета.'
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647)})
                        kash_person[id][4] = 102

                    else:
                        kash_person[id][4] = 0
                        text = "Вашего Учебного Заведения, к сожалению нет в нашей базе данных. Но вы можете предложить своему ВУЗУ вступить в программу лояльности от ВТБ!"
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                   "keyboard": keyboardExit})


                elif kash_person[id][4] == 102:  # Студик
                    if body.lower() in Student_id_list:
                        kash_antivor = Student_id_list.index(body.lower())
                        print(kash_antivor)
                        if kash_antivor not in kash_vuz_antivor:
                            text = "В данном ввузе нет такого студента, попробуйте еще раз."
                            vk.method("messages.send",
                                      {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647)})
                        else:
                            text = 'Укажите свою фамилию'
                            vk.method("messages.send",
                                      {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647)})
                            kash_person[id][4] = 103
                            kash_person[id][3] = body.lower()

                    else:
                        kash_person[id][4] = 102
                        text = "Такого номера у нас нет в бд. Попробуйте еще раз."
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647)})

                elif kash_person[id][4] == 103:  # Фамилии
                    print(body.lower() in name_list)
                    print(body.lower())
                    print(name_list)
                    if body.lower() in name_list and name_list.index(body.lower()) == kash_antivor:
                        text = "Поздравляю, верификация пройдена, теперь можете пользоваться всеми функциями нашей системы."
                        send_audio(id, text)
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                   'keyboard': keyboardMain})
                        kash_person[id][4] = 104
                        q.execute("""UPDATE Main
                                        Set id = {},
                                        Step = {}
                                        Where Student_id = {}
                                        """.format(id, 104, kash_person[id][3]))
                        connection.commit()
                        q.execute("SELECT * FROM Main Where id = {}".format(id))
                        kash_person[id] = list(q.fetchone())

                    else:
                        kash_person[id][4] = 103
                        text = "Такой фамилии у нас нет в бд. Попробуйте еще раз"
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647)})



                elif kash_person[id][4] == 104:

                    if body.lower() == "профиль 🙄":  # Профиль
                        print(kash_person[id])
                        if str(kash_person[id][5]) != '0':
                            xxx = len(str(kash_person[id][5]))
                        else:
                            xxx = 0

                        text = "Вас зовут {}\nВы учитесь в {}\nНомер вашего студенческого билета {}\nВы выполнили {} заданий\nВаш рейтинг {}".format(
                            kash_person[id][1], kash_person[id][2], kash_person[id][3], xxx,
                            str(kash_person[id][7])[:3])

                        sendphoto(id, text)

                        # VTB403
                    elif body == '💳 ВТБ-Профиль 💎':
                        data = requests.get(f"http://91.243.84.18/api/students/getbankvalues?vkid={id}")
                        jsonData = json.loads(data.text);
                        creditCardInfo = jsonData['creditCard']

                        text = f"Данные вашего ВТБ-Профиля:\n\tEmail: {creditCardInfo['email']}\n\t" \
                               f"ИНН: {creditCardInfo['inn']}\n\tСНИЛС: {creditCardInfo['snils']}\n\t" \
                               f"Номер: {creditCardInfo['mobilePhone']}\n\tДата рождения: {creditCardInfo['birthDate']}\n\t"

                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                   'keyboard': keyboardMain})





                    elif body.lower() == "задания 📒":
                        print(type(kash_person[id][5]), ' Это что за покемон ', kash_person[id][5])
                        if str(kash_person[id][5]) == '0':
                            text = "Для вас доступно 2 задания"
                            vk.method("messages.send",
                                      {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                       'keyboard': keyboardQ})
                        elif str(kash_person[id][5]) == '1':
                            text = "Для вас доступно 1 задание"
                            vk.method("messages.send",
                                      {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                       'keyboard': keyboardOne})
                        elif str(kash_person[id][5]) == '2':
                            text = "Для вас доступно 1 задание"
                            vk.method("messages.send",
                                      {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                       'keyboard': keyboardTwo})
                        elif str(kash_person[id][5]) == '21' or str(kash_person[id][5]) == '12':
                            text = "Для вас нет доступных заданий"
                            vk.method("messages.send",
                                      {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                       'keyboard': keyboardDouble})
                        else:
                            text = "Сначала посмотрите свой профиль."
                            vk.method("messages.send",
                                      {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                       'keyboard': keyboardMain})



                    elif body == "Задание 1. Подписаться на сообщество.":
                        if str(kash_person[id][5]) == '1' or str(kash_person[id][5]) == '12' or str(
                                kash_person[id][5]) == '21':
                            text = "Вы уже выполняли это задание."
                            vk.method("messages.send",
                                      {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                       'keyboard': keyboardMain})
                        else:
                            text = "Для выполнения задания и получения 0.2 баллов подпишитесь на сообщество банка:\nhttps://vk.com/vtb\nА после этого нажмите кнопку: Готово."
                            print(kash_person[id][6], ' Должно стать 1')
                            if int(kash_person[id][6]) == 0:
                                kash_person[id][6] = '1'
                            else:
                                kash_person[id][6] = '1'
                            print('Стало', kash_person[id][6])
                            vk.method("messages.send",
                                      {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                       'keyboard': keyboardReady})

                    elif body == "Задание 2. Поставить лайк.":
                        if kash_person[id][5] == '2' or kash_person[id][5] == '12' or kash_person[id][5] == '21':
                            text = "Вы уже выполняли это задание."
                            vk.method("messages.send",
                                      {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                       'keyboard': keyboardMain})
                        else:
                            text = "Для выполнения задания и получения 0.1 балла поставьте лайк последней записи ВТБ-банка\nhttps://vk.com/vtb?w=wall-22749457_24957\nА после этого нажмите кнопку: Готово."
                            print(kash_person[id][6], ' Должно стать 2')
                            if int(kash_person[id][6]) == 0:
                                kash_person[id][6] = '2'
                            else:
                                kash_person[id][6] = '2'
                            print('Стало', kash_person[id][6])
                            vk.method("messages.send",
                                      {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                       'keyboard': keyboardReady})


                    elif body == "Приложить достижение.":  # Приложить достижение
                        text = "Отправьте название мероприятия, в котором вы участвовали."
                        ahiv[id] = [id, "название", "Роль в мероприятии (участник, волонтёр, медиа, организатор)",
                                    "город, страна, международный)", 0, "prof"]
                        print(ahiv)
                        kash_person[id][4] = 110
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647)})


                    elif body == 'Готово.':
                        if kash_person[id][6] == '1':  # Если делает 1 задание
                            a = vk_user.method("groups.isMember", {'group_id': 'vtb', 'user_id': id})
                            if a == 1:  # Подписан
                                print("Подписан")
                                if str(kash_person[id][5]) == '2':
                                    kash_person[id][5] = '21'
                                    q.execute("SELECT * FROM Main")
                                    q.execute("UPDATE Main SET count_quest = {} Where id = {}".format(21, id))
                                    connection.commit()
                                    q.execute("SELECT * FROM Main")
                                    text = "Умничка, получай свои 0.2 балла!"
                                    kash_person[id][7] += 0.2
                                    q.execute("UPDATE Main SET rating = {} Where id = {}".format(kash_person[id][7],
                                                                                                 id))  # POINT403
                                    connection.commit()
                                    vk.method("messages.send", {"peer_id": id, "message": text,
                                                                "random_id": random.randint(1, 2147483647),
                                                                'keyboard': keyboardMain})

                                elif str(kash_person[id][5]) == '0':
                                    kash_person[id][5] = '1'
                                    q.execute("UPDATE Main SET count_quest = {} Where id = {}".format(1, id))
                                    connection.commit()
                                    text = "Умничка, получай свои 0.2 балла!"
                                    kash_person[id][7] += 0.2
                                    q.execute("UPDATE Main SET rating = {} Where id = {}".format(kash_person[id][7],
                                                                                                 id))  # POINT403
                                    connection.commit()
                                    vk.method("messages.send", {"peer_id": id, "message": text,
                                                                "random_id": random.randint(1, 2147483647),
                                                                'keyboard': keyboardMain})

                                else:
                                    text = "Что-то пошло не так"
                                    print(text)
                                    print(kash_person[id])
                                    vk.method("messages.send", {"peer_id": id, "message": text,
                                                                "random_id": random.randint(1, 2147483647),
                                                                'keyboard': keyboardMain})

                                    # vk.method("messages.send", {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647), 'keyboard': keyboardMain})



                            else:
                                text = "Вы не выполнили задание, нас не обмануть!.\nВозвращаемся в главное меню."
                                vk.method("messages.send",
                                          {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                           'keyboard': keyboardMain})


                        elif kash_person[id][6] == '2':  # Второе задание
                            a = vk_user.method("likes.isLiked",
                                               {'type': 'post', 'owner_id': -22749457, 'item_id': 24957, 'user_id': id})
                            if a['liked'] == 1:  # Лайк есть
                                print("лайкнул")
                                if str(kash_person[id][5]) == '1':
                                    kash_person[id][5] = '12'
                                    q.execute("UPDATE Main SET count_quest = {} Where id = {}".format(12, id))
                                    connection.commit()
                                    text = "Умничка, получай свои 0.1 балл!"
                                    kash_person[id][7] += 0.1
                                    q.execute("UPDATE Main SET rating = {} Where id = {}".format(kash_person[id][7],
                                                                                                 id))  # POINT403
                                    connection.commit()
                                    vk.method("messages.send", {"peer_id": id, "message": text,
                                                                "random_id": random.randint(1, 2147483647),
                                                                'keyboard': keyboardMain})


                                elif str(kash_person[id][5]) == '0':
                                    kash_person[id][5] = '2'
                                    q.execute("UPDATE Main SET count_quest = {} Where id = {}".format(2, id))
                                    connection.commit()
                                    kash_person[id][7] += 0.1
                                    q.execute("UPDATE Main SET rating = {} Where id = {}".format(kash_person[id][7],
                                                                                                 id))  # POINT403
                                    connection.commit()
                                    text = "Умничка, получай свои 0.1 балл!"
                                    vk.method("messages.send", {"peer_id": id, "message": text,
                                                                "random_id": random.randint(1, 2147483647),
                                                                'keyboard': keyboardMain})


                                else:  # Ошибка
                                    print(kash_person[id])
                            else:
                                text = "Вы не выполнили задание, нас не обмануть!.\nВозвращаемся в главное меню."
                                vk.method("messages.send",
                                          {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                           'keyboard': keyboardMain})

                        else:
                            text = "Что-то пошло не так"
                            vk.method("messages.send",
                                      {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                       'keyboard': keyboardMain})


                    elif body.lower() == "вернуться в главное меню.":
                        text = "Возвращаемся домой!"
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                   'keyboard': keyboardMain})

                    elif body.lower() == 'поддержка 🔧':
                        text = "По всем вопросам вы можете обратиться к тех. эксперту\nhttps://vk.com/xxx_kongo_porenti_xxx"
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                   'keyboard': keyboardMain})

                    elif body == 'Больше о программе лояльности 🔎':
                        text = """
                                Рады приветствовать тебя здесь. 
Наша платформа помогает абитуриентам, студентам и деканатам находить общий язык, повышать прозрачность и эффективность академической лояльности, взаимовыгодно для всех сторон интегрируя банк ВТБ и его партнёров в активную жизнь университета и города
                                """
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                   'keyboard': keyboardMain})


                    else:
                        text = "Я вас не понял, повторите запрос.\nКод ошибки {}".format("G0")
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                   'keyboard': keyboardMain})

                    # [id,"название","Роль в мероприятии (участник, волонтёр, медиа, организатор)","город, страна, международный)",0]
                elif kash_person[id][4] == 110:
                    kash_person[id][4] = 111
                    ahiv[id][1] = body.title()  # Название
                    text = "В качестве кого вы учавствовали в мероприятии?\nНажмите кнопку."
                    vk.method("messages.send",
                              {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                               'keyboard': keyboardAhiv})
                elif kash_person[id][4] == 111:
                    kash_person[id][4] = 112
                    ahiv[id][2] = body.title()  # Роль
                    text = "Каким по масштабу было данное мероприятие?\nНажмите кнопку."
                    vk.method("messages.send",
                              {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                               'keyboard': keyboardAhivONE})
                elif kash_person[id][4] == 112:
                    ahiv[id][3] = body.title()  # Масштаб
                    if ahiv[id][2] == "Участник":
                        kash_person[id][4] = 113
                        text = "И наконец, какое место вы заняли?\nНажмите кнопку."
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                   'keyboard': keyboardAhivTWO})
                    else:  # Если у него нет места, то отправляем
                        kash_person[id][4] = 115
                elif kash_person[id][4] == 113:
                    kash_person[id][4] = 115
                    ahiv[id][4] = body.title()  # Место
                elif kash_person[id][4] == 115:
                    print(ahiv[id])

                    kash_person[id][4] = 116
                    text = 'Прикрепите фотографию документа, доказывающего ваше участие в мероприятии "{}"'.format(
                        ahiv[id][1])
                    vk.method("messages.send",
                              {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647)})

                elif kash_person[id][4] == 116:
                    try:
                        ahiv[id][5] = messages["items"][0]["last_message"]['attachments'][0]['photo']['sizes'][
                            len(messages["items"][0]["last_message"]['attachments'][0]['photo']['sizes']) - 1]['url']
                        text = "Ваши данные отправляютя на проверку"
                        kash_person[id][4] == 104
                        print(ahiv[id])
                        sq = 'INSERT INTO Achiv (id,name,status,type,place,url) VALUES ({},"{}","{}","{}","{}","{}")'.format(
                            ahiv[id][0], ahiv[id][1], ahiv[id][2], ahiv[id][3], ahiv[id][4], ahiv[id][5])
                        print(sq)  # DB403

                        params = {
                            "eventName": ahiv[id][1],
                            "level": ahiv[id][3],
                            "role": ahiv[id][2],
                            "place": ahiv[id][4],
                            "vkId": id
                        }

                        reqstr = f"http://91.243.84.18/api/Students/AddAchievement?eventName={params['eventName']}&place={params['place']}&role={params['role']}&level={params['level']}&vkId={params['vkId']}";
                        requests.get(reqstr)


                        q.execute(sq)
                        connection.commit()
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                   'keyboard': keyboardMain})




                    except:
                        # print(messages["items"][0]["last_message"]['attachments'][0]['photo'])
                        text = "Не нашел фотографии в вашем сообщении"
                        vk.method("messages.send",
                                  {"peer_id": id, "message": text, "random_id": random.randint(1, 2147483647),
                                   'keyboard': keyboardMain})





                else:
                    kash_person[id][4] = 104
    except:
        print()
