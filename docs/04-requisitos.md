# Requisitos

## 1. Visão Geral

Este documento define os requisitos do **AI Customer Recovery**.

Os requisitos descrevem as funcionalidades, comportamentos, restrições e características que a plataforma deverá possuir.

O objetivo é estabelecer uma base clara para o desenvolvimento do sistema antes da implementação.

---

# 2. Objetivo dos Requisitos

Os requisitos deverão ajudar a:

* definir o escopo do produto;
* orientar o desenvolvimento;
* evitar funcionalidades desnecessárias no MVP;
* facilitar a criação de testes;
* documentar decisões do projeto;
* estabelecer critérios de aceitação;
* permitir evolução futura da plataforma.

---

# 3. Escopo

O sistema deverá permitir que empresas:

```text
Cadastrar empresa
       ↓
Cadastrar usuários
       ↓
Cadastrar leads/clientes
       ↓
Registrar interações
       ↓
Identificar oportunidades
       ↓
Configurar automações
       ↓
Executar follow-ups
       ↓
Utilizar IA
       ↓
Acompanhar respostas
       ↓
Medir resultados
```

---

# 4. Classificação dos Requisitos

Os requisitos serão classificados em:

```text
RF  → Requisito Funcional
RNF → Requisito Não Funcional
RN  → Regra de Negócio
IA  → Requisito relacionado à Inteligência Artificial
SEG → Requisito de Segurança
LGPD → Requisito de Privacidade e Proteção de Dados
INT → Requisito de Integração
```

---

# 5. Requisitos Funcionais

## RF01 — Cadastro de Empresa

O sistema deverá permitir o cadastro de uma empresa.

Dados mínimos:

* nome;
* e-mail;
* telefone;
* informações básicas;
* configurações da conta.

### Critérios de aceitação

```text
Dado que o usuário não possui uma empresa
        ↓
Realiza o cadastro
        ↓
Sistema valida os dados
        ↓
Empresa é criada
```

---

## RF02 — Autenticação

O sistema deverá permitir que usuários façam login.

Funcionalidades:

* login;
* logout;
* recuperação de acesso;
* proteção de sessão;
* gerenciamento de credenciais.

### Critérios de aceitação

```text
Credenciais válidas
       ↓
Acesso autorizado
```

```text
Credenciais inválidas
       ↓
Acesso negado
```

---

## RF03 — Gerenciamento de Usuários

O administrador da empresa deverá poder gerenciar usuários.

Possíveis informações:

* nome;
* e-mail;
* função;
* status;
* permissões.

Possíveis funções:

```text
Administrador
Gestor
Atendente
```

---

## RF04 — Controle de Permissões

O sistema deverá controlar o acesso às funcionalidades de acordo com as permissões do usuário.

Exemplo:

```text
Administrador
 ├── Usuários
 ├── Configurações
 ├── Automações
 ├── Clientes
 └── Relatórios

Gestor
 ├── Automações
 ├── Clientes
 ├── Conversas
 └── Relatórios

Atendente
 ├── Clientes
 ├── Conversas
 └── Atendimento
```

As permissões deverão ser definidas de forma centralizada.

---

## RF05 — Cadastro de Clientes

O sistema deverá permitir cadastrar clientes.

Informações possíveis:

* nome;
* telefone;
* e-mail;
* tags;
* status;
* origem;
* observações;
* data do último contato.

---

## RF06 — Cadastro de Leads

O sistema deverá permitir registrar leads.

Um lead poderá possuir:

* identificação;
* origem;
* status;
* interesse;
* data de criação;
* última interação;
* responsável;
* histórico.

Possíveis estados:

```text
Novo
 ↓
Em atendimento
 ↓
Interessado
 ↓
Follow-up
 ↓
Convertido
```

Também deverão existir estados para situações como:

```text
Sem resposta
Perdido
Encerrado
```

---

## RF07 — Histórico do Cliente

O sistema deverá manter o histórico de interações do cliente.

Exemplo:

```text
Cliente criado
      ↓
Mensagem recebida
      ↓
Mensagem enviada
      ↓
Orçamento
      ↓
Sem resposta
      ↓
Follow-up
      ↓
Resposta
```

---

## RF08 — Registro de Conversas

O sistema deverá registrar conversas entre empresa e cliente.

Cada mensagem poderá possuir:

* remetente;
* destinatário;
* conteúdo;
* data;
* canal;
* status;
* identificador externo.

