# MVP — Minimum Viable Product

## 1. Visão Geral

O **MVP (Minimum Viable Product)** do **AI Customer Recovery** representa a primeira versão funcional da plataforma.

O objetivo do MVP não é construir um sistema completo de CRM ou uma plataforma de automação extremamente complexa.

O objetivo é validar uma hipótese simples:

> **Empresas perdem oportunidades porque muitos leads e clientes deixam de receber acompanhamento adequado após uma interação inicial.**

O MVP deverá demonstrar que é possível:

```text
Identificar oportunidade
        ↓
Detectar falta de resposta
        ↓
Aplicar uma regra
        ↓
Aguardar período
        ↓
Gerar follow-up
        ↓
Enviar mensagem
        ↓
Detectar resposta
        ↓
Interromper automação
        ↓
Registrar resultado
```

---

# 2. Objetivo do MVP

O MVP deverá criar uma versão pequena, funcional e testável do produto.

Os principais objetivos são:

* validar o problema;
* validar o fluxo de recuperação;
* testar automações;
* testar geração de mensagens com IA;
* testar integração com comunicação;
* medir respostas;
* identificar problemas reais;
* obter feedback de empresas;
* validar disposição para utilizar o produto.

---

# 3. Hipótese Principal

A hipótese inicial do produto é:

> Empresas possuem leads ou clientes que demonstraram interesse, mas acabam não sendo acompanhados adequadamente por falta de tempo, organização ou processos de follow-up.

O MVP deverá permitir testar essa hipótese na prática.

---

# 4. Problema que o MVP Resolve

O MVP será focado principalmente neste cenário:

```text
Empresa recebe lead
       ↓
Lead demonstra interesse
       ↓
Empresa conversa com lead
       ↓
Lead deixa de responder
       ↓
Empresa não realiza novo contato
       ↓
Oportunidade é perdida
```

O sistema deverá transformar esse processo em:

```text
Empresa recebe lead
       ↓
Sistema registra interação
       ↓
Lead deixa de responder
       ↓
Sistema identifica oportunidade
       ↓
Aguarda período configurado
       ↓
IA gera follow-up
       ↓
Mensagem é enviada
       ↓
Cliente responde?
    ↙       ↘
  SIM       NÃO
   ↓          ↓
Interrompe   Novo follow-up
automação       ↓
             Limite?
              ↙ ↘
            SIM NÃO
             ↓   ↓
          Encerra Continua
```

---

# 5. Escopo do MVP

O MVP deverá conter:

```text
┌───────────────────────────────────────┐
│                 MVP                   │
├───────────────────────────────────────┤
│                                       │
│  Empresa                              │
│      ↓                                │
│  Usuários                             │
│      ↓                                │
│  Clientes / Leads                     │
│      ↓                                │
│  Conversas                            │
│      ↓                                │
│  Mensagens                            │
│      ↓                                │
│  Automação                            │
│      ↓                                │
│  Follow-up                            │
│      ↓                                │
│  IA                                   │
│      ↓                                │
│  Canal de comunicação                 │
│      ↓                                │
│  Resposta                             │
│      ↓                                │
│  Histórico + Métricas                 │
│                                       │
└───────────────────────────────────────┘
```

---

# 6. Funcionalidades do MVP

## 6.1 Cadastro da Empresa

O usuário deverá conseguir criar uma conta para sua empresa.

Informações mínimas:

* nome da empresa;
* e-mail;
* telefone;
* informações básicas.

Fluxo:

```text
Cadastro
   ↓
Validação
   ↓
Empresa criada
   ↓
Administrador criado
   ↓
Dashboard
```

---

# 7. Autenticação

O MVP deverá possuir autenticação.

Funcionalidades:

* login;
* logout;
* sessão autenticada;
* recuperação de acesso, se implementada;
* proteção das rotas privadas.

Fluxo:

```text
E-mail + senha
      ↓
Validação
      ↓
Credenciais corretas?
    ↙       ↘
  SIM       NÃO
   ↓         ↓
Acesso     Erro
```

---

# 8. Usuários

O MVP deverá permitir pelo menos dois níveis de usuário:

```text
Administrador
Atendente
```

## Administrador

Poderá:

* gerenciar empresa;
* gerenciar usuários;
* gerenciar clientes;
* configurar automações;
* visualizar métricas;
* visualizar histórico.

## Atendente

Poderá:

* visualizar clientes;
* visualizar conversas;
* atender clientes;
* assumir conversas.

---

# 9. Clientes e Leads

O MVP deverá permitir cadastrar clientes e leads.

Dados básicos:

```text
Cliente
├── ID
├── Nome
├── Telefone
├── E-mail
├── Status
├── Tags
├── Origem
├── Criado em
└── Último contato
```

