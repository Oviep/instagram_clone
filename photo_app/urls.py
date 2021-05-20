from django.urls import path

from photo_app.views import PostView

urlpatterns = [
    path('', PostView.as_view(), name="posts")
]