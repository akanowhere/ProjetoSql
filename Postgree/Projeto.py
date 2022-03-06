import requests
import zipfile
import io
import pandas as pd
import psycopg2





def criar_tabela(self):
    conn = psycopg2.connect(database="tutorial",
                            user='postgres', password='tlaush2020',
                            host='localhost'
                            )

    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS {};".format("ACIDENTES"))

    sql = '''CREATE TABLE ACIDENTES(
    idpk SERIAL PRIMARY KEY, 
    id varchar(20),\
    pesid varchar(10),\
    data_inversa timestamp,\
    dia_semana varchar(20),\
    horario time,\
    uf varchar(4),\
    br varchar(4),\
    km varchar(16),\
    municipio varchar(50),\
    causa_principal varchar(10),\
    causa_acidente varchar(100),\
    ordem_tipo_acidente varchar(20),\
    tipo_acidente varchar(50),\
    classificacao_acidente varchar(40),\
    fase_dia varchar(20),\
    sentido_via varchar(20),\
    condicao_metereologica varchar(20),\
    tipo_pista varchar(20),\
    tracado_via varchar(50),\
    uso_solo varchar(10),\
    id_veiculo varchar(20),\
    tipo_veiculo varchar(40),\
    marca varchar(60),\
    ano_fabricacao_veiculo varchar(10),\
    tipo_envolvido varchar(20),\
    estado_fisico varchar(40),\
    idade varchar(10),\
    sexo varchar(20),\
    ilesos int,\
    feridos_leves int,\
    feridos_graves int,\
    mortos int ,\
    latitude varchar(20),\
    longitude varchar(20),\
    regional varchar(20),\
    delegacia varchar(20),\
    uop varchar(40)\
    );'''

    cursor.execute(sql)
    conn.commit()
    conn.close()




def importar(self):
    url = ['https://arquivos.prf.gov.br/arquivos/index.php/s/kgJ0ea8QZrix5Yt/download','https://arquivos.prf.gov.br/arquivos/index.php/s/EF4uPKCihT0ouXd/download','https://arquivos.prf.gov.br/arquivos/index.php/s/sdvJndbl5wLyh3J/download','https://arquivos.prf.gov.br/arquivos/index.php/s/hXimwPNR9lyqdMS/download','http://arquivos.prf.gov.br/arquivos/index.php/s/AbbxlG5pYA27WPU/download']


    for link in url:
        res = requests.get(link, allow_redirects=True)
        zip = zipfile.ZipFile(io.BytesIO(res.content))
        open(zip.namelist()[0], 'wb').write(res.content)
        zip.extractall()
        conn = psycopg2.connect(database="tutorial",
                            user='postgres', password='tlaush2020',
                            host='localhost'
                            )
        cur = conn.cursor()
        with open(zip.namelist()[0], 'r', encoding='Latin-1') as f:
            next(f)
            cur.copy_from(f, 'ACIDENTES', sep=';', null='\\N', columns=['id', 'pesid', 'data_inversa', 'dia_semana', 'horario', 'uf', 'br', 'km', 'municipio', 'causa_principal', 'causa_acidente', 'ordem_tipo_acidente', 'tipo_acidente', 'classificacao_acidente', 'fase_dia', 'sentido_via', 'condicao_metereologica', 'tipo_pista', 'tracado_via', 'uso_solo', 'id_veiculo', 'tipo_veiculo', 'marca', 'ano_fabricacao_veiculo', 'tipo_envolvido', 'estado_fisico', 'idade', 'sexo', 'ilesos', 'feridos_leves', 'feridos_graves', 'mortos', 'latitude', 'longitude', 'regional', 'delegacia', 'uop'])
        conn.commit()


a = 'joao'
criar_tabela(a)
importar(a)