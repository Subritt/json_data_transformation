import pandas as pd
import os

def create_csv(task_data, worker_data, folder_path, source_file_name, master) -> bool:
    """
    Creates two CSV files
    1. Master CSV file consisting of all the input and additional status and assignee columns.
    2. Individual worker CSV file consisting of only input columns.

    Parameters:
    task_data (pandas.DataFrame): task_data after the random row assignment to workers.
    worker_data (list): worker data list to assign the task.
    folder_path (str): primary folder for CSV dump.
    source_file_name (str): name of the primary json file to be used to create a sub folder with this name.
    master (str): name to be given to the master CSV file.

    Returns:
    returns True after executing the method.
    """
    # if master has a name CSV file will be creaeted
    if master:
        # check folder availability
        final_destination_folder = folder_check(folder_path, source_file_name)

        # create csv
        file_name = f"{master}.csv"
        task_data.to_csv(os.path.join(final_destination_folder, file_name), index=False)
        print(f"{master}.csv created!")

    # creating individual CSV files for each worker
    if worker_data:
        for worker in worker_data:
            print("creating CSV for ->", worker)
            try:
                # slicing DataFrame for each worker
                worker_df = task_data.loc[
                    task_data["Assignee"] == worker
                ].copy()

                # drop Assignee column
                worker_df.drop(columns=["Assignee", "Status"], axis=1, inplace=True)

                # check folder availability
                final_destination_folder = folder_check(folder_path, source_file_name)

                # create csv
                file_name = f"{worker}.csv"
                worker_df.to_csv(os.path.join(final_destination_folder, file_name), index=False)
                print(f"{worker}.csv created!")
            except Exception as e:
                print("Exception: ", e)
    
    return True

def folder_check(folder_path, source_file_name) -> str:
    """
    a. Checks if the primary CSV dump folder exists.
    b. Also checks if the sub folder with the json file name.
    Creates if does not exist.

    Parameters:
    folder_path (str): primary CSV dump folder.
    source_file_name (str): name of the json file.

    Returns:
    returns final destination folder path for CSV dump.
    """
    final_destination_folder = f"{folder_path}/{source_file_name}"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        os.makedirs(final_destination_folder)
        return final_destination_folder
    else:
        if not os.path.exists(final_destination_folder):
            os.makedirs(final_destination_folder)
            return final_destination_folder
        return final_destination_folder
