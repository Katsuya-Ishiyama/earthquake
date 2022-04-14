import pytest
import utils
import yaml


class TestLoadConfig:
    @pytest.fixture(scope="function")
    def config_path(self, tmp_path):
        _yml = """\
data:
  train:
    start: 1919-01-01 00:00:00
    end: 2009-12-31 23:59:59
  test:
    start: 2010-01-01 00:00:00
    end: 2019-12-31 23:59:59
"""
        p = tmp_path / "config.yml"
        p.write_text(_yml)
        return p

    def test_load_config(self, config_path):
        actual = utils.load_config(config_path)

        with config_path.open("r") as f:
            expected = yaml.safe_load(f)

        assert actual == expected
