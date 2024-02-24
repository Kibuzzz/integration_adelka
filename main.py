from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime as dt


class EventStatuses(Enum):
    ACTUAL = 1  # Мероприятие еще не произошло
    NOT_ACTUAL = -1  # Мероприятие уже прошло или нет билетов


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.id = uuid4()
        self.tickets = []


class Ticket:
    def __init__(self, name_event: str, date_event: str, id: UUID, name: str) -> None:
        self.name_event = name_event
        self.date_event = date_event
        self.id = uuid4()
        self.name = name


users: list[User] = []


class Event:

    def __init__(self, name: str, date_string: str, tickets_number: int) -> None:
        self.name = name
        self.status = EventStatuses.ACTUAL
        self.date = dt.strptime(date_string, '%d.%m.%y %H:%M')
        self.tickets_number = tickets_number


events: list[Event] = []

# Добавить пользователя


def addUser(user_name: str) -> User:
    new_user = User(user_name)
    users.append(new_user)
    return new_user

# Добавить мероприятие и купить на него билет


def addEvent(event_name: str, date_string: str, tickets_number: int) -> None:
    new_event = Event(event_name, date_string, tickets_number)
    events.append(new_event)


def buyTicket(user_id: UUID, name_event: str) -> None:
    user = next((user for user in users if user.id == user_id), None)
    event = next((event for event in events if event.name == name_event), None)
    if user is None:
        print(f"Пользователь с id '{user_id}' не найден.")
        return
    if event is None:
        print(f"Мероприятие с именем '{name_event}' не найдено.")
        return
    if event.tickets_number < 1:
        print(f"Билеты на мероприятие '{name_event}' кончились.")
        return
    else:
        ticket = Ticket(event.name, event.date, user_id, user.name)
        user.tickets.append(ticket)
        event.tickets_number -= 1
        print(
            f"Билет на мероприятие '{name_event}' куплен для пользователя {user.name}.")
        return


# Получить список актуальных мероприятий

def getActualEvents() -> list[str]:
    today = dt.now()
    for event in events:
        if today > event.date:
            event.status = EventStatuses.NOT_ACTUAL
    return [event.name for event in events if event.status == EventStatuses.ACTUAL]

# Прислать напоминание о мероприятии


def sentNotifications(event_name: str) -> None:
    event = next((e for e in events if e.name == event_name), None)
    if event is None:
        print("Мероприятие не найдено")
    else:
        print(
            f"Напоминание: Скоро начнется мероприятие '{event.name}' в {event.date}")

# Выгрузка о посещении мероприятий конкретным пользователем


def userAttendance(user_id: UUID) -> list[str]:
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        print(f"Пользователь с id {user_id} не найден.")
        return []
    return [ticket.name_event for ticket in user.tickets]
