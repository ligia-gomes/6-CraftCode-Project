##################### get parent directory to import functions.py modules ###################
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

#############################################################################################

from functions import nom_list, START_GREEN, END_COLORS

#############################################################################################

noml = nom_list

def report_function():

    establist = ['ValX', 'ValY']
    bandlist = ['ValZ']
    df_report = noml[noml['Col12'].isin(establist)].copy()
    df_report = df_report[df_report['Col4'].isin(bandlist)]

    # PSEUDO-CODE: exception_ids = load_exception_list('exception_ids.csv')
    # PSEUDO-CODE: df_report = df_report[~df_report['Col2'].isin(exception_ids)]
    # PSEUDO-CODE: df_report['Needs_Review'] = df_report['AWF_FTE'] == ''

    return df_report

print()
print(START_GREEN + "OK " + END_COLORS + 'Report 401 file was created!')
