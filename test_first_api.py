import pytest
import requests


class TestFirstApi:
    names = [
        ("Elena"),
        ("Maksim"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    def test_say_hello_by_name_you_specify(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        payload = {"name": name}

        response = requests.get(url, params=payload)

        assert response.status_code == 200, \
            "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, \
            "There is no 'answer' field in the response"

        if len(name) ==0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"

        actual_response_text = response_dict["answer"]

        assert actual_response_text == expected_response_text, \
            "Actual text in the response is not correct"
