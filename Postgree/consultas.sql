-- serie histórica
SELECT
date_part('year', data_inversa) AS ANO,
date_part('month', data_inversa) AS MES,
uf,
COUNT(uf)
FROM public.acidentes
GROUP BY ANO,MES,UF;


-- Municipio com maior vítimas no carnaval de 2021

SELECT
municipio,
COUNT(municipio)
FROM public.acidentes
WHERE data_inversa BETWEEN '2021-02-12 00:00:00' AND  '2021-02-17 00:00:00'
AND mortos = 1
GROUP BY municipio
ORDER BY COUNT(municipio) DESC;

-- Causa principal de acidente em cada regiao 2021
SELECT
	causa_acidente,
	count(causa_acidente),
	CASE
	WHEN uf LIKE ('%SP%') OR uf LIKE ('%ES%') OR uf LIKE ('%RJ%') OR uf LIKE ('%MG%') THEN 'SUDESTE'
	WHEN uf LIKE ('%RS%') OR uf LIKE ('%SC%') OR uf LIKE ('%PR%') THEN 'SUL'
	WHEN uf LIKE ('%MS%') OR uf LIKE ('%MG%') OR uf LIKE ('%DF%') OR uf LIKE ('%GO%')THEN 'CENTRO-OESTE'
	WHEN uf LIKE ('%AC%') OR uf LIKE ('%AP%') OR uf LIKE ('%AM%') OR uf LIKE ('%PA%') OR uf LIKE ('%RO%') OR uf LIKE ('%RR%')  OR uf LIKE ('%TO%') THEN 'NORTE'
	WHEN uf LIKE ('%AL%') OR uf LIKE ('%BA%') OR uf LIKE ('%CE%') OR uf LIKE ('%MA%') OR uf LIKE ('%PB%') OR uf LIKE ('%PI')OR uf LIKE ('%RN') THEN 'NORDESTE'
	ELSE 'SEM ESTADO'
	END as regioes
FROM public.acidentes WHERE data_inversa BETWEEN '2021-01-01 00:00:00' AND  '2021-12-31 00:00:00'
GROUP BY regioes,uf,causa_acidente
ORDER BY count(causa_acidente) DESC;

-- Acidentes mes de janeiro em cada capital
SELECT * FROM (
SELECT
date_part('year', data_inversa) AS ANO,
date_part('month', data_inversa) AS MES,
municipio,
COUNT(municipio) AS QTD_MUN
FROM public.acidentes
WHERE municipio LIKE ANY (VALUES('"RIO BRANCO"'), ('"MACAPA"'), ('"MANAUS"'),
('"BELEM"'), ('"PORTO VELHO"'), ('"BOA VISTA"'), ('"PALMAS"'), ('"MACEIO"'), ('"SALVADOR"'), ('"FORTALEZA"'), ('"SAO LUIS"'), ('"JOAO PESSOA"'), ('"RECIFE"'), ('"TERESINA"'),
('"NATAL"'), ('"ARACAJU"'), ('"GOIANIA"'), ('"CUIABA"'), ('"CAMPO GRANDE"'), ('"BRASILIA"'), ('"VITORIA"'), ('"BELO HORIZONTE"'), ('"SAO PAULO"'), ('"RIO DE JANEIRO"'),
('"CURITIBA"'), ('"PORTO ALEGRE"'), ('"FLORIANOPOLIS"')) AND data_inversa BETWEEN '2017-01-01 00:00:00' AND '2021-12-31 00:00:00'
GROUP BY ANO, MES, municipio) as A
WHERE MES = 1;

