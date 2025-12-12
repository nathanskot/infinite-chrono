def seconds_to_formatted_time(seconds: int):
    hh = seconds // 3600
    mm = (seconds - hh * 3600) // 60
    ss = seconds - hh * 3600 - mm * 60
    return f"{str(hh).rjust(2, '0')}:{str(mm).rjust(2, '0')}:{str(ss).rjust(2, '0')}"