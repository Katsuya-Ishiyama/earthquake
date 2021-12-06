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


def extract_magnitude(magnitude_str: str) -> float:
    return float(magnitude_str.strip()) / 10.0


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
    extracted["magnitude1"] = extract_magnitude(line[52:54])
    extracted["magnitude1_type"] = line[54].strip()
    extracted["magnitude2"] = extract_magnitude(line[55:57])
    extracted["magnitude2_type"] = line[57].strip()
    extracted["travel_time_type"] = int(line[58].strip())
    extracted["epicenter_evaluation"] = int(line[59].strip())
    extracted["epicenter_information"] = int(line[60].strip())
    extracted["max_seismic"] = int(line[61].strip())
    extracted["damage"] = int(line[62].strip())
    extracted["tsunami"] = int(line[63].strip())
    extracted["region1"] = int(line[64].strip())
    extracted["region2"] = int(line[65:68].strip())
    extracted["epicenter_name"] = line[68:90].split(" ")[0]
    extracted["observation_point"] = int(line[-6:-1].strip())
    extracted["epicenter_decision"] = line[-1].strip()

    return extracted
