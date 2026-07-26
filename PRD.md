# Product Requirement Document (PRD)

## Sistema de Gestão Imobiliária — Gestão Imob

---

## 1. Visão Geral

Sistema multitenant de gestão imobiliária voltado para corretores autônomos e pequenas imobiliárias. Cada corretor/imobiliária (tenant) possui um painel privado para gerenciar seus imóveis, locações e finanças, além de uma página pública personalizável para divulgar seus imóveis disponíveis.

---

## 2. Objetivos

- Permitir que corretores autônomos e pequenas imobiliárias organizem seu portfólio de imóveis
- Gerar páginas públicas bonitas e personalizáveis para divulgação dos imóveis
- Controlar locações, inquilinos e recebimentos mensais
- Fornecer visão financeira clara do fluxo de caixa por imóvel
- Ser administrado centralizadamente por um super admin que controla acessos e prazos

---

## 3. Público-Alvo

| Ator | Descrição |
|------|-----------|
| **Super Admin** | Administrador do sistema. Cria e gerencia tenants, define prazos de acesso, visualiza dados globais |
| **Corretor / Imobiliária (Tenant)** | Usuário final. Acessa o painel para gerenciar imóveis, locações e finanças. Personaliza sua página pública |
| **Visitante** | Público geral. Acessa a página pública do corretor para visualizar e filtrar imóveis disponíveis |

---

## 4. Funcionalidades (Requisitos Funcionais)

### 4.1 Autenticação e Acesso

- RF01. Login com username/e-mail + senha
- RF02. Super admin cria tenants manualmente e gera senha aleatória
- RF03. Senha temporária exibida **apenas uma vez** no momento da criação
- RF04. Redefinição de senha obrigatória no primeiro acesso
- RF05. Recuperação de senha via e-mail (console em dev)

### 4.2 Super Admin (Painel Administrativo)

- RF06. CRUD de tenants (pessoas físicas ou jurídicas)
- RF07. Geração automática de login/senha ao criar tenant
- RF08. Definição de prazo de acesso (30, 60, 90 dias, ou data personalizada)
- RF09. Visualização global de todos os tenants, imóveis, locações
- RF10. Ativar/desativar tenant
- RF11. Histórico de acessos de cada tenant

### 4.3 Gerenciamento de Imóveis (Painel do Tenant)

- RF12. CRUD completo de imóveis
- RF13. Campos: título, descrição, tipo (venda/aluguel), valor venda, valor aluguel, tamanho m², quartos, banheiros, vagas garagem, endereço completo
- RF14. Upload de múltiplas fotos com compressão automática e geração de thumbnail
- RF15. Status do imóvel: disponível, alugado, vendido, reservado
- RF16. Marcar imóvel como destaque (aparece primeiro na página pública)
- RF17. Ordenação personalizada dos imóveis

### 4.4 Locações

- RF18. CRUD de locações vinculadas a um imóvel
- RF19. Dados do inquilino: nome, CPF, telefone, e-mail
- RF20. Período da locação: data início, data fim
- RF21. Valor mensal e dia de vencimento (1 a 31)
- RF22. Upload do contrato e documentos adicionais (PDF)
- RF23. Ao criar locação → status do imóvel muda automaticamente para "alugado"
- RF24. Ao encerrar locação → status do imóvel volta para "disponível"
- RF25. Histórico de locações por imóvel

### 4.5 Financeiro

- RF26. Registro de pagamentos mensais por locação
- RF27. Status do pagamento: pendente, pago, atrasado
- RF28. Ao marcar como pago: registrar data e valor automaticamente
- RF29. Dashboard financeiro com fluxo de caixa mensal
- RF30. Total recebido vs. total a receber por mês
- RF31. Histórico de pagamentos por locação

### 4.6 Personalização da Página Pública

- RF32. Upload de logo ou uso de nome (texto) como identidade visual
- RF33. Personalização de cores: primária e secundária (seletor de cor)
- RF34. Pré-visualização em tempo real no painel
- RF35. URL pública no formato: `/corretor-slug/`
- RF36. Design responsivo e moderno

