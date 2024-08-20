# importação de biblioteca
import winapps

for item in winapps.list_installed():
    print(f'Programa: {item.name}.')
    print(f'Versão: {item.version}.')
    print(f'Data de instalação: {item.install_date}.')
    print(f'Data de publicação: {item.publisher}.')
    print(f'Local de desinstalação: {item.uninstall_string}.')
    print('-'*50)