---

# 10. Status do Lead

O MVP poderá utilizar estados simples:

```text
NOVO
   ↓
EM_ATENDIMENTO
   ↓
INTERESSADO
   ↓
SEM_RESPOSTA
   ↓
FOLLOW_UP
   ↓
CONVERTIDO
```

Também deverão existir estados para:

```text
PERDIDO
ENCERRADO
```

---

# 11. Conversas

O MVP deverá armazenar o histórico das conversas.

Exemplo:

```text
Cliente
  │
  ├── Mensagem recebida
  │
  ├── Mensagem enviada
  │
  ├── Mensagem recebida
  │
  └── Follow-up
```

Cada mensagem deverá possuir informações como:

* conteúdo;
* data/hora;
* origem;
* destino;
* canal;
* status.

---

# 12. Canal Inicial

O MVP deverá começar com **um único canal de comunicação**.

A arquitetura deverá ser criada de forma desacoplada para permitir outros canais posteriormente.

Exemplo:

```text
             AI Customer Recovery
                      │
                      ▼
              Message Service
                      │
              ┌───────┴───────┐
              ▼               ▼
          Canal 1          Futuro
                              │
                         E-mail / SMS
```

O primeiro canal deverá ser escolhido de acordo com a viabilidade técnica, custo e validação comercial.

---

# 13. Detecção de Falta de Resposta

O sistema deverá identificar quando um lead está sem responder.

Exemplo:

```text
Última mensagem:
10:00

Tempo configurado:
24 horas

         ↓

10:00 do dia seguinte

         ↓

Cliente não respondeu

         ↓

Lead elegível para follow-up
```

---

# 14. Automação Principal

A primeira automação será:

> **Recuperação de lead sem resposta.**

Fluxo:

```text
LEAD
 │
 ▼
Interação
 │
 ▼
Sem resposta
 │
 ▼
Aguardar
 │
 ▼
Verificar condições
 │
 ▼
Gerar mensagem
 │
 ▼
Enviar
 │
 ▼
Aguardar resposta
 │
 ├───────────────┐
 ▼               ▼
Responde       Não responde
 │               │
 ▼               ▼
Encerrar       Próximo follow-up
```

---

# 15. Configuração da Automação

O administrador deverá conseguir configurar pelo menos:

* nome da automação;
* tempo de espera;
* número máximo de tentativas;
* canal;
* objetivo;
* ativação/desativação.

Exemplo:

```text
Automação:
Recuperação de Lead

Aguardar:
24 horas

Máximo:
2 follow-ups

Canal:
Canal inicial

Status:
Ativa
```

---

# 16. Gatilho

O primeiro gatilho será:

```text
LEAD_SEM_RESPOSTA
```

Exemplo:

```text
Última interação
       ↓
Passou período configurado
       ↓
Nenhuma resposta
       ↓
Gatilho ativado
```

---

# 17. Condições

Antes de executar o follow-up, o sistema deverá verificar condições.

Exemplo:

```text
IF

lead está ativo

AND

não respondeu

AND

não está bloqueado

AND

não existe atendimento humano ativo

AND

limite de tentativas não foi atingido

THEN

executar follow-up
```

---

# 18. Follow-up

Um follow-up representa uma tentativa de reativar a conversa.

Exemplo:

```text
Follow-up #1
      ↓
Mensagem enviada
      ↓
Aguardar
      ↓
Cliente respondeu?
    ↙       ↘
  SIM       NÃO
   ↓          ↓
Encerra     Follow-up #2
```

---

# 19. Limite de Tentativas

O sistema deverá impedir que a automação envie mensagens indefinidamente.

Exemplo:

```text
Máximo = 2

Follow-up #1
      ↓
Follow-up #2
      ↓
Fim
```

---

# 20. Intervalo

O sistema deverá respeitar o intervalo definido.

Exemplo:

```text
Dia 1
Cliente não responde
      ↓
24 horas
      ↓
Follow-up #1
      ↓
48 horas
      ↓
Follow-up #2
```

---

# 21. Geração de Mensagem com IA

A IA deverá gerar ou adaptar a mensagem de follow-up.

Contexto mínimo:

```text
Nome do cliente
Última interação
Interesse
Objetivo do follow-up
Tom da mensagem
```

Exemplo de entrada conceitual:

```text
Cliente:
Ana

Interesse:
Serviço X

Última interação:
"Vou analisar e te retorno."

Objetivo:
Retomar conversa
```

A IA deverá produzir uma mensagem contextualizada.

---

# 22. Controle da IA

A IA não deverá possuir liberdade ilimitada.

A estrutura será:

