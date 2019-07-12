import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):

    def append(self, o):
        super(LoggableList, self).append(o)
        self.log(o)