---

## RF09 — Registro de Eventos

O sistema deverá registrar eventos importantes.

Exemplos:

```text
Lead criado
Mensagem recebida
Mensagem enviada
Follow-up criado
Follow-up enviado
Follow-up cancelado
Cliente respondeu
Automação executada
Automação encerrada
Atendente assumiu conversa
```

---

## RF10 — Identificação de Leads Sem Resposta

O sistema deverá identificar leads que não responderam dentro do período definido.

Exemplo:

```text
Última mensagem
      ↓
Aguardar 24 horas
      ↓
Cliente não respondeu
      ↓
Lead elegível para follow-up
```

O período deverá ser configurável.

---

## RF11 — Criação de Automação

O sistema deverá permitir criar automações.

Uma automação deverá possuir:

* nome;
* descrição;
* status;
* gatilho;
* condições;
* ações;
* intervalo;
* limite de tentativas.

---

## RF12 — Gatilhos

As automações deverão poder ser iniciadas por eventos.

Exemplos:

```text
Lead criado
Cliente sem resposta
Orçamento enviado
Cliente inativo
Agendamento cancelado
Status alterado
Evento recebido de integração
```

O conjunto inicial de gatilhos será definido pelo MVP.

---

## RF13 — Condições

Uma automação poderá possuir condições.

Exemplo:

```text
SE

último contato > 24 horas

E

status = interessado

E

não existe follow-up pendente

ENTÃO

executar automação
```

---

## RF14 — Ações

Uma automação poderá executar ações.

Exemplos:

```text
Enviar mensagem
Aguardar período
Alterar status
Adicionar tag
Criar tarefa
Encaminhar para humano
Encerrar automação
```

---

## RF15 — Agendamento de Follow-up

O sistema deverá permitir agendar follow-ups.

Cada follow-up deverá possuir:

* cliente;
* automação;
* data/hora;
* status;
* tentativa;
* mensagem;
* canal.

Possíveis estados:

```text
Pendente
Agendado
Enviado
Cancelado
Falhou
Concluído
```

---

## RF16 — Cancelamento Automático

Quando o cliente responder, follow-ups pendentes relacionados àquela conversa deverão ser cancelados quando a regra da automação determinar esse comportamento.

Exemplo:

```text
Follow-up agendado
       ↓
Cliente responde
       ↓
Sistema detecta resposta
       ↓
Follow-up cancelado
```

---

## RF17 — Limite de Follow-ups

O sistema deverá permitir definir um número máximo de tentativas.

Exemplo:

```text
Follow-up 1
     ↓
Follow-up 2
     ↓
Máximo atingido
     ↓
Automação encerrada
```

---

## RF18 — Intervalo entre Follow-ups

O sistema deverá permitir configurar o intervalo entre tentativas.

Exemplo:

```text
Interação
   ↓
24h
   ↓
Follow-up 1
   ↓
48h
   ↓
Follow-up 2
```

---

## RF19 — Geração de Mensagens com IA

O sistema deverá permitir utilizar IA para gerar mensagens.

A IA poderá receber informações como:

```text
Nome
Contexto
Última interação
Produto/serviço
Status
Objetivo do follow-up
Tom da comunicação
```

---

## RF20 — Personalização de Mensagens

As mensagens geradas deverão poder utilizar informações disponíveis sobre o cliente e o contexto.

Exemplo:

```text
Nome: Ana
Interesse: Serviço X
Última interação: 2 dias
```

Resultado:

```text
Mensagem contextualizada
```

A IA não deverá inventar informações que não estejam disponíveis.

---

## RF21 — Aprovação de Mensagens

O sistema poderá permitir que determinados fluxos exijam aprovação humana antes do envio.

Exemplo:

```text
IA gera mensagem
       ↓
Revisão humana
       ↓
Aprovar
       ↓
Enviar
```

Essa funcionalidade poderá ser priorizada conforme o caso de uso.

---

## RF22 — Classificação de Respostas

A IA poderá classificar respostas dos clientes.

Exemplos:

```text
Interessado
Dúvida
Negociação
Solicita humano
Recusa
Opt-out
Sem relação
```

A lista final será configurável conforme o produto evoluir.

---

## RF23 — Encaminhamento para Humano

