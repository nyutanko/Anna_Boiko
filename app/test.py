import requests
import json


class Scenario:

    def __init__(self, access_token, file):
        self.access_token = access_token
        self.file = file

    def upload(self):
        url = 'https://content.dropboxapi.com/2/files/upload'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Dropbox-API-Arg': json.dumps({
                "autorename": False,
                "mode": "add",
                "mute": False,
                "path": f"/{self.file}",
                "strict_conflict": False
            }),
            'Content-Type': 'application/octet-stream'
        }
        with open(self.file, 'rb') as file:
            data = file.read()
            return requests.post(url, headers, data)

    def get_metadata(self):
        url = 'https://api.dropboxapi.com/2/files/alpha/get_metadata'
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        data = json.dumps({'path': f'/{self.file}'})
        return requests.post(url, headers, data)

    def delete(self):
        url = 'https://api.dropboxapi.com/2/files/delete'
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        data = json.dumps({'path': f'/{self.file}'})
        return requests.post(url, headers, data)
