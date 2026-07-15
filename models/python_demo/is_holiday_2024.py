import holidays
import pandas as pd

def model(dbt, session):
    dbt.config(
        materialized="table",
        packages=['holidays', 'pandas']
    )

    us_holidays = holidays.US(years=2024)

    df = dbt.ref('date_spine').to_pandas()

    df['is_holiday'] = df['DATE_DAY'].apply(lambda date: date in us_holidays)

    return df