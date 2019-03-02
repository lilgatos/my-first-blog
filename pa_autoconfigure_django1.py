import requests
my_domain = 'lilgatos.pythonanywhere.com'
username = 'lilgatos'
token = 'cd618586cef8ebdb40b11e85a8dac76ff7d0a00c'

response = requests.post(
  'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
      username=username, domain=my_domain
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
  print('All OK')
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
                        
