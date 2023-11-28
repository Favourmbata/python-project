class Entry:

    def __init__(self, entry_id, title, body):
        self.id = entry_id
        self.title = title
        self.body = body

    def get_id(self):
        return self.body

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def set_title(self, new_title):
        self.title = new_title

    def set_body(self, new_body):
        self.body = new_body
