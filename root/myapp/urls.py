from django.urls import path
from myapp.views import HomePage

app_name = "myapp"

urlpatterns = [
    path("", HomePage.as_view(), name="home_page")
]
