import psycopg2

class Contato:
    def __init__(self, cep, endereco, telefone, email, data_nasc):
        self.cep = cep
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.data_nasc = data_nasc
    
    @property
    def cep(self):
        return self.cep
    
    @cep.setter
    def cep(self, novo_cep):
        if len(novo_cep):
            self.cep = novo_cep
        else:
            raise ValueError("CEP inválido")

    @property
    def endereco(self):
        return self.endereco
    
    @endereco.setter
    def endereco(self, novo_endereco):
        if len(novo_endereco) <= 100 and novo_endereco != '':
            self.endereco = novo_endereco
        else:
            raise ValueError("Endereço inválido")
    
    @property
    def telefone(self):
        return self.telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        if len(novo_telefone) >= 10:
            self.telefone = novo_telefone
        else:
            raise ValueError("telefone inválido")
        
    @property
    def email(self):
        return self.email
    
    @email.setter
    def email(self, novo_email):
        if len(novo_email) <= 40 and '@' in novo_email:
            self.email = novo_email
        else:
            raise ValueError("email inválido")
        
    @property
    def data_nasc(self):
        return self.data_nasc
    
    @data_nasc.setter
    def data_nasc(self, novo_data_nasc):
            self.data_nasc = novo_data_nasc


    def __str__(self):
        return f"Endereço:{self.endereco} - {self.cep}, email:{self.email}, telefone:{self.telefone}\nData de nascimento:{self.data_nasc}"

        
