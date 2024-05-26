import utilities.extract as extract
import utilities.transformation as transformation
import utilities.load as load
import resources
import os
import pandas as pd

def folder_iter() -> list:
    """
    Iterates through .json files with the source folder.

    Returns:
    returns json file_name and file_path
    """
    source_folder_path: str = resources.source_folder_path
    path_details = []

    # iterate through the folder.
    # check if the file is in .json format
    if os.path.exists(source_folder_path):
        print("source_folder found!")
        for file_name in os.listdir(source_folder_path):
            print("file_name ->", file_name)
            if file_name.lower().endswith(".json"):
                print("file is in .json format")
                file_path: str = os.path.join(source_folder_path, file_name)
                path_details.append([file_name, file_path])
            else:
                print("Not a json file!")
    else:
        print("source_folder not found!")
    
    return path_details

def extraction(file_path) -> pd.DataFrame:
    """
    Extracts the json task file and converts it to a Pandas DataFrame.

    Parameters:
    file_path (str): location of the json file to be extracted

    Returns:
    returns a DataFrame of the task data.
    """

    # json data extraction
    json_data: list = extract.extract_json(file_path)
    
    # convert json data to Pandas DataFrame
    data_df: pd.DataFrame = extract.change_to_dataframe(json_data)

    return data_df

def transform(task_data, worker_data) -> pd.DataFrame:
    """
    Perform these condition checks
    a. Type is one of: 4800a, 501c, or 325d.
    b. Series starts with INV and has only 3 digits.

    Parameters:
    task_data (pandas.DataFrame): task_data DataFrame to perform checks at.
    worker_data (list): worker data list to assign the task.
    """
    # passing task_data to further check the conditions
    task_data_condition_checked = transformation.condition_check(task_data)

    # assigning tasks to each worker
    master_data = transformation.assign_task(task_data_condition_checked, worker_data)

    return master_data

def load_data(master_data, worker_data, folder_path, file_name, master):
    """
    Creates folder if does not exits. Creates a master CSV file and each worker task CSV file.

    Parameters:
    master_data (pandas.DataFrame): task data in Pandas DataFrame.
    worker_data (list): worker data list to assign the task.
    folder_path (str): folder path where the CSV files are to be created.
    file_name (str): json file name for creating a subfolder with this name.

    Returns:
    Does not return anything.
    """
    status = load.create_csv(master_data, worker_data, folder_path, file_name, master)
    print("")
    print("csv load status ->", status)

if __name__ == "__main__":
    print("Running as driver.py")

    # get the file_name and folder_path
    folder_detail = folder_iter()
    print("")

    for detail in folder_detail:
        file_name = detail[0]
        file_path = detail[1]
        print("")
        print(f"---> Working for {file_name} <---")
        print("")

        # data extraction
        task_data = extraction(file_path)
        print("")

        # data transformation, assigning worker
        worker_data = resources.worker_data
        master_data = transform(task_data, worker_data)
        print("")

        # load: create respective CSV file
        folder_path = resources.folder_path
        load_data(master_data, worker_data, folder_path, file_name, resources.master_csv_file_name)
