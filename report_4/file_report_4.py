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

    establist = ['ValS', 'ValT']
    bandlist = ['ValU', 'ValV', 'ValW']
    df_report = noml[noml['Col12'].isin(establist)].copy()
    df_report = df_report[df_report['Col4'].isin(bandlist)]

    # PSEUDO-CODE: df_report = df_report[df_report['Col7'].isin(['Val6', 'Val7'])]
    # PSEUDO-CODE: df_report = df_report.merge(band_mapping, on='Col4', how='left')
    # PSEUDO-CODE: df_report = df_report.drop_duplicates(subset=['Col2'])

    return df_report

print()
print(START_GREEN + "OK " + END_COLORS + 'Report 4 file was created!')
