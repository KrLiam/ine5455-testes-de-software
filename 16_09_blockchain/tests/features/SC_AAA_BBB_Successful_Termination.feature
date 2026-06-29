Feature: SC_AAA_BBB Successful Termination

  Background:
    Given O contratante é AAA Consultoria Empresarial Ltda.
    And A contratada é BBB Tecnologia Ltda.

  Scenario: Successful termination #1 of SC_AAA_BBB contract
    Given A data de criação é 01/06/2026
    And O valor é 23425
    And O contrato é criado
    And O contrato está ativo
    When A contratada presta os serviços contratados
    And A contratante paga 50% da assinatura no dia 01/06/2026
    And A contratante paga os 50% restantes no dia 16/06/2026
    Then O contrato é terminado com sucesso
    And O pacote de 20 horas mensais é disposto
