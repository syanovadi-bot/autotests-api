import httpx

client = httpx.Client(base_url="http://localhost:8000")

with client:
    auth_data = {
        "email": "user@example.com",
        "password": "string"
    }
    try:
        tokens_response = client.post('/api/v1/authentication/login', json=auth_data)
        tokens_response.raise_for_status()
        access_token = tokens_response.json().get('token').get('accessToken', None)
        if access_token:
            headers = {"Authorization": f"Bearer {access_token}"}
            current_user_response = client.get('/api/v1/users/me', headers=headers)
            print(current_user_response.json())
            print(f"Status code: {current_user_response.status_code}")
        else:
            print("No access token")

    except httpx.HTTPStatusError as e:
        print(f"HTTP status error: {e}")
