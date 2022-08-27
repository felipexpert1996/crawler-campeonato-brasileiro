import scrapy


class Tabela2022Spider(scrapy.Spider):
    name = 'tabelas_2022'

    def start_requests(self):
        urls = [
            'https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        tabela = response.css('.col-main table tr')
        tamanho_tabela = len(tabela)
        tamanho_tabela = len(tabela)
        for index in range(1, tamanho_tabela):
            yield {
                'nome':tabela[index].css('.team-name a::text').get(),
                'pontos':tabela[index].css('.points::text').get(),
                'jogos':tabela[index].xpath('td[@title="Jogos"]/text()').get(),
                'vitorias':tabela[index].xpath('td[@title="Vitórias"]/text()').get(),
                'empates':tabela[index].xpath('td[@title="Empates"]/text()').get(),
                'derrotas':tabela[index].xpath('td[@title="Derrotas"]/text()').get(),
                'gols_marcados':tabela[index].xpath('td[@title="Gols Pró"]/text()').get(),
                'gols_sofridos':tabela[index].xpath('td[@title="Gols Contra"]/text()').get(),
                'gols_saldo':tabela[index].xpath('td[@title="Saldo de Gols"]/text()').get(),
            }
