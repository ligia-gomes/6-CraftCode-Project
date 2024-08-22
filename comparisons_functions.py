import pandas as pd
from functions import call_path_last_output, call_path_output

start_green = "\033[32m"
start_red = "\033[31m"
end_colors = "\033[0;0m"

################################################################################################

#Paths
last_report_path = call_path_last_output()
path = call_path_output() 

def read_function(input_file):
    raw_input = pd.read_csv(input_file, delimiter = ',', header = 23, encoding = 'UTF-8', low_memory=False)
    return raw_input

def column_structure_comparison(old_df, new_df):    
    #Verifies if columns structures are the same
    equal_cols = set(old_df.columns) == set (new_df.columns)
    if equal_cols:
        print('\n' + start_green + "✓ " + end_colors +  "Columns structures for the report match!\n-> Going to the next comparison\n")
    else:
        missing_columns = set(old_df.columns) - set(new_df.columns)
        additional_columns = set(new_df.columns) - set(old_df.columns)

        if missing_columns:
            confirm_miss_cols = input("\nWe have " + str(missing_columns) + " columns missing, do you want to proceed? (Y/N)").strip().lower()
            if confirm_miss_cols != 'y':
                print(start_red + "Operation Cancelled!" + end_colors)
                return "Cancelled"
            print("---> Continuing to create the report...\n")
            
        if additional_columns:
            confirm_added_cols = input("We have " + str(additional_columns) + " columns added, do you want to proceed? (Y/N)").strip().lower()
            if confirm_added_cols != 'y':
                print(start_red + "Operation Cancelled!" + end_colors)
                return
            print("---> Continuing to create the report...\n")


def compare_awf_headcount(old_df, new_df):
    #Verifies if there is differences in the necessary columns
    sum_column_new_file = new_df['AWF Head'].sum()
    sum_column_old_file = old_df['AWF Head'].sum()

    percentage_diff = ((sum_column_new_file - sum_column_old_file)/ sum_column_new_file) *100 # Percentage difference of the AWF 

    if percentage_diff == 0:
        confirm_continue = input("We have the same AWF headcount as previous month, it's suspicius! Do you want to proceed? (Y/N)").strip().lower()
        if confirm_continue != 'y':
            print(start_red + "Operation Cancelled!" + end_colors)
            return
        print("---> Continuing to create the report...\n")
        return 'Ok'

    elif percentage_diff > 0.01 and percentage_diff <= 10:
        print(start_green + "✓ " + end_colors + "The difference between AWF Headcount is " + start_green + f"{percentage_diff:.2f}%!" + end_colors + "\n-> The code will finish the report creation....\n")
        return 'Ok'

    elif percentage_diff > 10:
        confirm_continue = input(f"We have a {percentage_diff:.2f}% higher AWF headcount when compared to previous month, it's VERY suspicius! Do you want to continue? (Y/N)\n").strip().lower()
        if confirm_continue != 'y':
            print(start_red + "Operation Cancelled!" + end_colors)
            return
        print("---> Continuing to create the report...\n")
        return 'Ok'

    elif percentage_diff < 0:
        confirm_continue = input(f"We have a {percentage_diff:.2f}% lower AWF headcount when compared to previous month, it's VERY suspicius! Do you want to continue? (Y/N)\n").strip().lower()
        if confirm_continue != 'y':
            print(start_red + "Operation Cancelled!" + end_colors)
            return
        print("---> Continuing to create the report...\n")
        return 'Ok'
    

def compare_fte_headcount(old_df, new_df):
    #Verifies if there is differences in the necessary columns
    sum_column_new_file = new_df['AWF_FTE'].sum()
    sum_column_old_file = old_df['AWF_FTE'].sum()

    percentage_diff = ((sum_column_new_file - sum_column_old_file)/ sum_column_new_file) *100 # Percentage difference of the FTE column 

    if percentage_diff == 0:
        confirm_continue = input("We have the same FTE as previous month, it's suspicius! Do you want to proceed? (Y/N)").strip().lower()
        if confirm_continue != 'y':
            print(start_red + "Operation Cancelled!" + end_colors)
            return
        print("---> Continuing to create the report...\n")
        return 'Ok'

    elif percentage_diff > 0.01 and percentage_diff <= 10:
        print(start_green + "✓ " + end_colors + "The difference between FTE is " + start_green + f"{percentage_diff:.2f}%!" + end_colors + "\n-> The code will finish the report creation....\n")
        return 'Ok'

    elif percentage_diff > 10:
        confirm_continue = input(f"We have a {percentage_diff:.2f}% higher FTE when compared to previous month, it's VERY suspicius! Do you want to continue? (Y/N)\n").strip().lower()
        if confirm_continue != 'y':
            print(start_red + "Operation Cancelled!" + end_colors)
            return
        print("---> Continuing to create the report...\n")
        return 'Ok'

    elif percentage_diff < 0:
        confirm_continue = input(f"We have a {percentage_diff:.2f}% lower FTE when compared to previous month, it's VERY suspicius! Do you want to continue? (Y/N)\n").strip().lower()
        if confirm_continue != 'y':
            print(start_red + "Operation Cancelled!" + end_colors)
            return
        print("---> Continuing to create the report...\n")
        return 'Ok'


def compare_shape(old_df, new_df):
    #Verifies if there is differences in the necessary columns
    sum_column_new_file = len(new_df)
    sum_column_old_file = len(old_df)

    percentage_diff = ((sum_column_new_file - sum_column_old_file)/ sum_column_new_file) *100 # Percentage difference of number of rows 

    if percentage_diff == 0:
        confirm_continue = input("We have the same number of rows as previous month, it's suspicius! Do you want to proceed? (Y/N)").strip().lower()
        if confirm_continue != 'y':
            print(start_red + "Operation Cancelled!" + end_colors)
            return
        print("---> Continuing to create the report...\n")
        return 'Ok'

    elif percentage_diff > 0.01 and percentage_diff <= 10:
        print(start_green + "✓ " + end_colors + "The difference between number of rows is " + start_green + f"{percentage_diff:.2f}%!" + end_colors + "\n-> The code will finish the report creation....\n")
        return 'Ok'

    elif percentage_diff > 10:
        confirm_continue = input(f"We have a {percentage_diff:.2f}% higher number of rows when compared to previous month, it's VERY suspicius! Do you want to continue? (Y/N)\n").strip().lower()
        if confirm_continue != 'y':
            print(start_red + "Operation Cancelled!" + end_colors)
            return
        print("---> Continuing to create the report...\n")
        return 'Ok'

    elif percentage_diff < 0:
        confirm_continue = input(f"We have a {percentage_diff:.2f}% lower number of rows when compared to previous month, it's VERY suspicius! Do you want to continue? (Y/N)\n").strip().lower()
        if confirm_continue != 'y':
            print(start_red + "Operation Cancelled!" + end_colors)
            return
        print("---> Continuing to create the report...\n")
        return 'Ok'
    


print('\n', start_green + "✓ " + end_colors + 'Functions for comparisons were created!')




