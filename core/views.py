from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView



class IndexView(TemplateView):

    template_name = "estagio.index.html"


class SegundaPaginaView(TemplateView):
    template_name = "segundapagina.index.html"

class TerceiraPaginaView(TemplateView):

    template_name = "play.index.html"

class QuartaPaginaView(TemplateView):

    template_name = "canais.index.html"


class QuintaPaginaView(TemplateView):

    template_name = "aplicativos.index.html"

class SextaPaginaView(TemplateView):

    template_name = "dicas.index.html"