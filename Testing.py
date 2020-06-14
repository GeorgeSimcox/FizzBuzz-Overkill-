import pandas as pd

file = "setting.txt"
opened = open(file, "r")
readed = pd.read_csv(file)
print(readed)