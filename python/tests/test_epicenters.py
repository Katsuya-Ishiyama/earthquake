import epicenters
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal


class TestLoadData:
    @pytest.fixture(scope="function")
    def parquet_data(self, tmp_path):
        path_parquet = tmp_path / "epicenters"
        train_start = "1919-01-01 00:00:00"
        train_end = "2009-12-31 23:59:59"
        test_start = "2010-01-01 00:00:00"
        test_end = "2019-12-31 23:59:59"

        _yml = f"""\
data:
  path: {path_parquet}
  train:
    start: {train_start}
    end: {train_end}
  test:
    start: {test_start}
    end: {test_end}
"""
        path_yml = tmp_path / "config.yml"
        path_yml.write_text(_yml)

        data = {
            "time": [
                "1918-12-31 23:59:59",
                "1919-01-01 00:00:00",
                "2009-12-31 23:59:59",
                "2010-01-01 00:00:00",
                "2019-12-31 23:59:59",
                "2020-01-01 00:00:00",
            ],
            "col1": [1, 2, 3, 4, 5, 6],
        }
        df_all = pd.DataFrame(data)
        df_all["time"] = pd.to_datetime(df_all.time)
        df_all["year"] = df_all.time.map(lambda x: x.year)
        df_all.to_parquet(
            path_parquet, compression="gzip", partition_cols="year"
        )

        df_all["year"] = df_all.year.astype("category")

        is_train = (train_start <= df_all.time) & (df_all.time <= train_end)
        df_expected_train = df_all[is_train].copy()

        is_test = (test_start <= df_all.time) & (df_all.time <= test_end)
        df_expected_test = df_all[is_test].copy()
        return path_yml, df_expected_train, df_expected_test

    def test_load_training_data(self, parquet_data):
        path_config, df_expected_train, _ = parquet_data
        df_actual_train = epicenters.load_training_data(path_config)

        assert_frame_equal(df_actual_train, df_expected_train)

    def test_load_test_data(self, parquet_data):
        path_config, _, df_expected_test = parquet_data
        df_actual_test = epicenters.load_test_data(path_config)

        assert_frame_equal(df_actual_test, df_expected_test)
