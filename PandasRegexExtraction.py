from typing import List
import re
import pandas as pd

def extract_and_combine(df: pd.DataFrame, column: str, job_codes: List[str]) -> pd.DataFrame:
    # Create a new DataFrame with existing columns
    new_df = pd.DataFrame(df)

    # Define a regex pattern for job codes
    regex_pattern = '|'.join(job_codes)

    # Extract job codes from JustificationNote column and concatenate them
    new_df['MatchingJobCodes'] = df[column].str.findall(regex_pattern, flags=re.IGNORECASE).apply(','.join)

    return new_df

if __name__ == "__main__":
    # Set options to display all columns and rows
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # Sample data
    data = {
        'UNIT_LONG_NAME': ['711HPW', 'JSMC', 'BarrelHW'],
        'PDInputTypeNar': ['blah', 'oiue', 'blue'],
        'PDComplete': [True, 'iujo', 'is'],
        'ParkingComplete': [True, 'hjk', 'my'],
        'CRMWhatever': [False, 'ghjk', 'favorite'],
        'DutyTitle': ['ComputerScientist', 'ghj', 'color'],
        'AFSC': ['11F', 'R011F4Y', '012S4W'],
        'JustificationNote': ['Blah blah blah also 12C or 16A is fine',
                              'blah blah blah idk 16G or 12S is also fine for this position',
                              'blah blah blah 11R is fine or 11m should match because it\'s case insensitive']
    }

    df = pd.DataFrame(data)

    # List of job codes to search for
    all_AFSC = ["011F4Y", "R011F4Y", "01364B"]
    all_3DigAFSC = ["11F", "11G", "11H", "11J", "11K", "11M", "11R", "11S", "11T", "11U", "11X"]

    # Call the function
    result_df = extract_and_combine(df, 'JustificationNote', all_AFSC + all_3DigAFSC)

    # Display the result
    print(result_df.head())