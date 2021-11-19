from datetime import datetime


def extract_datetime(line: str) -> datetime:
    year = int(line[1:5])
    month = int(line[5:7])
    day = int(line[7:9])
    hour = int(line[9:11])
    minute = int(line[11:13])
    second = int(line[13:15])
    return datetime(year, month, day, hour, minute, second)


def convert_latitude_longitude_deg(degree: str, minute: str, second: str) -> float:
    deg_degree = int(degree)
    deg_minute = int(minute) / 60
    deg_second = int(second) / 3600
    return deg_degree + deg_minute + deg_second


def extract_depth(line: str) -> float:
    return int(line[44:47]) + int(line[47:49]) / 100


def extract_epicenter(line: str):
    extracted = {}

    extracted["time"] = extract_datetime(line)
    extracted["latitude"] = convert_latitude_longitude_deg(
        degree=line[21:24],
        minute=line[24:26],
        second=line[26:28]
    )
    extracted["longitude"] = convert_latitude_longitude_deg(
        degree=line[32:36],
        minute=line[36:38],
        second=line[38:40]
    )
    extracted["depth"] = extract_depth(line)

    return extracted
