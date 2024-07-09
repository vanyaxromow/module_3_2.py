def send_email(massage, recipient, *, sender="university.help@gmail.com"):
    str = "@"
    list2 = [".com", ".ru", ".net"]
    for i in list2:
        if i not in sender and recipient:

            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
            break

        elif str not in recipient and sender:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
            break
        elif sender == recipient:
            print("Нельзя отправить письмо самому себе!")
            break

        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
            break

        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
            break


# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
