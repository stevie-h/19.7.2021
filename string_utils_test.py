# ex24

import pytest
import string_utils


@pytest.mark.parametrize("s, expected", [("World", "WORLD"), ("WO", "WO")])
def test_make_upper(s, expected):
    assert string_utils.make_upper(s) == expected


@pytest.mark.parametrize("s, expected", [("Hello", "hello"),
                                         ("he", "he")])
def test_three_make_lower(s, expected):
    assert string_utils.make_lower(s) == expected


@pytest.mark.parametrize("s, e, expected", [("Why", "h", True),
                                            ("Where", "a", False)])
def test_check_e(s, e, expected):
    assert string_utils.check_e(s, e) == expected


