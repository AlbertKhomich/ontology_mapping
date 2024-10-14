def merge_nt_files(file1, file2, output_file):
    unique_triples = set()

    with open(file1, 'r') as f1:
        for line in f1:
            line = line.strip()
            if line:
                unique_triples.add((line.split(' ')[0], line.split(' ')[2]))
    
    with open(file2, 'r') as f2:
        for line in f2:
            line = line.strip()
            if line:
                unique_triples.add((line.split(' ')[0], line.split(' ')[2]))

    with open(output_file, 'w') as f_out:
        for triple in unique_triples:
            # f_out.write(f'{triple[0]} <http://www.w3.org/2002/07/owl#equivalentClass> {triple[1]} .\n')
            f_out.write(f'{triple[0]} <http://www.w3.org/2002/07/owl#sameAs> {triple[1]} .\n')

file1 = '/Users/admin/scripts/add-rdf-type/data/alignments/WDC_wikidata_alignment_props.nt'
file2 = '/Users/admin/scripts/add-rdf-type/data/alignments/WDC_wikidata_props_alignment.nt'
output_file = '/Users/admin/scripts/add-rdf-type/data/alignments/WDC_wikidata_props_alignment_heavy.nt'

merge_nt_files(file1, file2, output_file)
