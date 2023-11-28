import diaries


def main():
    print("Welcome to my Diary")


Diaries = diaries
while True:
    try:
        print("""
            Main Menu
                1. Create Diary
                2. Unlock Diary
                3. Lock Diary
                4. Create Entry
                5. Delete Entry
                6. Update Entry
                7. Find Entry by ID
                8. Exit
            """)
        user_input = int(input("Choose an action:"))
        if user_input == 1:
            user_name = input("Enter username for the new Diary:")
            password = input("Enter password for the new Diary:")
            diaries.add(user_name, password)
            print("Diary created")


        elif user_input == 2:
            unlock_username = input("Enter username to unlock the Diary: ")
            unlock_password = input("Enter the password: ")
            unlocked_diary = diaries.find_by_username(unlock_username)
            if unlocked_diary:
                unlocked = unlocked_diary.unlock_diary(unlock_password)
                if unlocked:
                    print("Diary unlocked successfully.")
                else:
                    print("Incorrect password. Diary is still locked.")
            else:
                print("Diary not found.")

        elif user_input == 3:
            lock_username = input("Enter userName to Lock Diary:")
            lock_diary = diaries.find_by_username(lock_username)
            if lock_diary:
                lock_diary.lock_diary()
                print("Diary is locked:")
            else:
                print("Diary not found")

        elif user_input == 4:
            create_username = input("Enter username to create an entry: ")
            create_diary = diaries.find_by_username(create_username)
            if create_diary:
                entry_id = int(input("Enter entry ID: "))
                title = input("Enter entry title: ")
                entry_body = input("Enter entry body: ")
                create_diary.create_entry(entry_id, title, entry_body)
                print("Entry created.")
            else:
                print("Diary not found.")

        elif user_input == 5:
            delete_username = input("Enter username to delete an entry: ")
            delete_diary = diaries.find_by_username(delete_username)
            if delete_diary:
                entry_id = int(input("Enter entry ID to delete: "))
                delete_diary.delete_entry(entry_id)
            else:
                print("Diary not found.")
        elif user_input == 6:
            update_username = input("Enter username to update an entry: ")
            update_diary = diaries.find_by_username(update_username)
            if update_diary:
                update_entry_id = int(input("Enter entry ID to update: "))
                new_title = input("Enter new entry title: ")
                new_body = input("Enter new entry body: ")
                update_diary.update_entry(update_entry_id, new_title, new_body)
            else:
                print("Diary not found")
        elif user_input == 7:
            find_username = input("Enter username to find an entry: ")
            find_diary = diaries.find_by_username(find_username)
            if find_diary:
                find_entry_id = int(input("Enter entry ID to find: "))
                found_entry = find_diary.find_entry_by_id(find_entry_id)
                if found_entry:
                    print("Entry details:\n" + found_entry.display_format())
                else:
                    print("Entry not found.")
            else:
                print("Diary not found.")

        else:
            print("Invalid option.please choose a valid option")
    except ValueError:
        print("please enter a valid number for option")
