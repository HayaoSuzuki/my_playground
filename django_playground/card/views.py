from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from .forms import CardModelForm
from .models import Card


class CardListView(generic.ListView):
    context_object_name = "card_list"
    template_name = "card/card_list.html"
    model = Card


class CardCreateView(generic.FormView):
    form_class = CardModelForm
    template_name = "card/card_create.html"
    success_url = reverse_lazy("card:list")

    def form_valid(self, form: CardModelForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)
