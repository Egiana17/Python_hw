import requests 


base_url = "https://ru.yougile.com"
key = "xBEFU-KbRU8CihpCPgOjdcu28rBPbSShV1ye-IL4uqMXp6B6nkUP7ur1nj8KBIe4"


def test_kreat_progect_positive():
    headers = {"Authorization": f"Bearer {key}"}
    body = {"title": "Учебный проект"}
    response = requests.post(f"{base_url}/api-v2/projects", headers=headers, json=body)
    assert response.status_code == 201

def test_kreat_progect_negative():
    headers = {"Authorization": "Bearer "}
    body = {"title": "Учебный проект"}
    response = requests.post(f"{base_url}/api-v2/projects", headers=headers, json=body)
    assert response.status_code == 401

def test_apdet_progect_positive():
    headers = {"Authorization": f"Bearer {key}"}
    body = {"title": "Учебный проект"}
    PROJECT_ID = "c7da1d90-e6f6-4e27-88f6-f1935f67844e"
    response = requests.put(f"{base_url}/api-v2/projects/{PROJECT_ID}", headers=headers, json=body)
    assert response.status_code == 200   

def test_get_progect_positive():
    headers = {"Authorization": f"Bearer {key}"}
    
    PROJECT_ID = "c7da1d90-e6f6-4e27-88f6-f1935f67844e"
    response = requests.get(f"{base_url}/api-v2/projects/{PROJECT_ID}", headers=headers)
    assert response.status_code == 200
