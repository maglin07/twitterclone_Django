from django.urls import path
from notification.views import (
    notification_view,
)

urlpatterns = [
    path("notifications/", notification_view, name='notification')
    ]