from source import code3

def get_json_data_mock(id):
    return {'name':'サプー'}

def test_get_user_names(monkeypatch):
    monkeypatch.setattr(code3,'get_json_data',get_json_data_mock)
    result=code3.get_user_names(['001', '009'])

    assert list(result.keys())==['001']
    assert list(result.values())==['サプー']