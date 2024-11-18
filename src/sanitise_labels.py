def sanitize(input, output):
    with open(input, 'r', encoding='utf-8') as infile, open(output, 'w', encoding='utf-8') as outfile:
        for line in infile:
            parts = line.split(' ')
            label = parts[2]
            outfile.write(f'{parts[0]} {parts[1]} "{label.replace('"', '')}" .\n')

sanitize('/Users/admin/scripts/map_helper/data/clinical_trials/clinical_trials_classes.nt', '/Users/admin/scripts/map_helper/data/clinical_trials/clinical_trials_classes_clean.nt')
