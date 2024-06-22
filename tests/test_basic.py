# content of test_sample.py

#from sample.helpers import get_tidy_data_path
import pandas as pd
from movie_loader.helpers import get_dynamo_recouce

#def test_check_dataframe_size():
#    df = pd.read_parquet(get_tidy_data_path() / 'current_race.parquet')
#    assert df.shape[1] == 26

def test_check_item():
    dynamo = get_dynamo_recouce()
    tables = []
    for table in dynamo.tables.all():
        tables.append(table.name)

    assert 'doc-example-table-movies' in tables