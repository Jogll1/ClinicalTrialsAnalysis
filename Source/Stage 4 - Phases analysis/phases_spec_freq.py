import pandas as pd
import json

# overview
# gather a list of all conditions:phase ('condition_with_phase.txt')
# go through this list and
# if the condition is not in mapped_conditions just remove for now
# this then means we can map the left over conditions to their specialisation and include the phase
# then for each specialisation count the amount of different phases

# paths
output_txt_path1 = 'Data/Stage 4/test.txt'

with open(output_txt_path1, 'w', encoding='utf-8') as f:
    f.write("yo")