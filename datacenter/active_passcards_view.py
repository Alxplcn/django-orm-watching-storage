from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datetime import datetime, timedelta


def active_passcards_view(request):
    passcards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': passcards,  # люди с активными пропусками
    }
    return render(request, 'active_passcards.html', context)
