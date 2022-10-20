import json
import logging
import os
import sys
from typing import Any

import requests

sys.path.append(os.path.dirname(__file__) + '/..')
from settings.common.config import settings  # noqa: E402

# create console handler and set level to debug
_log_handler = logging.StreamHandler()
_log_handler.setLevel(logging.DEBUG)


logger = logging.getLogger('fast_api')
logger.addHandler(_log_handler)
logger.setLevel(logging.DEBUG)


def get_data_from_auth(user_id: str) -> Any:
    params = {'user_id': user_id}
    response = requests.get(
        f'{settings.AUTH_SERVICE}/v1/user_by_id',
        params=params,
    )
    logger.info(response.content)
    print(response.content)
    json_data = json.loads(response.content)
    return json_data['user']


if __name__ == '__main__':
    get_data_from_auth('56d2cbdc-d46c-44c7-b61f-3716863a2977')
