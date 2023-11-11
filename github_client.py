import base64
import requests


class GitHubClient:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = 'https://api.github.com'
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28',
        }

    def _request(
        self,
        method,
        url,
        data=None,
        params=None,
        headers=None,
    ):
        print('【start】GitHubClient._request()')
        print(f'method: {method}')
        print(f'url: {url}')
        print(f'data: {data}')

        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                json=data,
                params=params
            )
        except Exception as e:
            raise Exception(e)

        if response.status_code != 200:
            raise Exception(response.text)

        print('【end】GitHubClient._request()')

        return response

    def get_repo(self, repo_owner, repo_name):
        request_url = f'{self.base_url}/repos/{repo_owner}/{repo_name}'
        method = 'GET'
        response = self._request(method, request_url, headers=self.headers)

        return response.json()

    def upload_image(
        self,
        repo_owner,
        repo_name,
        image_path,
        output_path,
    ):
        request_url = f'{self.base_url}/repos/{repo_owner}/{repo_name}/contents/{output_path}'
        method = 'PUT'

        # 画像ファイルの読み込み
        with open(image_path, 'rb') as f:
            image_data = f.read()
            image_data = base64.b64encode(image_data)

        # リクエストヘッダー
        headers = self.headers
        print(headers)

        # リクエストボディ
        data = {
            'message': 'add image',
            'content': image_data.decode('utf-8'),
        }

        # 画像をアップロード
        response = self._request(method, request_url, data=data, headers=headers)

        # レスポンスを返す
        return response.json()

    def get_contents(self, repo_owner, repo_name, file_path):
        request_url = f'{self.base_url}/repos/{repo_owner}/{repo_name}/contents/{file_path}'
        method = 'GET'
        headers = self.headers

        # ファイルの内容を取得
        response = self._request(method, request_url, headers=headers)

        # レスポンスを返す
        return response.json()
