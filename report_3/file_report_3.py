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

    establist = ['ValO', 'ValP', 'ValQ']
    bandlist = ['ValR']
    df_report = noml[noml['Col12'].isin(establist)].copy()
    df_report = df_report[df_report['Col4'].isin(bandlist)]

    # PSEUDO-CODE: df_report = df_report[df_report['Temps_Heads'] > 0]
    # PSEUDO-CODE: df_report = df_report.assign(Month=report_date())
    # PSEUDO-CODE: df_report = df_report.sort_values(['Col4', 'Col2'])

    return df_report

print()
print(START_GREEN + "OK " + END_COLORS + 'Report 3 file was created!')
