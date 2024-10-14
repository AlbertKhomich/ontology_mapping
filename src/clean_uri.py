from pathlib import Path
from rdflib import Graph, URIRef

current_dir = Path(__file__).resolve().parent
data_dir = current_dir.parent / "data"

file_path = data_dir / "WDC/WDC_properties_new.rdf"

def correct_concat(uri):
    uri = uri.replace('"', '') 

    last_https = uri.rfind('https://')
    last_http = uri.rfind('http://')

    # take the last part of concatenated URI
    if last_https != -1 and last_http != -1:
        if last_https > last_http:
            return 'https://' + uri.split('https://')[-1]
        else:
            return 'http://' + uri.split('http://')[-1]
        
    # remove multiple '#' in URI
    if uri.count('#') > 1:
        uri = uri.split('#', 1)[0] + '#' + uri.split('#', 1)[1].split('/')[0]
        
    return uri

g = Graph()

try:
    g.parse(file_path, format="xml")

    for s, p, o in g:
        if isinstance(s, URIRef) and not s.startswith('http'):
            g.remove((s, p ,o))
            continue

        checked_uri = correct_concat(str(s))
        if checked_uri != str(s):
            g.remove((s, p, o))
            g.add((URIRef(checked_uri), p, o))

    g.serialize(data_dir / 'WDC/WDC_properties_cleaned.rdf', format='pretty-xml')
    print("Cleaned RDF file saved as 'cleaned_output.rdf'.")

except Exception as e:
    print(f"Error while parsing RDF: {e}")
