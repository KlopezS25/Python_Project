notes = []

def write_note():
    content = input("Dear Diary, ")
    new_note = f"🌟 Note 🌟\nDear Diary,\n\n{content}\n"
    notes.append(new_note)
    print("Your note has been saved!")

def view_notes():
    if not notes:
        print("Oh no! You don't have any notes!")
        return

    print("\n✨✨ Your Past Notes ✨✨")
    print("="*50)
    for note in notes:
        print(note)
        print("Goodbye.. 💋 ")
    print("="*50)

def main():
    while True:
        print("\n✨✨ Welcome to Your Personal Diary! ✨✨")
        print("Choose from the following: ")
        print("1. Write a new note")
        print("2. View past notes")
        print("3. Exit")
        choice = input("Choice: ")

        if choice == '1':
            write_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            print("\n✨✨ Have a Good Day!! ✨✨")
            break
        else:
            print("Invalid option. PLease try again.")

if __name__ == "__main__":
    main()