from datetime import datetime

# for school period reminders

school_days_periods = {
    'Mon': [f"{i[:2]}h {i[2:]}min" for i in ['0830', '1050','1020', '1155', '1250', '1425', '1440', '1615']], 
    'Tue': [f"{i[:2]}h {i[2:]}min" for i in ['0830', '1050','1020', '1155', '1250', '1335', '1340', '1425', '1440', '1615']],
    'Wed': [f"{i[:2]}h {i[2:]}min" for i in ['0830', '1050','1020', '1155', '1250', '1425', '1440', '1525']],
    'Thu': [f"{i[:2]}h {i[2:]}min" for i in ['0830', '1050','1020', '1155', '1250', '1425', '1440', '1615']],
    'Fri': [f"{i[:2]}h {i[2:]}min" for i in ['0830', '1050','1020', '1155', '1250', '1425']]
}

classes = {
    'Mon': ['Deutsch BEGINN', 'Deutsch ENDE', 'Englisch BEGINN', 'Pause', 'Ethik BEGINN', 'Ethik ENDE', 'Geographie BEGINN', 'ENDE DES SCHULTAGS'],
    'Tue': ['Geschichte BEGINN', 'Geschichte ENDE', 'Physik BEGINN', 'Pause', 'Deutsch BEGINN', 'Deutsch ENDE', 'Mathe BEGINN', 'Mathe ENDE', 'Sport BEGINN', 'ENDE DES SCHULTAGS'],
    'Wed': ['Kunst BEGINN', 'Kunst ENDE', 'Mathe BEGINN', 'Pause', 'Französisch BEGINN', 'Französisch ENDE', 'Mathe BEGINN', 'ENDE DES SCHULTAGS'],
    'Thu': ['Chemie BEGINN', 'Chemie ENDE', 'Mathe BEGINN', 'Pause', 'Deutsch BEGINN', 'Deutsch ENDE', 'Englisch BEGINN', 'ENDE DES SCHULTAGS'],
    'Fri': ['Musik BEGINN', 'Musik ENDE', 'Französisch BEGINN', 'Pause', 'Bio BEGINN', 'ENDE DES SCHULTAGS']
}

# all of the remaining holidays/days off
holidays = ['1705', '1206', '0707'] + \
    ['0' + str(i) + '07' if i < 10 else str(i) + '07' for i in range(8, 32)] + \
    ['0' + str(i) + '08' if i < 10 else str(i) + '08' for i in range(1, 32)]


def school_reminder(last_day=0, last_period_time=0):
    now = datetime.now().strftime("%a%d%B%m_%H%M")
    date, time = now.split('_')
    time = f"{time[:2]}h {time[2:]}min"

    day = date[:3]
    day_num = date[3:5]
    month = date[5:8]
    month_num = date[8:]

    if day != any(['Sun', 'Sat']):
        if last_day != day and last_period_time not in school_days_periods[day]:
            if day_num+month_num not in holidays:
                for i in range(len(school_days_periods[day])):
                    if time == school_days_periods[day][i]:
                        period = f"{time} {classes[day][i]}"
                        play = True
                        return (play, day, period)

    play = False
    return (play, last_day, last_period_time)

print(school_reminder(0, 0))
