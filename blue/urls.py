from django.urls import path
from .import views



urlpatterns = [
    path('', views.BlueCreateView.as_view(), name="create_blue"),
    path('list/', views.BlueListView.as_view(), name="blue_list"),
    path('detail/<int:id>', views.BlueDetailView.as_view(), name="blue_detail"),
    path('update/<int:id>', views.BlueUpdateView.as_view(), name="blue_update"),
    path('delete/<int:id>', views.BlueDeleteView.as_view(), name="blue_delete")
]
