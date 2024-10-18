import pandas as pd

if "species_df" not in locals(): # if the species_df is not already loaded. Is it a bad way to do it?
    species_df = pd.read_csv('data/species.csv', sep = '\t')
    name_from_key_dict = dict(zip(species_df["taxonKey"], species_df["scientificName"]))
    name_from_key = lambda key: name_from_key_dict[key]

def branch(taxonKey: int):
    '''
    Given a taxon key, returns a dictionary with the taxon and all its ancestors.

    The dictionnary is of the form {group: name, groupKey: key, ...} with group 
    in ["kingdom", "phylum", "class", "order", "family", "genus", "species"]
    in that order.
    If the taxonKey is on a higher level than species, the lower level values are
    NaN.

    Parameters:
    -----------
    taxonKey: int
        The taxon key of the species

    '''
    return dict(species_df[species_df["taxonKey"] == taxonKey].iloc[0][7:-1])

def get_group(data : pd.DataFrame, taxonkey: int, group_level: int | str = 1):
    '''
    Get the lines of data that are in the same group of level group_level as the taxonkey.
    Return a new dataframe with the filtered data.

    Parameters:
    -----------
    data: pd.DataFrame
        The data to filter
    taxonkey: int
        The taxonkey of the species to filter on
    group_level: int or str
        The level of the group to filter on. Can be an integer between 1 and 7 or a string
        Should be higher than the level of the taxonkey
    '''

    b = branch(taxonkey)
    for i, (k, v) in enumerate(b.items()):
        if v == taxonkey:
            break
    
    levels = {"kingdom": 7, "phylum": 6, "class": 5, "order": 4, "family": 3, "genus": 2, "species": 1}
    if group_level in levels or group_level in range(1, 8):
        if type(group_level) == str:
            group_level = levels[group_level]
    else:
        raise Exception("Invalid group level")
    
    current_level = levels[k[:-3]]
    if group_level < current_level:
        raise Exception("Group level requested is lower than taxon provided")

    group_col = list(levels.keys())[7-group_level]+"Key"
    group_key = b[group_col]
    keys = set(species_df[species_df[group_col] == group_key]["taxonKey"])
    return data[data["taxonKey"].isin(keys)]