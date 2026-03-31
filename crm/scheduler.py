from datetime import timedelta
from django.utils import timezone
from .models import HotelBooking


def hotel_reminder():

    now = timezone.now()

    reminder_time = now + timedelta(hours=24)

    hotels = HotelBooking.objects.filter(
        check_out__gte=now,
        check_out__lte=reminder_time,
        reminder_sent=False
    )

    for h in hotels:

        print(
            f"Reminder: {h.candidate.name} checkout tomorrow"
        )

        h.reminder_sent = True
        h.save()