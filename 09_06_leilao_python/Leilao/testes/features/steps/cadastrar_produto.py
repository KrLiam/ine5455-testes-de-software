from behave import given, when, then
from mercado_leilao import MercadoLeilao

@given(u'o cadastro do usuario Ernani Cesar foi realizado')
def step_impl(context):
    context.mercado = MercadoLeilao()
    context.mercado.cadastra_usuario("Ernani Cesar", "UFSC", "ernani@posgrad.ufsc.br", "055.761.919-00")

@given(u'o nome do produto {nome}')
def step_impl(context, nome):
    context.nome_produto = nome

@given(u'a descricao do produto {descricao}')
def step_impl(context, descricao):
    context.descricao_produto = descricao

@given(u'e o lance {lance}')
def step_impl(context, lance):
    context.lance_produto = float(lance)

@given(u'e o cpf do leiloador {cpf}')
def step_impl(context, cpf):
    context.cpf_leiloador = cpf

@given(u'{nome} {descricao} ja foi cadastrado')
def step_impl(context, nome, descricao):
    context.mercado.cadastra_produto(
        nome,
        descricao,
        100.0,
        "055.761.919-00",
        "01/01/2050"
    )

@when(u'cadastrar o produto')
def step_impl(context):
    try:
        context.mercado.cadastra_produto(
            context.nome_produto,
            context.descricao_produto,
            context.lance_produto,
            context.cpf_leiloador,
            "01/01/2050"
        )
        context.mensagem = "sucesso"
    except Exception as e:
        context.mensagem = str(e)

@then(u'o sistema cadastra com sucesso')
def step_impl(context):
    assert context.mensagem == "sucesso"

@then(u'o sistema mostra a mensagem {mensagem}')
def step_impl(context, mensagem):
    assert context.mensagem == mensagem
