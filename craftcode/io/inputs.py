import pandas as pd
import re

from craftcode.config import settings


def read_raw_input(input_file):
    return pd.read_csv(
        input_file,
        delimiter=settings.CSV_DELIMITER,
        header=settings.CSV_HEADER_ROW,
        encoding=settings.CSV_ENCODING,
        low_memory=False,
    )


def preprocess_nom_list(noml):
    noml.drop(noml.loc[noml['Col1'].str.startswith('Val1')].index, inplace=True)
    noml.dropna(subset=['Col2', 'Col3'], inplace=True, axis=0)
    noml['Col2'] = noml['Col2'].astype(int)

    def b_lev(noml_df):
        noml_df['B_Lev'] = noml_df.apply(
            lambda row: 'BVB' if row['Col4'] == 'Val2' and row['Col5'] == 'Val3'
            else 'BVA' if row['Col4'] == 'Val2' and row['Col5'] == 'Val4'
            else None,
            axis=1,
        )

    b_lev(noml)

    AWF = 'Val5'

    WC_Temps = 'Val6'
    WC_Early_Career = 'Val7'
    WC_Limited = 'Val8'
    WC_Unlimited = 'Val9'

    PWT_Temps = 'Val10'
    PWT_Trainee = 'Val11'
    PWT_Apprentice = 'Val12'

    def awf_heads(noml_df):
        noml_df['AWF_Heads'] = noml_df.apply(
            lambda row: 1 if (row['Col6'] == AWF and row['Col7'] == WC_Limited) or
            (row['Col6'] == AWF and row['Col7'] == WC_Unlimited) else 0,
            axis=1,
        )

    awf_heads(noml)

    def temps_heads(noml_df):
        noml_df['Temps_Heads'] = noml_df.apply(
            lambda row: 1 if (row['Col7'] == WC_Temps and row['Col8'] == PWT_Temps)
            else 0,
            axis=1,
        )

    temps_heads(noml)

    def trainees_heads(noml_df):
        noml_df['Trainees_Heads'] = noml_df.apply(
            lambda row: 1 if (row['Col7'] == WC_Early_Career and row['Col8'] == PWT_Trainee)
            else 0,
            axis=1,
        )

    trainees_heads(noml)

    def apprentices_heads(noml_df):
        noml_df['Apprentices_Heads'] = noml_df.apply(
            lambda row: 1 if (row['Col7'] == WC_Early_Career and row['Col8'] == PWT_Apprentice)
            else 0,
            axis=1,
        )

    apprentices_heads(noml)

    def awf_fte(noml_df):
        noml_df['AWF_FTE'] = noml_df.apply(
            lambda row: row['Col9'] if (row['Col6'] == AWF and row['Col7'] == WC_Limited and row['Col9'] > 0.000) or
            (row['Col6'] == AWF and row['Col7'] == WC_Unlimited and row['Col9'] > 0.000) else '',
            axis=1,
        )

    awf_fte(noml)

    def temps_fte(noml_df):
        noml_df['Temps_FTE'] = noml_df.apply(
            lambda row: row['Col9'] if (row['Col7'] == WC_Temps and row['Col8'] == PWT_Temps and row['Col9'] > 0.000)
            else '',
            axis=1,
        )

    temps_fte(noml)

    return noml


def load_nom_list(path):
    print("\nReading the nominative list...")
    noml = read_raw_input(path)
    return preprocess_nom_list(noml)


def load_movements(mov_path):
    df_mov = pd.read_excel(mov_path, dtype={'Col2': 'int'})
    df_mov.drop(df_mov.loc[df_mov['Col1'].str.startswith('Val1')].index, inplace=True)
    df_mov['Col10'] = df_mov['Col1'].str.extract(r'(^.*?)\s', re.M)
    df_mov['Col11'] = df_mov['Col11'].str.extract(r'(^.*?)\s', re.M)
    return df_mov
