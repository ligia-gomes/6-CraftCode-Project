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

    establist = ['ValA', 'ValB', 'ValC', 'ValD', 'ValE', 'ValF']
    bandlist = ['ValG', 'ValH', 'ValI']
    df_report = noml[noml['Col12'].isin(establist)].copy()
    df_report = df_report[df_report['Col4'].isin(bandlist)]

    # PSEUDO-CODE: df_report = df_report.merge(cost_center_map, on='Col2', how='left')
    # PSEUDO-CODE: df_report['KPI_1'] = df_report['AWF_Heads'] * factor
    # PSEUDO-CODE: df_report = df_report[df_report['AWF_FTE'] > 0]

    return df_report

print()
print(START_GREEN + "OK " + END_COLORS + 'Report 1 file was created!')
