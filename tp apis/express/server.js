import express from 'express'
import publicRouter from './routes/public.js'
import postgres from 'pg'

const {Client} = postgres // importanto a classe Client responsável pelo conexão com o PostgreSQL

const conexao = new Client({
  user: 'express',
  host: 'localhost',
  database: 'express',
  password: 'express',
  port: 5432,
})

await conexao.connect() // Espera o termino da conexão assincrona. Garante que a conexão seja estabelecida antes do uso.

const app = express()

app.use(express.json()) // responder com JSON

app.use('/public', publicRouter)

app.use('/private', publicRouter)


app.listen(8000, () => console.log("Rodando api "))

export default conexao