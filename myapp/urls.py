from django.urls import path
from myapp.views import Myview

urlpatterns = [
    path('about/', Myview.as_view())
]