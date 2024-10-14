from pathlib import Path
from rdflib import Graph, Namespace

current_dir = Path(__file__).resolve().parent
data_dir = current_dir.parent / "data"

file_path = data_dir / "output_file.rdf"

RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")

g = Graph()
g.parse(data_dir / 'output_file.rdf', format="xml")

class_to_labels = {}

for s, p ,o in g.triples((None, RDFS.label, None)):
    cls = str(s)
    label = str(o)

    if cls not in class_to_labels:
        class_to_labels[cls] = []
    else:
        print(cls)