```text
                 DADOS
                   │
                   ▼
              REGRAS
                   │
                   ▼
                  IA
                   │
                   ▼
              VALIDAÇÃO
                   │
                   ▼
                 ENVIO
```

A IA será responsável principalmente pela geração e interpretação de mensagens.

As regras de negócio permanecerão sob controle do sistema.

---

# 23. Proteção contra Informações Inventadas

A IA não deverá inventar:

* preços;
* descontos;
* horários;
* produtos;
* serviços;
* condições comerciais;
* informações pessoais;
* promessas da empresa.

Exemplo:

```text
Informação não existe
       ↓
IA não deve inventar
       ↓
Usar resposta segura
ou
Encaminhar para humano
```

---

# 24. Detecção de Resposta

Quando o cliente responder, o sistema deverá identificar a nova mensagem.

Fluxo:

```text
Follow-up enviado
       ↓
Cliente responde
       ↓
Sistema recebe evento
       ↓
Registra mensagem
       ↓
Identifica conversa
       ↓
Cancela follow-up pendente
```

---

# 25. Cancelamento Automático

Caso o cliente responda, a automação deverá ser interrompida conforme a regra configurada.

```text
Follow-up pendente
       ↓
Cliente responde
       ↓
Follow-up cancelado
       ↓
Conversa continua
```

---

# 26. Encaminhamento para Humano

Quando a situação exigir atendimento humano, o sistema deverá permitir encaminhamento.

Exemplo:

```text
Cliente responde
       ↓
IA analisa
       ↓
Necessita humano?
       ↓
SIM
       ↓
Atendente assume
       ↓
Automação interrompida
```

---

# 27. Histórico

O sistema deverá manter histórico das automações.

Exemplo:

```text
Lead #1024

10/09 — Lead criado
10/09 — Mensagem recebida
10/09 — Mensagem enviada
11/09 — Sem resposta
12/09 — Follow-up #1 enviado
12/09 — Cliente respondeu
12/09 — Automação encerrada
```

---

# 28. Dashboard

O MVP deverá possuir um dashboard simples.

Informações principais:

```text
┌────────────────────────────────────┐
│           DASHBOARD                │
├────────────────────────────────────┤
│                                    │
│ Leads            125               │
│ Follow-ups        87               │
│ Respostas         31               │
│ Recuperados       18               │
│                                    │
├────────────────────────────────────┤
│                                    │
│ Automações ativas: 3               │
│ Conversas abertas: 14              │
│                                    │
└────────────────────────────────────┘
```

Os valores acima são apenas exemplos.

---

# 29. Métricas do MVP

As primeiras métricas serão:

## Leads acompanhados

Quantidade de leads que passaram pelo sistema.

---

## Follow-ups enviados

Quantidade de mensagens automáticas enviadas.

---

## Respostas

Quantidade de leads que responderam após um follow-up.

---

## Leads recuperados

Quantidade de oportunidades que voltaram a interagir após uma automação.

---

## Taxa de resposta

Fórmula:

```text
Taxa de resposta =
respostas / follow-ups enviados × 100
```

---

## Taxa de recuperação

Fórmula:

```text
Taxa de recuperação =
leads recuperados / leads elegíveis × 100
```

Essas métricas deverão ser refinadas após os primeiros testes.

---

# 30. Página de Clientes

A página deverá permitir:

```text
┌─────────────────────────────────────────┐
│ Clientes                                │
├─────────────────────────────────────────┤
│ Buscar: [____________________]           │
│                                         │
│ Nome       Status        Último contato │
│ Ana        Interessado   2 dias         │
│ João       Sem resposta  3 dias         │
│ Maria      Convertido    1 dia          │
│                                         │
└─────────────────────────────────────────┘
```

---

# 31. Página de Conversas

A interface poderá seguir um modelo semelhante:

```text
┌──────────────┬──────────────────────────┐
│ Conversas    │ Conversa                │
├──────────────┤                          │
│ Ana          │ Ana                      │
│ João         │                          │
│ Maria        │ Cliente: Olá             │
│ Carlos       │ Empresa: Olá!            │
│              │ Cliente: Tenho interesse │
│              │                          │
│              │ [ Digite uma mensagem ]  │
└──────────────┴──────────────────────────┘
```

---

# 32. Página de Automações

Exemplo:

```text
┌────────────────────────────────────────┐
│ Automações                             │
├────────────────────────────────────────┤
│                                        │
│ Recuperação de Lead       [ATIVA]      │
│ Espera: 24h                            │
│ Máximo: 2 tentativas                   │
│                                        │
│ Recuperação de Orçamento  [INATIVA]    │
│                                        │
└────────────────────────────────────────┘
```

---

# 33. Criar Automação

