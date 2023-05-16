from json.decoder import JSONDecodeError
import requests


def say_hello_by_name_you_specify_get_metod(name):
    payload = {"name": name}
    response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)

    try:
        parsed_response_text = response.json()
        print(parsed_response_text["answer"])

    except JSONDecodeError:
        print("Response is not a JSON format")


def say_what_type_of_requesr_it_is_post_metod():
    payload = {"param1": "value1"}
    response = requests.post("https://playground.learnqa.ru/api/check_type", data=payload)

    print(response.text)


def get_response_with_500_code_get_metod():
    response = requests.get("https://playground.learnqa.ru/api/get_500")

    print(response.status_code)

def get_response_with_404_code_get_metod():
    response = requests.get("https://playground.learnqa.ru/api/something")

    print(response.status_code)
    print(response.text)


def get_response_with_301_code_without_redirects_get_method():
    response = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=False)

    print(response.status_code)
    print(response.text)


def get_history_of_redirects_get_method():
    response = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)

    first_response = response.history[0]
    second_response = response

    print(first_response.url)
    print(second_response.url)


def show_all_headers_from_request_get_method():
    headers = {"some_header": "123"}
    response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)

    print(response.text)
    print(response.headers)


def set_auth_cookie_by_login_and_password_post_method():
    payload = {"login": "secret_login", "password": "secret_pass"}
    response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

    print(response.text)
    print(response.status_code)
    print(dict(response.cookies))


def returns_text_depends_on_has_you_auth_cookie_or_not_post_method():
    payload = {"login": "secret_login", "password": "secret_pass"}
    response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

    cookie_value = response1.cookies.get("auth_cookie")

    cookies = {}
    if cookie_value is not None:
        cookies.update({"auth_cookie": cookie_value})

    response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

    print(response2.text)
