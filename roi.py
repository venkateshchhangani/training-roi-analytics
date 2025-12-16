import pandas as pd

data = pd.read_csv("roi_data.csv")

data['Improvement'] = data['Post Score'] - data['Pre Score']
roi = data['Improvement'].mean()

print("Average Training Improvement Score:", round(roi, 2))