A criação poderá seguir:

```text
1. Nome
      ↓
2. Gatilho
      ↓
3. Condições
      ↓
4. Tempo de espera
      ↓
5. Ação
      ↓
6. Limite
      ↓
7. Ativar
```

---

# 34. Estados da Automação

Uma automação poderá possuir:

```text
DRAFT
ACTIVE
PAUSED
DISABLED
```

Fluxo:

```text
DRAFT
  ↓
ACTIVE
  ↓
PAUSED
  ↓
ACTIVE

ou

ACTIVE
  ↓
DISABLED
```

---

# 35. Estados do Follow-up

```text
PENDING
   ↓
SCHEDULED
   ↓
SENDING
   ↓
SENT
   ↓
RESPONDED
```

Também:

```text
CANCELLED
FAILED
```

---

# 36. Scheduler

O MVP deverá possuir um mecanismo responsável por verificar ações programadas.

Fluxo:

```text
Scheduler
    │
    ▼
Busca follow-ups vencidos
    │
    ▼
Verifica condições
    │
    ▼
Executa ação
    │
    ▼
Registra resultado
```

---

# 37. Processamento Assíncrono

Quando necessário, processos poderão ser executados em background.

Exemplo:

```text
API
 │
 ▼
Fila
 │
 ├── Gerar IA
 │
 ├── Enviar mensagem
 │
 └── Processar evento
```

Isso evita que operações demoradas bloqueiem requisições da aplicação.

---

# 38. Multi-Tenancy

Mesmo no MVP, a estrutura deverá considerar múltiplas empresas.

Exemplo:

```text
                    SISTEMA
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      Empresa A    Empresa B    Empresa C
          │            │            │
       Dados A      Dados B      Dados C
```

Cada registro deverá estar associado à empresa correspondente.

---

# 39. Isolamento de Dados

Regra fundamental:

```text
Empresa A
   ↓
Pode acessar somente dados A

Empresa B
   ↓
Pode acessar somente dados B
```

Uma empresa nunca deverá conseguir consultar dados de outra empresa.

---

# 40. Segurança do MVP

O MVP deverá implementar pelo menos:

* autenticação;
* autorização;
* hash de senhas;
* validação de entrada;
* proteção de rotas;
* isolamento por empresa;
* variáveis de ambiente;
* proteção de credenciais;
* logs controlados.

---

# 41. Privacidade

O MVP deverá considerar princípios de proteção de dados.

Prioridades:

```text
Coletar somente o necessário
        ↓
Controlar acesso
        ↓
Proteger dados
        ↓
Controlar retenção
        ↓
Permitir tratamento de solicitações
```

A implementação definitiva das obrigações legais deverá ser validada conforme o contexto real de uso.

---

# 42. Banco de Dados Inicial

As principais entidades previstas são:

```text
Company
   │
   ├── User
   │
   ├── Customer
   │       │
   │       └── Conversation
   │                  │
   │                  └── Message
   │
   ├── Automation
   │       │
   │       └── FollowUp
   │
   └── Event
```

---

# 43. Entidades Principais

## Company

Representa uma empresa.

```text
Company
├── id
├── name
├── email
├── phone
├── status
├── created_at
└── updated_at
```

---

## User

Representa um usuário.

```text
User
├── id
├── company_id
├── name
├── email
├── password_hash
├── role
├── status
├── created_at
└── updated_at
```

---

## Customer

Representa um cliente ou lead.

```text
Customer
├── id
├── company_id
├── name
├── phone
├── email
├── status
├── source
├── created_at
└── updated_at
```

---

## Conversation

Representa uma conversa.

```text
Conversation
├── id
├── company_id
├── customer_id
├── channel
├── status
├── started_at
└── updated_at
```

---

## Message

Representa uma mensagem.

```text
Message
├── id
├── conversation_id
├── direction
├── content
├── status
├── external_id
└── created_at
```

---

## Automation

Representa uma automação.

```text
Automation
├── id
├── company_id
├── name
├── trigger
├── status
├── wait_time
├── max_attempts
├── created_at
└── updated_at
```

---

## FollowUp

Representa uma execução de follow-up.

```text
FollowUp
├── id
├── automation_id
├── customer_id
├── conversation_id
├── attempt
├── scheduled_at
├── sent_at
├── status
└── created_at
```

---

## Event

Representa um evento do sistema.

```text
Event
├── id
├── company_id
├── type
├── entity
├── entity_id
├── payload
└── created_at
```

---

# 44. API Inicial

Endpoints conceituais:

