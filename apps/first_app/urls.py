from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^postresult$', views.postresult),
    url(r'^remove$', views.remove),
    url(r'^delete$', views.delete),
    # url(r'^session-test/$', views.session_test_1),
    # url(r'^session-test/done/$', views.session_test_2),

]
