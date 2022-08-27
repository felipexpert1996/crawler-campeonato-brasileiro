import json
import sqlite3

arquivo = open('scrap/brasileirao/resultado.json')
data = json.load(arquivo)
connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

for resultado in data:
    
    if connection:
        
        cursor.execute(f"SELECT * FROM brasileirao_time where nome='{resultado['nome'].capitalize()}'")
        rows = cursor.fetchall()
        if len(rows) == 0:
            cursor.execute(f"INSERT INTO brasileirao_time (nome) VALUES ('{resultado['nome'].capitalize()}')")
            connection.commit()
            cursor.execute(f"SELECT * FROM brasileirao_time where nome='{resultado['nome'].capitalize()}'")
            rows = cursor.fetchall()
            id_time = rows[0][0]
        else:
            id_time = rows[0][0]
        
        cursor.execute(f"SELECT * FROM brasileirao_campeonato where ano='{resultado['ano']}'")
        rows = cursor.fetchall()
        if len(rows) == 0:
            cursor.execute(f"INSERT INTO brasileirao_campeonato (ano) VALUES ('{resultado['ano']}')")
            connection.commit()
            cursor.execute(f"SELECT * FROM brasileirao_campeonato where ano='{resultado['ano']}'")
            rows = cursor.fetchall()
            id_campeonato = rows[0][0]
        else:
            id_campeonato = rows[0][0]
        

        cursor.execute(f"SELECT * FROM brasileirao_tabela where campeonato_id='{id_campeonato}' and time_id='{id_time}'")
        rows = cursor.fetchall()
        if len(rows) == 0:
            cursor.execute(f"INSERT INTO brasileirao_tabela (campeonato_id, time_id, jogos, pontos, vitorias, empates, derrotas, gols_marcados, gols_sofridos, gols_saldo) VALUES ('{id_campeonato}', '{id_time}', '{resultado['jogos']}', '{resultado['pontos']}', '{resultado['vitorias']}', '{resultado['empates']}', '{resultado['derrotas']}', '{resultado['gols_marcados']}', '{resultado['gols_sofridos']}', '{int(resultado['gols_marcados']) - int(resultado['gols_sofridos'])}')")
            connection.commit()

arquivo = open('scrap/brasileirao/resultado_2022.json')
data = json.load(arquivo)
for resultado in data:

    if connection:
        cursor.execute(f"SELECT * FROM brasileirao_time where nome='{resultado['nome'].capitalize()}'")
        rows = cursor.fetchall()
        if len(rows) == 0:
            cursor.execute(f"INSERT INTO brasileirao_time (nome) VALUES ('{resultado['nome'].capitalize()}')")
            connection.commit()
            cursor.execute(f"SELECT * FROM brasileirao_time where nome='{resultado['nome'].capitalize()}'")
            rows = cursor.fetchall()
            id_time = rows[0][0]
        else:
            id_time = rows[0][0]
        
        cursor.execute(f"SELECT * FROM brasileirao_campeonato where ano='2022'")
        rows = cursor.fetchall()
        if len(rows) == 0:
            cursor.execute(f"INSERT INTO brasileirao_campeonato (ano) VALUES ('2022')")
            connection.commit()
            cursor.execute(f"SELECT * FROM brasileirao_campeonato where ano='2022'")
            rows = cursor.fetchall()
            id_campeonato = rows[0][0]
        else:
            id_campeonato = rows[0][0]
        

        cursor.execute(f"SELECT * FROM brasileirao_tabela where campeonato_id='{id_campeonato}' and time_id='{id_time}'")
        rows = cursor.fetchall()
        if len(rows) == 0:
            cursor.execute(f"DELETE FROM brasileirao_tabela WHERE campeonato_id='{id_campeonato}' and time_id='{id_time}'")
            connection.commit()
            cursor.execute(f"INSERT INTO brasileirao_tabela (campeonato_id, time_id, jogos, pontos, vitorias, empates, derrotas, gols_marcados, gols_sofridos, gols_saldo) VALUES ('{id_campeonato}', '{id_time}', '{resultado['jogos']}', '{resultado['pontos']}', '{resultado['vitorias']}', '{resultado['empates']}', '{resultado['derrotas']}', '{resultado['gols_marcados']}', '{resultado['gols_sofridos']}', '{int(resultado['gols_marcados']) - int(resultado['gols_sofridos'])}')")
            connection.commit()

cursor.close()
connection.close()
arquivo.close()
