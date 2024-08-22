##################### get parent directory to import functions.py modules ###################
import os
import sys

start_green = "\033[32m"
start_red = "\033[31m"
end_colors = "\033[0;0m"

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

#############################################################################################

from functions import nom_list

#############################################################################################

noml = nom_list

def report_function():

    establist = ['ValA','ValB','ValC','ValD','ValE','ValF']
    bandlist = ['ValG','ValH','ValI']
    df_report = noml[noml['Col12'].isin(establist)].copy()
    df_report = df_report[df_report['Col4'].isin(bandlist)]
    
    return df_report

print('\n', start_green + "✓ " + end_colors + 'Report file was created!')