```text
POST   /auth/login
POST   /auth/logout

GET    /companies/me
PATCH  /companies/me

GET    /users
POST   /users
PATCH  /users/:id
DELETE /users/:id

GET    /customers
POST   /customers
GET    /customers/:id
PATCH  /customers/:id

GET    /conversations
GET    /conversations/:id
POST   /conversations/:id/messages

GET    /automations
POST   /automations
GET    /automations/:id
PATCH  /automations/:id
DELETE /automations/:id

GET    /follow-ups
GET    /events

GET    /dashboard
```

Os endpoints definitivos serão definidos durante a documentação da API.

---

# 45. Arquitetura Inicial

Arquitetura conceitual:

```text
                    FRONTEND
                       │
                       ▼
                  API / BACKEND
                       │
        ┌──────────────┼───────────────┐
        │              │               │
        ▼              ▼               ▼
     Database      Automation        IA
        │           Engine             │
        │              │               │
        │              ▼               │
        │          Scheduler            │
        │              │               │
        └──────────────┼───────────────┘
                       ▼
                Message Service
                       │
                       ▼
                Canal externo
```

---

# 46. Separação de Responsabilidades

O sistema deverá evitar colocar toda a lógica em um único componente.

Exemplo:

```text
Controller
    ↓
Service
    ↓
Business Rules
    ↓
Repository
    ↓
Database
```

Para IA:

```text
Automation
    ↓
AI Service
    ↓
LLM Provider
```

Para comunicação:

```text
Automation
    ↓
Message Service
    ↓
Channel Provider
```

---

# 47. Tecnologias Previstas

Uma implementação inicial poderá utilizar:

```text
Frontend
├── Next.js
├── React
└── TypeScript

Backend
├── Python
├── FastAPI
└── Pydantic

Database
└── PostgreSQL

Infraestrutura
├── Docker
└── Linux

IA
└── API de modelo de linguagem

Versionamento
└── Git + GitHub
```

As tecnologias poderão ser alteradas conforme decisões técnicas e necessidades do produto.

---

# 48. O que NÃO será desenvolvido no MVP

Para evitar aumento excessivo de escopo, ficam inicialmente fora:

```text
❌ CRM completo
❌ Aplicativo mobile nativo
❌ IA de voz
❌ Agentes totalmente autônomos
❌ RAG complexo
❌ Marketplace
❌ White-label completo
❌ Dezenas de integrações
❌ Sistema financeiro completo
❌ Contabilidade
❌ ERP
❌ Analytics avançado
❌ Campanhas massivas
❌ Programa de afiliados
❌ Automação para todos os segmentos
```

---

# 49. MVP versus Futuro

| Funcionalidade               | MVP | Futuro |
| ---------------------------- | --: | -----: |
| Empresas                     |   ✓ |      ✓ |
| Usuários                     |   ✓ |      ✓ |
| Clientes                     |   ✓ |      ✓ |
| Leads                        |   ✓ |      ✓ |
| Conversas                    |   ✓ |      ✓ |
| Follow-up                    |   ✓ |      ✓ |
| IA                           |   ✓ |      ✓ |
| Scheduler                    |   ✓ |      ✓ |
| Dashboard básico             |   ✓ |      ✓ |
| Métricas básicas             |   ✓ |      ✓ |
| Multi-tenancy                |   ✓ |      ✓ |
| Segurança                    |   ✓ |      ✓ |
| WhatsApp/outro canal inicial |   ✓ |      ✓ |
| E-mail                       |   — |      ✓ |
| SMS                          |   — |      ✓ |
| CRM completo                 |   — |      ✓ |
| IA de voz                    |   — |      ✓ |
| Agentes avançados            |   — |      ✓ |
| RAG                          |   — |      ✓ |
| Billing                      |   — |      ✓ |
| Marketplace                  |   — |      ✓ |
| White-label                  |   — |      ✓ |

---

# 50. Critérios de Aceitação do MVP

O MVP será considerado funcional quando o seguinte fluxo puder ser executado:

```text
1. Empresa criada
        ↓
2. Usuário autenticado
        ↓
3. Lead cadastrado
        ↓
4. Conversa registrada
        ↓
5. Lead deixa de responder
        ↓
6. Scheduler identifica condição
        ↓
7. Automação é acionada
        ↓
8. IA gera mensagem
        ↓
9. Mensagem passa pelas validações
        ↓
10. Mensagem é enviada
        ↓
11. Cliente responde
        ↓
12. Sistema registra resposta
        ↓
13. Follow-up pendente é cancelado
        ↓
14. Automação é encerrada
        ↓
15. Resultado aparece no histórico
```

---

# 51. Cenário de Teste Principal

## Cenário

Um lead demonstra interesse, deixa de responder e depois responde ao follow-up.

### Dados

