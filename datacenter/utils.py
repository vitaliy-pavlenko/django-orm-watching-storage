import datetime


def get_hours(duration: datetime.timedelta):
    seconds = duration.total_seconds()
    return seconds // 3600


def get_minutes(duration: datetime.timedelta):
    seconds = duration.total_seconds()
    return (seconds % 3600) // 60


def get_total_minutes(duration: datetime.timedelta):
    seconds = duration.total_seconds()
    return seconds // 60


def format_duration(duration: datetime.timedelta):
    hours = get_hours(duration)
    minutes = get_minutes(duration)
    return f'{int(hours)}ч {int(minutes)}мин'
