# Day 22
# Add Under_Score

def add_hash(txt : str):
    return "#".join(txt)

def add_underscore(txt : str):
    return txt.replace("#","_")

def remove_underscore(txt : str):
    return txt.replace("_","")

if __name__ == "__main__":
    print(remove_underscore(add_underscore(add_hash("Python"))))