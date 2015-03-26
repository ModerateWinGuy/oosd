__author__ = 'mazurdm1'
import datetime


class Twit():

    def __init__(self, box):
        self.observers = []
        self.statuses = []  # Any of the people they follow's posts
        self.post_feed = []  # The user's own statuses
        self.feed_box = box

    def post_update(self, new_post):
        self.post_feed = Status(new_post)
        self.feed_box.clear()
        self.feed_box.insertItems(0, str(self.post_feed))

        for i in self.observers:
            i.receive_update(Status(new_post))

    def receive_update(self, stat):
        self.statuses.append(stat)
        self.feed_box.clear()
        self.feed_box.insertItems(0, str(self.statuses))

    def add_observer(self, observer):
        self.observers.append(observer)


class Status:

    def __init__(self, message):
        self.time = datetime.datetime.now()
        self.message = message

    def __str__(self):
        to_return = ""
        to_return = self.time.time().__str__() + " || " + self.message
        return to_return