```text
Lead:
Ana

Status:
INTERESSADO

Última interação:
Hoje às 10:00

Regra:
Aguardar 24 horas

Máximo:
2 follow-ups
```

### Execução

```text
Dia 1 — 10:00
Cliente conversa com empresa
        ↓
Cliente para de responder
```

```text
Dia 2 — 10:00
Scheduler verifica
        ↓
24 horas passaram
        ↓
Lead elegível
```

```text
Dia 2 — 10:01
IA gera mensagem
        ↓
Sistema valida
        ↓
Mensagem enviada
```

```text
Dia 2 — 10:20
Cliente responde
        ↓
Sistema registra resposta
        ↓
Follow-up cancelado
        ↓
Automação encerrada
```

---

# 52. Cenário de Falha

Caso a mensagem não possa ser enviada:

```text
Follow-up
    ↓
Tentativa de envio
    ↓
Falha
    ↓
Registrar erro
    ↓
Retry conforme política
    ↓
Falha novamente?
    ↓
Registrar falha definitiva
```

O sistema não deverá considerar uma mensagem como enviada quando o provedor confirmar uma falha.

---

# 53. Cenário de Opt-Out

Caso o cliente solicite não receber mais comunicações:

```text
Cliente solicita interrupção
        ↓
Sistema registra evento
        ↓
Cliente recebe status apropriado
        ↓
Novas mensagens automáticas são bloqueadas
```

O comportamento deverá ser compatível com as regras de comunicação e requisitos legais aplicáveis.

---

# 54. Cenário de Atendimento Humano

```text
Cliente responde
       ↓
Sistema identifica necessidade de humano
       ↓
Conversa marcada para atendimento
       ↓
Atendente assume
       ↓
Automação interrompida
```

---

# 55. Métricas de Validação do MVP

Além das métricas do sistema, o MVP deverá ser avaliado por indicadores de produto.

## Indicadores técnicos

* quantidade de automações executadas;
* quantidade de mensagens enviadas;
* taxa de falha;
* quantidade de respostas processadas;
* tempo de processamento;
* erros de integração.

## Indicadores de uso

* empresas cadastradas;
* empresas ativas;
* automações criadas;
* leads acompanhados;
* follow-ups utilizados;
* usuários ativos.

## Indicadores de resultado

* respostas após follow-up;
* oportunidades recuperadas;
* conversões atribuídas;
* percepção de valor pelo cliente.

---

# 56. Perguntas que o MVP Deve Responder

O MVP deverá ajudar a responder:

```text
1. O problema realmente existe?

2. Empresas possuem leads sem acompanhamento?

3. Empresas aceitariam automatizar o follow-up?

4. Mensagens personalizadas aumentam a interação?

5. A IA gera mensagens suficientemente úteis?

6. O fluxo automático é confiável?

7. Empresas conseguem configurar o sistema?

8. O sistema economiza tempo?

9. O sistema recupera oportunidades?

10. Empresas pagariam por essa solução?
```

---

# 57. Validação com Empresas

O MVP deverá ser testado inicialmente com poucas empresas.

Fluxo:

```text
MVP
 ↓
Primeira empresa
 ↓
Uso real
 ↓
Feedback
 ↓
Correções
 ↓
Segunda empresa
 ↓
Comparação
 ↓
Melhoria
```

O objetivo inicial não será atingir grande quantidade de clientes.

O objetivo será descobrir se o problema, solução e fluxo possuem valor real.

---

# 58. Estratégia de Desenvolvimento

A implementação deverá seguir pequenos incrementos.

```text
Fase 1
Projeto
   ↓
Fase 2
Banco
   ↓
Fase 3
Autenticação
   ↓
Fase 4
Clientes
   ↓
Fase 5
Conversas
   ↓
Fase 6
Automações
   ↓
Fase 7
Scheduler
   ↓
Fase 8
IA
   ↓
Fase 9
Canal
   ↓
Fase 10
Dashboard
   ↓
Fase 11
Testes
   ↓
Fase 12
Deploy
```

---

# 59. Ordem de Implementação

## Etapa 1 — Estrutura

* criar repositório;
* configurar backend;
* configurar frontend;
* configurar ambiente;
* configurar Git;
* configurar Docker.

---

## Etapa 2 — Banco

Implementar:

```text
Company
User
Customer
Conversation
Message
Automation
FollowUp
Event
```

---

## Etapa 3 — Autenticação

Implementar:

* cadastro;
* login;
* autenticação;
* autorização;
* proteção de rotas.

---

## Etapa 4 — Clientes

Implementar:

* criação;
* edição;
* listagem;
* consulta;
* status.

---

## Etapa 5 — Conversas

Implementar:

* criação;
* mensagens;
* histórico;
* status.

---

