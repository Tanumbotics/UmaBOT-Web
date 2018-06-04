from django.views.generic import RedirectView
from django.urls import include, path
from tensorflow_web import views


urlpatterns = [
    path('upload/', views.upload_file, name='upload'),
    path('', RedirectView.as_view(url='upload/'))
]
