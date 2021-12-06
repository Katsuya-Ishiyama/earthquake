from datetime import datetime
import pytest
import extract_data as ex


@pytest.fixture(scope="function")
def epicenter_records():
    line1 = "A2011031114461812 026 380621 056 1425166 087 237429590W84D5117662 64三陸沖                 2901K\n"
    expected1 = {
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

    line2 = "A19190101121537   99  3414   99  13510   99   0            8 1      詳細不明                  1N\n"
    expected2 = {
        "time": datetime(1919, 1, 1, 12, 15, 37),
        "latitude": 34.233333333333334,
        "longitude": 135.16666666666666,
        "depth": 0.0,
        "magnitude1": None,
        "magnitude1_type": None,
        "magnitude2": None,
        "magnitude2_type": None,
        "travel_time_type": None,
        "epicenter_evaluation": 8,
        "epicenter_information": None,
        "max_seismic": 1,
        "damage": None,
        "tsunami": None,
        "region1": None,
        "region2": None,
        "epicenter_name": "詳細不明",
        "observation_point": 1,
        "epicenter_decision": "N"
    }

    line3 = "A191901091518     99  3615   99  13758   99   0            8 1      詳細不明                  1N\n"
    expected3 = {
        "time": datetime(1919, 1, 9, 15, 18),
        "latitude": 36.25000000,
        "longitude": 137.96666666666667,
        "depth": 0.0,
        "magnitude1": None,
        "magnitude1_type": None,
        "magnitude2": None,
        "magnitude2_type": None,
        "travel_time_type": None,
        "epicenter_evaluation": 8,
        "epicenter_information": None,
        "max_seismic": 1,
        "damage": None,
        "tsunami": None,
        "region1": None,
        "region2": None,
        "epicenter_name": "詳細不明",
        "observation_point": 1,
        "epicenter_decision": "N"
    }

    records = [
        (line1, expected1),
        (line2, expected2),
        (line3, expected3),
    ]
    return records


def test_extract_datetime(epicenter_records):
    for line, expected in epicenter_records:
        actual = ex.extract_datetime(line)
        assert actual == expected["time"]


class TestConvertLatitudeLongitudeDeg:

    def test_latitude(self, epicenter_records):
        for line, expected in epicenter_records:
            actual = ex.convert_latitude_longitude_deg(
                degree=line[21:24],
                minute=line[24:26],
                second=line[26:28]
            )
            assert actual == expected["latitude"]

    def test_longitude(self, epicenter_records):
        for line, expected in epicenter_records:
            actual = ex.convert_latitude_longitude_deg(
                degree=line[32:36],
                minute=line[36:38],
                second=line[38:40]
            )
            assert actual == expected["longitude"]


def test_extract_depth(epicenter_records):
    for line, expected in epicenter_records:
        actual = ex.extract_depth(line)

        assert actual == expected["depth"]


def test_extract_magnitude(epicenter_records):
    for line, expected in epicenter_records:
        actual = ex.extract_magnitude(line[52:54])

        assert actual == expected["magnitude1"]


def test_extract_epicenter(epicenter_records):
    for line, expected in epicenter_records:
        actual = ex.extract_epicenter(line)

        for key, exp in expected.items():
            assert actual[key] == exp


@pytest.fixture(scope="function")
def abnormal_epicenter_records():
    line1 = "A19190316169120   99  2823   99  12930   99   0            8 1      詳細不明                  1N\n"
    return (line1,)


def test_extract_epicenter_raise_ExtractError(abnormal_epicenter_records):
    for line in abnormal_epicenter_records:
        with pytest.raises(ex.ExtractError):
            ex.extract_epicenter(line)

