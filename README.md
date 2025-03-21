
# Rate limiting

Este projeto tem como objetivo desenvolver uma solução eficiente de rate limiting para controlar as requisições de um payload.


## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/)
- [Redis](https://redis.io/docs/latest/commands/)
- [Poetry](https://python-poetry.org/)
## Instalação e Configuração

1 - Clone o repositório do projeto e acesse o diretório correspondente

```bash
  git clone https://github.com/williansebastiao/rate_limiting
```

2- Entre no diretório criado

```bash
  cd rate_limiting
```

3- Configure o projeto

```bash
  make scaffold
```

4 - Suba os containers

```bash
  make build
```

5 - Acesse a url do swagger

```bash
http://localhost:8000/api/docs
```

## Configuração no VS Code

Caso utilize o Visual Studio Code como IDE, é recomendável configurar o ambiente virtual criado pelo Poetry. Para isso, defina o interpretador do Python para o caminho correto dentro do VS Code:

1- Acesse Command Palette (Ctrl+Shift+P) e busque por Python: Select Interpreter.

2 - Selecione o ambiente gerenciado pelo Poetry, geralmente localizado em:

```bash
~/.cache/pypoetry/virtualenvs/nome-do-projeto/bin/python
```

## Análise de Código (Linting)

O projeto já possui ferramentas de lint configuradas para garantir padrões de qualidade no código. Para executar a verificação, utilize o seguinte comando:

```bash
  make lint
```

## Testes

Para rodar os testes unitários e garantir a integridade do código, execute:

```bash
  make test
```
