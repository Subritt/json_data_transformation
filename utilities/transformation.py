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
    print(task_data.info())
    print(task_data)
    # print(task_data.loc[0, "Series"])

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
    task_data = task_data.apply(check, axis="columns")
    return task_data

"""
1. randomly shuffle rows
2. calculate task_division_number len / total_worker
3. based on the condition assign worker
4. re-arrange the rows back to it's original order
"""
def assign_task(task_data_condition_checked, worker_data) -> pd.DataFrame:
    print("inside assign_task method")
    task_data_condition_checked["original_index"] = task_data_condition_checked.index
    # shuffled rows
    task_data_shuffled = task_data_condition_checked.sample(frac=1).reset_index(drop=True)
    task_data_shuffled["checker_index"] = task_data_shuffled.index
    print("shuffled data")
    print(task_data_shuffled)

    task_data_filtered = task_data_condition_checked.loc[task_data_condition_checked["Status"].isin([""])]
    task_division_number = len(task_data_filtered) // len(worker_data)
    print("task division ->", task_division_number)
    
    # method for apply to check condition and assign worker
    def worker_assignment(row, worker, assignment_counter):
        if assignment_counter[0] == task_division_number:

            # checker print statements
            print("after counter condition == 165")
            print("original_index ->", row["checker_index"])
            print("Assignee ->", "")
            
            row["Assignee"] = ""
            return row
            
        if row["Status"] == "" and row["Assignee"] == "":
            row["Assignee"] = worker
            assignment_counter[0] += 1
            
            # checker print statements
            print("counter ->", assignment_counter[0])
            print("original_index ->", row["checker_index"])
            print("Assignee ->", worker)
        
        # if assignment_counter[0] == "remaining" and row["Status"] == "" and row["Assignee"] == "":
        return row
    
    assignment_counter = [0]
    for worker in worker_data:
        print(worker)
        task_data_shuffled = task_data_shuffled.apply(
            worker_assignment, worker=worker, assignment_counter=assignment_counter, axis="columns"
        )
        assignment_counter = [0]

    task_data_shuffled = task_data_shuffled.apply(
        worker_assignment, worker=worker_data[len(worker_data)-1],
        assignment_counter=assignment_counter, axis="columns"
    )

    task_data_shuffled = task_data_shuffled.sort_values(by="original_index").reset_index(drop=True)
    task_data_shuffled.drop(columns=["original_index", "checker_index"], inplace=True)
    print(task_data_shuffled)

    return task_data_shuffled
