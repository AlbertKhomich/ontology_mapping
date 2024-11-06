import sys
from pathlib import Path
from rdflib import Graph, URIRef

def correct_concat(uri):
    uri = uri.replace('"', '') 

    if uri.endswith('/'):
        uri = uri[:-1]

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

def process_graph(file_path, format):
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

        output_file = file_path.with_name(file_path.stem + '_cleaned' + file_path.suffix)
        g.serialize(output_file, format=format)
        print(f"Cleaned file saved as '{output_file.name}'.")

    except Exception as e:
        print(f"Error while parsing {format}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 clean_uri.py <input_file> <format>")
        print("Format options: 'xml' for RDF/XML, 'nt' for N-Triples")
    else:
        input_file = Path(sys.argv[1])
        format = sys.argv[2].strip().lower()

        if format not in ['xml', 'nt']:
            print("Invalid format. Please use 'xml' for RDF/XML or 'nt' for N_Triples.")
        else:
            process_graph(input_file, format)
