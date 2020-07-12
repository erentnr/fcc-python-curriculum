def add_time(start, duration, *day):

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']

    passed_days = 0

    start_hour = start.split()[0].split(':')[0]
    start_min = start.split()[0].split(':')[1]
    add_hour = duration.split(':')[0]
    add_min = duration.split(':')[1]
    time_period = start.split()[1]

    final_min = int(start_min) + int(add_min)
    if final_min > 60:
        extra_hours = final_min // 60
        final_min = final_min % 60
        final_hour = int(start_hour) + int(add_hour) + extra_hours
    else:
        final_hour = int(start_hour) + int(add_hour)

    passed_periods = final_hour // 12

    if time_period == 'AM':
        if final_hour > 12:
            if (passed_periods % 2)  == 1:
                time_period = 'PM'
            passed_days = final_hour // 24
            final_hour = final_hour % 12
            if final_hour == 0:
                final_hour = 12
        if (passed_periods % 2)  == 1:
            time_period = 'PM'
    else:
        if final_hour > 12:
            passed_days = (final_hour // 24) + 1
            final_hour = final_hour % 12
            if final_hour == 0:
                final_hour = 12
        if (passed_periods % 2)  == 1:
            time_period = 'AM'

    if day:
        day = day[0].capitalize()
        current_day = days.index(day)
        new_day = days[(current_day + (passed_days % 7)) % 7]
        if passed_days == 0:
            new_time = '%d:%02d %s, %s' % (final_hour, final_min, time_period, new_day)
        elif passed_days == 1:
            new_time = '%d:%02d %s, %s (next day)' % (final_hour, final_min, time_period, new_day)
        else:
            new_time = '%d:%02d %s, %s (%s days later)' % (final_hour, final_min, time_period, new_day, passed_days)
    else:
        if passed_days == 0:
            new_time = '%d:%02d %s' % (final_hour, final_min, time_period)
        elif passed_days == 1:
            new_time = '%d:%02d %s (next day)' % (final_hour, final_min, time_period)

        else:
            new_time = '%d:%02d %s (%s days later)' % (final_hour, final_min, time_period, passed_days)


    return new_time
