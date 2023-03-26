def routers(question):
    if "расп" in question:
        schedule()
    elif "трен" in question:
        trainer()
    elif "плат" in question:
        payment()
    elif "оценк" in question:
        marks()
    elif "баланс" in question:
        balance()
    elif "данные" in question:
        my_data()
    else:
        print("Введите вопрос корректно")

def schedule():
    print("Понедельник: 15:00 - 16:30\nВторник:14:30 - 16:00\nПятница:12:50 - 14:00")
def trainer():
    print("ФИО:Джемакулов Эдгар Робертович\nТелефон:89376456374\ntelegram:lov66")
def payment():
    print("Сумма к оплате занятия: 12000 р.")
def marks():
    print("На данный момент у вас 3 пятерки по литературе")
def balance():
    print("Ваш баланс:76890 р.")
def my_data():
    print("ФИО:Еникеева Виолетта Витальевна\nКонтактый телефон:89378496660\nДата рождения:03.05.2006\nПол:жен.")




