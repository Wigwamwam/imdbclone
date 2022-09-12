from django.urls import path, include
# c
# from watchlist_app.api.views import movie_list, movie_details
# class based view:
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamListAV

urlpatterns = [
	# path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_details, name='movie-details'),

    # class based view:
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='watch-detail'),
    path('stream/', StreamListAV.as_view(), name='stream'),
]