O sistema deverá permitir encaminhar uma conversa para um atendente.

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
```

---

## RF24 — Atendimento Humano

Um usuário autorizado deverá poder visualizar e assumir conversas.

A intervenção humana deverá interromper ou alterar as automações conforme as regras configuradas.

---

## RF25 — Status das Conversas

Cada conversa deverá possuir um status.

Exemplos:

```text
Aberta
Em automação
Aguardando cliente
Aguardando atendente
Em atendimento
Resolvida
Encerrada
```

---

## RF26 — Dashboard

O sistema deverá possuir um dashboard básico.

Informações possíveis:

```text
Leads
Clientes
Follow-ups
Respostas
Clientes recuperados
Conversões
Automações executadas
```

---

## RF27 — Métricas

O sistema deverá calcular métricas relacionadas às automações.

Possíveis métricas:

* leads acompanhados;
* follow-ups enviados;
* respostas;
* leads recuperados;
* conversões;
* taxa de resposta;
* taxa de recuperação;
* automações concluídas.

---

## RF28 — Histórico de Automação

O sistema deverá permitir consultar o histórico das automações.

Exemplo:

```text
Automação: Recuperação de Lead

Lead: #1234

09:00 → Lead identificado
09:01 → Follow-up criado
09:02 → Mensagem enviada
11:30 → Cliente respondeu
11:30 → Follow-up cancelado
```

---

## RF29 — Configuração de Templates

O sistema poderá permitir criar templates de mensagens.

Exemplo:

```text
Olá, {{nome}}!

Vi que você demonstrou interesse em
{{servico}}.

Posso ajudar com mais informações?
```

Templates poderão ser utilizados diretamente ou como referência para geração pela IA.

---

## RF30 — Tags

O sistema deverá permitir categorizar clientes utilizando tags.

Exemplos:

```text
interessado
cliente-inativo
orcamento
prioridade
novo-lead
```

---

## RF31 — Busca

O sistema deverá permitir pesquisar clientes, leads e conversas.

Possíveis filtros:

* nome;
* telefone;
* e-mail;
* status;
* tag;
* período;
* automação;
* responsável.

---

## RF32 — Filtros

O usuário deverá poder filtrar dados relevantes.

Exemplo:

```text
Status: Sem resposta
Período: últimos 30 dias
Automação: Recuperação
```

---

## RF33 — Notificações

O sistema poderá enviar notificações relacionadas a eventos importantes.

Exemplos:

* cliente solicitou humano;
* automação falhou;
* integração ficou indisponível;
* tarefa foi criada.

---

## RF34 — Configurações da Empresa

O administrador deverá poder configurar:

* dados da empresa;
* usuários;
* automações;
* canais;
* horários;
* regras;
* preferências;
* configurações de IA.

---

# 6. Requisitos Não Funcionais

## RNF01 — Usabilidade

A interface deverá ser simples e permitir que usuários não técnicos configurem automações básicas.

---

## RNF02 — Responsividade

A interface deverá funcionar adequadamente em:

* desktop;
* notebook;
* tablet;
* dispositivos móveis, quando aplicável.

---

## RNF03 — Desempenho

As operações comuns deverão possuir tempo de resposta adequado.

Processos demorados deverão ser executados de forma assíncrona quando necessário.

---

## RNF04 — Escalabilidade

A arquitetura deverá permitir crescimento de:

```text
1 empresa
 ↓
10 empresas
 ↓
100 empresas
 ↓
1.000+ empresas
```

sem necessidade de reescrever completamente o sistema.

---

## RNF05 — Disponibilidade

O sistema deverá ser projetado para minimizar indisponibilidades.

Componentes críticos deverão possuir tratamento adequado de falhas.

---

## RNF06 — Manutenibilidade

O código deverá ser organizado de forma modular.

Princípios:

* separação de responsabilidades;
* baixo acoplamento;
* componentes reutilizáveis;
* documentação;
* testes;
* padrões consistentes.

---

## RNF07 — Testabilidade

As funcionalidades principais deverão possuir testes automatizados quando aplicável.

Prioridades:

```text
Regras de negócio
       ↓
Automações
       ↓
Follow-ups
       ↓
Integrações
       ↓
