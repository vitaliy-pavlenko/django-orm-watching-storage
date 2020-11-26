from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from .utils import format_duration


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
        non_closed_visits.append({
            'who_entered': Passcard.objects.get(owner_name=visit.passcard),
            'entered_at': visit.entered_at,
            'duration': format_duration(visit.get_duration()),
            'is_strange': visit.is_visit_long()
        })
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
