from DiaryApp import entry
from DiaryApp.entry import Entry


class Diary:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.is_locked = True
        self.entries = []

    def unlock_diary(self, password):
        try:
            if self.password == password:
                self.is_locked = False
                return True
            else:
                raise Exception("Incorrect password. Diary remains locked.")
        except Exception as e:
            print("Error unlocking Diary:", e)

    def lock_diary(self):
        self.is_locked = True

    def is_lock(self):
        return self.is_locked

    def create_entry(self, entry_id, title, body):
        try:
            if not self.is_locked:
                diary_entry = Entry(entry_id, title, body)
                self.entries.append(diary_entry)
            else:
                raise Exception("Diary is locked. Cannot create an entry.")
        except Exception as e:
            print("Error deleting entry")

    def delete_entry(self, entry_id):
        try:
            if not self.is_locked:
                self.entries = [entry for entry in self.entries if entry.get_id() != entry_id]
            else:
                raise Exception("Diary is locked. Cannot delete an entry.")
        except Exception as e:
            print("Error deleting entry:", e)

    def find_entry_by_id(self, entry_id):
        for entry in self.entries:
            if entry.get_id() == entry_id:
                return entry
            return None

    def update_entry(self, entry_id, newTitle, new_body):
        try:
            if not self.is_locked:
                entry.set_title(newTitle)
                entry.set_body(new_body)
            else:
                raise Exception("Diary is locked. Cannot update an entry.")
        except Exception as e:
            print("error updating entry:", e)

    def get_entries(self):
        try:
            if not self.is_locked:
                return self.entries
            else:
                raise Exception("Diary is locked. Cannot access entries.")
        except Exception as e:
            print("Error accessing entries:", e)
            return []

    def get_username(self):
        return self.user_name

    def get_password(self):
        return self.password
