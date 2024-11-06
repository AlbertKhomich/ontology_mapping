import csv

input_file = '/Users/admin/scripts/map_helper/data/goa_merged/Goa_properties.csv'
output_file = '/Users/admin/scripts/map_helper/data/goa_merged/Goa_properties.nt'

def csv_to_nt(input_file, output_file):
    with open(input_file, 'r', encoding='ISO-8859-1') as csvfile, open(output_file, 'w', encoding='utf-8') as ntfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            subject = row['subject']
            predicate = row['predicate']
            obj = row['object']

            nt_line = f'<{subject}> <{predicate}> "{obj}" .\n'
            ntfile.write(nt_line)

csv_to_nt(input_file, output_file)
print("Conversion complete. Check the output file:", output_file)
