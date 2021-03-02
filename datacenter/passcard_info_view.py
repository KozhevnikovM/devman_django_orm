from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .helpers import *


def passcard_info_view(request, passcode):
    current_passcard = Passcard.objects.all().get(passcode=passcode)
    this_passcard_visits = [
        {
            "entered_at": visit.entered_at,
            "duration": format_duration(get_duration(visit)),
            "is_strange": is_visit_long(visit, 3600)
        } 
        for visit in Visit.objects.all().filter(passcard=current_passcard)
    ]
    context = {
        "passcard": current_passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
