import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Erro ao tentar acessar o site')
else:
    print('Site acessado com sucesso')