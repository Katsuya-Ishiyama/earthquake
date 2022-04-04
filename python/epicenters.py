import pandas as pd
import utils

EPICENTERS_PATH = "../data/parquet/epicenters"


def load_training_data(path: str):
    config = utils.load_config(path)
    epicenters_path = config["data"]["path"]
    train_start = pd.to_datetime(config["data"]["train"]["start"])
    train_end = pd.to_datetime(config["data"]["train"]["end"])

    df_all = pd.read_parquet(epicenters_path)
    is_train = (df_all["time"] >= train_start) & (df_all["time"] <= train_end)
    df_train = df_all[is_train].copy()

    return df_train


def load_test_data(path: str):
    config = utils.load_config(path)
    epicenters_path = config["data"]["path"]
    test_start = pd.to_datetime(config["data"]["test"]["start"])
    test_end = pd.to_datetime(config["data"]["test"]["end"])

    df_all = pd.read_parquet(epicenters_path)
    is_test = (df_all["time"] >= test_start) & (df_all["time"] <= test_end)
    df_test = df_all[is_test].copy()

    return df_test
