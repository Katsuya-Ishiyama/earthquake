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
    try:
        deg_second = int(second) / 3600
    except ValueError:
        deg_second = 0.0
    except Exception as e:
        raise e

    return deg_degree + deg_minute + deg_second


def extract_depth(line: str) -> float:
    _int = int(line[44:47])
    try:
        _decimal = int(line[47:49]) / 100
    except ValueError:
        _decimal = 0
    except Exception as e:
        raise e
    return _int + _decimal


def extract_magnitude(magnitude_str: str) -> float:
    try:
        magnitude = float(magnitude_str.strip()) / 10.0
    except ValueError:
        magnitude = None
    except Exception as e:
        raise e
    return magnitude


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
    extracted["magnitude1_type"] = line[54] if line[54] != " " else None
    extracted["magnitude2"] = extract_magnitude(line[55:57])
    extracted["magnitude2_type"] = line[57] if line[57] != " " else None
    extracted["travel_time_type"] = int(line[58]) if line[58] != " " else None
    extracted["epicenter_evaluation"] = int(line[59]) if line[59] != " " else None
    extracted["epicenter_information"] = int(line[60]) if line[60] != " " else None
    extracted["max_seismic"] = int(line[61].strip())
    extracted["damage"] = int(line[62]) if line[62] != " " else None
    extracted["tsunami"] = int(line[63]) if line[63] != " " else None
    extracted["region1"] = int(line[64]) if line[64] != " " else None
    extracted["region2"] = int(line[65:68].strip()) if line[65:68] != "   " else None
    extracted["epicenter_name"] = line[68:90].split(" ")[0]
    extracted["observation_point"] = int(line[-6:-1].strip())
    extracted["epicenter_decision"] = line[-1].strip()

    return extracted
