from django.shortcuts import render
from notification.models import Notification
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="login")
def notification_view(request):
    count = 0
    notices = Notification.objects.filter(receiver=request.user)
    has_readed_notices = []
    for notice in notices:
        if notice.has_readed is False:
            count += 1
            has_readed_notices.append(notice.tweet)
            notice.has_readed = True
            notice.save()
    return render(request, 'notification.html', {
        "has_readed_notices": has_readed_notices
    })




