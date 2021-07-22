class NotConnectedError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return 'Statuscode: {}\nDetail:{}'.format(self.status_code, self.message)
