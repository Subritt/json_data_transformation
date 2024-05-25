import pandas as pd
import re
import extract
import resources

def condition_check(task_data):
    """
    Check 'Type' and 'Series' as
    Type is one of: 4800a, 501c, or 325d
    Series starts with INV and has only 3 digits

    Parameters:
    task_data (Pandas DataFrame): Task Data extracted from .json file as DataFrame

    Returns:
    Pandas DataFrame after applying the filters.
    """

    print("transformation.py -> condition_check()")
    print(task_data.info())
    print(task_data)
    # print(task_data.loc[0, "Series"])

    def check(row):
        series_check_pattern = r'^INV\d{3}$'
        if row["Type"] not in ["4800a", "501c", "325d"]:
            row["Status"] = "Incorrect Type"
        elif not bool(re.match(series_check_pattern, row["Series"])):
            row["Status"] = "Incorrect Series"
        else:
            row["Status"] = ""
        return row
    task_data = task_data.apply(check, axis="columns")
    return task_data

def data_extractor():
    # file path
    file_path = resources.json_file_path
    print("file_path ->", file_path)

    # json data extraction
    json_data = extract.extract_json(file_path)
    print("json length ->", len(json_data))
    # print(json_data)
    
    # convert json data to Pandas DataFrame
    data_df = extract.change_to_dataframe(json_data)
    print("data_df length ->", len(data_df))
    # print(data_df)
    return data_df  

if __name__ == "__main__":
    print("Running as transformation.py")
    
    # data extractor
    task_data = data_extractor()

    # passing task_data to further check the conditions
    task_data_condition_checked = condition_check(task_data)
    print(task_data_condition_checked)
