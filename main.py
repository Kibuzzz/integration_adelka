from datetime import datetime as dt


class User:

    count_users = 0

    def __init__(self, name: str) -> None:
        self.status = 1  # 1 - Активный пользователь, 0 - Неактивный пользователь
        self.name = name
        self.id = User.count_users
        self.status = User.count_users
        self.tickets = []
        User.count_users += 1

    def __str__(self) -> str:
        return "{} {} {} {}".format(self.id, self.name, self.status, self.tickets)


class Event:

    def __init__(self, name: str, date_string: str) -> None:
        self.name = name
        self.status = 1  # 1 - Актуальны, 0 - Неактуальный
        self.event_date = dt.strptime(date_string, '%d.%m.%y %H:%M')

    def __str__(self) -> str:
        str_status = ""
        if self.status:
            str_status = "Актуально"
        else:
            str_status = "Не актуально"

        return "{} {} {}".format(self.name, self.event_date, str_status)


events: list[Event] = []

# Добавить мероприятие и купить на него билет


def addEvent(name_event: str, date_string: str) -> None:
    new_event = Event(name_event, date_string)
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
# Прислать выгрузку о посещении мероприятий конкретным пользователем


u = User("kiril")
e = Event("Новогодняя елка", "31.12.23 12:48")
events.append(e)
addEvent("Дискотека", "13.01.24 14:50")
for e in events:
    print(e)
