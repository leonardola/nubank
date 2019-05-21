## Projeto Nubank

```pip install pymysql
pip install peewee
pip install pyyaml
pip install pandas
pip install Pillow
```
Copie o arquivo config.yml.dist para config.yml e troque as credenciais 

Crie o banco de dados no mysql chamado nubank 
Importe o arquivo database/database.sql


Executar o servidor

```python3.5 Index.py```

Agora acesse 

```localhost:5000```
Clique em iniciar sincronização, escaneie o qr code e clique em sincronizar. Depois é só recarregar a pagina

Tela Inicial
![alt text](https://raw.githubusercontent.com/leonardola/nubank/master/static/image/inicio.png)

Escaneie o QR code e Sincronize sua conta
![alt text](https://raw.githubusercontent.com/leonardola/nubank/master/static/image/qr.png)

Adicione movimentos manualmente
![alt text](https://raw.githubusercontent.com/leonardola/nubank/master/static/image/add.png)

Tagueie seus gastos e visualise no grafico
![alt text](https://raw.githubusercontent.com/leonardola/nubank/master/static/image/tag.png)