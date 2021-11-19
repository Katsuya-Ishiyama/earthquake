#!/bin/bash

INPUT_DIR="src/zip"
OUTPUT_DIR="src/dat"

target_files=$(find ${INPUT_DIR} -name "*.zip")
for file in ${target_files}; do
    unzip ${file} -d ${OUTPUT_DIR}
done