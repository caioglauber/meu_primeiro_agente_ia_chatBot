#CRIANDO MEU PRIMEIRO AGENTE DE IA



import os
from langchain_groq import ChatGroq               #importa do groq o chat
from langchain.prompts import ChatPromptTemplate #importa do langchain o prompt template

# API KEY segura via Secrets
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")

chat = ChatGroq(model = 'llama-3.3-70b-versatile') #modelo de minhan llm

#minha função
def resposta_bot(mensagens):
  mensagens_modelo = [
      ('system','Você é uma assistente amigavel chamado AI_AGENT')
      ]
  mensagens_modelo += mensagens

  template = ChatPromptTemplate.from_messages(mensagens_modelo)
  
  chain = template | chat
  return chain.invoke({}).content #invoque será passado vazio, porém ja esta a ultima mensagem

#Inicio do programa

print('Bem vindo ao meu FirstAgentAi')

mensagens = []

while True:
  pergunta = input('\nO que gostaria de saber?(Digite x para sair) ')
  if pergunta.lower() == 'x':
    break
 
  mensagens.append(('user', pergunta)) #tupla abre e fecha com parentese, igual a uma lista porém imutável
  resposta = resposta_bot(mensagens)
  mensagens.append(('assistant', resposta))
  print(f'Bot:{resposta}')

print('\nMuito Obrigado por usa o FirstAgentAi')
print(mensagens)