IA
```

---

## RNF08 — Observabilidade

O sistema deverá registrar informações necessárias para identificar problemas.

Possíveis recursos:

* logs;
* métricas;
* eventos;
* monitoramento;
* rastreamento de erros.

---

## RNF09 — Configurabilidade

Sempre que possível, regras que variam entre empresas deverão ser configuráveis em vez de codificadas diretamente.

---

# 7. Requisitos de Inteligência Artificial

## IA01 — Contexto

A IA deverá receber somente o contexto necessário para executar determinada tarefa.

---

## IA02 — Não Invenção

A IA não deverá inventar:

* preços;
* horários;
* produtos;
* serviços;
* políticas;
* informações sobre clientes;
* condições comerciais.

Quando uma informação não estiver disponível, deverá seguir a regra definida pelo sistema.

---

## IA03 — Controle por Regras

A IA deverá operar dentro das regras de negócio.

```text
Dados
 ↓
Regras
 ↓
IA
 ↓
Validação
 ↓
Ação
```

A IA não deverá determinar sozinha todas as regras do sistema.

---

## IA04 — Escalonamento para Humano

A IA deverá poder indicar que uma conversa necessita de atendimento humano.

---

## IA05 — Detecção de Opt-Out

Quando aplicável, o sistema deverá identificar solicitações de interrupção de comunicação e executar as regras correspondentes.

Exemplos:

```text
"Não quero mais receber mensagens."
"Pare de me mandar mensagens."
"Remova meu contato."
```

O comportamento final deverá ser definido pelas regras de comunicação e requisitos legais aplicáveis.

---

## IA06 — Controle de Custos

Chamadas à IA deverão ser controladas para evitar consumo desnecessário.

Possíveis estratégias:

* limitar tamanho do contexto;
* utilizar modelos adequados à tarefa;
* armazenar resultados quando apropriado;
* evitar chamadas duplicadas;
* estabelecer limites de uso.

---

## IA07 — Registro

Quando apropriado, o sistema deverá registrar informações suficientes sobre operações realizadas pela IA para permitir auditoria e investigação de problemas.

---

# 8. Regras de Negócio

## RN01 — Resposta do Cliente

Se o cliente responder a uma conversa com follow-up pendente:

```text
Cliente responde
       ↓
Identificar resposta
       ↓
Cancelar follow-up pendente
       ↓
Continuar fluxo apropriado
```

---

## RN02 — Limite de Tentativas

Uma automação não poderá ultrapassar o número máximo de tentativas configurado.

---

## RN03 — Intervalo Mínimo

O sistema deverá respeitar o intervalo mínimo configurado entre mensagens automáticas.

---

## RN04 — Automação Desativada

Se uma automação estiver desativada:

```text
Automação = INATIVA
       ↓
Não criar novas ações automáticas
```

Ações já programadas deverão seguir uma regra definida para o sistema.

---

## RN05 — Atendimento Humano

Quando uma conversa for assumida por um atendente, o sistema deverá respeitar a configuração da automação relacionada à intervenção humana.

---

## RN06 — Cliente Bloqueado

Clientes bloqueados ou impedidos de receber determinadas comunicações não deverão receber mensagens automáticas.

---

## RN07 — Dados Obrigatórios

O sistema deverá validar dados obrigatórios antes de executar uma automação.

---

## RN08 — Canal Indisponível

Se o canal de comunicação estiver indisponível:

```text
Tentativa de envio
       ↓
Falha
       ↓
Registrar erro
       ↓
Aplicar política de retry
```

---

## RN09 — Falha Repetida

Após determinado número de falhas, o sistema deverá interromper novas tentativas automáticas e registrar o problema.

---

## RN10 — Encerramento

Uma automação deverá possuir condições de encerramento.

Exemplos:

```text
Cliente respondeu
Limite atingido
Cliente convertido
Cliente recusou
Opt-out
Atendente assumiu
Automação desativada
```

---

# 9. Requisitos de Segurança

## SEG01 — Autenticação

Acesso às áreas privadas deverá exigir autenticação.

---

## SEG02 — Autorização

Usuários somente poderão executar ações permitidas por suas funções.

---

## SEG03 — Senhas

Senhas não deverão ser armazenadas em texto puro.

---

## SEG04 — Segredos

Credenciais de APIs e serviços externos não deverão ser armazenadas diretamente no código.

Utilizar:

```text
Variáveis de ambiente
Secret Manager
```

conforme o ambiente.

---

## SEG05 — Comunicação

As comunicações entre cliente e servidor deverão utilizar mecanismos seguros de transporte quando disponíveis.

---

## SEG06 — Validação

Dados recebidos pela API deverão ser validados antes de serem processados.

---

## SEG07 — Isolamento de Empresas

Uma empresa não poderá acessar dados pertencentes a outra empresa.

```text
Empresa A
   ↓
