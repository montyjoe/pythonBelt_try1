from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^trips$', views.trips),
    url(r'^trips/join$', views.join),
    url(r'^trips/destination$', views.destination),
    url(r'^trips/add_page$', views.add_trip_page),
    url(r'^trips/add$', views.add_trip),
    # url(r'^trips/destination/(?P<trip_id>\d+)$', views.trip_details),
    # url(r'^books/add$', views.add_books),
    # url(r'^books/(?P<book_id>\d+)$', views.books_id),

]
