import logging
import subprocess
import time

logger = logging.getLogger(__name__)
stdout_handler = logging.StreamHandler()
logging.basicConfig(
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    handlers=[stdout_handler],
    level=logging.INFO
)

START_YEAR = 1919
END_YEAR = 2019

for year in range(START_YEAR, END_YEAR+1):
    download_url = f"https://www.data.jma.go.jp/svd/eqev/data/bulletin/data/shindo/i{year}.zip"
    file_name = download_url.split("/")[-1]
    save_path = f"src/zip/{file_name}"

    command = ["curl", download_url, "--silent", "-o", save_path]
    logger.info("Execute: %s", " ".join(command))
    response = subprocess.run(command)
    response.check_returncode()
    logger.info("download success: %s", save_path)
    time.sleep(3)