Dados A

Empresa B
   ↓
Dados B
```

---

## SEG08 — Logs

Logs não deverão expor informações sensíveis desnecessariamente.

---

## SEG09 — Webhooks

Webhooks de serviços externos deverão possuir mecanismos de validação/autenticação quando suportados.

---

## SEG10 — Rate Limiting

Endpoints sensíveis deverão possuir mecanismos de proteção contra uso excessivo quando necessário.

---

# 10. Requisitos de Privacidade e LGPD

## LGPD01 — Minimização

O sistema deverá coletar apenas os dados necessários para suas funcionalidades.

---

## LGPD02 — Finalidade

Os dados deverão ser utilizados de acordo com finalidades definidas.

---

## LGPD03 — Controle de Acesso

Dados pessoais deverão ser acessíveis somente por usuários autorizados.

---

## LGPD04 — Retenção

O sistema deverá possuir política de retenção de dados.

---

## LGPD05 — Exclusão

Deverá existir mecanismo para tratar solicitações de exclusão quando aplicável.

---

## LGPD06 — Dados Enviados à IA

Antes de enviar informações para serviços externos de IA, o sistema deverá considerar:

* necessidade do dado;
* finalidade;
* segurança;
* configuração do provedor;
* requisitos contratuais;
* requisitos legais aplicáveis.

---

## LGPD07 — Dados de Comunicação

O sistema deverá considerar as regras aplicáveis à comunicação com clientes, incluindo solicitações para interromper comunicações.

---

# 11. Requisitos de Integração

## INT01 — Arquitetura de Integração

A comunicação com serviços externos deverá ser isolada em módulos específicos.

Exemplo:

```text
Core
 │
 └── Message Service
        │
        ├── WhatsApp
        ├── E-mail
        └── Outros
```

---

## INT02 — Webhooks

O sistema deverá ser capaz de receber eventos de serviços externos quando necessário.

Exemplos:

```text
Mensagem recebida
Mensagem entregue
Mensagem enviada
Mensagem falhou
```

---

## INT03 — Tratamento de Falhas

Falhas externas deverão ser tratadas sem comprometer o restante do sistema.

---

## INT04 — Retry

Operações que falharem por motivos temporários poderão ser repetidas de acordo com uma política de retry.

---

## INT05 — Idempotência

Eventos externos que possam ser recebidos mais de uma vez deverão ser tratados de maneira a evitar duplicação de operações.

---

# 12. Requisitos de Banco de Dados

O banco deverá armazenar informações necessárias para:

```text
Empresas
Usuários
Clientes
Leads
Conversas
Mensagens
Automações
Follow-ups
Eventos
Configurações
```

---

## DB01 — Relacionamento com Empresa

Dados pertencentes a uma empresa deverão estar associados ao respectivo identificador da empresa.

---

## DB02 — Integridade

O sistema deverá preservar a integridade dos relacionamentos entre entidades.

---

## DB03 — Histórico

Informações necessárias para auditoria e acompanhamento deverão ser armazenadas de acordo com as políticas definidas.

---

## DB04 — Índices

Consultas frequentes deverão possuir índices adequados quando necessário.

---

# 13. Requisitos de API

## API01 — REST

O backend poderá utilizar uma API REST para comunicação com o frontend e integrações.

---

## API02 — Validação

Dados recebidos deverão ser validados.

---

## API03 — Autenticação

Endpoints privados deverão exigir autenticação.

---

## API04 — Autorização

Endpoints deverão verificar as permissões do usuário.

---

## API05 — Respostas

A API deverá utilizar respostas consistentes.

Exemplo:

```text
200 → sucesso
201 → recurso criado
400 → requisição inválida
401 → não autenticado
403 → sem permissão
404 → recurso não encontrado
409 → conflito
422 → dados inválidos
429 → limite excedido
500 → erro interno
```

Os códigos exatos poderão variar conforme a implementação.

---

# 14. Requisitos de Interface

## UI01 — Dashboard

O dashboard deverá apresentar as principais informações de forma simples.

---

## UI02 — Clientes

O usuário deverá conseguir:

* listar;
* pesquisar;
* filtrar;
* visualizar;
* editar;
* consultar histórico.

---

## UI03 — Automações

O usuário deverá conseguir:

* visualizar automações;
* criar;
* editar;
* ativar;
* desativar;
* consultar histórico.

---

## UI04 — Conversas

O usuário deverá conseguir:

* visualizar conversas;
* consultar histórico;
* identificar status;
* assumir atendimento quando autorizado.

---

## UI05 — Feedback

A interface deverá apresentar mensagens claras para:

* sucesso;
* erro;
* carregamento;
* validação;
* indisponibilidade.

---

# 15. Requisitos de Assinatura

A arquitetura deverá permitir futuramente a criação de planos.

Possíveis limites:

```text
Plano
 ↓
