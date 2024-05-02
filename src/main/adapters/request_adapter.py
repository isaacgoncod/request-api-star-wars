from typing import Callable
from fastapi import Request as RequestFastApi


async def request_adapter(request: RequestFastApi, callback: Callable):
    '''
      FastAPI request adapter
    '''

    body = None

    try:
        body = await request.json()
    except:
        pass

    http_request = {
        'query_paramns': request.query_params,
        'body': body
    }

    try:
        http_response = callback(http_request)
        return http_response
    except:
        print('An error has ocurred')
