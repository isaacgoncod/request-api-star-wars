from src.infra.swapi_api_consumer import SwapiApiConsumer
from src.data.usecases.starships_list_colector import StarshipsListColector
from src.presenters.controllers.starships_list_colector_controller import StarshipsListColectorController


def get_starships_in_pagination_composer():
    ''' get_starships_in_pagination_composer usecase '''

    infra = SwapiApiConsumer()
    usecase = StarshipsListColector(infra)
    controller = StarshipsListColectorController(usecase)

    return controller
