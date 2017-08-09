from django.conf.urls import url
from django.contrib import admin

from emp.views import(app_create,
                      app_detail,
                      app_list,
                      app_update,
                      app_delete)

urlpatterns = [
    url(r'^$', app_list, name="App list"),
    url(r'^create', app_create, name="App_Create"),
    url(r'^detail', app_detail, name="App_Detail"),
    url(r'^update', app_update, name="App_Update"),
    url(r'^delete', app_delete, name="App_Delete"),
]
