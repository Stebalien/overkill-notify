import notify2

class Notify:
    summary = ""
    message = None

    def __init__(self):
        notify2.init('Stuff')
        self.notification = notify2.Notification(self.summary)

    def show(self):
        self.notification.update(self.summary, self.message)
        self.notification.show()

