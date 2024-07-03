import pandas as pd


def add_one(x: int) ->int:
    return x+1

def add_together(x: int, y: int) -> int:
    return x + x

## custom functions
# one in - one out
def new_column_based_on_custom_function(daf: pd.DataFrame, column_in: str) -> pd.DataFrame:
    daf["new_column"] = daf[column_in].apply(lambda x: pd.Series(add_one(x)))
    return daf

# two in - one out
def new_column_based_on_custom_function_multiple_inputs(daf: pd.DataFrame, col1: str, col2:str) -> pd.DataFrame:
    daf[f'added'] = daf.apply(lambda row: add_together(row[col1], row[col2]), axis=1)
    return daf

## non-custom function
# one in - two out
def new_columns_based_on_fixed_function(daf: pd.DataFrame, column_in: str):
    daf[[f'str_1', f'str_2']] = daf[column_in].str.split('|', expand=True)
    return daf

def main():
    daf = pd.DataFrame({"input1": [1,2,3,4], "input2": [11,21,31,41],"strings": ["1|2", "2|3", "3|4", "5|6"]})
    daf = new_column_based_on_custom_function(daf, "input1")
    daf = new_column_based_on_custom_function_multiple_inputs(daf, "input1", "input2")
    daf = new_columns_based_on_fixed_function(daf, "strings")
    print(daf)


if __name__ == "__main__":
    main()