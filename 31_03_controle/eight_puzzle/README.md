
# Como executar

Entrar no diretório src

```
cd src
```

Visualizar cobertura de comandos 

```
coverage run --branch -m unittest arquivo_testes.TesteComandos
coverage html
```


Visualizar cobertura de ramos 

```
coverage run --branch -m unittest arquivo_testes.TesteRamos
coverage html
```