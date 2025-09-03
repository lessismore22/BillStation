from urllib import response
from wsgiref import headers
from django import urls
import requests
import json

BASE_URL = 'https://billstation-3.onrender.com'

class AuthAPITester:
    def __init__(self):
        self.session = requests.Session()
        self.access_token = None
        self.refresh_token = None
    
    def test_registration(self):
        """Test user registration"""
        data = {
            'email': 'test@example.com',
            'full_name': 'Test User',
            'password': 'TestPassword123!',
            'password_confirm': 'TestPassword123!'
        }
        
        response = self.session.post(f'{BASE_URL}/register/', json=data)
        print(f"Registration: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        
        if response.status_code == 201:
            tokens = response.json().get('tokens', {})
            self.access_token = tokens.get('access')
            self.refresh_token = tokens.get('refresh')
        
        return response
    
    def test_login(self):
        """Test user login"""
        data = {
            'email': 'test@example.com',
            'password': 'TestPassword123!'
        }
        
        response = self.session.post(f'{BASE_URL}/login/', json=data)
        print(f"Login: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        
        if response.status_code == 200:
            tokens = response.json().get('tokens', {})
            self.access_token = tokens.get('access')
            self.refresh_token = tokens.get('refresh')
        
        return response
    
    def test_profile(self):
        """Test getting user profile"""
        headers = {'Authorization': f'Bearer {self.access_token}'}
        
        response = self.session.get(f'{BASE_URL}/profile/', headers=headers)
        print(f"Profile: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        
        return response
    
    # def test_forgot_password(self):
    #     """Test forgot password"""
    #     data = {'email': 'test@example.com'}
        
    #     response = self.session.post(f'{BASE_URL}/forgot-password/', json=data)
    #     print(f"Forgot Password: {response.status_code}")
    #     print(json.dumps(response.json(), indent=2))
        
    #     response = requests.post(urls, json=data, headers=headers)

    #     print("Status code:", response.status_code)
    #     print("Content-Type:", response.headers.get("Content-Type"))
    #     print("Response text:", response.text)

    #     try:
    #        response_json = response.json()
    #        print("JSON response:", json.dumps(response_json, indent=2))
    #     except requests.exceptions.JSONDecodeError:
    #         print("Response is not valid JSON. Check server logs for errors.")
    
    def test_change_password(self):
        """Test password change"""
        headers = {'Authorization': f'Bearer {self.access_token}'}
        data = {
            'current_password': 'TestPassword123!',
            'new_password': 'NewPassword123!',
            'new_password_confirm': 'NewPassword123!'
        }
        
        response = self.session.post(f'{BASE_URL}/change-password/', json=data, headers=headers)
        print(f"Change Password: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        
        return response
    
    def test_logout(self):
        """Test user logout"""
        headers = {'Authorization': f'Bearer {self.access_token}'}
        data = {'refresh': self.refresh_token}
        
        response = self.session.post(f'{BASE_URL}/logout/', json=data, headers=headers)
        print(f"Logout: {response.status_code}")
        print(json.dumps(response.json(), indent=2))
        
        return response
    
    def run_all_tests(self):
        """Run all API tests"""
        print("=== Testing Auth API ===\\n")
        
        print("1. Testing Registration...")
        self.test_registration()
        print()
        
        print("2. Testing Profile Access...")
        self.test_profile()
        print()
        
        # print("3. Testing Forgot Password...")
        # self.test_forgot_password()
        # print()
        
        print("4. Testing Change Password...")
        self.test_change_password()
        print()
        
        print("5. Testing Logout...")
        self.test_logout()
        print()

if __name__ == '__main__':
    tester = AuthAPITester()
    tester.run_all_tests()