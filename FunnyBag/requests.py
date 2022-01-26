
# Обработка GET-запроса с параметрами
class GetRequests:

    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            # Делим параметры через &
            params = data.split('&')
            for item in params:
                # Делим ключ и значение через =
                k, v = item.split('=')
                result[k] = v
        return result

    @staticmethod
    def get_request_params(environ):
        # Получаем параметры запроса
        query_string = environ['QUERY_STRING']
        # Превращаем параметры в словарь
        request_params = GetRequests.parse_input_data(query_string)
        return request_params