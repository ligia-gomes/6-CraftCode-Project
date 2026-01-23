##################### get parent directory to import functions.py modules ###################
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

#############################################################################################

from functions import report_date, call_path_output, START_GREEN, START_RED, END_COLORS
from report.file_report import report_function

############################################### Function to Save Files
def save_file_report():   
    try:
        report_function().to_excel(call_path_output() + 'name_of_report_file '  + report_date() + '.xlsx' , index = False, sheet_name = "Raw Data")
        print('Report "' + START_GREEN + 'name_of_report_file ' + report_date() + ".xlsx"+ END_COLORS +'" was created and saved successfully!')
    except FileExistsError:
        print('Report ' + START_RED + 'name_of_report_file '+ report_date() +'.xlsx' + END_COLORS + ' not saved successfully - check error!')

print('\n', START_GREEN + "âœ“ " + END_COLORS + 'Function save is ready to use!')
