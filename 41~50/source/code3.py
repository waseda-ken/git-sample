import requests

def get_json_data(id):
    res=requests.get('http://xxxxxx', params={'id':id})
    res_json=res.json()
    return res_json

def get_user_names(user_ids):
    user_names={}
    for id in user_ids:
        json_date=get_json_data(id)
        user_names[id]=json_date['name']
        return user_names