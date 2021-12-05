# HTMX

Htmx é uma biblioteca que permite acessar recursos modernos do navegador diretamente de HTML, em vez de usar javascript.

## Instalação

`HTMX` é uma biblioteca javascript livre de dependências. Ele pode ser usado via NPM como "htmx.org" ou baixado ou incluído a partir do unpkg ou de seu outro CDN baseado em NPM favorito:

``` bash
<script src="https://unpkg.com/htmx.org@1.6.1"></script>
```

## Uso

O núcleo do htmx é um conjunto de atributos que permitem emitir solicitações AJAX diretamente do HTML:

_Exemplo_:

``` markdown
  <div hx-put="/messages">
    Mensagem
  </div>
```

## Atributos utilizados no projeto

| Attributo | Descrição |
|-----------|-------------|
| [hx-get](/attributes/hx-get) | Emite uma solicitação `GET` para o URL fornecido|
| [hx-post](/attributes/hx-post) | Emite uma solicitação `POST` para o URL fornecido
| [hx-delete](/attributes/hx-delete) | Emite uma solicitação `DELETE` para o URL fornecido

# Opinião

O uso do HTMX foi útil neste projeto, mas devido ser um projeto pequeno e de baixa complexidade. Utilizar a tecnologia Javascript de maneira oculta nas tags HTML não nos trazem domnínio completo do que se pode fazer utilizando diretamente a linguaguem proposta. Nos exime o controle sobre os erros e impede de desenvolver um melhor produto, se o mesmo for de média ou larga escala.

Em resumo, apesar do não aprofundamento geral da tecnologia (`HTMX`) não recomendo o uso da ferramenta de modo geral.