
input_path = 'Data/Stage 2/mapped_conditions2.txt'
output_path = 'Data/Stage 2/stripped_mapped_conditions2.txt'

with open(input_path, 'r') as f_in, open(output_path, 'w') as f_out:
    for line in f_in:
        writeLine = line.strip('"\n')
        f_out.write(writeLine + '\n')