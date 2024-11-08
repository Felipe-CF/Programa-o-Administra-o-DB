import psycopg2

class Contato:
    def __init__(self, id, nome, email, endereco, telefone, cep):
        self.id = id
        self.cep = cep
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.nome = nome
    
    # @property
    # def id(self):
    #     return self.id
    
    # @id.setter
    # def id(self, novo_id):
    #     self._id = novo_id

    # @property
    # def cep(self):
    #     return self.cep
    
    # @cep.setter
    # def cep(self, novo_cep):
    #     if len(novo_cep):
    #         self._cep = novo_cep
    #     else:
    #         raise ValueError("CEP inválido")

    # @property
    # def endereco(self):
    #     return self.endereco
    
    # @endereco.setter
    # def endereco(self, novo_endereco):
    #     if len(novo_endereco) <= 100 and novo_endereco != '':
    #         self._endereco = novo_endereco
    #     else:
    #         raise ValueError("Endereço inválido")
    
    # @property
    # def telefone(self):
    #     return self.telefone
    
    # @telefone.setter
    # def telefone(self, novo_telefone):
    #     if len(novo_telefone) >= 10:
    #         self._telefone = novo_telefone
    #     else:
    #         raise ValueError("telefone inválido")
        
    # @property
    # def email(self):
    #     return self.email
    
    # @email.setter
    # def email(self, novo_email):
    #     if len(novo_email) <= 40 and '@' in novo_email:
    #         self._email = novo_email
    #     else:
    #         raise ValueError("email inválido")
        
    # @property
    # def nome(self):
    #     return self.nome
    
    # @nome.setter
    # def nome(self, novo_nome):
    #         self._nome = novo_nome


    def __str__(self):
        return f"ID: {self.id} Nome:{self.nome}, Endereço: {self.endereco} - {self.cep}, email:{self.email}, telefone:{self.telefone} Data de nascimento:{self.nome}"

        
