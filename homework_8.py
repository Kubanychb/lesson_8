import sqlite3

databace_plan = sqlite3.connect("data_plan")
sql = databace_plan.cursor()

sql.execute(
    """CREATE TABLE IF NOT EXISTS users(
    planning TEXT,
    password TEXT,
    fulfilled TEXT
    )
    """
)
databace_plan.commit()

def planning_user():
    enter_plans()
    global user_planning, user_password, user_fulfilled
    user_planning = input("planning for today: ")
    user_password = input("password: ")
    user_fulfilled = input("plan fulfilled yes or no?: ")

    sql.execute(f"SELECT planning FROM users WHERE planning = '{user_planning}'")

    if user_fulfilled == "yes":
        print("you fulfilled the plan")
        delete_plan()
        for value in sql.execute("SELECT * FROM users"):
            print(value)

    elif user_fulfilled == "no":
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_planning, user_password, user_fulfilled))
            databace_plan.commit()
            print("User planning")

            for value in sql.execute("SELECT * FROM users"):
                print(value)

        else:
            print("User plan already exits! Choose another one")

            for value in sql.execute("SELECT * FROM users"):
                print(value)

    answer = input("Do you want to add a new plan? yes or no ")
    if answer == "yes":
        user_planning = input("planning for today: ")
        user_password = input("password: ")
        user_fulfilled = input("plan fulfilled yes or no?: ")
        sql.execute(f"SELECT planning FROM users WHERE planning = '{user_planning}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_planning, user_password, user_fulfilled))
            databace_plan.commit()
            print("New custom plans have been updated")

            for value in sql.execute("SELECT * FROM users"):
                print(value)

        else:
            print("User plan already exits! Choose another one")
            for value in sql.execute("SELECT * FROM users"):
                print(value)

    else:
        for value in sql.execute("SELECT * FROM users"):
            print(value)



def delete_plan():
    sql.execute(f"DELETE FROM users WHERE planning = '{user_planning}'")
    databace_plan.commit()
    print("Plan deleted")

def enter_plans():
    print("Your plans")
    sql.execute(f"SELECT planning, fulfilled FROM users")
    row = sql.fetchall()
    print(row)




if __name__ == '__main__':
    planning_user()