### 4.7 Página Pública

- RF37. Grid de imóveis com cards contendo foto principal, título, valor, tipo, localização
- RF38. Filtros AJAX: tipo (venda/aluguel), faixa de valor, quartos, localização
- RF39. Página individual do imóvel com galeria de fotos e detalhes completos
- RF40. Dados de contato do corretor na página
- RF41. Botão "Compartilhar" e "Imprimir" no imóvel individual
- RF42. Exibir apenas imóveis com status "disponível"
- RF43. Nenhum link ou referência ao painel de login

### 4.8 Notificações

- RF44. Notificações em tempo real via interface para tasks assíncronas
- RF45. Loading em botões durante processos em segundo plano
- RF46. Notificação quando task for concluída

---

## 5. Requisitos Não Funcionais

| Código | Requisito |
|--------|-----------|
| RNF01 | **Responsividade** — O sistema deve funcionar corretamente em dispositivos de todos os tamanhos (mobile, tablet, desktop) |
| RNF02 | **Segurança** — Dados sensíveis não devem ser expostos. Rotas fechadas para não autenticados. Sistema de permissões multitenant que garanta isolamento total de dados, incluindo arquivos de mídia |
| RNF03 | **UI/UX Excelente** — Baseado em design system. Bom contraste, tipografia consistente, cores harmônicas. Fundos adequados. Jornadas fluidas e intuitivas |
| RNF04 | **Feedback de Tasks Assíncronas** — Loading no botão + aviso "Você será notificado quando ficar pronto". Notificação na interface ao finalizar. Nunca bloqueante |
| RNF05 | **Desempenho** — Filtros e telas rápidos. Nada bloqueante. Queries otimizadas. Uso de índice nas colunas mais buscadas |
| RNF06 | **Multitenancy** — Isolamento total de dados entre tenants desde a primeira migração |
| RNF07 | **Código Limpo** — Type hints em todos os modelos e views. Docstrings em classes e funções. PEP8 |
| RNF08 | **Tratamento de Erros** — Mensagens amigáveis para o usuário. Logs estruturados para o admin |
| RNF09 | **Acessibilidade** — Atributos ARIA, contraste mínimo, navegação por teclado |
| RNF10 | **Performance de Upload** — Compressão automática de imagens. Limite de 5MB por arquivo. Formatos permitidos: JPG, PNG, WebP |

---

## 6. Arquitetura Técnica

### 6.1 Stack Tecnológica

| Camada | Tecnologia |
|--------|------------|
| Backend | Python 3.12+ / Django 6.0 |
| Frontend | Django Templates + Tailwind CSS + JavaScript (Vanilla) |
| Banco (Dev) | SQLite |
| Banco (Prod) | PostgreSQL |
| Task Queue | Celery + RabbitMQ |
| Cache / Broker | Redis |
| Containerização | Docker / Docker Compose |
| IA (futuro) | LangChain / LangGraph |
| Armazenamento | FileSystem (dev) / S3 (prod futuro) |

### 6.2 Estrutura de Diretórios

```
gestao_imob/
├── .env                          # Variáveis de ambiente
├── .env.example                  # Template do .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements.txt
├── core/                         # App principal (settings, urls, wsgi)
│   ├── __init__.py
│   ├── asgi.py
│   ├── urls.py
│   ├── wsgi.py
│   └── settings.py
├── apps/
│   ├── accounts/                 # Autenticação e registro
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   ├── backends.py
│   │   └── templates/
│   ├── tenants/                  # Gerenciamento de tenants (super admin)
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   ├── imoveis/                  # CRUD de imóveis
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── templates/
│   ├── locacoes/                 # Locações e contratos
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── templates/
│   ├── financeiro/               # Pagamentos e fluxo de caixa
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   └── public/                   # Página pública do corretor
│       ├── views.py
│       ├── urls.py
│       └── templates/
├── media/                        # Uploads (fotos, contratos, logos)
├── static/                       # Arquivos estáticos
├── templates/                    # Templates globais
│   ├── base.html
│   ├── includes/
│   └── components/
└── design_system/                # Design tokens e referências
    └── refs/
```

