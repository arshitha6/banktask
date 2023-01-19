from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('/register', views.register, name="register"),
    path('/login', views.login, name="login"),
    path('/logout', views.logout, name="logout"),
    path('/person', views.personDetail, name="person"),
    path('/info', views.infodata, name="info"),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax_load_branches', views.load_branches, name='ajax_load_branches'),
    path('/pop_up', views.pop_up, name="pop_up"),
]
