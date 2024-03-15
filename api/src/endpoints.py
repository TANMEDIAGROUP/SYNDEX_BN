from django.urls import path
from .routes import routes

urlpatterns=[
    path('',routes.root),
    path('user/all',routes.getUsers),
    path('user/create',routes.createUsers)
]