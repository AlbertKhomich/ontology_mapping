from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, OWL, RDFS
from pathlib import Path

current_dir = Path(__file__).resolve().parent
data_dir = current_dir.parent / "data"

file_path_input = "/Users/admin/scripts/add-rdf-type/data/alignments/WDC_wikidata_props_alignment.rdf"
file_path_output = "/Users/admin/scripts/add-rdf-type/data/alignments/WDC_wikidata_props_alignment.nt"

ALIGN = Namespace("http://knowledgeweb.semanticweb.org/heterogeneity/alignment")

g = Graph()
g.parse(file_path_input, format="application/rdf+xml")

output_graph = Graph()

for cell in g.subjects(RDF.type, ALIGN.Cell):
    entity1 = g.value(cell, ALIGN.entity1)
    entity2 = g.value(cell, ALIGN.entity2)

    if isinstance(entity1, URIRef) and isinstance(entity2, URIRef):
        # output_graph.add((entity1, OWL.equivalentClass, entity2))
        output_graph.add((entity1, OWL.sameAs, entity2))

output_graph.serialize(destination=file_path_output, format="nt")
