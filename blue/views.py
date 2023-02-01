from .models import Blue
from django.views import generic
from django.urls import reverse_lazy




class BlueCreateView(generic.CreateView):
    model = Blue
    fields = "__all__"
    template_name = "add.html"
    success_url = reverse_lazy("blue_list")


class BlueListView(generic.ListView):
    model = Blue
    fields = "__all__"
    template_name = "list.html"


class BlueDetailView(generic.DetailView):
    model = Blue
    fields = "__all__"
    template_name = "detail.html"
    success_url = reverse_lazy("blue_list")


class BlueUpdateView(generic.UpdateView):
    model = Blue
    fields = "__all__"
    template_name = "detail.html"
    success_url = reverse_lazy("blue_list")


class BlueDeleteView(generic.UpdateView):
    model = Blue
    fields = "__all__"
    template_name = "Blue/detail.html"
    success_url = reverse_lazy("blue_list")
