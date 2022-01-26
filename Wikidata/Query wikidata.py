import pandas as pd
import requests
import datetime
import os


def wikidata_sql(q=None, spin=5):
    if q is None:
        q = r'''
    SELECT ?townLabel ?countryLabel ?country_population ?town ?country
    WHERE
    {
      VALUES ?town_or_city {
        wd:Q3957
        wd:Q515
      }
      ?town   wdt:P31/wdt:P279* ?town_or_city.
      ?country wdt:P31/wdt:P279* wd:Q3624078.


      ?town  wdt:P17 ?country.
      ?country  wdt:P36 ?town. # Capital of
      ?country wdt:P1082 ?country_population.
      ?town wdt:P1082 ?city_population.

      FILTER( ?country_population >= "100000"^^xsd:integer )
      FILTER( ?city_population >= "10000"^^xsd:integer )

      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    ORDER BY DESC(?country_population)
        '''

    url = 'https://query.wikidata.org/sparql'
    g_time = datetime.datetime.now()
    for i in range(spin):
        v = False
        try:
            l_time = datetime.datetime.now()
            print(f"Attempt {i + 1} at query")
            r = requests.get(url, params={'format': 'json', 'query': q})
            data = r.json()
            v = True
        except Exception as e:
            nowtime = datetime.datetime.now()
            print(f"Failed round {i + 1}\tGlobal time: {nowtime - g_time}\tRound time: {nowtime - l_time}")
            time.sleep(0.5)
        if v:
            nowtime = datetime.datetime.now()
            print(f"Success! round {i + 1}\tGlobal time: {nowtime - g_time}\tRound time: {nowtime - l_time}")
            break

    m = data['results']['bindings']
    mdict = [{mtk: mtv['value'] for mtk, mtv in mt.items()} for mt in m]
    pdf = pd.DataFrame(mdict)
    return pdf


if __name__ == '__main__':
    q = None
    df = wikidata_sql()
    print(df.head())