Feature: SC_AAA_BBB Creation
\
  Background:
    Given O contratante é AAA Consultoria Empresarial Ltda.
    And A contratada é BBB Tecnologia Ltda.

  Scenario: Create the SC_AAA_BBB contract
    Given A data de criação é 01/06/2026
    And O valor é 23425
    When O contrato é criado
    Then O contrato é criado com sucesso
    And O contratante é AAA Consultoria Empresarial Ltda.
    And A contratada é BBB Tecnologia Ltda.
    And O contrato não está ativo

  Scenario: Activate the SC_AAA_BBB contract
    Given A data de criação é 01/06/2026
    And O valor é 23425
    And O contrato é criado
    When 15 dias sepassaram desde a data de criação
    Then O contrato está ativo
