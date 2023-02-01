from django.urls import path
from .import views



urlpatterns = [
    path('', views.AquaCreateView.as_view(), name="create_aqua"),
    path('list/', views.AquaListView.as_view(), name="aqua_list"),
    path('detail/<int:id>', views.AquaDetailView.as_view(), name="aqua_detail"),
    path('update/<int:id>', views.AquaUpdateView.as_view(), name="aqua_update"),
    path('delete/<int:id>', views.AquaDeleteView.as_view(), name="aqua_delete")
]
