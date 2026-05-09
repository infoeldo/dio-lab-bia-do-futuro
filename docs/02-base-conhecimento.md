# Base de Conhecimento

## Dados Utilizados

O agente utiliza conteúdos educativos, fundamentos financeiros e informações do mercado brasileiro para ajudar os usuários a aprenderem sobre investimentos de forma simples e segura.

| Arquivo                       | Formato | Utilização no Agente                                                   |
| ----------------------------- | ------- | ---------------------------------------------------------------------- |
| `ativos_b3.json`              | JSON    | Informações básicas sobre ações, FIIs e ETFs da bolsa brasileira       |
| `glossario_financeiro.json`   | JSON    | Explicação de termos técnicos de investimentos em linguagem simples    |
| `perfil_investidor.json`      | JSON    | Identificação do perfil do usuário (conservador, moderado ou arrojado) |
| `fundamentos_empresas.csv`    | CSV     | Dados fundamentalistas como P/L, Dividend Yield e setor das empresas   |
| `educacao_financeira.json`    | JSON    | Conteúdo educativo sobre investimentos, riscos e diversificação        |
| `faq_investimentos.json`      | JSON    | Respostas para dúvidas frequentes de investidores iniciantes           |
| `simulacoes_investimento.csv` | CSV     | Exemplos educativos de crescimento patrimonial e aportes               |
| `historico_interacoes.json`   | JSON    | Contextualização da evolução e aprendizado do usuário                  |


> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados foram adaptados para focar exclusivamente em educação financeira e investimentos na bolsa brasileira. Foram adicionados:

Glossário simplificado para iniciantes;
Classificação de perfil de investidor;
Dados básicos de ações, FIIs e ETFs;
Conteúdos educativos sobre risco, dividendos e longo prazo;
Simulações educativas de aportes mensais;
Perguntas frequentes de investidores iniciantes;
Explicações simplificadas de indicadores financeiros.

Os dados técnicos foram transformados em linguagem acessível para melhorar a experiência de usuários iniciantes.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos JSON e CSV são carregados no início da sessão do agente e organizados em memória para consulta rápida. Informações financeiras atualizadas podem ser complementadas através de APIs externas de mercado.

O agente também mantém um histórico leve de interações para adaptar o nível de explicação conforme a evolução do usuário.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados principais de comportamento, regras de segurança e personalidade ficam no system prompt.

Os conteúdos financeiros, fundamentos de ativos e materiais educativos são consultados dinamicamente conforme a intenção do usuário. Isso reduz alucinações e melhora a precisão das respostas.

O agente utiliza:

Contexto dinâmico baseado na pergunta;
Perfil do investidor;
Histórico recente de aprendizado;
Base educativa sobre investimentos;
Dados financeiros estruturados.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Perfil do Usuário:
- Nome: Carlos
- Nível de conhecimento: Iniciante
- Perfil de investidor: Moderado
- Objetivo: Investimento de longo prazo
- Interesse atual: Dividendos

Contexto Financeiro:
- Ação consultada: ITSA4
- Setor: Financeiro
- Dividend Yield: 7,2%
- Tipo de ativo: Ação pagadora de dividendos

Conteúdo Educativo Relacionado:
- O que são dividendos
- Diferença entre ações e FIIs
- Importância da diversificação
- Riscos da renda variável

Regras do Agente:
- Não prometer rentabilidade
- Explicar riscos antes de sugestões
- Utilizar linguagem acessível
- Respeitar o ritmo de aprendizado do usuário
...
```
