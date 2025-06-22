import datetime, bday_messages
today = datetime.date.today()
next_birthday = datetime.date(2026, 3, 31)
days_away = time_difference = next_birthday - today

if today == next_birthday:
    print (random_message)
else:
    print (f'My next birthday is {days_away} Days away!')

halo_two_release = datetime.date(2004, 11, 9)
days_since_halo_release = today - halo_two_release

print (f'Halo 2 was released {days_since_halo_release} days ago')