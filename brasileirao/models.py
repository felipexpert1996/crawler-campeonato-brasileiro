from django.db import models

class Time(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Campeonato(models.Model):
    ano = models.CharField(max_length=4)

    def __str__(self):
        return self.ano


class Tabela(models.Model):
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    pontos = models.IntegerField()
    jogos = models.IntegerField()
    vitorias = models.IntegerField()
    empates = models.IntegerField()
    derrotas = models.IntegerField()
    gols_marcados = models.IntegerField()
    gols_sofridos = models.IntegerField()
    gols_saldo = models.IntegerField()

    def __str__(self):
        return f'{self.campeonato} - {self.time}'
