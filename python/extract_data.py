import re
from datetime import datetime
from logging import getLogger

logger = getLogger(__name__)


class ExtractError(Exception):
    pass


def extract_line_identifier(line: str):
    return line[:15].replace(" ", "")


def extract_datetime(line: str) -> datetime:
    year = int(line[1:5])
    month = int(line[5:7])
    day = int(line[7:9])
    hour = int(line[9:11])

    minute = int(line[11:13])
    if (minute < 0) or (59 < minute):
        line_id = extract_line_identifier(line)
        logger.warning("minute was out of range: %d, %s", minute, line_id)
        raise ExtractError

    try:
        second = int(line[13:15])
    except ValueError:
        second = 0
        line_id = extract_line_identifier(line)
        logger.warning(
            'second "%s" was converted into %d, %s',
            line[13:15],
            second,
            line_id,
        )
    except Exception as e:
        raise e
    return datetime(year, month, day, hour, minute, second)


def convert_latitude_longitude_deg(
    line: str, degree: int, minute: int, second: int
) -> float:
    _degree = line[degree:minute]
    _minute = line[minute:second]
    _second = line[second : (second + 2)]

    try:
        deg_degree = int(_degree)
    except Exception:
        raise ExtractError

    try:
        deg_minute = int(_minute) / 60
    except ValueError:
        deg_minute = 0.0
        line_id = extract_line_identifier(line)
        logger.warning(
            'second "%s" was converted into %d, %s',
            _minute,
            deg_minute,
            line_id,
        )
    except Exception as e:
        raise e

    try:
        deg_second = int(_second) / 3600
    except ValueError:
        deg_second = 0.0
        line_id = extract_line_identifier(line)
        logger.warning(
            'second "%s" was converted into %d, %s',
            _second,
            deg_second,
            line_id,
        )
    except Exception as e:
        raise e

    return deg_degree + deg_minute + deg_second


def extract_depth(line: str) -> float:
    try:
        _int = int(line[44:47])
    except:
        line_id = extract_line_identifier(line)
        logger.warning('depth was replaced with None from "   ", %s', line_id)
        return None

    try:
        _decimal = int(line[47:49]) / 100
    except ValueError:
        _decimal = 0
        line_id = extract_line_identifier(line)
        logger.warning(
            'decimal "%s" was converted into %d, %s',
            line[47:49],
            _decimal,
            line_id,
        )
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


def extract_damage(line: str) -> str:
    damage_str = line[62]
    if damage_str == " ":
        return None
    return damage_str


FIELDNAMES = (
    "id",
    "time",
    "latitude",
    "longitude",
    "depth",
    "magnitude1",
    "magnitude1_type",
    "magnitude2",
    "magnitude2_type",
    "travel_time_type",
    "epicenter_evaluation",
    "epicenter_information",
    "max_seismic",
    "damage",
    "tsunami",
    "region1",
    "region2",
    "epicenter_name",
    "observation_point",
    "epicenter_decision",
)


def extract_epicenter(_line: str):
    extracted = {}
    _line = _line.strip("\n")

    extracted["id"] = extract_line_identifier(_line)
    extracted["time"] = extract_datetime(_line)
    extracted["latitude"] = convert_latitude_longitude_deg(
        line=_line, degree=21, minute=24, second=26
    )
    extracted["longitude"] = convert_latitude_longitude_deg(
        line=_line, degree=32, minute=36, second=38
    )
    extracted["depth"] = extract_depth(_line)
    extracted["magnitude1"] = extract_magnitude(_line[52:54])
    extracted["magnitude1_type"] = _line[54] if _line[54] != " " else None
    extracted["magnitude2"] = extract_magnitude(_line[55:57])
    extracted["magnitude2_type"] = _line[57] if _line[57] != " " else None
    extracted["travel_time_type"] = (
        int(_line[58]) if _line[58] != " " else None
    )
    extracted["epicenter_evaluation"] = (
        int(_line[59]) if _line[59] != " " else None
    )
    extracted["epicenter_information"] = (
        int(_line[60]) if _line[60] != " " else None
    )
    extracted["max_seismic"] = _line[61].strip()
    extracted["damage"] = extract_damage(_line)
    extracted["tsunami"] = _line[63] if _line[63] != " " else None
    extracted["region1"] = int(_line[64]) if _line[64] != " " else None
    extracted["region2"] = (
        int(_line[65:68].strip()) if _line[65:68] != "   " else None
    )
    extracted["epicenter_name"] = _line[68:90].split(" ")[0]
    extracted["observation_point"] = int(_line[-6:-1].strip())
    extracted["epicenter_decision"] = (
        _line[-1].strip() if _line[-1] != " " else None
    )

    return extracted
