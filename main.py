import sys

print("\nLet's create our monthlies!")
from functions import report_date, report_month, START_GREEN, START_RED, END_COLORS
print('\nThe report date is', START_GREEN + report_date() + END_COLORS)
print('The report month is', START_GREEN + report_month() + END_COLORS)

from functions import call_path_input, call_path_last_input, START_GREEN, START_RED, END_COLORS
from comparisons_functions import column_structure_comparison, read_function
print('\n', START_GREEN + "âœ“ " + END_COLORS + 'The nominative list was processed and headcounts created!')
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

from report_1.comparison_report_1 import compare_file_report as compare_report_1
from report_2.comparison_report_2 import compare_file_report as compare_report_2
from report_3.comparison_report_3 import compare_file_report as compare_report_3
from report_4.comparison_report_4 import compare_file_report as compare_report_4
from report_x.comparison_report_x import compare_file_report as compare_report_x

REPORTS = {
    "1": ("1_name_of_report_file", compare_report_1),
    "2": ("2_name_of_report_file", compare_report_2),
    "3": ("3_name_of_report_file", compare_report_3),
    "4": ("4_name_of_report_file", compare_report_4),
    "x": ("401_name_of_report_file", compare_report_x),
}

def parse_report_selection(selection):
    if not selection:
        return list(REPORTS.keys())
    normalized = selection.replace(" ", "").lower()
    if normalized == "all":
        return list(REPORTS.keys())

    selected = set()
    for token in normalized.split(","):
        if "-" in token:
            start, end = token.split("-", 1)
            if start.isdigit() and end.isdigit():
                for report_id in REPORTS:
                    if report_id.isdigit() and int(start) <= int(report_id) <= int(end):
                        selected.add(report_id)
            continue
        if token in REPORTS:
            selected.add(token)
    return sorted(selected)

# start saving reports...
print('\nComparing and saving the files...')
print('Available reports:', ", ".join(REPORTS.keys()))
print('Do you want to:')
print('1 - Run all reports')
print('2 - Run a specific report')
print('3 - Run a sequence or batch of reports')
menu_choice = input('Choose an option (1/2/3): ').strip()

if menu_choice == '1':
    selected_reports = list(REPORTS.keys())
elif menu_choice == '2':
    selection = input('Which Report you want to run? ').strip()
    selected_reports = parse_report_selection(selection)
elif menu_choice == '3':
    selection = input('Which sequence or batch you want to run? (e.g. 1,2 or 1-3): ').strip()
    selected_reports = parse_report_selection(selection)
else:
    selected_reports = []

if not selected_reports:
    print(START_RED + "No valid reports selected. Exiting." + END_COLORS)
    sys.exit(0)

for report_id in selected_reports:
    report_name, report_fn = REPORTS[report_id]
    print('\nRunning report', report_id, '-', report_name)
    report_fn()
