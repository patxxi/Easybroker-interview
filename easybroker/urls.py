from django.urls import path
from easybroker import views

urlpatterns = [
    path(
        route='',
        view=views.ListPropertiesView.as_view(),
    )
]
