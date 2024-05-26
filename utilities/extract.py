import json
import pandas as pd

# function to read .json file
def extract_json(file_path) -> json:
    """
    Read a .json file.

    Parameters:
    file_path (str): File location where the json file is

    Returns:
    returns variable consisting of the json data
    """
    print("extract.py -> extract_json()")
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    
    return json_data

def change_to_dataframe(json_data) -> pd.DataFrame:
    """
    Change Json file into a Pandas DataFrame

    Parameters:
    json_data (json): json data

    Returns:
    returns pandas DataFrame
    """
    print("extract.py -> change_to_dataframe()")
    data_df = pd.DataFrame(json_data)
    return data_df
