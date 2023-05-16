import requests


def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get('http://api.zippopotam.us/us/90210')
    assert 200 == response.status_code, \
        'Status code should be 200'


def test_get_locations_for_us_90210_check_content_type_equals_json():
    response = requests.get('http://api.zippopotam.us/us/90210')
    assert 'application/json' == response.headers['Content-Type'], \
        'Content type should be json'


def test_get_locations_for_us_90210_check_country_equals_united_states():
    response = requests.get('http://api.zippopotam.us/us/90210')
    response_body = response.json()
    assert "United States" == response_body["country"], \
        'Country should be United Stated'


def test_get_locations_for_us_90210_check_city_equals_beverly_hills():
    response = requests.get('http://api.zippopotam.us/us/90210')
    response_body = response.json()
    assert "Beverly Hills" == response_body["places"][0]["place name"], \
        'Place name should be Beverly Hills'


def test_get_locations_for_us_90210_check_one_place_is_returned():
    response = requests.get('http://api.zippopotam.us/us/90210')
    response_body = response.json()
    assert 1 == len(response_body["places"]), \
        'One place should be returned'
