##################### get parent directory to import functions.py modules ###################
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

#############################################################################################

start_green = "\033[32m"
start_red = "\033[31m"
end_colors = "\033[0;0m"

from functions import report_date, call_path_output
from report.file_report import report_function

############################################### Function to Save Files
def save_file_report():   
    try:
        report_function().to_excel(call_path_output() + 'name_of_report_file '  + report_date() + '.xlsx' , index = False, sheet_name = "Raw Data")
        print('Report "' + start_green + 'name_of_report_file ' + report_date() + ".xlsx"+ end_colors +'" was created and saved successfully!')
    except FileExistsError:
        print('Report ' + start_red + 'name_of_report_file '+ report_date() +'.xlsx' + end_colors + ' not saved successfully - check error!')

print('\n', start_green + "✓ " + end_colors + 'Function save is ready to use!')
