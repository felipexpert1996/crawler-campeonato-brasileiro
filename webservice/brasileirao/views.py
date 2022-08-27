from django.views.generic.list import ListView
from .models import Tabela, Time
from django.db.models import Sum


class TabelaListViewset(ListView):
    model = Tabela
    template_name = 'tabela_list.html'
    context_object_name = 'object'

    def get_queryset(self):
        return Tabela.objects.all().values('time__nome').distinct().annotate(Sum('pontos'), Sum('jogos'), Sum('vitorias'), Sum('vitorias'), Sum('empates'), Sum('derrotas'), Sum('gols_marcados'), Sum('gols_sofridos'), Sum('gols_saldo')).order_by('-pontos__sum')
