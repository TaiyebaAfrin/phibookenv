from django.urls import path
from userauth import views
#from django.contrib.auth import login_view, signup_view
from django.conf.urls.static import static
from userauth.views import login_view, signup_view, logout_view, explore, profile, upload, follow, delete, search_results, likes, home_post, home_view 






urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'), 
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='login'),
    path('upload', upload),
    path('like-post/<str:id>', likes, name='like-post'),
    path('#<str:id>', home_post),
    path('explore', explore, name='explore'),
    path('profile/<str:id_user>', profile),
    path('follow', follow, name='follow'),
    path('delete/<str:id>', delete),
    path('search-results', search_results, name='search_results'),
]
