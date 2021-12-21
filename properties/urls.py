from django.urls import path
from properties import views

urlpatterns = [
    path(
        route='',
        view=views.ListPropertiesView.as_view(),
    ),
    path(
        route='detail/<str:id>',
        view=views.DetailPropertyView.as_view(),
        name='detail'
    )
]
