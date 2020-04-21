import pandas as pd
import math


def get_entrophy(df: pd.DataFrame, label_column: str):
    '''
    df is pandas DataFrame
    label_column is column name for label(y), to calculate entrophy
    '''
    col = df[label_column]
    val_counts = col.value_counts()

    # print(type(val_counts))
    # print(val_counts)

    ttl = sum(
        val_counts.values)  # 返回的val_counts是Series类，可直接用index遍历器和values遍历器
    # print(ttl)

    entrophy = 0
    for val in val_counts.values:
        possibility = val / ttl
        log2p = math.log(possibility, 2)
        entrophy += -(possibility * log2p)

    # dicts = {}
    # for r in df.itertuples():
    #     label = getattr(r, label_column)
    #     if label not in dicts.keys():
    #         dicts[label] = 1
    #     else:
    #         dicts[label] += 1
    # total = sum(dicts.values())
    # entrophy = 0
    # for k in dicts.values():
    #     p = k / total  #possibility
    #     entrophy += -p * math.log(p, 2)
    return entrophy


def get_sub_entrophy(df: pd.DataFrame, label_column: str, feature_column: str):
    '''
    df is pandas dataframe
    label_column
    feature_column is feature to divide
    '''
    # fv_df={} # feature valus to dataframes dict
    # fv_ct = {}  # feature values to count
    # for r in df.itertuples():
    #     fv = getattr(r, feature_column)
    #     # print(type(r))
    #     if fv not in fv_ct.keys():
    #         # temp_df=pd.DataFrame(r)
    #         # fv_df[fv]=temp_df
    #         fv_ct[fv] = 1
    #     else:
    #         # fv_df[fv]=fv_df[fv].append(pd.DataFrame(r),ignore_index=True)
    #         fv_ct[fv] += 1
    # # print(fv_df["sunny"].describe())
    # ttl = sum(fv_ct.values())

    # to get feature values' count
    feature_col = df[feature_column]
    fval_ct = feature_col.value_counts()
    ttl = sum(fval_ct.values)

    sub_entrophy = 0
    for fval in fval_ct.index:
        sub_possibility = fval_ct[fval] / ttl
        sub_df = df[df[feature_column] == fval]
        sub_entrophy_by_this_fval = get_entrophy(sub_df, label_column)
        sub_entrophy += sub_possibility * sub_entrophy_by_this_fval
    return sub_entrophy


data_file_path = r"C:\Users\Zwm\Desktop\weather.nominal.csv"
data = pd.read_csv(data_file_path)
# print(data.describe())
# print(get_entrophy(data, "play"))
print(get_sub_entrophy(data, "play", "outlook"))
# help(pd.Series)
