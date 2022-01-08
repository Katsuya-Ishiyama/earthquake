from datetime import datetime
import pytest
import extract_data as ex


@pytest.fixture(scope="function")
def epicenter_records():
    line1 = "A2011031114461812 026 380621 056 1425166 087 237429590W84D5117662 64三陸沖                 2901K\n"
    expected1 = {
        "id": "A20110311144618",
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
        "max_seismic": "7",
        "damage": "6",
        "tsunami": "6",
        "region1": 2,
        "region2": 64,
        "epicenter_name": "三陸沖",
        "observation_point": 2901,
        "epicenter_decision": "K"
    }

    line2 = "A19190101121537   99  3414   99  13510   99   0            8 1      詳細不明                  1N\n"
    expected2 = {
        "id": "A19190101121537",
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
        "max_seismic": "1",
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
        "id": "A191901091518",
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
        "max_seismic": "1",
        "damage": None,
        "tsunami": None,
        "region1": None,
        "region2": None,
        "epicenter_name": "詳細不明",
        "observation_point": 1,
        "epicenter_decision": "N"
    }

    line4 = "A1968022501013347 075 341843 355 1391630 456 39     49J   5213Y 3103新島・神津島近海          3K\n"
    expected4 = {
        "id": "A19680225010133",
        "time": datetime(1968, 2, 25, 1, 1, 33),
        "latitude": 34.31194444444444,
        "longitude": 139.27500000,
        "depth": 39,
        "magnitude1": 4.9,
        "magnitude1_type": "J",
        "magnitude2": None,
        "magnitude2_type": None,
        "travel_time_type": 5,
        "epicenter_evaluation": 2,
        "epicenter_information": 1,
        "max_seismic": "3",
        "damage": "Y",
        "tsunami": None,
        "region1": 3,
        "region2": 103,
        "epicenter_name": "新島・神津島近海",
        "observation_point": 3,
        "epicenter_decision": "K"
    }

    line5 = "A1968040109420403 048 322693 237 1322627 184 22     75J   52153T7300日向灘                   77K\n"
    expected5 = {
        "id": "A19680401094204",
        "time": datetime(1968, 4, 1, 9, 42, 4),
        "latitude": 32.45916666666666,
        "longitude": 132.44083333333333,
        "depth": 22,
        "magnitude1": 7.5,
        "magnitude1_type": "J",
        "magnitude2": None,
        "magnitude2_type": None,
        "travel_time_type": 5,
        "epicenter_evaluation": 2,
        "epicenter_information": 1,
        "max_seismic": "5",
        "damage": "3",
        "tsunami": "T",
        "region1": 7,
        "region2": 300,
        "epicenter_name": "日向灘",
        "observation_point": 77,
        "epicenter_decision": "K"
    }

    line6 = "A2007032509415791 008 371324 016 1364116 040 107005369D66V511D314167能登半島沖             1740K\n"
    expected6 = {
        "id": "A20070325094157",
        "time": datetime(2007, 3, 25, 9, 41, 57),
        "latitude": 37.223333333333336,
        "longitude": 136.68777777777777,
        "depth": 10.7,
        "magnitude1": 6.9,
        "magnitude1_type": "D",
        "magnitude2": 6.6,
        "magnitude2_type": "V",
        "travel_time_type": 5,
        "epicenter_evaluation": 1,
        "epicenter_information": 1,
        "max_seismic": "D",
        "damage": "3",
        "tsunami": "1",
        "region1": 4,
        "region2": 167,
        "epicenter_name": "能登半島沖",
        "observation_point": 1740,
        "epicenter_decision": "K"
    }

    line7 = "A19481221080719       2324       12136                      11  8311台湾付近                  1I\n"
    expected7 = {
        "id": "A19481221080719",
        "time": datetime(1948, 12, 21, 8, 7, 19),
        "latitude": 23.40000000,
        "longitude": 121.60000000,
        "depth": None,
        "magnitude1": None,
        "magnitude1_type": None,
        "magnitude2": None,
        "magnitude2_type": None,
        "travel_time_type": None,
        "epicenter_evaluation": None,
        "epicenter_information": 1,
        "max_seismic": "1",
        "damage": None,
        "tsunami": None,
        "region1": 8,
        "region2": 311,
        "epicenter_name": "台湾付近",
        "observation_point": 1,
        "epicenter_decision": "I"
    }

    line8 = "A19610414002611       27         12818      197            212  7294沖縄本島近海              2I\n"
    expected8 = {
        "id": "A19610414002611",
        "time": datetime(1961, 4, 14, 0, 26, 11),
        "latitude": 27,
        "longitude": 128.30000000,
        "depth": 197,
        "magnitude1": None,
        "magnitude1_type": None,
        "magnitude2": None,
        "magnitude2_type": None,
        "travel_time_type": None,
        "epicenter_evaluation": 2,
        "epicenter_information": 1,
        "max_seismic": "2",
        "damage": None,
        "tsunami": None,
        "region1": 7,
        "region2": 294,
        "epicenter_name": "沖縄本島近海",
        "observation_point": 2,
        "epicenter_decision": "I"
    }

    line9 = "A1920092202421216     445124     1532832     150    65W      1      千島列島南東沖            2 \n"
    expected9 = {
        "id": "A19200922024212",
        "time": datetime(1920, 9, 22, 2, 42, 12),
        "latitude": 44.85666666666667,
        "longitude": 153.47555555555556,
        "depth": 15.0,
        "magnitude1": 6.5,
        "magnitude1_type": "W",
        "magnitude2": None,
        "magnitude2_type": None,
        "travel_time_type": None,
        "epicenter_evaluation": None,
        "epicenter_information": None,
        "max_seismic": "1",
        "damage": None,
        "tsunami": None,
        "region1": None,
        "region2": None,
        "epicenter_name": "千島列島南東沖",
        "observation_point": 2,
        "epicenter_decision": None
    }

    records = [
        (line1, expected1),
        (line2, expected2),
        (line3, expected3),
        (line4, expected4),
        (line5, expected5),
        (line6, expected6),
        (line7, expected7),
        (line8, expected8),
        (line9, expected9),
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
                line=line,
                degree=21,
                minute=24,
                second=26
            )
            assert actual == expected["latitude"]

    def test_longitude(self, epicenter_records):
        for line, expected in epicenter_records:
            actual = ex.convert_latitude_longitude_deg(
                line=line,
                degree=32,
                minute=36,
                second=38
            )
            assert actual == expected["longitude"]

    def test_latitude_raise_ExtractError(self):
        line = "A194804282359000                                             1      時分不明データ  　　　    1D\n"
        with pytest.raises(ex.ExtractError):
            ex.convert_latitude_longitude_deg(
                line=line,
                degree=21,
                minute=24,
                second=26
            )


def test_extract_depth(epicenter_records):
    for line, expected in epicenter_records:
        actual = ex.extract_depth(line)

        assert actual == expected["depth"]


def test_extract_magnitude(epicenter_records):
    for line, expected in epicenter_records:
        actual = ex.extract_magnitude(line[52:54])

        assert actual == expected["magnitude1"]


def test_extract_damage(epicenter_records):
    for line, expected in epicenter_records:
        actual = ex.extract_damage(line)

        assert actual == expected["damage"]


@pytest.fixture(scope="function")
def abnormal_epicenter_records():
    line1 = "A19190316169120   99  2823   99  12930   99   0            8 1      詳細不明                  1N\n"
    return (line1,)


class TestExtractEpicenter:

    def test_normal_records(self, epicenter_records):
        for line, expected in epicenter_records:
            actual = ex.extract_epicenter(line)
            for key, exp in expected.items():
                assert actual[key] == exp


    def test_raise_ExtractError(self, abnormal_epicenter_records):
        for line in abnormal_epicenter_records:
            with pytest.raises(ex.ExtractError):
                ex.extract_epicenter(line)
