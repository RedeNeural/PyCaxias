# PyCaxias 2026 — site

Site do evento da comunidade Python de Caxias do Sul.
Gerado com [Pelican](https://docs.getpelican.com/), sem framework de CSS e sem jQuery.

**Evento:** 26 de setembro de 2026 · sábado · Uniftec Caxias do Sul

---

## Rodando local

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

invoke serve      # http://localhost:8000, recarrega ao salvar
```

Outras tarefas:

```shell
invoke build      # gera em output/
invoke publish    # gera com as URLs de produção (publishconf.py)
invoke gh-pages   # publica no branch gh-pages
invoke clean      # apaga output/
```

---

## Onde mexer em cada coisa

### Datas, local, links, contatos → `pelicanconf.py`

Tudo que muda de um ano para o outro está no topo do arquivo. O tema lê esses
valores; nenhum template tem data ou endereço escrito na mão.

| Variável | Para quê serve |
| --- | --- |
| `SITEYEAR` | Filtra o conteúdo do ano. **Só aparece no site o conteúdo com `Date` deste ano.** |
| `DAY_EVENT`, `DAY_EVENT_SHORT` | Data por extenso e curta |
| `DAY_EVENT_ISO` | Alimenta a contagem regressiva e o schema.org |
| `LOCAL`, `LOCAL_ADDRESS`, `LOCAL_MAP` | Local do evento |
| `INCRICAO_OPENED` + `INSCRICAO_LINK` | Liga a seção de ingressos e o botão do topo |
| `CALL_FOR_PAPERS_OPENED` + `CALL_FOR_PAPERS` | Liga os botões de envio de palestra |
| `MENU`, `OLD_EVENTS` | Navegação e lista de edições anteriores |
| `CONTATOS`, `SOCIAL`, `EMAIL` | Rodapé e seção de contato |

### Agenda → `content/horarios/*.md`

Um arquivo por item da grade. A ordem na página vem do campo `Date`.

```markdown
Title: Observabilidade em microserviços
Date: 2026-09-26 09:45
Category: horarios
Tags: horarios
Slug: palestra2
Author: Nome de quem palestra

Texto opcional. Se existir, o item da agenda vira link para uma página própria
da palestra. Se ficar vazio, o item aparece só na grade.
```

Para coffee break, almoço e credenciamento, acrescente `Tipo: intervalo` — o item
fica visualmente mais discreto que as palestras.

### Patrocinadores → `content/patrocinadores/*.md`

```markdown
Title: Nome da empresa
Save_as:
URL:
Subtitle: Frase que aparece ao passar o mouse
Date: 2026-05-01 08:30
Category: diamante
imagem: /theme/img/patrocinadores/2026/empresa.png
imagem_alt: Logo da Empresa
link: https://empresa.com.br/
```

`Category` aceita `diamante`, `ouro`, `prata` ou `apoiadores`.
As linhas `Save_as:` e `URL:` vazias impedem que o Pelican crie uma página para
cada patrocinador — não remova.

Os logos de 2025 já estão em `theme/static/img/patrocinadores/2025/`. **Os
arquivos em `content/patrocinadores/` ainda estão com data de 2025**, ou seja,
não aparecem no site. Conforme cada empresa confirmar para 2026, mude o `Date`
para 2026 e aponte a `imagem` para a pasta nova.

Enquanto nenhum patrocinador estiver confirmado, a seção mostra sozinha uma
chamada de "cotas abertas" com o botão de contato.

### Palestrantes → `content/palestrantes/*.md`

```markdown
Title: Nome da pessoa
Date: 2026-09-26 09:45
Category: palestrantes
Slug: nome-da-pessoa
image: nome-da-pessoa.png
palestra: Título da palestra

Mini biografia.
```

A foto vai em `theme/static/img/palestrantes/`, quadrada, de preferência 800×800.
Sem nenhum arquivo nessa categoria, a seção vira um convite ao call for papers.

---

## Identidade visual

Manual de 2026 por **Fabio Agto** ([@fabio_agto](https://www.instagram.com/fabio_agto)).

### Cores (em `theme/static/css/pycaxias.css`, bloco `:root`)

| Token | Hex | Uso |
| --- | --- | --- |
| `--neon` | `#64FF00` | Ações, destaques, o verde que puxa o olho |
| `--lima` | `#95C22E` | Rótulos, detalhes, estados intermediários |
| `--sage` | `#D2DDB8` | Base do texto |
| `--floresta` | `#00230F` | Fundo das seções alternadas |
| `--void` | `#04070A` | Fundo geral |
| `--magenta` / `--azul` | `#FF2E9F` / `#29A9E0` | Pontos de apoio, usados com parcimônia |

### Tipografia — atenção

O manual pede **Play Pretend** (institucional) e **Metropolis** (auxiliar).
Nenhuma das duas está no Google Fonts, então o site usa substitutas próximas:

- **Saira** no lugar da Play Pretend — o eixo de largura em 118% + itálico
  aproxima bem o lettering largo e inclinado do manual
- **Poppins** no lugar da Metropolis — mesma lógica geométrica
- **JetBrains Mono** para horários, rótulos e dados

Para trocar pelas fontes reais quando as licenças estiverem em mãos:

1. coloque os `.woff2` em `theme/static/fonts/`
2. declare os `@font-face` no topo do `pycaxias.css`
3. mude só `--fonte-display` e `--fonte-corpo` no bloco `:root`

Nenhuma outra regra do CSS precisa mudar.

### Imagens da marca

Extraídas do PDF do manual, em `theme/static/img/`:

| Arquivo | O que é |
| --- | --- |
| `logo-2026.png` | Assinatura horizontal, fundo transparente |
| `logo-2026-stack.png` | Assinatura empilhada (rodapé) |
| `simbolo-2026.png` | Só o símbolo da cobra |
| `elemento-cobra.png` | Traço de apoio usado atrás do hero |
| `favicon.png`, `apple-touch-icon.png` | Ícones |
| `og-pycaxias-2026.png` | Imagem de compartilhamento, 1200×630 |

---

## O que mudou em relação ao site anterior

- Saiu o template comprado **TheEvent** (BootstrapMade) e toda a atribuição dele
- Saíram jQuery, Bootstrap, superfish, wow.js, venobox, owlcarousel e Font Awesome —
  cerca de 1 MB de JS e CSS. O site agora carrega **um CSS e um JS**, sem dependência externa
- O logo do cabeçalho não está mais chumbado em 2024
- Marcação semântica: `schema.org/Event`, Open Graph, `<time datetime>`, skip link,
  foco de teclado visível, `prefers-reduced-motion` respeitado
- Seções vazias viram convite à ação em vez de sumirem da página
- Contagem regressiva calculada a partir de `DAY_EVENT_ISO`
- Folha de estilo de impressão: a grade do dia cabe numa folha A4

## Pendências

- [ ] Confirmar o endereço da Uniftec em `LOCAL_ADDRESS` (está com o do campus da
      Rua Ludovico Cavinato — conferir qual bloco recebe o evento)
- [ ] Abrir inscrições: preencher `INSCRICAO_LINK` e virar `INCRICAO_OPENED = True`
- [ ] Atualizar o PDF do plano de patrocínio com a data e o local novos
      (`theme/static/pdf/`) — os arquivos ainda são os de 2025
- [ ] Licenciar Play Pretend e Metropolis, ou fechar com as substitutas
- [ ] Copiar a pasta `old/` do repositório atual para manter as edições anteriores no ar
- [ ] Trocar `GA_ID` se a propriedade do Analytics mudar
