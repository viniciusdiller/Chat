#Título: Hashzap   
#Botao: Iniciar Chat 
# Abrir poup up/modal 
    # Título : Bem vindo ao Hashzap 
    # Chatbox pra escrever o nome 
    # Botao entrar no chat   
        #Sumir com o tíotulo e o botao
        #Fechar poupup  
        #Criar o chat
            #Campo de texto
            #Botao Enviar
            #Vai aparecver a mensagem no chat com o nome do usuario  

#Flet (Framework em python para trabalhar com apilcaçoes em site, aplicativos e programas)

#importar o flet
import flet as ft


#criar a função princeipal do seu sistema
def main(pagina):
    #criar algo
    #criar o título
    titulo = ft.Text("Hashzap")

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) # cria o tunel de comunicação

    titulo_janela = ft.Text("Bem-vindo ao Hashzap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat") #Rotulo
    

    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"
        #enviar a mensagem no chat:
            #Usuario:mensagem

        #enviar uma mensagem
        pagina.pubsub.send_all(texto) #envia a mensagem no tunel

        #limpar o campo de mensagem
        texto_mensagem.value = ""
        pagina.update()


    texto_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem) #apertar enter vai enviar a mensagem
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem) #envia a mensagem


    chat = ft.Column()


    #COLUNAS E LINHAS
    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])


    def entrar_chat(evento):
        #tirar titulo
        pagina.remove(titulo)   
        # tirar o botao_iniciar
        pagina.remove(botao_iniciar)   
        # fechar a janela criar o chat    
        janela.open = False
        #criar o chat
        pagina.add(chat)
        #adicionar linha de mensagem
        pagina.add(linha_mensagem)
        # criar um campo de texto de enviar mensagem
        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat" #COMO SE FOSSE O SCANF DE "C"
        pagina.pubsub.send_all(texto_entrou_chat)
        
        pagina.update()


    botao_entrar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_poupup(evento):#TODA FUNÇÃO DENTRO DE FUNÇÃO TEM QUE RECEBER UM EVENTO
        pagina.dialog = janela
        janela.open = True
        pagina.update()#isso é obrigatório para atualizar a página (com se fosse um F5 automático)
       

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_poupup)
   
    #colocar na pagina
    # adicionar o titulo na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)


#executar o seu sistema
ft.app(main, view=ft.WEB_BROWSER)
