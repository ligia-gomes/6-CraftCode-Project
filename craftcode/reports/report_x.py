def build_report(noml, context):
    establist = ['ValX', 'ValY']
    bandlist = ['ValZ']
    df_report = noml[noml['Col12'].isin(establist)].copy()
    df_report = df_report[df_report['Col4'].isin(bandlist)]

    # PSEUDO-CODE: exception_ids = load_exception_list('exception_ids.csv')
    # PSEUDO-CODE: df_report = df_report[~df_report['Col2'].isin(exception_ids)]
    # PSEUDO-CODE: df_report['Needs_Review'] = df_report['AWF_FTE'] == ''

    return df_report
