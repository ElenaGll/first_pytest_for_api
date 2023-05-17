from requests import Response


class BaseCase:

    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, \
            f"Cannot find cookies with the name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, \
            f"Cannot find header with the name {header_name} in the last response"
        return response.headers[header_name]
