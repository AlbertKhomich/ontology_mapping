from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef, Literal
from rdflib.namespace import RDF, RDFS, OWL
import sys

def determine_property_type(uri):
    uri_str = str(uri).lower()
    object_keywords = ['item', 'list', 'organization', 'webpage', 'breadcrumb']
    if any(keyword in uri_str for keyword in object_keywords):
        return OWL.ObjectProperty
    else:
        return OWL.DatatypeProperty
    
def nt_to_owl(nt_file_path, owl_file_path):
    nt_graph = Graph()
    owl_graph = Graph()

    owl_graph.bind("owl", OWL)
    owl_graph.bind("rdfs", RDFS)
    owl_graph.bind("rdf", RDF)

    nt_graph.parse(nt_file_path, format='nt')

    for s, p, o in nt_graph:
        if p == RDFS.label and isinstance(o, Literal):
            prop_type = determine_property_type(s)

            owl_graph.add((s, RDF.type, prop_type))

            owl_graph.add((s, RDFS.label, Literal(o)))

    owl_content = owl_graph.serialize(format='pretty-xml')

    with open(owl_file_path, 'w', encoding='utf-8') as f:
        f.write(owl_content)

    print(f"Successfully transformed '{nt_file_path}' to '{owl_file_path}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 nt_to_owl.py input.nt output.owl")
    else:
        input_nt = sys.argv[1]
        output_owl = sys.argv[2]
        nt_to_owl(input_nt, output_owl)
