from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'test_upload$',views.test_upload,name='test_upload'),
]

