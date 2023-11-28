import diary

from DiaryApp.diary import Diary


class Diaries:
    def __init__(self):
        self.diaries = []
    #
    # def add(self, user_name, password):
    #     try:
    #         diary = Diary(user_name, password)
    #         self.diaries.append(diary)
    #     except ValueError as e:
    #         print("Error while adding a Diary:", e)
    #         print("Failed to add Diary. Please provide a valid username and password.")

    def find_by_username(self, user_name):
        for Diary in self.diaries:
            if diary.get_username() == user_name:
                return diary
        return None

    def delete(self, user_name, password):
        try:
            diary = self.find_by_username(user_name)
            if diary and diary.is_locked() and diary.get_password() == password:
                self.diaries.remove(diary)
            else:
                print("Diary not found or password incorrect. Cannot delete.")
        except Exception as e:
            print("Error while deleting a Diary:", e)
            print("Failed to delete Diary. An unexpected error occurred.")

    def add(self, user_name, password):
        try:
            diary = Diary(user_name, password)
            self.diaries.append(diary)
        except ValueError as e:
            print("Error while adding a Diary:", e)
            print("Failed to add Diary. Please provide a valid username and password.")


