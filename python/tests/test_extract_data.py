from datetime import datetime
import pytest
import extract_data as ex


@pytest.fixture(scope="function")
def epicenter_record():
    line = "A2011031114461812 026 380621 056 1425166 087 237429590W84D5117662 64三陸沖                 2901K"
    expected = {
        "time": datetime(2011, 3, 11, 14, 46, 18),
        "latitude": 38.10583333333334,
        "longitude": 142.86833333333334,
        "depth": 23.74,
        "magnitude1": 9.0,
        "magnitude1_type": "W",
        "magnitude2": 8.4,
        "magnitude2_type": "D",
        "travel_time_type": 5,
        "epicenter_evaluation": 1,
        "epicenter_information": 1,
        "max_seismic": 7,
        "damage": 6,
        "tsunami": 6,
        "region1": 2,
        "region2": 64,
        "epicenter_name": "三陸沖",
        "observation_point": 2901,
        "epicenter_decision": "K"
    }

    return line, expected


def test_extract_datetime(epicenter_record):
    line, expected = epicenter_record
    actual = ex.extract_datetime(line)
    assert actual == expected["time"]


class TestConvertLatitudeLongitudeDeg:

    def test_latitude(self, epicenter_record):
        line, expected = epicenter_record
        actual = ex.convert_latitude_longitude_deg(
            degree=line[21:24],
            minute=line[24:26],
            second=line[26:28]
        )
        assert actual == expected["latitude"]

    def test_longitude(self, epicenter_record):
        line, expected = epicenter_record
        actual = ex.convert_latitude_longitude_deg(
            degree=line[32:36],
            minute=line[36:38],
            second=line[38:40]
        )
        assert actual == expected["longitude"]


def test_extract_depth(epicenter_record):
    line, expected = epicenter_record
    actual = ex.extract_depth(line)

    assert actual == expected["depth"]


def test_extract_epicenter(epicenter_record):
    line, expected = epicenter_record
    actual = ex.extract_epicenter(line)

    for key, exp in expected.items():
        assert actual[key] == exp


