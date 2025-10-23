import requests

# Replace with your actual API token and space ID
API_TOKEN = 'gb_api_NXUx0Oiz26S3tb8m8lLnHNVYN2DaAC7JSoCZT5va'
SPACE_ID = 'vLb8mfTOGtaVps0KaAUg'

# Base URL for GitBook API
BASE_URL = 'https://api.gitbook.com/v1'

# Headers for authentication
headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json'
}

def get_space_pages(space_id):
    url = f'{BASE_URL}/spaces/{space_id}/content'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_page_content(page_id):
    url = f'{BASE_URL}/spaces/{SPACE_ID}/content/{page_id}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def main():
    # Fetch all pages in the space
    pages = get_space_pages(SPACE_ID)
    for page in pages['pages']:
        page_id = page['id']
        page_title = page['title']
        page_url = page['url']
        print(f'Title: {page_title}')
        print(f'URL: {page_url}')
        # Fetch and print page content
        content = get_page_content(page_id)
        print(f'Content: {content["content"]}\n')

if __name__ == '__main__':
    main()
