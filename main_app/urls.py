from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('finches/', views.finches_index, name='index'),
    path('finches/', views.finches_index, name="finches_index"),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/add_photo', views.add_photo, name='add_photo'),
    #Finch-park associate and unassociate functions: Many-to-Many
    path('finches/<int:finch_id>/assoc_park/<int:park_id>', views.assoc_park, name='assoc_park'),
    path('finches/<int:finch_id>/unassoc_park/<int:park_id>', views.unassoc_park, name='unassoc_park'),
    #parks paths
    path('parks/', views.ParkList.as_view(), name='parks_index'),
    path('parks/<int:pk>', views.ParkDetail.as_view(), name='parks_detail'),
    path('parks/create/', views.ParkCreate.as_view(), name='parks_create'),
    path('park/<int:pk>/update/', views.ParkUpdate.as_view(), name='parks_update'),
    path('parks/<int:pk>/delete/', views.ParkDelete.as_view(), name='parks_delete'),
    #Auth
    path('accounts/signup/', views.signup, name='signup'),
    
]
