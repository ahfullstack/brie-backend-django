from django.urls import path
from . import views

urlpatterns = [
    path('api/status', views.StatusList.as_view(), name='status_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/status/<int:pk>', views.StatusDetail.as_view(), name='status_detail'), # api/contacts will be routed to the ContactDetail view for handling
]