### 6.3 Modelagem de Dados

```
Tenant
├── id, nome, slug (único), logo, cor_primaria, cor_secundaria
├── ativo, data_expiracao, created_by (FK -> User)
└── data_cadastro

Imovel
├── id, tenant (FK -> Tenant)
├── titulo, descricao, tipo (venda/aluguel)
├── valor_venda, valor_aluguel, tamanho_m2
├── quartos, banheiros, vagas
├── endereco, status (disponivel/alugado/vendido/reservado)
├── destaque, ordem, data_cadastro
└── fotos (FK -> FotoImovel)

FotoImovel
├── id, imovel (FK -> Imovel)
├── imagem, thumbnail
└── ordem

Locacao
├── id, imovel (FK -> Imovel)
├── inquilino_nome, inquilino_cpf, inquilino_telefone, inquilino_email
├── data_inicio, data_fim, valor_mensal, dia_vencimento
├── contrato (file), status (ativo/en buzzerrado)
└── data_cadastro

Pagamento
├── id, locacao (FK -> Locacao)
├── mes_referencia, ano_referencia
├── data_pagamento, valor_pago
├── status (pendente/pago/atrasado)
└── observacao
```

### 6.4 Estratégia Multitenant

- **Abordagem:** Isolamento por `tenant_id` em todas as queries (Shared Database)
- **Middleware:** Middleware personalizado que identifica o tenant do usuário logado e adiciona o filtro automaticamente em todas as queries
- **Super Admin:** Visualização global — ignorar filtro de tenant
- **Mídias:** Arquivos organizados em pastas por tenant: `media/tenants/{tenant_id}/fotos/`, `media/tenants/{tenant_id}/contratos/`, `media/tenants/{tenant_id}/logos/`
- **Proteção de Arquivos:** Views que servem arquivos de mídia verificam permissão do usuário

---

## 7. Design System

### 7.1 Core Tokens (globais)

```css
/* Cores base do sistema */
--color-bg-primary: #f8fafc;
--color-bg-secondary: #ffffff;
--color-text-primary: #0f172a;
--color-text-secondary: #475569;
--color-border: #e2e8f0;
--color-success: #22c55e;
--color-warning: #f59e0b;
--color-error: #ef4444;
--color-info: #3b82f6;
```

### 7.2 Cores dos Tenants (dinâmicas)

```css
/* Definidas pelo tenant no painel */
--tenant-color-primary: #1d4ed8;   /* Azul padrão */
--tenant-color-secondary: #f59e0b; /* Âmbar padrão */
```

Essas cores são injetadas no CSS da página pública via `style` inline ou variáveis CSS no `<head>`.

### 7.3 Tipografia

- Font family: `Inter` (sistema) / `system-ui` (fallback)
- Tamanhos: `text-xs` (12px), `text-sm` (14px), `text-base` (16px), `text-lg` (18px), `text-xl` (20px), `text-2xl` (24px), `text-3xl` (30px)

### 7.4 Componentes

- Cards de imóveis com sombra suave e bordas arredondadas
- Botões com estados (hover, active, disabled, loading)
- Formulários com labels flutuantes ou superiores
- Modais para confirmação de ações destrutivas
- Toasts para notificações
- Tabelas responsivas com scroll horizontal em mobile
- Grid responsive: 1 col (mobile), 2 col (md), 3 col (lg), 4 col (xl)

---

## 8. Regras de Segurança

- CSRF protection ativo em todos os formulários
- File upload validation (extensão permitida: jpg, jpeg, png, webp, pdf)
- Tamanho máximo de upload: 5MB por arquivo
- Views da página pública: públicas (sem login)
- Views do painel: exigem login + verificação de pertence ao tenant
- Super admin pode acessar tudo
- Tenant NUNCA vê dados de outro tenant
- Arquivos de mídia servidos via view que verifica permissão (não via `MEDIA_URL` direta)
- Senha temporária exibida apenas uma vez
- Rate limiting em login (futuro)