Usuários
 ↓
Clientes
 ↓
Automações
 ↓
Mensagens
 ↓
Uso de IA
 ↓
Integrações
```

A cobrança não será necessariamente implementada no primeiro MVP.

---

# 16. Requisitos de Uso

O sistema deverá permitir estabelecer limites de utilização.

Possíveis limites:

* mensagens;
* clientes;
* automações;
* usuários;
* chamadas de IA;
* histórico;
* integrações.

---

# 17. Requisitos de Auditoria

O sistema deverá registrar operações importantes.

Exemplos:

```text
Usuário criou automação
Usuário alterou automação
Usuário desativou automação
Mensagem automática enviada
Cliente respondeu
Atendente assumiu conversa
Configuração alterada
```

---

# 18. Requisitos de Escalabilidade

A plataforma deverá ser projetada considerando:

```text
                    Plataforma
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
      Empresa A       Empresa B       Empresa C
        │               │               │
      Dados A         Dados B         Dados C
```

O crescimento do número de empresas não deverá comprometer o isolamento dos dados.

---

# 19. Requisitos de Processamento Assíncrono

Processos demorados ou que não precisam bloquear a resposta da API deverão poder ser executados em segundo plano.

Exemplos:

```text
Envio de mensagens
Geração de IA
Processamento de eventos
Follow-ups
Relatórios
```

Arquitetura possível:

```text
API
 ↓
Fila
 ↓
Worker
 ↓
Processamento
 ↓
Resultado
```

---

# 20. Requisitos de Scheduler

O sistema deverá possuir um mecanismo para executar ações programadas.

Exemplo:

```text
Follow-up:
2026-09-25 14:00

        ↓

Scheduler verifica

        ↓

Data atingida

        ↓

Executa follow-up
```

O mecanismo poderá ser substituído ou evoluído conforme a escala do sistema.

---

# 21. Requisitos de Testes

## TEST01 — Testes Unitários

Testar principalmente:

* regras de negócio;
* condições;
* estados;
* cálculo de intervalos;
* limites.

---

## TEST02 — Testes de Integração

Testar:

* banco;
* API;
* scheduler;
* serviços externos;
* webhooks.

---

## TEST03 — Testes de Fluxo

Exemplo:

```text
Lead
 ↓
Sem resposta
 ↓
Follow-up
 ↓
Cliente responde
 ↓
Follow-up cancelado
```

---

## TEST04 — Testes de Segurança

Testar:

* autenticação;
* autorização;
* isolamento entre empresas;
* validação;
* acesso indevido;
* exposição de dados.

---

## TEST05 — Testes de IA

Avaliar:

* qualidade das mensagens;
* respeito ao contexto;
* ausência de informações inventadas;
* classificação;
* encaminhamento para humano;
* comportamento em situações inesperadas.

---

# 22. Requisitos do MVP

O MVP deverá priorizar os seguintes requisitos:

```text
┌──────────────────────────────────────┐
│               MVP                    │
├──────────────────────────────────────┤
│ ✓ Cadastro de empresa               │
│ ✓ Autenticação                      │
│ ✓ Usuários                          │
│ ✓ Clientes / Leads                  │
│ ✓ Conversas                         │
│ ✓ Mensagens                         │
│ ✓ Follow-ups                        │
│ ✓ Regras de automação               │
│ ✓ Scheduler                         │
│ ✓ IA para geração de mensagens      │
│ ✓ Detecção de resposta              │
│ ✓ Cancelamento de follow-up         │
│ ✓ Encaminhamento para humano        │
│ ✓ Histórico                         │
│ ✓ Dashboard básico                  │
│ ✓ Controle de acesso                │
│ ✓ Segurança básica                  │
└──────────────────────────────────────┘
```

---

# 23. Fora do MVP

As seguintes funcionalidades não serão prioridade inicial:

```text
✗ Aplicativo mobile nativo
✗ IA de voz
✗ CRM completo
✗ Marketplace
✗ Dezenas de integrações
✗ Automação extremamente complexa
✗ Analytics avançado
✗ Sistema financeiro completo
✗ Programa de afiliados
✗ White-label completo
```

Esses recursos poderão ser considerados futuramente.

---

# 24. Prioridade dos Requisitos

A prioridade inicial será:

## Alta

```text
Autenticação
Empresas
Usuários
Clientes
Leads
Conversas
Mensagens
Follow-ups
Regras
Scheduler
IA
Integração de comunicação
Histórico
Segurança
```

## Média

```text
Dashboard avançado
Templates
Tags
Filtros avançados
Notificações
Relatórios
```

## Baixa / Futuro

```text
IA de voz
Aplicativo mobile
White-label
Marketplace
Integrações adicionais
Analytics avançado
```

---

# 25. Critérios Gerais de Aceitação

O produto deverá atender aos seguintes critérios:

```text
1. Usuário consegue criar uma empresa
          ↓
