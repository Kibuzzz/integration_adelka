import unittest
from main import events, users, addUser, addEvent, buyTicket, getActualEvents, userAttendance


class TestEvents(unittest.TestCase):
    def setUp(self):
        self.user = addUser("TestUser")
        self.event_name = "TestEvent"
        self.event_date = "01.01.25 12:00"
        addEvent(self.event_name, self.event_date, 10)

    def test_getActualEvents(self):
        addEvent("PastEvent", "01.01.23 12:00", 10)
        self.assertEqual(len(getActualEvents()), 1)

    def test_addEvent(self):
        self.assertTrue(any(event.name == self.event_name for event in events))

    def test_buyTicket(self):
        buyTicket(self.user.id, self.event_name)
        self.assertEqual(len(self.user.tickets), 1)

    def test_userAttendance(self):
        buyTicket(self.user.id, self.event_name)
        attendance = userAttendance(self.user.id)
        self.assertEqual(attendance, [self.event_name])

    def tearDown(self):
        events.clear()
        users.clear()


if __name__ == "__main__":
    unittest.main()
