import pandas as pd
from functions import call_path_last_output, call_path_output, START_GREEN, START_RED, END_COLORS

################################################################################################

# Paths
last_report_path = call_path_last_output()
path = call_path_output()

def read_function(input_file):
    raw_input = pd.read_csv(input_file, delimiter = ',', header = 23, encoding = 'UTF-8', low_memory=False)
    return raw_input

def column_structure_comparison(old_df, new_df):
    # Verifies if columns structures are the same
    equal_cols = set(old_df.columns) == set(new_df.columns)
    if equal_cols:
        print('\n' + START_GREEN + "OK " + END_COLORS +  "Columns structures for the report match!\n-> Going to the next comparison\n")
    else:
        missing_columns = set(old_df.columns) - set(new_df.columns)
        additional_columns = set(new_df.columns) - set(old_df.columns)

        if missing_columns:
            confirm_miss_cols = input("\nWe have " + str(missing_columns) + " columns missing, do you want to proceed? (Y/N)").strip().lower()
            if confirm_miss_cols != 'y':
                print(START_RED + "Operation Cancelled!" + END_COLORS)
                return "Cancelled"
            print("---> Continuing to create the report...\n")

        if additional_columns:
            confirm_added_cols = input("We have " + str(additional_columns) + " columns added, do you want to proceed? (Y/N)").strip().lower()
            if confirm_added_cols != 'y':
                print(START_RED + "Operation Cancelled!" + END_COLORS)
                return
            print("---> Continuing to create the report...\n")

def compare_awf_headcount(old_df, new_df):
    # Verifies if there is differences in the necessary columns
    sum_column_new_file = new_df['AWF Head'].sum()
    sum_column_old_file = old_df['AWF Head'].sum()

    if sum_column_new_file == 0:
        print(START_RED + "New AWF headcount is zero; skipping comparison." + END_COLORS)
        return

    percentage_diff = ((sum_column_new_file - sum_column_old_file) / sum_column_new_file) * 100
    threshold = 5

    if abs(percentage_diff) <= threshold:
        print(START_GREEN + "OK " + END_COLORS + "The difference between AWF Headcount is " + START_GREEN + f"{percentage_diff:.2f}%!" + END_COLORS + "\n-> The code will finish the report creation....\n")
        return 'Ok'

    if percentage_diff > threshold:
        confirm_continue = input(f"We have a {percentage_diff:.2f}% higher AWF headcount when compared to previous month, it's VERY suspicius! Do you want to continue? (Y/N)\n").strip().lower()
    else:
        confirm_continue = input(f"We have a {percentage_diff:.2f}% lower AWF headcount when compared to previous month, it's VERY suspicius! Do you want to continue? (Y/N)\n").strip().lower()

    if confirm_continue != 'y':
        print(START_RED + "Operation Cancelled!" + END_COLORS)
        return
    print("---> Continuing to create the report...\n")
    return 'Ok'

def compare_fte_headcount(old_df, new_df):
    # Verifies if there is differences in the necessary columns
    sum_column_new_file = new_df['AWF_FTE'].sum()
    sum_column_old_file = old_df['AWF_FTE'].sum()

    if sum_column_new_file == 0:
        print(START_RED + "New FTE headcount is zero; skipping comparison." + END_COLORS)
        return

    percentage_diff = ((sum_column_new_file - sum_column_old_file) / sum_column_new_file) * 100
    threshold = 5

    if abs(percentage_diff) <= threshold:
        print(START_GREEN + "OK " + END_COLORS + "The difference between FTE is " + START_GREEN + f"{percentage_diff:.2f}%!" + END_COLORS + "\n-> The code will finish the report creation....\n")
        return 'Ok'

    if percentage_diff > threshold:
        confirm_continue = input(f"We have a {percentage_diff:.2f}% higher FTE when compared to previous month, it's VERY suspicius! Do you want to continue? (Y/N)\n").strip().lower()
    else:
        confirm_continue = input(f"We have a {percentage_diff:.2f}% lower FTE when compared to previous month, it's VERY suspicius! Do you want to continue? (Y/N)\n").strip().lower()

    if confirm_continue != 'y':
        print(START_RED + "Operation Cancelled!" + END_COLORS)
        return
    print("---> Continuing to create the report...\n")
    return 'Ok'

def compare_shape(old_df, new_df):
    # Verifies if there is differences in the necessary columns
    sum_column_new_file = len(new_df)
    sum_column_old_file = len(old_df)

    if sum_column_new_file == 0:
        print(START_RED + "New report has zero rows; skipping comparison." + END_COLORS)
        return

    percentage_diff = ((sum_column_new_file - sum_column_old_file) / sum_column_new_file) * 100
    threshold = 5

    if abs(percentage_diff) <= threshold:
        print(START_GREEN + "OK " + END_COLORS + "The difference between number of rows is " + START_GREEN + f"{percentage_diff:.2f}%!" + END_COLORS + "\n-> The code will finish the report creation....\n")
        return 'Ok'

    if percentage_diff > threshold:
        confirm_continue = input(f"We have a {percentage_diff:.2f}% higher number of rows when compared to previous month, it's VERY suspicius! Do you want to continue? (Y/N)\n").strip().lower()
    else:
        confirm_continue = input(f"We have a {percentage_diff:.2f}% lower number of rows when compared to previous month, it's VERY suspicius! Do you want to continue? (Y/N)\n").strip().lower()

    if confirm_continue != 'y':
        print(START_RED + "Operation Cancelled!" + END_COLORS)
        return
    print("---> Continuing to create the report...\n")
    return 'Ok'

print('\n', START_GREEN + "OK " + END_COLORS + 'Functions for comparisons were created!')
