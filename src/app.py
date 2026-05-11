import json
import pandas as pd
import requests
import streamlit as st  

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO ='gpt-oss:20b'



#CVSs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv') 
#JSONs  
with open('data/perfil_investidor.json') as f:
    perfil = json.load(f)
with open('data/produtos_financeiros.json') as f:
    produtos = json.load(f) 

# ============= MONTAR CONTEXTO ===================
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, {perfil['profissao']}, renda mensal de R${perfil['renda_mensal']}, perfil de investidor {perfil['perfil_investidor']}.
OBJETIVO: {perfil['objetivo_principal']}.
PATRIMÔNIO: R${perfil['patrimonio_total']} |RESERVA DE EMERGÊNCIA: R${perfil['reserva_emergencia_atual']}.

TRANSAÇÕES RECENTES:
{transacoes.tail(5).to_string(index=False)} 
ATENDIMENTOS ANTERIORES:
{historico.tail(5).to_string(index=False)}
PRODUTOS FINANCEIROS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)} 
"""

# SYSTEM PROMPT
system_prompt = f""" Você é um assistente financeiro virtual especializado em análise de perfil de investidor e recomendação de produtos financeiros.
Sua função é analisar o perfil do cliente, suas transações recentes, histórico de atendimentos e os produtos financeiros disponíveis para fornecer recomendações personalizadas de investimento.
Use as seguintes informações para entender o contexto do cliente:           
{contexto}
Com base nesse contexto, responda às seguintes perguntas:                   
1. Qual é o perfil de investidor do cliente?
2. O cliente tem uma reserva de emergência adequada para sua situação financeira?
3. Quais produtos financeiros seriam mais adequados para o cliente, considerando seu perfil e objetivos
4. O cliente tem alguma transação recente que indique um comportamento financeiro específico?
5. O histórico de atendimentos do cliente revela alguma preocupação ou necessidade específica que deve ser considerada ao fazer recomendações?
Forneça respostas detalhadas e fundamentadas para cada pergunta, utilizando as informações disponíveis no contexto  e os dados fornecidos. 
Seja claro e objetivo em suas recomendações, levando em consideração o perfil e os objetivos do cliente. 
"""
def perguntar(msg):
    prompt = f"""
    CONTEXTO DO CLIENTE:
    {contexto}
    PERGUNTA: {msg}
    """    

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": True})                                                                            
    resposta = ""
    for line in r.iter_lines():
        if line:
            data = line.decode('utf-8')
            if data.startswith('data: '):
                data = data[6:]
            try:
                json_data = json.loads(data)
                if 'response' in json_data:
                    resposta += json_data['response']
                if json_data.get('done', False):
                    break
            except json.JSONDecodeError:
                continue
    return resposta
# INTERFACE
st.title("Assistente Financeiro Virtual")
if pergunta := st.chat_input("Faça uma pergunta sobre o perfil de investidor ou recomendações financeiras:"):
    st.chat_message('user').write(pergunta)
    with st.chat_message('assistant'):
        st.write("Analisando...")
        resposta = perguntar(pergunta)
        st.write(resposta)                         
