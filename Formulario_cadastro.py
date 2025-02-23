import flet as ft

def main(page: ft.Page):
    formulario_cadastro = ft.Text(value='Formulario de cadastro', size= 30, color='green')
    nome_usuario = ft.TextField(label='Digite seu Nome', width= 500, bgcolor='blue')
    sobrenome_usuario = ft.TextField(label='Digite seu sobrenome', width= 500, bgcolor='blue')
    email_usuario = ft.TextField(label='Digite seu email', width= 500, bgcolor='blue')
    # campo_senha = ft.TextField(label='Digite uma senha', password=True, can_reveal_password=True, width=500)

    def cadastrar(e):
        dlg = ft.AlertDialog(
            title=ft.Text('Usuario cadastrado'),
            on_dismiss=lambda e:page.add(ft.Text('Cadastrado'))
        )
        page.open(dlg)
    botao_cadastrar = ft.ElevatedButton(text='Cadastrar', width= 500, on_click=cadastrar)
    
    
    
    page.controls.append(formulario_cadastro)
    page.controls.append(nome_usuario)
    page.controls.append(sobrenome_usuario)
    page.controls.append(email_usuario)
    # page.controls.append(campo_senha)
    page.controls.append(botao_cadastrar)











    page.update()
ft.app(target =main)