import pandas as pd

mydict = {"a": "jim", "b": "sarah", "c": "cook"}
df = pd.DataFrame(mydict)
df.columns = ["colname"]

col = df["colname"]
df.loc

