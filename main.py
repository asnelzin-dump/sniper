import pickle
import vk_auth
import json
import requests
from settings import settings, logger


def _call_api(method, params):
    """Call VK.Api method"""
    url = "https://api.vk.com/method/{}".format(method)
    response = requests.get(url, params=params)
    return json.loads(response.text)['response']


def get_user_friends(sid, user_id):
    params = {
        'access_token': sid,
        'user_id': user_id,
    }
    response = _call_api('friends.get', params)
    return {
        'count': len(response),
        'friends': response
    }


def update_task():
    sid, _ = vk_auth.auth(settings['email'], settings['password'], settings['api_id'], "audio")
    data = get_user_friends(sid, settings['user_id'])
    with open('latest_data.pkl', 'r+b') as _file:
        old_data = pickle.load(_file)
        diff = {
            'deletions': set(old_data['friends']) - set(data['friends']),
            'insertions': set(data['friends']) - set(old_data['friends'])
        }
        diff.update({'ins_len': len(diff['insertions']),
                     'insertions': '{ ' + ', '.join([str(item) for item in diff['insertions']]) + ' }',
                     'del_len': len(diff['deletions']),
                     'deletions': '{ ' + ', '.join([str(item) for item in diff['deletions']]) + ' }'})
        logger.info('', extra=diff)
        _file.seek(0)
        pickle.dump(data, _file)


def main():
    update_task()

if __name__ == '__main__':
    main()