---

## 9. Experiência do Usuário (UX)

### 9.1 Jornada do Super Admin

1. Acessa `/admin/` → login
2. Cria novo tenant → formulário com dados da pessoa/empresa
3. Sistema gera login + senha aleatória → exibe na tela (única vez)
4. Define prazo de acesso (30/60/90 dias ou data personalizada)
5. Visualiza dashboard global com estatísticas

### 9.2 Jornada do Corretor (Tenant)

1. Recebe link de acesso + credenciais
2. Primeiro login → obrigado a redefinir senha
3. Acessa painel → dashboard com visão geral
4. Cadastra imóveis com fotos e características
5. Personaliza página pública (logo, cores)
6. Quando aluga um imóvel → cadastra locação com dados do inquilino
7. Anexa contrato em PDF
8. Controle financeiro: marca pagamentos como recebidos
9. Visualiza fluxo de caixa mensal

### 9.3 Jornada do Visitante

1. Acessa link público do corretor
2. Visualiza imóveis disponíveis em grid
3. Usa filtros para refinar busca
4. Clica em um imóvel → página de detalhes com galeria
5. Vê informações de contato do corretor

---

## 10. Fluxos de Dados Críticos

### 10.1 Ciclo de Vida de um Imóvel

```
disponível → [alugou] → alugado → [encerrou] → disponível
disponível → [vendeu] → vendido
disponível → [reservou] → reservado → [confirmou] → alugado/vendido
```

### 10.2 Fluxo de Locação + Financeiro

```
Criar Locação
  ├── Imóvel → status = "alugado"
  ├── Gera pagamentos futuros (mês a mês) com status "pendente"
  └── Contrato anexado

Registrar Pagamento
  ├── Status do pagamento → "pago"
  ├── Data de pagamento registrada
  └── Valor entra no fluxo de caixa do mês

Encerrar Locação
  ├── Imóvel → status = "disponível"
  └── Pagamentos futuros cancelados
```

---

## 11. Interface e Experiência

### 11.1 Telas do Painel (Tenant)

| Tela | Funcionalidades |
|------|-----------------|
| **Dashboard** | Resumo: total imóveis, disponíveis, alugados, financeiro do mês |
| **Meus Imóveis** | Lista com busca, filtros. CRUD. Ordenação por destaque |
| **Cadastrar Imóvel** | Formulário completo + upload múltiplo de fotos |
| **Editar Imóvel** | Edição do imóvel + gerenciamento de fotos |
| **Locações** | Lista de locações ativas e encerradas |
| **Nova Locação** | Formulário vinculado a um imóvel |
| **Detalhes Locação** | Dados da locação + contratos + pagamentos |
| **Financeiro** | Dashboard com gráfico de fluxo de caixa mensal |
| **Página Pública** | Personalização: logo, cores, pré-visualização |
| **Configurações** | Dados do perfil, alterar senha |

### 11.2 Telas do Super Admin

| Tela | Funcionalidades |
|------|-----------------|
| **Dashboard** | Estatísticas globais: total tenants, imóveis, locações |
| **Tenants** | Lista de todos os tenants com status e prazo |
| **Criar Tenant** | Formulário de cadastro + geração de senha |
| **Editar Tenant** | Dados, extensão de prazo, ativar/desativar |
| **Detalhes Tenant** | Visão completa dos dados do tenant |

### 11.3 Página Pública

| Seção | Descrição |
|-------|-----------|
| **Header** | Logo ou nome do corretor + cores personalizadas |
| **Filtros** | Tipo, valor, quartos, localização — filtrando via AJAX |
| **Grid Imóveis** | Cards com foto principal, título, valor, tipo, status |
| **Imóvel Individual** | Galeria de fotos, descrição completa, características |
| **Contato** | Informações do corretor (pode ser no rodapé) |
| **Footer** | Links, créditos (se houver) |

