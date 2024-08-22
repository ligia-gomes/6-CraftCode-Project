import sys

start_green = "\033[32m"
start_red = "\033[31m"
end_colors = "\033[0;0m"

print("\nLet's create our monthlies!")
from functions import report_date, report_month
print('\nThe report date is', start_green + report_date() + end_colors)
print('The report month is', start_green + report_month() + end_colors)

from functions import call_path_input, call_path_last_input
from comparisons_functions import column_structure_comparison, read_function
print('\n', start_green + "✓ " + end_colors + 'The nominative list was processed and headcounts created!')
#import_preprocess_movlist('mov.xlsx')
#print('Movements list is ready to use.')

last_input_file = call_path_last_input()
current_input_file = call_path_input()

#comparison in input files
print('\nStarting comparison between current and last nominative list...')
input_comparison = column_structure_comparison(read_function(last_input_file), read_function(current_input_file)) 


def comp_aux():
    if input_comparison == "Cancelled":
        sys.exit(0) 
comp_aux()  

# start saving reports...
print('\nComparing and saving the files...')

from report.comparisons_report import compare_file_report
compare_file_report()


