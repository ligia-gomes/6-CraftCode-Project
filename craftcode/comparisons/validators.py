from craftcode.core.console import green, red


def column_structure_comparison(old_df, new_df, confirm_fn):
    equal_cols = set(old_df.columns) == set(new_df.columns)
    if equal_cols:
        print("\n" + green("OK ") + "Columns structures for the report match!\n-> Going to the next comparison\n")
        return True

    missing_columns = set(old_df.columns) - set(new_df.columns)
    additional_columns = set(new_df.columns) - set(old_df.columns)

    if missing_columns:
        confirm_miss_cols = confirm_fn(
            f"We have {missing_columns} columns missing, do you want to proceed?"
        )
        if not confirm_miss_cols:
            print(red("Operation Cancelled!"))
            return False
        print("---> Continuing to create the report...\n")

    if additional_columns:
        confirm_added_cols = confirm_fn(
            f"We have {additional_columns} columns added, do you want to proceed?"
        )
        if not confirm_added_cols:
            print(red("Operation Cancelled!"))
            return False
        print("---> Continuing to create the report...\n")

    return True


def compare_awf_headcount(old_df, new_df, threshold, confirm_fn):
    sum_column_new_file = new_df['AWF_Heads'].sum()
    sum_column_old_file = old_df['AWF_Heads'].sum()

    if sum_column_new_file == 0:
        print(red("New AWF headcount is zero; skipping comparison."))
        return False

    percentage_diff = ((sum_column_new_file - sum_column_old_file) / sum_column_new_file) * 100

    if abs(percentage_diff) <= threshold:
        print(green("OK ") + f"The difference between AWF Headcount is {percentage_diff:.2f}%!\n-> The code will finish the report creation....\n")
        return True

    if percentage_diff > threshold:
        message = f"We have a {percentage_diff:.2f}% higher AWF headcount when compared to previous month, it's very suspicious! Do you want to continue?"
    else:
        message = f"We have a {percentage_diff:.2f}% lower AWF headcount when compared to previous month, it's very suspicious! Do you want to continue?"

    if not confirm_fn(message):
        print(red("Operation Cancelled!"))
        return False
    print("---> Continuing to create the report...\n")
    return True


def compare_fte_headcount(old_df, new_df, threshold, confirm_fn):
    sum_column_new_file = new_df['AWF_FTE'].sum()
    sum_column_old_file = old_df['AWF_FTE'].sum()

    if sum_column_new_file == 0:
        print(red("New FTE headcount is zero; skipping comparison."))
        return False

    percentage_diff = ((sum_column_new_file - sum_column_old_file) / sum_column_new_file) * 100

    if abs(percentage_diff) <= threshold:
        print(green("OK ") + f"The difference between FTE is {percentage_diff:.2f}%!\n-> The code will finish the report creation....\n")
        return True

    if percentage_diff > threshold:
        message = f"We have a {percentage_diff:.2f}% higher FTE when compared to previous month, it's very suspicious! Do you want to continue?"
    else:
        message = f"We have a {percentage_diff:.2f}% lower FTE when compared to previous month, it's very suspicious! Do you want to continue?"

    if not confirm_fn(message):
        print(red("Operation Cancelled!"))
        return False
    print("---> Continuing to create the report...\n")
    return True


def compare_shape(old_df, new_df, threshold, confirm_fn):
    sum_column_new_file = len(new_df)
    sum_column_old_file = len(old_df)

    if sum_column_new_file == 0:
        print(red("New report has zero rows; skipping comparison."))
        return False

    percentage_diff = ((sum_column_new_file - sum_column_old_file) / sum_column_new_file) * 100

    if abs(percentage_diff) <= threshold:
        print(green("OK ") + f"The difference between number of rows is {percentage_diff:.2f}%!\n-> The code will finish the report creation....\n")
        return True

    if percentage_diff > threshold:
        message = f"We have a {percentage_diff:.2f}% higher number of rows when compared to previous month, it's very suspicious! Do you want to continue?"
    else:
        message = f"We have a {percentage_diff:.2f}% lower number of rows when compared to previous month, it's very suspicious! Do you want to continue?"

    if not confirm_fn(message):
        print(red("Operation Cancelled!"))
        return False
    print("---> Continuing to create the report...\n")
    return True
