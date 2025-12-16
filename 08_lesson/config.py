import requests 


base_url = "https://ru.yougile.com"
key = "xBEFU-KbRU8CihpCPgOjdcu28rBPbSShV1ye-IL4uqMXp6B6nkUP7ur1nj8KBIe4"


def test_kreat_progect_positive():
    headers = {"Authorization": f"Bearer {key}"}
    body = {"title": "Учебный проект"}
    response = requests.post(f"{base_url}/api-v2/projects", headers=headers, json=body)
    assert response.status_code == 201
    response_json = response.json()
    assert response_json['title'] == 'Учебный проект'
