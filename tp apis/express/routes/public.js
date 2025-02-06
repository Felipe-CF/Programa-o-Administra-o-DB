import express from 'express'
import conexao from '../server.js' // importando a conexao feita ao postgreSQL

const router = express.Router()

router.post('/usuario', async (requisicao, resposta) => {
    try{

        const dados = requisicao.body
    
        const resultado = await  conexao.query(
            `INSERT INTO usuarios (nome, email) VALUES ($1, $2) RETURNING *`,
            [dados.user, dados.email]
        );
    
        const retorno = resultado.rows[0]
    
        resposta.status(201).json({
            mensagem : 'Usuário cadastrado', 
            user : retorno
        })
    } catch(error){
        resposta.status(500).json({
            mensagem: 'Erro ao cadastrar usuário'
        })
    }

})

router.get('/usuario', async (requisicao, resposta) => {
    
    const resultado = await conexao.query(
        'SELECT * FROM usuarios ORDER BY id ASC', (erro, resultado) =>{
        if(erro)
            throw erro

        resposta.status(200).json(resultado.rows)
    })
})



export default router