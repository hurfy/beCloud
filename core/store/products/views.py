from typing                     import Any
from requests                   import post, get, delete, put
from django.http                import JsonResponse
from rest_framework.views       import APIView
from rest_framework.permissions import IsAuthenticated

STORE_ADDRESS = f'http://127.0.0.1:80/items/'


class ProductsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: Any, item_id: int = None) -> JsonResponse:
        """
        Реализация GET запроса на получение всего списка товаров, либо конкретного товара по ID
        :param request:        request
        :param item_id:   int: ID товара = None
        :return: JsonResponse: Ответ
        """
        response = get(STORE_ADDRESS) if item_id is None \
            else get(f'{STORE_ADDRESS}{item_id}/')

        print(STORE_ADDRESS)

        match response.status_code:
            case 200:
                return JsonResponse(response.json(), safe=False)

            case 404:
                return JsonResponse({'error': 'Item not found'}, status=404)

            case _:
                return JsonResponse({'error': 'Failed to fetch products'}, status=500)

    def post(self, request: Any) -> JsonResponse:
        """
        Реализация POST запроса на создание нового товара
        :param request:        request
        :return: JsonResponse: Ответ
        """
        response = post(STORE_ADDRESS, json=request.data)

        match response.status_code:
            case 200:
                return JsonResponse(response.json(), safe=False, status=201)

            case _:
                return JsonResponse({'error': 'Failed to create product'}, status=500)

    def put(self, request: Any, item_id: int) -> JsonResponse:
        """
        Реализация PUT запроса на изменение товара по ID
        :param request:        request
        :param item_id:   int: ID товара
        :return: JsonResponse: Ответ
        """
        response = put(f'{STORE_ADDRESS}{item_id}/', json=request.data)

        match response.status_code:
            case 200:
                return JsonResponse(response.json(), safe=False)

            case _:
                return JsonResponse({'error': 'Failed to update product'}, status=500)

    def delete(self, request: Any, item_id: int = None) -> JsonResponse:
        """
        Реализация DELETE запроса на удаление всех товаров из списка, либо конкретного товара по ID
        :param request:        request
        :param item_id:   int: ID товара = None
        :return: JsonResponse: Ответ
        """
        response = delete(STORE_ADDRESS) if item_id is None \
            else delete(f'{STORE_ADDRESS}{item_id}/')

        match response.status_code:
            case 200:
                return JsonResponse({'delete': 'Successfully deleted!'}, status=204)

            case _:
                return JsonResponse({'error': 'Failed to delete product'}, status=500)