2. Usuário consegue cadastrar clientes
          ↓
3. Sistema consegue registrar conversas
          ↓
4. Sistema identifica uma oportunidade elegível
          ↓
5. Automação é acionada
          ↓
6. Follow-up é programado
          ↓
7. IA gera mensagem conforme regras
          ↓
8. Mensagem é enviada
          ↓
9. Cliente responde
          ↓
10. Follow-up é cancelado
          ↓
11. Evento é registrado
          ↓
12. Resultado aparece no sistema
```

---

# 26. Requisitos Futuros

Após a validação do MVP, poderão ser adicionados:

```text
Integração com CRMs
        ↓
Mais canais
        ↓
Mais automações
        ↓
Reativação de clientes
        ↓
Recuperação de orçamentos
        ↓
Campanhas
        ↓
Analytics
        ↓
Planos e cobrança
        ↓
API pública
        ↓
Marketplace de automações
```

---

# 27. Matriz Resumida

| Código | Requisito                  | Prioridade |
| ------ | -------------------------- | ---------- |
| RF01   | Cadastro de empresa        | Alta       |
| RF02   | Autenticação               | Alta       |
| RF03   | Usuários                   | Alta       |
| RF04   | Permissões                 | Alta       |
| RF05   | Clientes                   | Alta       |
| RF06   | Leads                      | Alta       |
| RF07   | Histórico                  | Alta       |
| RF08   | Conversas                  | Alta       |
| RF10   | Identificação sem resposta | Alta       |
| RF11   | Automações                 | Alta       |
| RF14   | Ações                      | Alta       |
| RF15   | Follow-ups                 | Alta       |
| RF16   | Cancelamento automático    | Alta       |
| RF19   | IA                         | Alta       |
| RF23   | Encaminhamento humano      | Alta       |
| RF26   | Dashboard                  | Média      |
| RF27   | Métricas                   | Média      |
| RF29   | Templates                  | Média      |
| RF30   | Tags                       | Média      |
| RNF01  | Usabilidade                | Alta       |
| RNF04  | Escalabilidade             | Alta       |
| RNF06  | Manutenibilidade           | Alta       |
| SEG01  | Autenticação               | Alta       |
| SEG07  | Isolamento de empresas     | Alta       |
| LGPD01 | Minimização de dados       | Alta       |
| INT01  | Arquitetura de integração  | Alta       |

---

# 28. Resumo

O AI Customer Recovery deverá fornecer uma estrutura capaz de:

```text
IDENTIFICAR
    ↓
OPORTUNIDADES
    ↓
APLICAR REGRAS
    ↓
UTILIZAR IA
    ↓
EXECUTAR FOLLOW-UP
    ↓
MONITORAR RESPOSTA
    ↓
INTERROMPER OU CONTINUAR
    ↓
ENCAMINHAR PARA HUMANO
    ↓
REGISTRAR
    ↓
MEDIR
```

O sistema deverá priorizar **automação controlada**, **segurança**, **privacidade**, **escalabilidade** e **facilidade de uso**.

O MVP deverá resolver primeiro o caso de uso de **recuperação de leads que deixaram de responder**, mantendo a arquitetura preparada para futuras automações e diferentes segmentos de empresas.
