# Day 46
# Create a DataFrame

import pandas as pd

data = {
    "Year":[2009,2002,2009,2010,2009],
    "Tittle":["Brothers","Spider-man","WatchMen","Inception","Avatar"],
    "Genre":["Drama","Sci-fi","Drama","Sci-fi","Fantasy"]
}
df = pd.DataFrame(data,columns=["Year","Tittle","Genre"])

print(df)