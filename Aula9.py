# para instalar o ambiente virtual:

# primeiro utilizar o comando python3 -m venv venv
# segundo comando será source venv/bin/activate
# terceiro comando o pip install flet --break-system-packages
# quarto comando pip freeze > requirements.txt




import flet as ft

def main(page: ft.page):
    ola = ft.Text(value='ola, mundo!' ,size = 30,color="green")
    campo_usuario = ft.TextField(label="Usuário:", width= 300)
    campo_senha = ft.TextField(label="Senha" ,password=True, width= 300)
    page.controls.append(ola)
    page.controls.append(campo_usuario)
    page.controls.append(campo_senha)

    def logar(e):
        usuario_sistema = 'ravel'
        senha_sistema = '123'
        usuario_digitada = campo_usuario.value
        senha_digitada = campo_senha.value

        if usuario_sistema != usuario_digitada or senha_sistema != senha_digitada:
            dlg = ft.AlertDialog(
                title=ft.Text("Usuario ou senha incorreta!"),
        )
        
        elif usuario_sistema ==usuario_digitada and senha_sistema == senha_digitada:
            dlg = ft.AlertDialog(
                title=ft.Text("Logado com sucesso!"),
                on_dismiss=lambda e:page.add(ft.Text("Logado"))
            )
        page.open(dlg)


    botao_logar = ft.ElevatedButton(text="Logar", on_click=logar)
    page.controls.append(botao_logar)
    def mostrar_senha(e):
        if campo_senha.password == True:
            campo_senha.password = False
            page.update()
        else:
            campo_senha.password = True
            page.update()
    botao_mostrar_senha = ft.ElevatedButton(text='MOSTRAR/OCULTAR SENHA', on_click=mostrar_senha)
    page.controls.append(botao_mostrar_senha)


    page.update()


ft.app(target=main)