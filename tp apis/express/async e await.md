# Entendendo Async/Await e Operações Síncronas vs. Assíncronas em Node.js

## Funções Assíncronas (`async`)

- Uma função marcada como `async` pode conter operações assíncronas.
- Sempre retorna uma Promise, mesmo que não explicitamente.
- Permite o uso da palavra-chave `await` dentro dela.

## A Palavra-chave `await`

- Usada dentro de funções `async` para esperar a resolução de uma Promise.
- Pausa a execução da função até que a Promise seja resolvida.
- Não bloqueia a execução do programa inteiro, apenas da função assíncrona.

## Fluxo Síncrono vs. Assíncrono

- **Síncrono**: Cada operação é concluída antes de iniciar a próxima.
- **Assíncrono**: Operações podem ser iniciadas sem esperar que outras terminem.

## Por Que Usar Async/Await em Operações de Banco de Dados

1. **Não Bloqueio**: Evita bloquear o event loop do Node.js.
2. **Eficiência**: Permite que o servidor lide com múltiplas requisições simultaneamente.
3. **Legibilidade**: Torna o código assíncrono mais fácil de ler e manter.

## Exemplo Prático

```javascript
app.get('/usuarios', async (req, res) => {
  try {
    const resultado = await conexao.query('SELECT * FROM usuarios');
    res.json(resultado.rows);
  } catch (erro) {
    res.status(500).json({ erro: 'Erro ao buscar usuários' });
  }
});
```

## Conclusão

Operações de banco de dados em Node.js são inerentemente assíncronas.
Usar `async/await` é a abordagem recomendada, mesmo para operações GET.
Permite esperar pelos dados necessários de forma eficiente, sem comprometer o desempenho do servidor.