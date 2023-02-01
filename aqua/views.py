from aqua.models import Aqua
from django.views import generic
from django.urls import reverse_lazy




class AquaCreateView(generic.CreateView):
    model = Aqua
    fields = "__all__"
    template_name = "add.html"
    success_url = reverse_lazy("aqua_list")


class AquaListView(generic.ListView):
    model = Aqua
    fields = "__all__"
    template_name = "list.html"


class AquaDetailView(generic.DetailView):
    model = Aqua
    fields = "__all__"
    template_name = "detail.html"
    success_url = reverse_lazy("aqua_list")


class AquaUpdateView(generic.UpdateView):
    model = Aqua
    fields = "__all__"
    template_name = "detail.html"
    success_url = reverse_lazy("aqua_list")


class AquaDeleteView(generic.UpdateView):
    model = Aqua
    fields = "__all__"
    template_name = "aqua/detail.html"
    success_url = reverse_lazy("aqua_list")
