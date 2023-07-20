import pandas as pd

input_path = 'Data/Stage 7/ctg-with-spec.csv'

df = pd.read_csv(input_path)

# for i in range(55, 60):
print(df.iloc[55].values)