from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView
from webapp.models import Athletes, Scramble,Info_fit


class Tablo_View(ListView):
    template_name = 'index.html'
    model = Athletes
    context_object_name = 'athlet'


class Fight(DetailView):
    template_name = 'figtht.html'
    model = Scramble
    context_object_name = 'at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program = get_object_or_404(Athletes, pk=self.kwargs.get('pk'))
        sb = get_object_or_404(Scramble, pk=self.kwargs.get('pk'))
        info = get_object_or_404(Info_fit, pk=self.kwargs.get('pk'))

        context['programs'] = program
        context['info'] = info
        context['sbs'] = sb

        return context