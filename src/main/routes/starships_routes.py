from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.validators.get_starships_in_pagination_validator import get_pagination_validator
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.get_starships_in_pagination_composer import get_starships_in_pagination_composer

starships_routes = APIRouter()


@starships_routes.get('/api/starships/list')
async def get_starships_in_pagination(request: RequestFastApi):
    '''
      get starships in pagination
    '''
    get_pagination_validator(request)

    controller = get_starships_in_pagination_composer()

    response = await request_adapter(request, controller.handle)

    return JSONResponse(
        status_code=response['status_code'],
        content={'data': response['data']}
    )
