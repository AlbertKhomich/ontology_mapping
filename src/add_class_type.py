import sys
from pathlib import Path
from rdflib import Graph, Namespace, RDF

if len(sys.argv) != 3:
    print("Usage: python add_class_type.py <input_nt_file> <output_rdf_file>")

input_file_path = Path(sys.argv[1])
output_file_path = Path(sys.argv[2])

file_path = '/Users/admin/scripts/add-rdf-type/data/go/go_properties_correct.nt'

OWL = Namespace("http://www.w3.org/2002/07/owl#")

g = Graph()
g.parse(input_file_path, format="nt")

for subject in set(g.subjects()):
    g.add((subject, RDF.type, OWL.Class))

g.serialize(output_file_path, format="pretty-xml")

print(f"New RDF file created at: {output_file_path}")
