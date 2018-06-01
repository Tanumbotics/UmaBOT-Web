from django.urls import include, path
from tf_web import views


urlpatterns = [
    path('', views.upload_file, name='upload')
]
