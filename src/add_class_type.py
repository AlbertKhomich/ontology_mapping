from pathlib import Path
from rdflib import Graph, Namespace, RDF, URIRef

current_dir = Path(__file__).resolve().parent
data_dir = current_dir.parent / "data"

file_path = '/Users/admin/scripts/add-rdf-type/data/wikidata/wikidata_properties.rdf'

OWL = Namespace("http://www.w3.org/2002/07/owl#")

g = Graph()
g.parse(file_path, format="xml")

for subject in set(g.subjects()):
    g.add((subject, RDF.type, OWL.Class))

g.serialize('/Users/admin/scripts/add-rdf-type/data/wikidata/wikidata_properties_new.rdf', format="pretty-xml")

#Script adds OWL type:Class to .rdf
