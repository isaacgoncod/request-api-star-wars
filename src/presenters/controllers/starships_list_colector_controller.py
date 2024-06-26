from typing import Type, Dict
from src.domain.usecases.starships_list_colector import StarshipsListColectorInterface


class StarshipsListColectorController:
    ''' StarshipsListColectorController usecase '''

    def __init__(self, starships_list_colector: Type[StarshipsListColectorInterface]) -> None:
        self.__use_case = starships_list_colector

    def handle(self, http_request: Dict) -> None:
        ''' Handler to list collector usecase '''

        page = http_request['query_paramns']['page']
        starships_list = self.__use_case.list(page)
        http_response = {
            'status_code': 200,
            'data': starships_list
        }

        return http_response
