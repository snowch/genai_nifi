# SPDX-FileCopyrightText: 2024-present VASTDATA <www.vastdata.com>
#
# SPDX-License-Identifier: MIT

import pytest

from vastdb_nifi.processors.predicate_parser import parse_yaml_predicate


def test_single_column_predicate():
    yaml_predicate = """
    - column: extra
      op: ">"
      value: 2
    """
    ibis_expr = parse_yaml_predicate(yaml_predicate)
    assert str(ibis_expr) == "(_['extra'] > 2)"


def test_integer_value_predicate():
    yaml_predicate = """
    - column: vendor_id
      op: "=="
      value: 3
    """
    ibis_expr = parse_yaml_predicate(yaml_predicate)
    assert str(ibis_expr) == "(_['vendor_id'] == 3)"


def test_empty_operator():
    yaml_predicate = """
    - column: extra
      op:
      value: 2
    """
    with pytest.raises(ValueError, match="Missing or empty operator for column: extra"):
        parse_yaml_predicate(yaml_predicate)


def test_missing_operator():
    yaml_predicate = """
    - column: extra
      value: 2
    """
    with pytest.raises(ValueError, match="Missing or empty operator for column: extra"):
        parse_yaml_predicate(yaml_predicate)


if __name__ == "__main__":
    pytest.main()
