#!python
try:
    from mysql import connector
except ModuleNotFoundError:
    print('Mysql Connector não instalado!')
else:
    print('Mysql Connector instalado e pronto!')
    