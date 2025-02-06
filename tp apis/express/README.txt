
POSTGRES
npm install pg 

    ====    body-parser ====

=> O que é o body-parser?
O body-parser é um middleware para o Express que faz o parsing (análise e conversão) do corpo (body) das requisições HTTP. 
Ele é usado principalmente para extrair dados enviados no corpo de requisições POST, PUT, PATCH 
e outras que contenham um payload (carga útil).  

=> Para que Serve o body-parser?
Quando você envia dados em uma requisição HTTP (por exemplo, um formulário ou um JSON), 
esses dados são enviados no corpo da requisição (body). Por padrão, o Express não sabe como processar esses dados. 
O body-parser faz isso, convertendo os dados em um formato que você pode usar no seu código.

=> Tipos de dados = JSON, Text, Raw (binários ou não processados) e URL-encoded

=> A partir do express 4.16 ele já foi integrado, por isso pode ser utilizado assim = app.use(express.json()) 


=> Operações de banco de dados, incluindo GETs, são inerentemente assíncronas em Node.js.

