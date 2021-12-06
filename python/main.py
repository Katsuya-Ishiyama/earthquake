import logging
import extract_data as ex

logger = logging.getLogger(__name__)


def main():
    filepath = "../data/utf-8/i1919.dat"
    with open(filepath, "r") as f:
        for line in f:
            if not line.startswith("A"):
                continue

            try:
                epicenter = ex.extract_epicenter(line)
            except ex.ExtractError as e:
                logger.warning("skipped due to ExtractError: %s", line)
            #print(epicenter)


if __name__ == "__main__":
    logging.basicConfig(
        format="[%(asctime)s][%(levelname)s][%(name)s]L%(lineno)s - %(message)s",
        level=logging.INFO
    )
    main()