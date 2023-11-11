import requests


class GitHubClient:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_image(self, repo_owner, repo_name, image_path):
        # 画像ファイルを読み込む
        with open(image_path, 'rb') as f:
            image_data = f.read()

        # GitHubのAPIエンドポイント
        upload_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{image_path}'

        # リクエストヘッダー
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
        }

        # リクエストボディ
        data = {
            'message': '画像をアップロード',
            'content': image_data,
        }

        # 画像をアップロード
        response = requests.put(upload_url, headers=headers, json=data)

        # レスポンスを返す
        return response.json()
