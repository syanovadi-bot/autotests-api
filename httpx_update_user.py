import httpx

import time


def get_random_email() -> str:
    return f"test.{time.time()}@example.com"


client = httpx.Client(base_url="http://localhost:8000")

with client:
    try:
        user_data = {
            "email": "user123@example.com",
            "password": "nadezniyparol222",
            "lastName": "string2",
            "firstName": "string2",
            "middleName": "string2"
        }
        user_response = client.post('/api/v1/users', json=user_data)
        user_response.raise_for_status()
        user_id = user_response.json().get('user').get('id')
        print(f"User ID: {user_id}")
        if user_id:
            tokens_response = client.post('/api/v1/authentication/login',
                                          json={'email': user_data['email'], 'password': user_data['password']})
            tokens_response.raise_for_status()
            access_token = tokens_response.json().get('token').get('accessToken', None)
            print(access_token)
            if access_token:
                headers = {"Authorization": f"Bearer {access_token}"}
                update_data = {
                    "email": get_random_email(),
                    "lastName": "string3",
                    "firstName": "string3",
                    "middleName": "string3"
                }
                update_user_response = client.patch(f'/api/v1/users/{user_id}', json=update_data, headers=headers)
                update_user_response.raise_for_status()
                update_user_response.raise_for_status()
                print(update_user_response.json())
        else:
            print("No user found")
    except httpx.HTTPStatusError as e:
        print(f'Http status error: {e}')
