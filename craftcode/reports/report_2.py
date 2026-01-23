def build_report(noml, context):
    establist = ['ValJ', 'ValK', 'ValL']
    bandlist = ['ValM', 'ValN']
    df_report = noml[noml['Col12'].isin(establist)].copy()
    df_report = df_report[df_report['Col4'].isin(bandlist)]

    # PSEUDO-CODE: df_report = df_report[df_report['B_Lev'] == 'BVB']
    # PSEUDO-CODE: df_report = df_report.groupby('Col4').sum(numeric_only=True).reset_index()
    # PSEUDO-CODE: df_report['Share'] = df_report['AWF_Heads'] / df_report['AWF_Heads'].sum()

    return df_report
