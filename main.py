from datetime import datetime as dt


class User:

    ACTIVE = 1
    NOT_ACTIVE = 0

    count_users = 0

    def __init__(self, name: str) -> None:
        self.status = User.ACTIVE  # 1 - Активный пользователь, 0 - Неактивный пользователь
        self.name = name
        self.id = User.count_users
        self.status = User.count_users
        self.tickets = []
        User.count_users += 1

    def __str__(self) -> str:
        return "{} {} {} {}".format(self.id, self.name, self.status, self.tickets)


class Event:

    ACTUAL = 1
    NOT_ACTUAL = 0

    def __init__(self, name: str, date_string: str) -> None:
        self.name = name
        self.status = Event.ACTUAL  # 1 - Актуальны, 0 - Неактуальный
        self.event_date = dt.strptime(date_string, '%d.%m.%y %H:%M')

    def __str__(self) -> str:
        str_status = "Актуально" if self.status else "Не актуально"
        return "{} {} {}".format(self.name, self.event_date, str_status)


events: list[Event] = []

# Добавить мероприятие и купить на него билет


def addEvent(event_name: str, date_string: str) -> None:
    new_event = Event(event_name, date_string)
    events.append(new_event)


def buyTicket(user: User, event: str) -> None:
    if event in [event.name for event in events]:
        user.tickets.append(event)
        print("Билет успешно куплен")
    else:
        print("Что то пошло не так")


# Получить список актуальных мероприятий


def getActualEvents() -> list[Event]:
    return [event for event in events if event.status == 1]

# Прислать напоминание о мероприятии


def sentNotifications(event_name: str) -> None:
    event = [e for e in events if e.name == event_name][0]
    if event:
        print(
            f"Напоминание: Скоро начнется мероприятие '{event.name}' в {event.event_date}")
    else:
        print("Мероприятие не найдено")

# Выгрузка о посещении мероприятий конкретным пользователем


def userAttendance(user: User) -> None:
    return user.tickets


# Создание пользователя
u = User("kiril")

# Добавление мероприятий
addEvent("Новогодняя елка", "31.12.23 12:48")
addEvent("Дискотека", "13.01.24 14:50")

# Покупка билетов
buyTicket(u, "Новогодняя елка")
buyTicket(u, "Дискотека")

# Получение списка актуальных мероприятий
print("Актуальные мероприятия:")
for event in getActualEvents():
    print(event)

# Отправка уведомления о мероприятии
sentNotifications("Дискотека")

# Получение списка мероприятий, которые посетил пользователь
print("Посещенные мероприятия пользователем:")
print(userAttendance(u))
