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

    establist = ['ValJ', 'ValK', 'ValL']
    bandlist = ['ValM', 'ValN']
    df_report = noml[noml['Col12'].isin(establist)].copy()
    df_report = df_report[df_report['Col4'].isin(bandlist)]

    # PSEUDO-CODE: df_report = df_report[df_report['B_Lev'] == 'BVB']
    # PSEUDO-CODE: df_report = df_report.groupby('Col4').sum(numeric_only=True).reset_index()
    # PSEUDO-CODE: df_report['Share'] = df_report['AWF_Heads'] / df_report['AWF_Heads'].sum()

    return df_report

print()
print(START_GREEN + "OK " + END_COLORS + 'Report 2 file was created!')
