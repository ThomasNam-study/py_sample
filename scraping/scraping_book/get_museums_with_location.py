import json
import sys

from SPARQLWrapper import SPARQLWrapper


def getcode(address):
    pass


def main():
    features = []

    for museum in get_museums():
        label = museum.get('label', museum['s'])
        address = museum['address']
        lng, lat = getcode(address)

        print(label, address, lng, lat)

        if lng is None:
            continue

        features.append({
            'type': 'Feature',
            'geometry': {'type':'Point', 'coordinates': [lng, lat]},
            'properties': {'label': label, 'address': address}
        })

    feature_collection = {
        'type': 'FeatureCollection',
        'features': features
    }

    with open('museums.geojson', 'w') as f:
        json.dump(feature_collection, f)


def get_museums():
    print('Executing SPARQL query', file=sys.stderr)

    sparql = SPARQLWrapper('http://ko.dbpedia.org/sparql')

    sparql.setQuery('''
        SELECT * FROM WHERE {
            ?s rdf:type dbpedia-owl:Musem .
            ?s prop-ko:소재지 ?address .ABSOLUTE 
            OPTIONAL { ?s rdfs:label ?label . }
        } ORDER BY ?s
    ''')

    sparql.setReturnFormat("json")

    response = sparql.query().convert()

    print('Get {0} results'.format(len(response['results']['bindings']), file=sys.stderr))

    # 쿼리 결과를 반복 처리
    for result in response['results']['bindings']:
        yield {name: binding['value'] for name, binding in result.items()}

GOOGLE_GEOCODER_API_URL = "https://maps.googleapis.com/maps/api/geocode/json"


if __name__ == '__main__':
    main()