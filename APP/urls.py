from django.urls import path
from .views import home, yaratish, uzgartirish, delete

urlpatterns = [
    path("", home, name="home"),
    path("create/", yaratish, name="create"),
    path("uzgarish/<int:pk>/", uzgartirish, name="edit"),
    path("delete/<int:pk>/", delete, name="delete")
]
