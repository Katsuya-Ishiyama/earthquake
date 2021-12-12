import csv
import logging
from datetime import datetime
from pathlib import Path
import extract_data as ex

logger = logging.getLogger(__name__)


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

            writer.writerow(epicenter)
            converted_count += 1
    end_ts = datetime.now()
    elapsed_time = end_ts - start_ts
    logger.info(f"{output_filepath} has {converted_count} records, time {elapsed_time}"),


def main():
    input_dir = Path("../data/utf-8")
    output_dir = Path("../data/tsv")

    for input_filepath in input_dir.glob("i*.dat"):
        print(input_filepath)
        output_filepath = output_dir / f"{input_filepath.stem[1:]}.tsv"
        convert_dat_to_tsv(
            input_filepath=input_filepath,
            output_filepath=output_filepath
        )
        break


if __name__ == "__main__":
    file_handler = logging.FileHandler("../data/convert_data.log")
    logging.basicConfig(
        format="[%(asctime)s][%(levelname)s][%(name)s]L%(lineno)s - %(message)s",
        level=logging.INFO,
        handlers=[file_handler]
    )
    main()