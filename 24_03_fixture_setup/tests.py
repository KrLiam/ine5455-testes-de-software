
import unittest

from sistema_bancario import SistemaBancario
from dinheiro import Dinheiro, Moeda, ValorMonetario
from conta import Conta
from operacao import EstadosDeOperacao

class TesteDinheiro(unittest.TestCase):
    def test_criacao_moeda_brl(self):
        # Fixture Setup

        # Exercise SUT
        brl = Moeda.BRL

        # Result Verification
        self.assertEqual(brl.simbolo(), "R$")
        self.assertEqual(brl.base_fracionaria(), 100)
        # Fixture Teardown
    
    def test_criacao_dinheiro(self):
        # Fixture Setup

        # Exercise SUT
        dinheiro = Dinheiro(Moeda.BRL, 1, 50)

        # Result Verification
        self.assertEqual(dinheiro.moeda, Moeda.BRL)
        self.assertEqual(dinheiro.inteiro, 1)
        self.assertEqual(dinheiro.fracionado, 50)
        # Fixture Teardown

    def test_criacao_dinheiro_negativo(self):
        # Fixture Setup

        # Exercise SUT
        with self.assertRaises(ValueError):
            Dinheiro(Moeda.BRL, -1, 50)
        
        # Result Verification
        # Fixture Teardown

    def test_dinheiro_em_escala(self):
        # Inline Fixture Setup
        dinheiro = Dinheiro(Moeda.BRL, 1, 50)

        # Exercise SUT
        quantia = dinheiro.obter_quantia_em_escala()

        # Result Verification
        self.assertEqual(quantia, 150)
        # Fixture Teardown

    def test_valor_monetario_subtrair(self):
        # Inline Fixture Setup
        valor = ValorMonetario(Moeda.BRL, 1000)

        # Exercise SUT
        valor = valor.subtrair(Dinheiro(Moeda.BRL, 3, 0))

        # Result Verification
        dinheiro_total = valor.obter_quantia()
        quantia = dinheiro_total.obter_quantia_em_escala()
        self.assertEqual(quantia, 700)
        # Fixture Teardown

    def test_valor_monetario_somar(self):
        # Inline Fixture Setup
        valor = ValorMonetario(Moeda.BRL, 1000)

        # Exercise SUT
        valor = valor.somar(Dinheiro(Moeda.BRL, 3, 0))

        # Result Verification
        dinheiro_total = valor.obter_quantia()
        quantia = dinheiro_total.obter_quantia_em_escala()
        self.assertEqual(quantia, 1300)
        # Fixture Teardown


class TesteBanco(unittest.TestCase):
    def setUp(self):
        self.sistema_bancario = SistemaBancario()
        self.banco = self.sistema_bancario.criar_banco("BancoTeste", Moeda.BRL)
    
    def test_criar_agencia(self):
        # Implicit Fixture Setup

        # Exercise SUT
        agencia = self.banco.criar_agencia("Sede")

        # Result Verification
        num_agencias = len(self.banco.obter_agencias())
        self.assertEqual(num_agencias, 1)
        agencia2 = self.banco.obter_agencia("Sede")
        self.assertTrue(agencia is agencia2)
        # Fixture Teardown

class TesteAgencia(unittest.TestCase):
    def setUp(self):
        self.sistema_bancario = SistemaBancario()
        self.banco = self.sistema_bancario.criar_banco("BancoTeste", Moeda.BRL)
        self.agencia = self.banco.criar_agencia("Sede")
    
    def test_criar_conta(self):
        # Implicit Fixture Setup

        # Exercise SUT
        conta = self.agencia.criar_conta("Joao da Silva")
        
        # Result Verification
        num_contas = len(self.agencia.obter_contas())
        self.assertEqual(num_contas, 1)
        conta2 = self.agencia.obter_conta(conta.obter_identificador())
        self.assertTrue(conta is conta2)
        # Fixture Teardown


class TestHelperSistemaBancario:
    def __init__(self, sistema_bancario):
        self.sistema_bancario = sistema_bancario

    def criar_contas(self, *titulares) -> list[Conta]:
        banco = self.sistema_bancario.criar_banco("BancoTeste", Moeda.BRL)
        agencia = banco.criar_agencia("Sede")

        return [ agencia.criar_conta(titular) for titular in titulares ]


