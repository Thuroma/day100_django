from django.urls import path
from day100 import views

urlpatterns = [

    # User views
    # Create User
    path('user/create/', views.create_user),

    # Log User In
    path('user/login/', views.log_user_in),


    # API Views
    # Get all curriculums or create new curriculum
    path('api/curriculums/', views.get_all_curriculums),

    # Get three most recent curriculums
    path('api/curriculums/recent/', views.get_recent_curriculums),

    # Get, update, or delete one curriculum
    path('api/curriculums/<int:curriculum_id>/', views.get_one_curriculum),

    # Get all daylogs for curriculum or create new daylog
    path('api/curriculum/<int:curriculum_id>/daylogs/', views.get_all_daylogs),

    # Get three most recent daylogs for curriculum
    path('api/curriculum/<int:curriculum_id>/daylogs/recent/', views.get_recent_daylogs),

    # Get, update, or delete one daylog from curriculum
    path('api/curriculum/<int:curriculum_id>/daylogs/<int:daylog_id>/', views.get_one_daylog),
]