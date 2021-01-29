def get_hours(duration: float):
    return duration // 3600


def get_minutes(duration: float):
    return (duration % 3600) // 60


def get_total_minutes(duration: float):
    return duration // 60


def format_duration(duration: float):
    hours = get_hours(duration)
    minutes = get_minutes(duration)
    return f'{int(hours)}ч {int(minutes)}мин'