class TesteSistemaBancario(unittest.TestCase):
    def setUp(self):
        self.sistema_bancario = SistemaBancario()
        self.helper = TestHelperSistemaBancario(self.sistema_bancario)
    
    def test_criar_banco(self):
        # Implicit Fixture Setup

        # Exercise SUT
        banco = self.sistema_bancario.criar_banco("BancoTeste", Moeda.BRL)

        # Result Verification
        num_bancos = len(self.sistema_bancario.obter_bancos())
        self.assertEqual(num_bancos, 1)
        banco2 = self.sistema_bancario.obter_banco("BancoTeste")
        self.assertTrue(banco is banco2)
        # Fixture Teardown
    
    def test_depositar_com_sucesso(self):
        # Implicit Fixture Setup
        # Delegated Fixture Setup
        conta_fulano, *_ = self.helper.criar_contas("Fulano")

        # Exercise SUT
        operacao = self.sistema_bancario.depositar(conta_fulano, Dinheiro(Moeda.BRL, 5, 0))

        # Result Verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SUCESSO)
        dinheiro_fulano = conta_fulano.calcular_saldo().obter_quantia()
        self.assertEqual(dinheiro_fulano.obter_quantia_em_escala(), 500)
        # Fixture Teardown

    def test_depositar_repetidamente_acumula_saldo(self):
        # Implicit Fixture Setup
        # Delegated Fixture Setup
        conta_fulano, *_ = self.helper.criar_contas("Fulano")
        # Inline Fixture Setup
        operacao1 = self.sistema_bancario.depositar(conta_fulano, Dinheiro(Moeda.BRL, 5, 0))

        # Exercise SUT
        operacao2 = self.sistema_bancario.depositar(conta_fulano, Dinheiro(Moeda.BRL, 6, 0))

        # Result Verification
        self.assertEqual(operacao1.obter_estado(), EstadosDeOperacao.SUCESSO)
        self.assertEqual(operacao2.obter_estado(), EstadosDeOperacao.SUCESSO)
        dinheiro_fulano = conta_fulano.calcular_saldo().obter_quantia()
        self.assertEqual(dinheiro_fulano.obter_quantia_em_escala(), 1100)
        # Fixture Teardown

    def test_sacar_sucesso(self):
        # Implicit Fixture Setup
        # Delegated Fixture Setup
        conta_fulano, *_ = self.helper.criar_contas("Fulano")
        # Inline Fixture Setup
        self.sistema_bancario.depositar(conta_fulano, Dinheiro(Moeda.BRL, 10, 0))

        # Exercise SUT
        operacao = self.sistema_bancario.sacar(conta_fulano, Dinheiro(Moeda.BRL, 1, 0))

        # Result Verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SUCESSO)
        dinheiro_fulano = conta_fulano.calcular_saldo().obter_quantia()
        self.assertEqual(dinheiro_fulano.obter_quantia_em_escala(), 900)
        # Fixture Teardown

    def test_sacar_repetidamente(self):
        # Implicit Fixture Setup
        # Delegated Fixture Setup
        conta_fulano, *_ = self.helper.criar_contas("Fulano")
        # Inline Fixture Setup
        self.sistema_bancario.depositar(conta_fulano, Dinheiro(Moeda.BRL, 10, 0))
        operacao1 = self.sistema_bancario.sacar(conta_fulano, Dinheiro(Moeda.BRL, 5, 0))

        # Exercise SUT
        operacao2 = self.sistema_bancario.sacar(conta_fulano, Dinheiro(Moeda.BRL, 4, 0))

        # Result Verification
        self.assertEqual(operacao1.obter_estado(), EstadosDeOperacao.SUCESSO)
        self.assertEqual(operacao2.obter_estado(), EstadosDeOperacao.SUCESSO)
        dinheiro_fulano = conta_fulano.calcular_saldo().obter_quantia()
        self.assertEqual(dinheiro_fulano.obter_quantia_em_escala(), 100)
        # Fixture Teardown

    def test_sacar_saldo_insuficiente_valor_excedente(self):
        # Implicit Fixture Setup
        # Delegated Fixture Setup
        conta_fulano, *_ = self.helper.criar_contas("Fulano")
        # Inline Fixture Setup
        self.sistema_bancario.depositar(conta_fulano, Dinheiro(Moeda.BRL, 10, 0))

        # Exercise SUT
        operacao = self.sistema_bancario.sacar(conta_fulano, Dinheiro(Moeda.BRL, 11, 0))

        # Result Verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SALDO_INSUFICIENTE)
        # Fixture Teardown

    def test_sacar_saldo_insuficiente_conta_vazia(self):
        # Implicit Fixture Setup
        # Delegated Fixture Setup
        conta_fulano, *_ = self.helper.criar_contas("Fulano")
        
        # Exercise SUT
        operacao = self.sistema_bancario.sacar(conta_fulano, Dinheiro(Moeda.BRL, 1, 0))
        
        # Result Verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SALDO_INSUFICIENTE)
        # Fixture Teardown
    
    def test_sacar_zero(self):
        # Implicit Fixture Setup
        # Delegated Fixture Setup
        conta_fulano, *_ = self.helper.criar_contas("Fulano")
        
        # Exercise SUT
        operacao = self.sistema_bancario.sacar(conta_fulano, Dinheiro(Moeda.BRL, 0, 0))

        # Result Verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SUCESSO)
        # Fixture Teardown

    def test_sacar_moeda_diferente(self):
        # Implicit Fixture Setup
        # Delegated Fixture Setup
        conta_fulano, *_ = self.helper.criar_contas("Fulano")
        
        # Exercise SUT
        operacao = self.sistema_bancario.sacar(conta_fulano, Dinheiro(Moeda.USD, 1, 0))

        # Result Verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.MOEDA_INVALIDA)
        # Fixture Teardown
        
    def test_transferir_sucesso(self):
        # Implicit Fixture Setup
        # Delegated Fixture Setup
        conta_fulano, conta_ciclano = self.helper.criar_contas("Fulano", "Ciclano")
        # Inline Fixture Setup
        self.sistema_bancario.depositar(conta_fulano, Dinheiro(Moeda.BRL, 10, 0))

        # Exercise SUT
        operacao = self.sistema_bancario.transferir(conta_fulano, conta_ciclano, Dinheiro(Moeda.BRL, 4, 0))

        # Result Verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SUCESSO)
        dinheiro_fulano = conta_fulano.calcular_saldo().obter_quantia()
        dinheiro_ciclano = conta_ciclano.calcular_saldo().obter_quantia()
        self.assertEqual(dinheiro_fulano.obter_quantia_em_escala(), 600)
        self.assertEqual(dinheiro_ciclano.obter_quantia_em_escala(), 400)
        # Fixture Teardown

    def test_transferir_saldo_insuficiente(self):
        # Implicit Fixture Setup
        # Delegated Fixture Setup
        conta_fulano, conta_ciclano = self.helper.criar_contas("Fulano", "Ciclano")
        # Inline Fixture Setup
        self.sistema_bancario.depositar(conta_fulano, Dinheiro(Moeda.BRL, 10, 0))

        # Exercise SUT
        operacao = self.sistema_bancario.transferir(conta_fulano, conta_ciclano, Dinheiro(Moeda.BRL, 11, 0))

        # Result Verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SALDO_INSUFICIENTE)
        # Fixture Teardown

    def test_transferir_bancos_moedas_diferentes(self):
        # Implicit Fixture Setup
        # Inline Fixture Setup
        banco_br = self.sistema_bancario.criar_banco("BancoBrasil", Moeda.BRL).criar_agencia("Sede")
        banco_eua = self.sistema_bancario.criar_banco("BancoEUA", Moeda.USD).criar_agencia("Sede")
        conta_br = banco_br.criar_conta("Joao")
        conta_eua = banco_eua.criar_conta("John")
        self.sistema_bancario.depositar(conta_br, Dinheiro(Moeda.BRL, 10, 0))

        # Exercise SUT
        operacao = self.sistema_bancario.transferir(conta_br, conta_eua, Dinheiro(Moeda.BRL, 3, 0))

        # Result Verification
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.MOEDA_INVALIDA)
        # Fixture Teardown


if __name__ == '__main__':
    unittest.main()


