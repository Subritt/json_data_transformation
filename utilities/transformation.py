import pandas as pd
import re

def condition_check(task_data) -> pd.DataFrame:
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

    # method for apply Map function of Pandas DataFrame
    def check(row):
        series_check_pattern = r'^INV\d{3}$'
        if row["Type"] not in ["4800a", "501c", "325d"]:
            row["Status"] = "Incorrect Type"
            row["Assignee"] = ""
        elif not bool(re.match(series_check_pattern, row["Series"])):
            row["Status"] = "Incorrect Series"
            row["Assignee"] = ""
        else:
            row["Status"] = ""
            row["Assignee"] = ""
        return row
    
    # checking two required conditions
    task_data = task_data.apply(check, axis="columns")
    return task_data

def assign_task(task_data_condition_checked, worker_data) -> pd.DataFrame:
    """
    Performs the following activities
    1. randomly shuffle rows
    2. floor division for task_division_number = (length_of_conditioned_data / total_worker)
    3. based on the condition assign worker to each row
    4. re-arrange the rows back to it's original order

    Parameters:
    task_data_condition_checked (pandas.DataFrame): task data after checking the conditions.
    worker_data (list): worker data list to assign the task.

    Returns:
    returns a DataFrame with Assignee column consisting worker name.
    """
    print("transformation.py -> assign_task()")

    # set a column for bringing the shuffled rows back to original position after worker assignment
    task_data_condition_checked["original_index"] = task_data_condition_checked.index
    
    # shuffle rows
    task_data_shuffled = task_data_condition_checked.sample(frac=1).reset_index(drop=True)
    task_data_shuffled["checker_index"] = task_data_shuffled.index

    # calculate the number of rows to be assigned to each worker
    task_data_filtered = task_data_condition_checked.loc[task_data_condition_checked["Status"].isin([""])]
    task_division_number = len(task_data_filtered) // len(worker_data)
    
    # method for apply to check condition and assign worker
    def worker_assignment(row, worker, assignment_counter):
        if assignment_counter[0] == task_division_number:            
            row["Assignee"] = ""
            return row
            
        if row["Status"] == "" and row["Assignee"] == "":
            row["Assignee"] = worker
            assignment_counter[0] += 1
        
        return row
    
    # counter variable list
    assignment_counter = [0]
    
    # looping through the worker list for task assignment
    for worker in worker_data:
        task_data_shuffled = task_data_shuffled.apply(
            worker_assignment, worker=worker, assignment_counter=assignment_counter, axis="columns"
        )
        assignment_counter = [0]

    # assigning the remaining leftoverr tasks to the last worker in the list
    task_data_shuffled = task_data_shuffled.apply(
        worker_assignment, worker=worker_data[len(worker_data)-1],
        assignment_counter=assignment_counter, axis="columns"
    )

    # re-orering the shuffled rows to it's original position
    task_data_shuffled = task_data_shuffled.sort_values(by="original_index").reset_index(drop=True)
    task_data_shuffled.drop(columns=["original_index", "checker_index"], inplace=True)

    return task_data_shuffled
