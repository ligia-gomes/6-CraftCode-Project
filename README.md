# CraftCode-Project
Automacao local de relatorios mensais usando Python, com validacoes e comparacoes entre o mes atual e o mes anterior.

## Visao geral
- Le os arquivos de entrada locais.
- Processa e cria os relatorios do mes.
- Compara com o relatorio anterior e pede confirmacao manual se a diferenca ultrapassar o limite.
- Salva os arquivos na estrutura padrao de pastas por ano/mes.

## Estrutura de pastas
```
/
  comparisons_functions.py
  functions.py
  main.py
  report_1/
  report_2/
  report_3/
  report_4/
  report_x/
```

Cada pasta `report_*` possui:
- `comparison_report_*.py`: compara a estrutura e volume com o relatorio anterior.
- `file_report_*.py`: gera o dataframe do relatorio (com pseudocodigo comentado).
- `save_report_*.py`: salva o arquivo final no output.

## .env (local)
Crie um `.env` na raiz do projeto (use `.env.example` como base):
```
input=C:/Users/your_user/Documents/Input/
output=C:/Users/your_user/Documents/Output/
```

O sistema cria a estrutura por ano/mes dentro destes caminhos.

## Como rodar
```
python main.py
```

Menu principal:
```
Do you want to:
1 - Run all reports
2 - Run a specific report
3 - Run a sequence or batch of reports
```

## Observacoes
- O projeto usa pseudocodigo nos `file_report_*` para preservar confidencialidade.
- As comparacoes pedem confirmacao quando a variacao passa de 5%.
