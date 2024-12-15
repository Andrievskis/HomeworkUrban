def sed_email(message, recipient, *, sender='university.help@gmail.com'):
    if ('@' not in recipient or not recipient.endswith(('.com', '.ru', '.net'))
            and '@' not in sender or not sender.endswith(('.com', '.ru', '.net'))):
        print (f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return
    elif sender == recipient:
        print ("Нельзя отправить письмо самому себе!")
        return
    elif sender == 'university.help@gmail.com':
        print (f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
        return
    else:
        print (f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}")

sed_email('Hello!','vasyok1337@mail.com' )
sed_email('Hello!','urban.fan@mail.ru', sender='urban.info@mail.com')
sed_email('Hello!','urban.student@mail.ru', sender='urban.teacher@mail.uk')
sed_email('Hello!','urban.teacher@mail.ru', sender='urban.teacher@mail.ru')