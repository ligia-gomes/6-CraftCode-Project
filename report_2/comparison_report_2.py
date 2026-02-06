##################### get parent directory to import functions.py modules ###################
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

#############################################################################################

import pandas as pd
from report_2.file_report_2 import report_function

from functions import last_report_date, call_path_last_output
from comparisons_functions import column_structure_comparison, compare_shape
from report_2.save_report_2 import save_file_report

REPORT_FILE_NAME = "2_name_of_report_file "

# import old report and current report dataframe
old_report = pd.read_excel(call_path_last_output() + REPORT_FILE_NAME + last_report_date() + '.xlsx')
df_report = report_function()

old_df = old_report
new_df = df_report

#############################################################################################################

# Function to Compare Files

def compare_file_report():
    print()
    print('Comparing structure of columns...')
    column_structure_comparison(old_df, new_df)
    print()
    print('Comparing number of rows between outputs...')
    if compare_shape(old_df, new_df) == 'Ok':
        save_file_report()
