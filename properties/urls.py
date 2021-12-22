from django.urls import path
from properties import views

urlpatterns = [
    path(
        route='',
        view=views.ListPropertiesView.as_view(),
        name='home'
    ),
    path(
        route='detail/<str:id>',
        view=views.FormContactView.as_view(),
        name='detail'
    )

]
