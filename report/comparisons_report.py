##################### get parent directory to import functions.py modules ###################
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

#############################################################################################

import pandas as pd
from report.file_report import report_function

start_green = "\033[32m"
start_red = "\033[31m"
end_colors = "\033[0;0m"

from functions import last_report_date, call_path_last_output
from comparisons_functions import column_structure_comparison, compare_shape
from report.save_report import save_file_report

# import old report and current report dataframe
old_report = pd.read_excel(call_path_last_output() + 'name_of_report_file ' + last_report_date() + '.xlsx')
df_report = report_function()

old_df = old_report
new_df = df_report

#############################################################################################################

#Function to Compare Files

def compare_file_report():
    print('\nComparing structure of columns...')
    column_structure_comparison(old_df, new_df)
    print('\nComparing number of rows between outputs...')
    if compare_shape(old_df, new_df) == 'Ok':
        save_file_report()