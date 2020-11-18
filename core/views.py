from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView


class IndexView(TemplateView):

    template_name = "estagio.index.html"
