import datetime

class User:
    next_id = 1
    def __init__(self, name, email, todo_list:list[int] = None):
        self.uid = User.next_id
        self.name = name
        self.email = email
        self.todo_list = todo_list if todo_list is not None else []
        User.next_id += 1

    def create_todo(self, title1:str = None, content1:str = None):
        current_date = datetime.datetime.now().date()
        current_time = datetime.datetime.now().time()

        if (title1 or content1):
            new_todo = Todo(title1, content1, current_date, current_time)
            self.todo_list.append(new_todo)
            return
        
        title = input("Enter title of the Todo:\n")
        content = input("Enter content of the Todo:\n")
        new_todo = Todo(title, content, current_date, current_time)
        self.todo_list.append(new_todo)
        pass

    def edit_todo(self):
        todo_id = int(input("Enter Todo id:\n"))
        edit_field = input("What do you want to edit in your todo?\n").lower()
        changed = False
        for i in range(len(self.todo_list)):
            if (todo_id == self.todo_list[i].getID()):
                self.todo_list[i].change_field(edit_field)
                changed = True     #to check if its changed successfully or not
                break
        if (not changed):
            print("Note not found.\n")

    def change_field(self, field):
        if (field == "name"):
            value = input("Enter new name:\n")
            self.name = value
        elif (field == "email"):
            value = input("Enter new email for your id:\n")
            self.email = value
        print(f"{field} changed successfully.")

    def display_todo_byID(self, id1):
        for i in range(len(self.todo_list)):
            if id1 == self.todo_list[i].getID():
                self.todo_list[i].display()
                break

    def display_all_todos(self):
        print(f"---UserID: {self.uid}---User Name: {self.name}---Email: {self.email}")
        for i in range(len(self.todo_list)):
            self.todo_list[i].display()

    def getID(self):
        return self.uid
    
    def display_myself(self):
        print(f"User id: {self.uid}\nName: {self.name}\nEmail: {self.email}")

class Todo:
    next_id = 1

    def __init__(self, title, content, date_created, time):
        self.tid = Todo.next_id
        self.title = title
        self.content = content
        self.date_created = date_created
        self.time_created = time
        Todo.next_id += 1

    def getID(self):
        return self.tid
    
    def change_field(self, field):
        if (field == "title"):
            value = input("Enter new title of your todo:\n")
            self.title = value
        elif (field == "content"):
            value = input("Enter new content for your todo:\n")
            self.content = value

        print(f"{field} changed successfully.")

    def display(self):
        print(f"Todo Id: {self.tid}\nTitle: {self.title}\nContent: {self.content}\nDate_created: {self.date_created}\nTime created: {self.time_created}")
        pass

class system:
    def __init__(self):
        self.user_list: list[User] = []

    def delete_user(self, uid):
        for i in range(len(self.user_list)):
            if uid == self.user_list[i].getID():
                del self.user_list[i]
                print("User deleted successfully.")
                break

    def add_users(self, u1:User):
        self.user_list.append(u1)

    def display_all_users(self):
        for i in range(len(self.user_list)):
            self.user_list[i].display_myself()

    def modify_user(self):
        user_id = int(input("Enter user id:\n"))
        edit_field = input("What do you want to edit in your profile?\n").lower()
        changed = False
        for i in range(len(self.user_list)):
            if (user_id == self.user_list[i].getID()):
                self.user_list[i].change_field(edit_field)
                changed = True     #to check if its changed successfully or not
                break
        if (not changed):
            print("User not found.\n")

    def display_user_byID(self, uid):
        for i in range(len(self.user_list)):
            if (int(uid) == self.user_list[i].getID()):
                self.user_list[i].display_myself()
        pass

if __name__ == "__main__":
    u1 = User("Farhan", "farhan@gmail.com")
    u1.create_todo("note1", "slfkjsldfalkfjsd")
    u1.create_todo("note2", "sjldfjasdlfjksdalkfsd")
    u2 = User("ali", "ali@gmail.com")
    u2.create_todo("water the plants", "sepcifically the poppy plants")
    s1 = system()
    s1.add_users(u1)
    s1.add_users(u2)
    s1.delete_user(2)
    #s1.display_all_users()
    #s1.modify_user()
    #u1.edit_todo()
    #u1.display_todo_byID(2)
    #u2.display_all_todos()