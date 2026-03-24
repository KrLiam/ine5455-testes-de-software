
import unittest
import datetime

class Teste(unittest.TestCase):
    def setUp(self):
        ...
    
    def test_date_criacao(self):
        # Fixture Setup
        # Exercise SUT
        d = datetime.date(2026, 3, 17)
        # Result Verification
        self.assertEqual(d.year, 2026)
        self.assertEqual(d.month, 3)
        self.assertEqual(d.day, 17)
        # Fixture Teardown
    
    def test_date_criacao_invalida_dia_neg(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2026, 3, -1)
        # Result Verification
        # Fixture Teardown

    def test_date_criacao_invalida_mes_neg(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2026, -1, 17)
        # Result Verification
        # Fixture Teardown

    def test_date_criacao_invalida_ano_neg(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(-1, 3, 17)
        # Result Verification
        # Fixture Teardown

    def test_date_criacao_invalida_dia_32(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2026, 3, 32)
        # Result Verification
        # Fixture Teardown

    def test_date_criacao_invalida_mes_13(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2026, 13, 1)
        # Result Verification
        # Fixture Teardown

    def test_date_criacao_invalida_ano_nao_bissexto(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2026, 2, 29)
        # Result Verification
        # Fixture Teardown

    def test_date_criacao_invalida_ano_bissexto_2100(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.date(2100, 2, 29)
        # Result Verification
        # Fixture Teardown

    def test_date_toordinal(self):
        # Fixture Setup
        dia = datetime.date(2026, 3, 17)
        # Exercise SUT
        dia_ordinal = dia.toordinal()
        # Result Verification
        hoje_em_ordinal = 739692
        self.assertEqual(dia_ordinal, hoje_em_ordinal)
        # Fixture Teardown

    def test_date_weekday_tuesday(self):
        # Fixture Setup
        dia = datetime.date(2026, 3, 17)
        # Exercise SUT
        dia_da_semana = dia.weekday()
        # Result Verification
        terca = 1
        self.assertEqual(dia_da_semana, terca)
        # Fixture Teardown
    
    def test_date_replace(self):
        # Fixture Setup
        dia = datetime.date(2026, 3, 17)
        # Exercise SUT
        dia_em_abril = dia.replace(month=4)
        # Result Verification
        self.assertEqual(dia_em_abril.year, 2026)
        self.assertEqual(dia_em_abril.month, 4)
        self.assertEqual(dia_em_abril.day, 17)
        # Fixture Teardown

    def test_date_replace_invalido_mes_sem_dia_31(self):
        # Fixture Setup
        dia = datetime.date(2026, 3, 31)
        # Exercise SUT
        with self.assertRaises(ValueError):
            dia.replace(month=4)
        # Result Verification
        # Fixture Teardown


    def test_time_criacao(self):
        # Fixture Setup
        # Exercise SUT
        t = datetime.time(11, 50, 32)
        # Result Verification
        self.assertEqual(t.hour, 11)
        self.assertEqual(t.minute, 50)
        self.assertEqual(t.second, 32)
        # Fixture Teardown
    
    def test_time_criacao_invalida_hora_24(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.time(24, 50)
        # Result Verification
        # Fixture Teardown

    def test_time_criacao_invalida_minuto_60(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.time(11, 60)
        # Result Verification
        # Fixture Teardown

    def test_time_criacao_invalida_hora_neg(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.time(-1, 50)
        # Result Verification
        # Fixture Teardown

    def test_time_criacao_invalida_minuto_neg(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            datetime.time(11, -1)
        # Result Verification
        # Fixture Teardown


    def test_datetime_criacao(self):
        # Fixture Setup
        # Exercise SUT
        dt = datetime.datetime(2026, 3, 17, 9, 42)
        # Result Verification
        self.assertEqual(dt.year, 2026)
        self.assertEqual(dt.month, 3)
        self.assertEqual(dt.day, 17)
        self.assertEqual(dt.hour, 9)
        self.assertEqual(dt.minute, 42)
        # Fixture Teardown
    

    def test_timedelta_criacao_horas(self):
        # Fixture Setup
        # Exercise SUT
        delta = datetime.timedelta(hours=2)
        # Result Verification
        segs_em_2_horas = 2 * 60 * 60
        self.assertEqual(delta.seconds, segs_em_2_horas)
        # Fixture Teardown
    
    def test_timedelta_criacao_dias(self):
        # Fixture Setup
        # Exercise SUT
        delta = datetime.timedelta(days=1)
        # Result Verification
        self.assertEqual(delta.days, 1)
        self.assertEqual(delta.seconds, 0)
        segs_em_1_dia = 24 * (1 * 60 * 60)
        self.assertEqual(delta.total_seconds(), segs_em_1_dia)
        # Fixture Teardown

    def test_timedelta_diferenca_positiva_horas(self):
        # Fixture Setup
        inicio = datetime.datetime(2026, 3, 17, 8, 20)
        fim = datetime.datetime(2026, 3, 17, 11, 50)
        # Exercise SUT
        delta = fim - inicio
        # Result Verification
        aula_segs = (3*60 + 30) * 60
        self.assertEqual(delta.total_seconds(), aula_segs)
        # Fixture Teardown

    def test_timedelta_diferenca_positiva_dias(self):
        # Fixture Setup
        inicio = datetime.datetime(2026, 3, 17)
        fim = datetime.datetime(2026, 3, 19)
        # Exercise SUT
        delta = fim - inicio
        # Result Verification
        self.assertEqual(delta.days, 2)
        # Fixture Teardown
    
    def test_timedelta_virada_de_dia(self):
        # Fixture Setup
        dia = datetime.datetime(2026, 3, 17, 23, 40)
        delta = datetime.timedelta(hours=1)
        # Exercise SUT
        proxima_hora = dia + delta
        # Result Verification
        self.assertEqual(proxima_hora.year, 2026)
        self.assertEqual(proxima_hora.month, 3)
        self.assertEqual(proxima_hora.day, 18)
        self.assertEqual(proxima_hora.hour, 0)
        self.assertEqual(proxima_hora.minute, 40)
        # Fixture Teardown
        ...
    
    def test_timedelta_virada_de_mes(self):
        # Fixture Setup
        dia = datetime.date(2026, 3, 31)
        delta = datetime.timedelta(days=1)
        # Exercise SUT
        proximo_dia = dia + delta
        # Result Verification
        self.assertEqual(proximo_dia.year, 2026)
        self.assertEqual(proximo_dia.month, 4)
        self.assertEqual(proximo_dia.day, 1)
        # Fixture Teardown
        ...
    
    def test_timedelta_virada_de_ano(self):
        # Fixture Setup
        dia = datetime.date(2026, 12, 31)
        delta = datetime.timedelta(days=1)
        # Exercise SUT
        proximo_dia = dia + delta
        # Result Verification
        self.assertEqual(proximo_dia.year, 2027)
        self.assertEqual(proximo_dia.month, 1)
        self.assertEqual(proximo_dia.day, 1)
        # Fixture Teardown
        ...


if __name__ == '__main__':
    unittest.main()