import re

def is_valid_uri(uri):
    return re.match(r'^<([^:]+:[^\s"<>[\](){}]*)>$', uri)

def sanitize_literal(literal):
    return literal.replace('"', '').replace('\\', '')

def sanitize(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            parts = line.split(' ')
            if len(parts) < 3:
                continue

            subject = parts[0]
            predicate = parts[1]
            label = ' '.join(parts[2:]).strip()
            label = label[:-2].strip()

            if not is_valid_uri(subject) or not is_valid_uri(predicate):
                continue

            if label.startswith('"') and label.endswith('"'):
                label = sanitize_literal(label[1:-1])

            outfile.write(f'{subject} {predicate} "{label}" .\n')

sanitize(
    '/Users/admin/scripts/map_helper/data/clinical_trials/clinical_trials_classes.nt',
    '/Users/admin/scripts/map_helper/data/clinical_trials/clinical_trials_classes_clean.nt',
)
