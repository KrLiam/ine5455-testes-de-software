from behave.api.pending_step import StepNotImplementedError
from behave import given, when, then
from mercado_leilao import MercadoLeilao


@given(u'o nome de usuario de {nome_usuario}')
def step_impl(context, nome_usuario):
    context.nome_usuario = nome_usuario

@given(u'o cpf {cpf_usuario}')
def step_impl(context, cpf_usuario):
    context.cpf_usuario = cpf_usuario

@given(u'e o endereco {endereco_usuario}')
def step_impl(context, endereco_usuario):
    context.endereco_usuario = endereco_usuario


@given(u'e o e-mail {email_usuario}')
def step_impl(context, email_usuario):
    context.email_usuario = email_usuario


@when(u'cadastra o usuario')
def step_impl(context):
    context.mercado = MercadoLeilao()
    try:
        context.mercado.cadastra_usuario(
            context.nome_usuario,
            context.endereco_usuario,
            context.email_usuario,
            context.cpf_usuario
        )
        context.mensagem = "Usuario cadastrado com sucesso"
    except Exception as e:
        context.mensagem = str(e)


@then(u'o sistema retorna a mensagem {mensagem}')
def step_impl(context, mensagem):
    assert context.mensagem == mensagem
