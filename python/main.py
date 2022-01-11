import csv
import logging
from datetime import datetime
from pathlib import Path
import pandas as pd
import extract_data as ex

logger = logging.getLogger(__name__)


def read_dat_as_DataFrame(input_filepath):
    logger.info(f"reading {input_filepath}")
    converted_count = 0
    start_ts = datetime.now()
    records = []
    with input_filepath.open("r") as fin:
        for line in fin:
            if not line.startswith("A"):
                continue

            try:
                epicenter = ex.extract_epicenter(line)
            except ex.ExtractError as e:
                logger.warning("skipped due to ExtractError: %s", line)
                continue
            except Exception as e:
                logger.error("error line: %s", line)
                raise e

            records.append(epicenter)
            converted_count += 1

    df = pd.DataFrame.from_records(records)
    end_ts = datetime.now()
    elapsed_time = end_ts - start_ts
    logger.info(f"finish reading from {input_filepath}, shape: {df.shape}, time {elapsed_time}"),

    return df


def convert_dat_to_tsv(input_filepath, output_filepath):
    logger.info(f"convert {input_filepath} into {output_filepath}")
    converted_count = 0
    start_ts = datetime.now()
    with input_filepath.open("r") as fin, output_filepath.open("w") as fout:
        writer = csv.DictWriter(fout, fieldnames=ex.FIELDNAMES, delimiter="\t")
        writer.writeheader()

        for line in fin:
            if not line.startswith("A"):
                continue

            try:
                epicenter = ex.extract_epicenter(line)
            except ex.ExtractError as e:
                logger.warning("skipped due to ExtractError: %s", line)
                continue
            except Exception as e:
                logger.error("error line: %s", line)
                raise e

            writer.writerow(epicenter)
            converted_count += 1
    end_ts = datetime.now()
    elapsed_time = end_ts - start_ts
    logger.info(f"{output_filepath} has {converted_count} records, time {elapsed_time}"),


def main():
    input_dir = Path("../data/utf-8")

    df_list = [read_dat_as_DataFrame(path) for path in input_dir.glob("i*.dat")]
    df_all = pd.concat(df_list)
    df_all["year"] = df_all.time.map(lambda x: x.year)
    df_all.sort_values(by="id", inplace=True)
    df_all.to_parquet("../data/parquet/epicenters", compression="gzip", partition_cols="year")


if __name__ == "__main__":
    file_handler = logging.FileHandler("../data/convert_data.log")
    logging.basicConfig(
        format="[%(asctime)s][%(levelname)s][%(name)s]L%(lineno)s - %(message)s",
        level=logging.INFO,
        handlers=[file_handler]
    )
    main()