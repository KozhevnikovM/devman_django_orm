from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(visit):
        if not visit.leaved_at:
            return (localtime() - localtime(visit.entered_at)).total_seconds()
        return (visit.leaved_at - visit.entered_at).total_seconds()


    def is_visit_long(self, limit=3600):
        return self.get_duration() > limit

    def format_duration(self):
        hours, remainder = divmod(self.get_duration(), 3600)
        minutes, seconds = divmod(self.get_duration(), 60)
        return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
