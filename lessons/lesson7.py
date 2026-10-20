import sqlite3

# A4
connect = sqlite3.connect("users.db")
# Рука с карандашом
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()

# CRUD - Create Read Update Delete

def create_user(name, age, hobby):
    # cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")')
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES(?,?,?)',
        (name,age,hobby)
    )
    print("user create!!")
    connect.commit()

# create_user("Ardager", 27, "Спать!!")
# create_user("Олег", 18, "Горы")
# create_user("John Doe", 33, "Плавать!!")
# create_user("Слава", 10, "Бегать!!")
# create_user("Arzy", 10, "Бегать!!")
# 4530582
def get_users():
    cursor.execute('SELECT name, age FROM users')
    data = cursor.fetchall()
    print(data)

# get_users()

def update_user(new_name, rowid):

    cursor.execute(
        'UPDATE users SET name=? WHERE rowid=?',
        (new_name, rowid)
    )
    print('Update user name')
    connect.commit()

# update_user("John", 3)

def delete_user(user_id):
    cursor.execute(
        'DELETE FROM users where id=?',
        (user_id,)
    )
    print('delete user')
    connect.commit()

# delete_user(3)



# def test(index_obj, value_list):
#     return value_list[index_obj]

# 10 = 10 true
# 10 > 9 true
# test(4, [10,11])

nums, target_1 = [7,11,15,2], 9

def twoSum(array, target):
    num_map = {
        7: 0,
        11: 1,
        15: 2,

    }

    for index, item in enumerate(array):
        complement = target - item
        if complement in num_map:
            return [num_map[complement], index]
        num_map[item] = index
    return []

print(twoSum(nums, target_1))

