def user_name_validation(user_name):
    if user_name==None:
        raise ValueError('名前が設定されていません')