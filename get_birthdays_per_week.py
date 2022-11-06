from datetime import datetime, timedelta

users = [{'name': 'Alex', 'birthday': datetime(1994, 3, 28)},
         {'name': 'Olena', 'birthday': datetime(1994, 6, 1)},
         {'name': 'Mariia', 'birthday': datetime(2000, 11, 6)},
         {'name': 'Mommy', 'birthday': datetime(1968, 10, 11)},
         {'name': 'Jilly', 'birthday': datetime(2001, 11, 5)},
         {'name': 'John', 'birthday': datetime(2003, 11, 8)},
         {'name': 'Bill',  'birthday': datetime(1990, 11, 9)},
         {'name': 'Marco', 'birthday': datetime(1991, 11, 12)},
         {'name':'Jacob',  'birthday': datetime(1989, 11, 10)},
         {'name': 'Kim', 'birthday': datetime(1990, 11, 11)},
         {'name': 'Jan', 'birthday': datetime(1990, 11, 11)},
         {'name': 'Harry', 'birthday': datetime(1990, 9, 10)},
         {'name': 'Ron', 'birthday': datetime(1991, 11, 15)},
         {'name': 'Draco', 'birthday': datetime(1992, 11, 7)},
         {'name': 'Hagrid', 'birthday': datetime(1992, 11, 4)}]




def get_birthday_per_week(users: list):

    greeting = []
    result = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}

    current_day = datetime.now()
    if current_day.weekday() == 5:
        range_days = timedelta(days=6)
    elif current_day.weekday() == 6:
        range_days = timedelta(days=5)
    else:
        range_days = timedelta(days=7)

    for user in users:
        if current_day.day <= user.get('birthday').day <= (current_day + range_days).day and current_day.month == user.get('birthday').month:
            greeting.append({'name': user.get('name'), 'birthday': datetime(current_day.year, user.get('birthday').month, user.get('birthday').day)})

    for user in greeting:
        if user.get('birthday').weekday() not in (5, 6):
            result[user.get('birthday').strftime('%A')].append(user.get('name'))
        else:
            result['Monday'].append(user.get('name'))

    return print_result_list(result)


def print_result_list(result):
    for k, v in result.items():
        if v:
            print(f'{k}: {", ".join(v)}')


if __name__ == '__main__':
    get_birthday_per_week(users)
