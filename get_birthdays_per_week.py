from datetime import datetime, timedelta
from users import users



def get_birthdays_per_week(users: list):

    current_day = datetime.now()
    one_week = timedelta(weeks=1)
    last_day = current_day + one_week

    for user in users:
        for name in user:
            user[name] = user[name].replace(current_day.year).date()

    greeting = []
    if current_day.weekday() == 0:
        for user in users:
            for name in user:
                if user[name].month == current_day.month and (current_day.day - 2 <= user[name].day <= last_day.day):
                    greeting.append({name: user[name] for name in user})
    else:
        for user in users:
            for name in user:
                if user[name].month == current_day.month and (current_day.day <= user[name].day <= last_day.day) and user[name].weekday():
                    greeting.append({name: user[name] for name in user})


    result = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}
    for user in greeting:
        for name in user:
            if user[name].weekday() not in (5, 6):
                result[user[name].strftime('%A')].append(name)
            else:
                result['Monday'].append(name)
    for k, v in result.items():
        if v:
           print(f'{k}: {", ".join(v)}')



if __name__ == '__main__':
    get_birthdays_per_week(users)
