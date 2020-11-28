import requests

response = requests.get('https://api.github.com')
print (response)
#
# print ('status code is {}' .format( response.status_code))
#
# print (response.content)
#
# print (response.text)
#
# print ('encoding is {}'.format(response.encoding))
#
# print (response.json())
#
# print (response.headers)
#
#
# # Search GitHub's repositories for requests
# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
# )
#
# # Inspect some attributes of the `requests` repository
# json_response = response.json()
# repository = json_response['items'][0]
# print(f'Repository name: {repository["name"]}')  # Python 3.6+
# print(f'Repository description: {repository["description"]}')  # Python 3.6+
#
# response = requests.post('https://httpbin.org/post', json={'key':'value'})
# json_response = response.json()
# print (json_response['data'])
# print (json_response['headers']['Content-Type'])
#
#
# # Authentication
#
# from getpass import getpass
# print(requests.get('https://api.github.com/user', auth=('username', getpass())) )