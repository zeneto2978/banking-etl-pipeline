# Banking ETL Pipeline

Projeto de engenharia de dados em nível iniciante forte.

## Tecnologias
- Python
- Pandas
- SQL
- PostgreSQL
- Git
- GitHub
- GitHub Actions

## Estrutura
- Bronze: dados brutos
- Silver: dados tratados
- Gold: camada analítica futura

## Scripts
- `scripts/extract.py`: gera dados brutos
- `scripts/transform.py`: trata os dados
- `scripts/load_postgres.py`: carrega dados no PostgreSQL
- `main.py`: executa o pipeline local
- `tests/test_files.py`: testes básicos

## Como rodar

```bash
python main.py
pytest