import modin.pandas as pd

if "species_df" not in locals(): # if the species_df is not already loaded. Is it a bad way to do it?
    species_df = pd.read_csv('data/species.csv', sep = '\t')
    name_from_key_dict = dict(zip(species_df["taxonKey"], species_df["scientificName"]))
    name_from_key = lambda key: name_from_key_dict[key]

def get_group(data, group_key, group_level = 1):
    if type(group_level) == str:
        group_col = {"kingdom": 8, "phylum": 10, "class": 12, "order": 14, "family": 16, "genus": 18, "species": 20}[group_level]
    elif type(group_level) == int:
        group_col = {7:8, 6:10, 5:12, 4:14, 3:16, 2:18, 1:20}[group_level]
    else:
        raise Exception("Invalid group_level")
    
    col = species_df.columns[group_col]
    taxonKeys = set(species_df[species_df[col] == group_key]["taxonKey"]) 
    return data[data["taxonKey"].isin(taxonKeys)]

def branch(taxonKey):
    return dict(species_df[species_df["taxonKey"] == 8225376].iloc[0][7:-1])