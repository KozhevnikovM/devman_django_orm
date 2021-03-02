from django.utils.timezone import localtime

def get_duration(visit):
    if not visit.leaved_at:
        return (localtime() - localtime(visit.entered_at)).total_seconds()
    return (visit.leaved_at - visit.entered_at).total_seconds()


def is_visit_long(visit, limit):
    return get_duration(visit) > limit


def format_duration(duration):
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