---

## 12. Sprints de Desenvolvimento

### Sprint 1 — Setup e Base do Projeto

- [x] Criar ambiente virtual e instalar dependências iniciais (Django, python-decouple, Pillow)
- [x] Configurar `core/settings.py` com variáveis de ambiente via `python-decouple`
- [x] Configurar arquivos `.env` e `.env.example`
- [x] Configurar `ALLOWED_HOSTS`, `TIME_ZONE`, `LANGUAGE_CODE` via `.env`
- [x] Configurar `STATIC_URL`, `STATIC_ROOT`, `MEDIA_URL`, `MEDIA_ROOT`
- [x] Configurar `TEMPLATES` com `DIRS` apontando para `templates/`
- [x] Instalar e configurar Tailwind (via CDN em `base.html`)
- [x] Criar `templates/base.html` com estrutura HTML5 + CDN Tailwind + variáveis CSS + design system Lumion
- [x] Configurar `urls.py` principal com `include` e `static()` para media
- [x] Criar `.gitignore` completo
- [x] Rodar `migrate` e verificar que o projeto sobe (0 issues)
- [x] Criar app `accounts`

### Sprint 2 — Autenticação e Primeiro Acesso

- [x] Criar `apps/accounts/models.py` (UserProfile com `is_tenant`, `must_change_password`)
- [x] Criar `apps/accounts/forms.py` (LoginForm, FirstAccessPasswordChangeForm)
- [x] Criar `apps/accounts/views.py` (LoginView, LogoutView, FirstAccessView, DashboardView)
- [x] Criar `apps/accounts/urls.py` com rotas de login/logout/troca-senha/dashboard
- [x] Criar template `login.html` responsivo (Lumion design system)
- [x] Criar template `first_access.html` (troca de senha obrigatória)
- [x] Criar `apps/accounts/backends.py` (autenticação por username ou e-mail)
- [x] Configurar `AUTHENTICATION_BACKENDS`, `LOGIN_URL`, `LOGIN_REDIRECT_URL`, `LOGOUT_REDIRECT_URL`
- [x] Testar fluxo completo: login → primeiro acesso → redefinir senha → painel (11/11 testes)

### Sprint 3 — Multitenant e App Tenants

- [ ] Criar `apps/tenants/models.py` (model `Tenant` completo)
- [ ] Adicionar `tenant` ForeignKey no `User` (ou criar perfil)
- [ ] Criar middleware `TenantMiddleware` que identifica tenant do usuário logado
- [ ] Criar `apps/tenants/views.py` (CRUD de tenants — apenas super admin)
- [ ] Criar `apps/tenants/forms.py` (TenantForm com geração de senha automática)
- [ ] Criar `apps/tenants/urls.py`
- [ ] Criar templates: `tenant_list.html`, `tenant_form.html`, `tenant_detail.html`
- [ ] Implementar geração de senha aleatória + exibição única via mensagem flash
- [ ] Implementar controle de expiração (bloquear login se expirado)
- [ ] Implementar ativar/desativar tenant
- [ ] Testar isolamento: usuário de um tenant não vê dados de outro

### Sprint 4 — App Imóveis (CRUD + Fotos)

- [ ] Criar `apps/imoveis/models.py` (model `Imovel` + `FotoImovel`)
- [ ] Configurar upload de imagens com compressão via Pillow (máx 1920px, thumbnail 400x300)
- [ ] Criar `apps/imoveis/forms.py` (ImovelForm com upload múltiplo de fotos)
- [ ] Criar `apps/imoveis/views.py` (CRUD completo + ordenação por destaque)
- [ ] Criar `apps/imoveis/urls.py`
- [ ] Criar templates: `imovel_list.html`, `imovel_form.html`, `imovel_detail.html`
- [ ] Implementar upload múltiplo com preview via JavaScript
- [ ] Implementar ordenação drag-and-drop das fotos (opcional)
- [ ] Implementar campo de endereço completo
- [ ] Implementar busca/filtro na listagem
- [ ] Garantir que imóveis são sempre filtrados pelo tenant do usuário logado
- [ ] Testar CRUD completo e upload de imagens

