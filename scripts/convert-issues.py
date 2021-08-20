import urllib.request as request
import json

fhandle = open('todo.md', 'w')

uh = request.urlopen("http://api.github.com/repos/LukeSmithxyz/based.cooking/issues")
response = uh.read()

data = json.loads(response)

markdown = list()
markdown.append('# todos\n')
for entry in data:
  try:
    pr=entry['pull_request']
    pass
  except Exception as e:
    markdown.append('- [ ] {} [#{}]({}) 💬{}\n'.format(entry['title'], entry['number'], entry['url'], entry['comments']))

fhandle.write('\n'.join(markdown))

print('updated todo.md')
