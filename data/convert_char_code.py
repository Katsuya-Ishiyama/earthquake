"""This program will convert character code of a given file."""

import logging
from pathlib import Path

logger = logging.getLogger(__name__)

input_dir = Path("src/dat")
output_dir = Path("utf-8")


def convert_char_code(input_file: Path, output_dir: Path):
    output_file = output_dir / input_file.name
    try:
        with input_file.open(mode="r", encoding="sjis") as f_in:
            with output_file.open(mode="w", encoding="utf-8") as f_out:
                f_out.write(f_in.read())
        logger.info(f"successfully converted to utf-8: {output_file}")
    except Exception as e:
        logger.error(e)



if __name__ == "__main__":

    logging.basicConfig(
        format="%(asctime)s %(name)s [%(levelname)s] %(message)s",
        level=logging.INFO
    )

    for input_file in input_dir.iterdir():
        convert_char_code(input_file, output_dir)