### Sprint 5 — App Locações

- [ ] Criar `apps/locacoes/models.py` (model `Locacao` + campos do inquilino)
- [ ] Implementar signal: ao criar locação → imóvel status = "alugado"
- [ ] Implementar signal: ao encerrar locação → imóvel status = "disponível"
- [ ] Criar `apps/locacoes/forms.py` (LocacaoForm com upload de contrato)
- [ ] Criar `apps/locacoes/views.py` (CRUD completo)
- [ ] Criar `apps/locacoes/urls.py`
- [ ] Criar templates: `locacao_list.html`, `locacao_form.html`, `locacao_detail.html`
- [ ] Implementar upload de contrato (PDF) + documentos adicionais
- [ ] Na tela de detalhes da locação: exibir imóvel, inquilino, contrato, pagamentos
- [ ] Testar fluxo: criar locação → status muda → encerrar → status volta

### Sprint 6 — App Financeiro

- [ ] Criar `apps/financeiro/models.py` (model `Pagamento`)
- [ ] Implementar geração automática de pagamentos ao criar locação (mês a mês)
- [ ] Criar `apps/financeiro/views.py` (listar, marcar como pago, dashboard)
- [ ] Criar `apps/financeiro/urls.py`
- [ ] Criar templates: `pagamento_list.html`, `dashboard_financeiro.html`
- [ ] Implementar dashboard com totais: recebido, a receber, atrasados
- [ ] Implementar filtro por mês/ano no dashboard
- [ ] Implementar gráfico simples de fluxo de caixa (Chart.js ou CSS)
- [ ] Implementar exportação de relatório mensal (futuro)
- [ ] Testar: criar locação → pagamentos gerados → marcar como pago → dashboard atualiza

### Sprint 7 — Página Pública (Personalização + Exibição)

- [ ] Criar `apps/public/views.py` (home do tenant, detalhe do imóvel, filtros AJAX)
- [ ] Criar `apps/public/urls.py` (rota: `/<slug:tenant_slug>/`)
- [ ] Criar `apps/public/templates/` (página pública responsiva)
- [ ] Implementar header com logo (ou nome) + cores personalizadas via variáveis CSS
- [ ] Implementar grid de imóveis responsivo (1/2/3/4 colunas)
- [ ] Implementar card de imóvel com: foto, título, valor, tipo, localização
- [ ] Implementar página individual do imóvel com galeria de fotos
- [ ] Implementar filtros AJAX: tipo, valor (range), quartos, localização
- [ ] Implementar "sem resultados" amigável
- [ ] Configurar view pública sem exigir login
- [ ] Garantir que imóveis com status != "disponível" não aparecem
- [ ] Testar navegação completa na página pública

### Sprint 8 — Personalização da Página no Painel

- [ ] Criar seção no painel do tenant para personalização
- [ ] Formulário: upload de logo, nome (fallback), cores primária/secundária
- [ ] Seletor de cor (color picker) com preview ao vivo
- [ ] Pré-visualização da página pública dentro do painel (embed ou screenshot)
- [ ] Salvar configurações e refletir na página pública
- [ ] Testar: alterar logo/cores → página pública atualiza

### Sprint 9 — Notificações e Tasks Assíncronas

- [ ] Configurar Celery + Redis (ou RabbitMQ)
- [ ] Configurar `CELERY_BROKER_URL` e `CELERY_RESULT_BACKEND`
- [ ] Criar `tasks.py` nos apps relevantes (ex: compressão de imagens)
- [ ] Implementar sistema de notificações no frontend (toast via JavaScript ou Django Messages + polling SSE)
- [ ] Botão com estado de loading (desabilitado + spinner) durante task
- [ ] Notificação de conclusão com mensagem amigável
- [ ] Testar fluxo: disparar task → loading → notificação

