import scrapy


class TabelasSpider(scrapy.Spider):
    name = 'tabelas'

    def start_requests(self):
        urls = [
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2003_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2004_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2005_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2006_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2007_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2008_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2009_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2010_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2011_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2012_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2013_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2014_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2015_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2016_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2017_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2018_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2019_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2020_-_S%C3%A9rie_A',
            'https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2021_-_S%C3%A9rie_A',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        if int(response.url.split('_')[5]) <= 2016:

            tabela = response.xpath('//table[@class="wikitable"][@border="1"]')
            linhas = tabela.xpath('tbody/tr')
            for indice in range(1, len(linhas)):
                nome = linhas[indice].xpath('td[not(contains(@rowspan, "1")) and not(contains(@rowspan, "2")) and not(contains(@rowspan, "3")) and not(contains(@rowspan, "4")) and not(contains(@rowspan, "5")) and not(contains(@rowspan, "6"))]//a/text()').get()
                if indice == 1:
                    pontos = linhas[indice].xpath('td/b/text()').extract()[1]
                else:
                    pontos = linhas[indice].xpath('td/b/text()').get()
                jogos = linhas[indice].xpath('td[not(contains(@align, "left"))]/text()').extract()[1]
                vitorias = linhas[indice].xpath('td[not(contains(@align, "left"))]/text()').extract()[2]
                empates = linhas[indice].xpath('td[not(contains(@align, "left"))]/text()').extract()[3]
                derrotas = linhas[indice].xpath('td[not(contains(@align, "left"))]/text()').extract()[4]
                gols_marcados = linhas[indice].xpath('td[not(contains(@align, "left"))]/text()').extract()[5]
                gols_sofridos = linhas[indice].xpath('td[not(contains(@align, "left"))]/text()').extract()[6]
                gols_saldo = linhas[indice].xpath('td[not(contains(@align, "left"))]/text()').extract()[7].replace('+', '')

                yield {
                    'nome': nome,
                    'pontos':pontos,
                    'jogos':jogos,
                    'vitorias':vitorias,
                    'empates':empates,
                    'derrotas':derrotas,
                    'gols_marcados':gols_marcados,
                    'gols_sofridos':gols_sofridos,
                    'gols_saldo':gols_saldo,
                    'ano': response.url.split('_')[5]
                }
        elif int(response.url.split('_')[5]) <= 2019:
            tabela = response.xpath('//table[@class="wikitable"]')[1]
            linhas = tabela.xpath('tbody/tr')
            for indice in range(1, len(linhas)):
                nome = linhas[indice].xpath('td[not(contains(@rowspan, "6")) and not(contains(@rowspan, "2")) and not(contains(@rowspan, "4"))]//a/text()').get()
                pontos = linhas[indice].xpath('td/b/text()').extract()[len(linhas[indice].xpath('td/b').extract())-1]
                dados = linhas[indice].xpath('td[not(child::b) and not(child::a)]/text()').extract()
                jogos = dados[1]
                vitorias = dados[2]
                empates = dados[3]
                derrotas = dados[4]
                gols_marcados = dados[5]
                gols_sofridos = dados[6]
                gols_saldo = dados[7]

                yield {
                    'nome': nome,
                    'pontos':pontos,
                    'jogos':jogos,
                    'vitorias':vitorias,
                    'empates':empates,
                    'derrotas':derrotas,
                    'gols_marcados':gols_marcados,
                    'gols_sofridos':gols_sofridos,
                    'gols_saldo':gols_saldo,
                    'ano': response.url.split('_')[5]
                }
        else:
            tabela = response.xpath('//table[@class="wikitable"]')[2]
            linhas = tabela.xpath('tbody/tr')
            for indece in range(1, len(linhas)):
                linha = tabela.xpath('tbody/tr')[indece]
                nome = linha.xpath('td//a/text()').get()
                pontos = linha.xpath('td//b/text()').extract()[len(linha.xpath('td//b/text()'))-1]
                dados = linha.xpath('td[not(child::b) and not(child::a)]/text()').extract()
                jogos = dados[1]
                vitorias = dados[2]
                empates = dados[3]
                derrotas = dados[4]
                gols_marcados = dados[5]
                gols_sofridos = dados[6]
                gols_saldo = dados[7]
                yield {
                    'nome': nome,
                    'pontos':pontos,
                    'jogos':jogos,
                    'vitorias':vitorias,
                    'empates':empates,
                    'derrotas':derrotas,
                    'gols_marcados':gols_marcados,
                    'gols_sofridos':gols_sofridos,
                    'gols_saldo':gols_saldo,
                    'ano': response.url.split('_')[5]
                }