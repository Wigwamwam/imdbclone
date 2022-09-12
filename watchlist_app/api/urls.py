from django.urls import path, include
# c
# from watchlist_app.api.views import movie_list, movie_details
# class based view:
from watchlist_app.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
	# path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_details, name='movie-details'),

    # class based view:
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailAV.as_view(), name='movie-detail'),
]
