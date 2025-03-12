import pytest
from source import code4

def test_user_name_validation():
    with pytest.raises(ValueError) as e:
        code4.user_name_validation(None)
        assert str(e.value)=='名前が設定されていません'