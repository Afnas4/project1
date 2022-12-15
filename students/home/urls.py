from django.urls import path
from .import views

urlpatterns = [
     path('home',views.Home.as_view(),name="home"),
     path('staff',views.StaffS.as_view(),name="staff"),
     path('enquiry',views.Enquiry.as_view(),name="enquiry"),
     path('showstudent',views.Showstudent.as_view(),name="showstudent"),
     path('forms',views.Form.as_view(),name="forms"),
     path('profile',views.Profile.as_view(),name="profile"),
     path('edit',views.Edit.as_view(),name="edit"),

]
