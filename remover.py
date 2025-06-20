input_file = "output.txt"
output_file = "cleaned_emails.txt"

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        clean_line = line.strip().replace('\r', '')  # Remove both \r and surrounding whitespace
        if clean_line:
            outfile.write(clean_line + '\n')