## Etapa 6 — Automação

Implementar:

* criação;
* configuração;
* ativação;
* desativação;
* gatilhos;
* condições.

---

## Etapa 7 — Follow-up

Implementar:

* criação;
* agendamento;
* limite;
* cancelamento;
* histórico.

---

## Etapa 8 — Scheduler

Implementar:

```text
Buscar tarefas
      ↓
Verificar horário
      ↓
Validar condições
      ↓
Executar
      ↓
Registrar resultado
```

---

## Etapa 9 — IA

Implementar:

* integração com modelo;
* geração de mensagens;
* contexto;
* validação;
* limites;
* tratamento de erros.

---

## Etapa 10 — Comunicação

Implementar o primeiro canal escolhido.

Estrutura:

```text
Message Service
      ↓
Provider
      ↓
API externa
```

---

## Etapa 11 — Respostas

Implementar:

* recebimento de mensagens;
* webhooks;
* registro;
* identificação de conversa;
* cancelamento de follow-up.

---

## Etapa 12 — Dashboard

Implementar:

* leads;
* follow-ups;
* respostas;
* recuperações;
* automações.

---

## Etapa 13 — Testes

Criar:

* testes unitários;
* testes de integração;
* testes de automação;
* testes de segurança;
* testes de integração externa.

---

## Etapa 14 — Deploy

Preparar:

```text
Frontend
   ↓
Backend
   ↓
Database
   ↓
Scheduler / Worker
   ↓
Serviços externos
```

---

# 60. Backlog Inicial

## 🔴 Prioridade Alta

```text
[ ] Criar estrutura do projeto
[ ] Configurar banco
[ ] Criar Company
[ ] Criar User
[ ] Implementar autenticação
[ ] Criar Customer
[ ] Criar Conversation
[ ] Criar Message
[ ] Criar Automation
[ ] Criar FollowUp
[ ] Criar Event
[ ] Implementar regras
[ ] Implementar Scheduler
[ ] Integrar IA
[ ] Integrar canal inicial
[ ] Detectar respostas
[ ] Cancelar follow-ups
[ ] Implementar isolamento de empresas
```

---

## 🟡 Prioridade Média

```text
[ ] Dashboard
[ ] Métricas
[ ] Tags
[ ] Templates
[ ] Filtros
[ ] Notificações
[ ] Logs avançados
```

---

## 🟢 Futuro

```text
[ ] Billing
[ ] E-mail
[ ] SMS
[ ] CRM
[ ] IA de voz
[ ] Agentes
[ ] RAG
[ ] Marketplace
[ ] White-label
[ ] API pública
```

---

# 61. Definição de Pronto

Uma funcionalidade será considerada pronta quando:

```text
Código implementado
      ↓
Validação realizada
      ↓
Teste criado quando aplicável
      ↓
Erro tratado
      ↓
Documentação atualizada
      ↓
Commit realizado
```

---

# 62. Critérios Técnicos

Antes de considerar o MVP concluído:

```text
✓ Aplicação executa corretamente
✓ Banco funciona
✓ Autenticação funciona
✓ Empresas estão isoladas
✓ Clientes podem ser cadastrados
✓ Conversas são registradas
✓ Automação pode ser configurada
✓ Scheduler executa tarefas
✓ IA gera mensagens
✓ Mensagens podem ser enviadas
✓ Respostas são registradas
✓ Follow-ups são cancelados corretamente
✓ Falhas são registradas
✓ Testes principais passam
✓ Variáveis sensíveis não estão no Git
✓ Documentação está atualizada
```

---

# 63. Critérios de Produto

O MVP também deverá permitir verificar:

```text
✓ Empresa entende o funcionamento
✓ Empresa consegue configurar o fluxo
✓ Automação economiza trabalho manual
✓ Mensagens são úteis
✓ Cliente consegue responder normalmente
✓ Atendente consegue assumir conversa
✓ Empresa consegue visualizar resultados
```

---

# 64. Resultado Esperado

Ao final do MVP, deverá existir um sistema capaz de executar este fluxo real:

```text
                    EMPRESA
                       │
                       ▼
                    LEAD
                       │
                       ▼
                  CONVERSA
                       │
                       ▼
               SEM RESPOSTA
                       │
                       ▼
                  DETECÇÃO
                       │
                       ▼
                  AUTOMAÇÃO
                       │
                       ▼
                     IA
                       │
                       ▼
                FOLLOW-UP
                       │
                       ▼
                MENSAGEM
                       │
                 ┌─────┴─────┐
                 ▼           ▼
              RESPOSTA    SEM RESPOSTA
                 │           │
                 ▼           ▼
             HUMANO       NOVA TENTATIVA
                 │           │
                 └─────┬─────┘
                       ▼
                    RESULTADO
                       │
                       ▼
                   MÉTRICAS
```

