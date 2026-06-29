Feature: SC_AAA_BBB Unsuccessful Termination

  Background:
    Given O contratante é AAA Consultoria Empresarial Ltda.
    And A contratada é BBB Tecnologia Ltda.
    And A data de criação é 01/06/2026
    And O valor é 23425
    And O contrato é criado
    And O contrato está ativo

  Scenario: Unsuccessful termination #1 of SC_AAA_BBB contract
    Given O contrato está em vigor
    When A contratada não presta os serviços contratados
    Then O contrato é terminado sem sucesso
    And Todas as obrigações são encerradas

  Scenario: Unsuccessful termination #2 of SC_AAA_BBB contract
    Given O contrato está em vigor
    When A contratada não envia fatura e relatório das horas prestadas
    Then O contrato é terminado sem sucesso
    And Todas as obrigações são encerradas

  Scenario: Unsuccessful termination #3 of SC_AAA_BBB contract
    Given O contrato está em vigor
    When A contratante não paga 50% da assinatura no dia 01/06/2026
    Then O contrato é terminado sem sucesso
    And Todas as obrigações são encerradas

  Scenario: Unsuccessful termination #4 of SC_AAA_BBB contract
    Given O contrato está em vigor
    When A contratante não paga os 50% restantes no dia 16/06/2026
    Then O contrato é terminado sem sucesso
    And Todas as obrigações são encerradas