### Sprint 10 — Proteção de Mídia e Ajustes Finais

- [ ] Criar view para servir arquivos de mídia com verificação de permissão
- [ ] Desabilitar `MEDIA_URL` direta (ou proteger com `X-Accel-Redirect`/`X-Sendfile`)
- [ ] Validar extensões e tamanhos de upload em todos os formulários
- [ ] Implementar verificação de expiração no login (tenant expirado)
- [ ] Testes de segurança: tentar acessar mídia de outro tenant
- [ ] Testes de isolamento: tenant A não vê dados do tenant B
- [ ] Revisão de responsividade em todos os templates
- [ ] Revisão de mensagens de erro e validação
- [ ] Otimizar queries (select_related, prefetch_related, índices)

### Sprint 11 — Docker e Deploy

- [ ] Criar `Dockerfile` com configuração multi-estágio
- [ ] Criar `docker-compose.yml` com Django, PostgreSQL, Redis, Celery
- [ ] Criar `entrypoint.sh` com migrate + collectstatic + start
- [ ] Configurar PostgreSQL em produção
- [ ] Configurar `whitenoise` para servir estáticos
- [ ] Configurar env vars de produção
- [ ] Testar build e execução com Docker
- [ ] Escrever instruções de deploy no README.md

### Sprint 12 — Testes e Documentação

- [ ] Configurar pytest + pytest-django
- [ ] Criar testes de modelos para todos os apps
- [ ] Criar testes de views para todos os CRUDs
- [ ] Criar testes de segurança (isolamento multitenant)
- [ ] Criar testes de API (se houver)
- [ ] Criar testes de tasks (Celery)
- [ ] Cobrir fluxos críticos: locação → pagamento → dashboard
- [ ] Documentar setup local no README.md
- [ ] Documentar arquitetura no PRD.md (este arquivo)
- [ ] Documentar decisões técnicas em ADRs (se necessário)

---

## 13. Critérios de Aceitação (Geral)

- [ ] Super admin consegue criar, editar, desativar e visualizar tenants
- [ ] Tenant consegue fazer login e é obrigado a trocar senha no primeiro acesso
- [ ] Tenant consegue cadastrar, editar e excluir imóveis com fotos
- [ ] Ao cadastrar locação, status do imóvel muda automaticamente
- [ ] Pagamentos são gerados automaticamente e podem ser marcados como pagos
- [ ] Dashboard financeiro reflete os pagamentos corretamente
- [ ] Página pública exibe apenas imóveis disponíveis do tenant
- [ ] Cores e logo personalizadas refletem na página pública
- [ ] Tenant A NÃO vê dados do Tenant B
- [ ] Visitante consegue navegar e filtrar imóveis sem login
- [ ] Visitante NÃO TEM acesso a nenhuma rota do painel
- [ ] Sistema é 100% responsivo
- [ ] Uploads são validados e comprimidos
- [ ] Tasks assíncronas mostram loading e notificam ao concluir

---

## 14. Glossário

| Termo | Definição |
|-------|-----------|
| **Tenant** | Cliente do sistema (corretor ou imobiliária). Cada tenant é isolado dos demais |
| **Super Admin** | Administrador geral do sistema, gerencia todos os tenants |
| **Locação** | Contrato de aluguel de um imóvel para um inquilino |
| **Pagamento** | Registro mensal de recebimento de aluguel |
| **Fluxo de Caixa** | Saldo mensal de recebimentos de aluguel |
| **Página Pública** | Site personalizado do tenant para divulgar imóveis |
| **Multitenant** | Arquitetura onde múltiplos clientes compartilham o mesmo sistema com dados isolados |

---

## 15. Referências

- Design system tokens: `design_system/refs/`
- Documentação Django 6.0: https://docs.djangoproject.com/en/6.0/
- Documentação Tailwind CSS: https://tailwindcss.com/docs
- Documentação Celery: https://docs.celeryq.dev/
