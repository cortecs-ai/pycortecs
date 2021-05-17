from datetime import datetime

date_fmt = "%Y-%m-%d"


def is_valid_date(date_str):
    if get_datetime_from_string(date_str):
        return True
    return False


def get_datetime_from_string(date_str):
    try:
        return datetime.strptime(date_str, date_fmt)
    except:
        return None


