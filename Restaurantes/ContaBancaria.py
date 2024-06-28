class ContaBancaria:
    contas = []

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False
        ContaBancaria.contas.append(self)

    def __str__(self):
        return f'Titular: {self.titular}\nSaldo: R$ {self.saldo:.2f}\nStatus: {self._ativo}\n'

    @classmethod  # BOA PRÁTICA - para indicar que é um metodo da classe
    def listar_contas (cls):
        cont = 1
        for conta in cls.contas:
            print (f'CC{cont}\nTitular: {conta.titular}\nSaldo: R$ {conta.saldo:.2f}\nStatus: {conta.ativo}\n')
            cont += 1

    def ativar_conta(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'

cc01 = ContaBancaria('Danilo Alves', 20500.90)
cc02 = ContaBancaria('Talita Haneiko', 125900)

#print(f'CC01: {cc01}')
#print(f'CC02: {cc02}')

#cc01.ativar_conta()
#print(f'CC01: {cc01}')
cc01.ativar_conta()
ContaBancaria.listar_contas()