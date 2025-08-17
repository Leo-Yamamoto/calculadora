# Calculadora Web com Dash

Este projeto é uma calculadora web desenvolvida em Python utilizando o framework [Dash](https://dash.plotly.com/) e [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/). A interface é responsiva e amigável, permitindo realizar operações matemáticas básicas diretamente no navegador.

## Funcionalidades

- Soma, subtração, multiplicação e divisão
- Porcentagem
- Raiz quadrada
- Limpar visor
- Backspace
- Interface visual semelhante a uma calculadora física

## Requisitos

- Python 3.8 ou superior
- [UV](https://github.com/astral-sh/uv) (recomendado para ambiente virtual e instalação de dependências)
- Dash
- Dash Bootstrap Components

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/Leo-Yamamoto/calculadora.git
cd calculadora
```

### 2. Instale o UV (se ainda não tiver)

```bash
pip install uv
```

### 3. Crie e ative o ambiente virtual com UV

```bash
uv venv
```

- Para ativar no PowerShell:

  ```bash
  .\.venv\Scripts\Activate.ps1
  ```

- Para ativar no CMD:

  ```bash
  .\.venv\Scripts\activate.bat
  ```

### 4. Instale as dependências com UV

```bash
uv pip install dash dash-bootstrap-components
```

## Como executar

1. Navegue até a pasta `src`:

   ```bash
   cd src
   ```

2. Execute o arquivo principal:

   ```bash
   uv run python main.py
   ```

3. Abra o navegador e acesse [http://127.0.0.1:8050/](http://127.0.0.1:8050/)

## Personalização

- Para adicionar novas funcionalidades, modifique o arquivo `src/main.py`.
- Para adicionar bibliotecas, digite uv add [biblioteca]

## Licença

Este projeto está sob a licença MIT.

---

Desenvolvido por Leonardo Yamamoto.
