from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('order/', order, name='order'),
    path('support/', support, name='support'),
    path('feedback/', feedback, name='feedback'),
    path('about_project/', about_project, name='about_project'),
    path('about_us/', about_us, name='about_us'),
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_out/', sign_out, name='sign_out'),
    path('<slug:car_slug>/', CarDetailView.as_view(), name='car'),
]
