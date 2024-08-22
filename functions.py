import pandas as pd
import re
import os
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

######################### Path Creation ########################################

Own_Path_Output = "C:/Users/insert_your_user_here/Documents/Output/" #Here you insert the path for your output files
Own_Path_Input = "C:/Users/insert_your_user_here/Documents/Input/" #Here you insert the path for your input files

today = date.today()
current_year = datetime.now().strftime('%Y')
last_month_year = (today - relativedelta(months=2)).strftime('%Y')

def report_date():
    reportdate = (today - relativedelta(months=1)).strftime('%Y.%m')
    return reportdate

def last_report_date():
    last_reportdate = (today - relativedelta(months=2)).strftime('%Y.%m')
    return last_reportdate

def report_month():
    global effective_month
    effective_month = (today - relativedelta(months=1)).strftime('%m')
    return effective_month

def create_folder():
    global folder 
    folder = Own_Path_Output + current_year + '/' + report_date() + '/'
    try:
        os.mkdir(folder)
        return "Folder %s created!" % folder
    except FileExistsError:
        return "Folder %s already exists" % folder
    
# input
def call_path_last_input():
    last_input_path = Own_Path_Input + last_month_year + '/' + last_report_date() + '/' + 'NomSumHist_' + last_report_date() + '.csv'
    return last_input_path

def call_path_input():
    input_path = Own_Path_Input + current_year + '/' + report_date() + '/' + 'NomSumHist_' + report_date() + '.csv'
    return input_path

# output 
def call_path_last_output():
    last_output_path = Own_Path_Output + last_month_year + '/' + last_report_date() + '/'
    return last_output_path

def call_path_output():
    output_path = Own_Path_Output + current_year + '/' + report_date() + '/'
    return output_path

######################### Processing Noml & MovList ########################################

def import_preprocess_nomlist(df):
    print('\nReading the nominative list...')
    global noml
    noml = pd.read_csv(df, delimiter = ',', header = 23, encoding = 'UTF-8', low_memory=False)
    noml.drop(noml.loc[noml['Col1'].str.startswith('Val1')].index, inplace=True)
    noml.dropna(subset = ['Col2', 'Col3'],inplace = True, axis = 0)
    noml['Col2'] = noml['Col2'].astype(int)

    #Function that Creates the BVA and BVB on column B_Lev
    def b_lev(noml):
        noml['B_Lev'] = noml.apply(lambda row: 'BVB' if row['Col4'] == 'Val2' and row['Col5'] == 'Val3' else
                                   'BVA' if row['Col4'] == 'Val2' and row['Col5'] == 'Val4' else None, axis=1)
    b_lev(noml)

    #Variables
    AWF = 'Val5'

    #WC Variables
    WC_Temps = 'Val6'
    WC_Early_Career = 'Val7'
    WC_Limited = 'Val8'
    WC_Unlimited = 'Val9'

    PWT_Temps = 'Val10'
    PWT_Trainee = 'Val11'
    PWT_Apprentice = 'Val12'


    #HEADS Headcount
    def awf_heads(noml):
        noml['AWF_Heads'] = noml.apply(lambda row: 1 if (row['Col6'] == AWF and row['Col7'] == WC_Limited) or
                                (row['Col6'] == AWF and row['Col7'] == WC_Unlimited) else 0, axis=1)
    awf_heads(noml)
                                    
    def temps_heads(noml):
        noml['Temps_Heads'] = noml.apply(lambda row: 1 if (row['Col7'] == WC_Temps and row['Col8'] == PWT_Temps)
                                    else 0, axis=1)
    temps_heads(noml)

    def trainees_heads(noml):
        noml['Trainees_Heads'] = noml.apply(lambda row: 1 if (row['Col7'] == WC_Early_Career and row['Col8'] == PWT_Trainee)
                                    else 0, axis=1)
    trainees_heads(noml)

    def apprentices_heads(noml):
        noml['Apprentices_Heads'] = noml.apply(lambda row: 1 if (row['Col7'] == WC_Early_Career and row['Col8'] == PWT_Apprentice)
                                    else 0, axis=1)
    apprentices_heads(noml)

    # FTE Headcount
    def awf_fte(noml):
        noml['AWF_FTE'] = noml.apply(lambda row: row['Col9'] if (row['Col6'] == AWF and row['Col7'] == WC_Limited and row['Col9'] > 0.000) or
                                (row['Col6'] == AWF and row['Col7'] == WC_Unlimited and row['Col9'] > 0.000) else '', axis=1)
    awf_fte(noml)


    def temps_fte(noml):
        noml['Temps_FTE'] = noml.apply(lambda row: row['Col9'] if (row['Col7'] == WC_Temps and row['Col8'] == PWT_Temps and row['Col9'] > 0.000)
                                    else '', axis=1)
    temps_fte(noml)
        
    return noml

nom_list = import_preprocess_nomlist(call_path_input())

def import_preprocess_movlist(mov):
    df_mov = pd.read_excel(mov, dtype = {'Col2':'int'})
    df_mov.drop(df_mov.loc[df_mov['Col1'].str.startswith('Val1')].index, inplace=True)
    df_mov['Col10'] = df_mov['Col1'].str.extract(r'(^.*?)\s',re.M)
    df_mov['Col11'] = df_mov['Col11'].str.extract(r'(^.*?)\s',re.M)

    return df_mov