---

# 65. Limitações Conhecidas

O MVP não deverá ser tratado como produto final.

Possíveis limitações:

* poucos canais;
* regras simples;
* métricas básicas;
* IA limitada a tarefas específicas;
* poucas integrações;
* interface inicial;
* ausência de funcionalidades avançadas;
* necessidade de configuração manual;
* capacidade limitada de escala inicial.

Essas limitações são aceitáveis enquanto o objetivo for validar o produto.

---

# 66. Evolução Após o MVP

Após a validação, a evolução poderá seguir:

```text
MVP
 ↓
Melhoria do fluxo
 ↓
Mais automações
 ↓
Mais canais
 ↓
Mais integrações
 ↓
Analytics
 ↓
Planos
 ↓
Cobrança
 ↓
Escala
```

---

# 67. Possíveis Novas Automações

Depois da primeira automação, o sistema poderá evoluir para:

```text
Recuperação de lead
        ↓
Recuperação de orçamento
        ↓
Reativação de cliente
        ↓
Lembrete de atendimento
        ↓
Pós-atendimento
        ↓
Reativação de cliente inativo
        ↓
Recuperação de oportunidade
```

Todas essas automações deverão reutilizar a infraestrutura principal.

---

# 68. Arquitetura Evolutiva

O objetivo é evitar criar uma aplicação específica para apenas um fluxo.

A estrutura deverá permitir:

```text
                Automation Engine
                       │
       ┌───────────────┼────────────────┐
       ▼               ▼                ▼
   Lead Recovery   Budget Recovery   Customer Reactivation
       │               │                │
       └───────────────┼────────────────┘
                       ▼
                Message Service
                       │
            ┌──────────┼──────────┐
            ▼          ▼          ▼
         Canal A    Canal B    Canal C
```

Assim, novas automações poderão reutilizar componentes existentes.

---

# 69. Princípios do MVP

O desenvolvimento deverá seguir estes princípios:

## 1. Resolver um problema específico

Não tentar construir um sistema que faça tudo.

## 2. Começar pequeno

Implementar somente o necessário para validar a hipótese.

## 3. Automação controlada

A IA não deverá controlar indiscriminadamente o sistema.

## 4. Segurança desde o início

Isolamento de empresas e proteção de dados fazem parte do MVP.

## 5. Arquitetura preparada para crescimento

O código inicial deverá permitir evolução sem complexidade desnecessária.

## 6. Medir resultados

O sistema deverá registrar dados que permitam avaliar o funcionamento da solução.

## 7. Feedback real

O produto deverá evoluir com base no uso real.

---

# 70. Definição Final do MVP

O **AI Customer Recovery MVP** será uma plataforma capaz de:

```text
CADASTRAR EMPRESAS
        ↓
CADASTRAR LEADS
        ↓
REGISTRAR CONVERSAS
        ↓
IDENTIFICAR LEADS SEM RESPOSTA
        ↓
ACIONAR AUTOMAÇÕES
        ↓
AGENDAR FOLLOW-UPS
        ↓
GERAR MENSAGENS COM IA
        ↓
ENVIAR MENSAGENS
        ↓
DETECTAR RESPOSTAS
        ↓
CANCELAR AUTOMAÇÕES
        ↓
ENCAMINHAR PARA HUMANOS
        ↓
REGISTRAR HISTÓRICO
        ↓
MEDIR RESULTADOS
```

O foco inicial será **recuperar oportunidades que poderiam ser perdidas por falta de follow-up**, mantendo a arquitetura suficientemente genérica para posteriormente atender diferentes tipos de empresas e diferentes processos de recuperação.

---

# 71. Resumo

```text
┌─────────────────────────────────────────┐
│             AI CUSTOMER RECOVERY        │
├─────────────────────────────────────────┤
│                                         │
│  Entrada                                │
│     ↓                                   │
│  Lead / Cliente                         │
│     ↓                                   │
│  Interação                              │
│     ↓                                   │
│  Sem resposta                           │
│     ↓                                   │
│  Regra                                  │
│     ↓                                   │
│  Scheduler                              │
│     ↓                                   │
│  IA                                     │
│     ↓                                   │
│  Follow-up                              │
│     ↓                                   │
│  Comunicação                            │
│     ↓                                   │
│  Resposta                               │
│     ↓                                   │
│  Humano / Nova tentativa                │
│     ↓                                   │
│  Resultado                              │
│                                         │
└─────────────────────────────────────────┘
```

**O MVP não precisa ser grande. Precisa ser funcional, mensurável e capaz de validar o problema e a solução.**
