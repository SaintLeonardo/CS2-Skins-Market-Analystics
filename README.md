# CS2 Skin Market Analytics

Projeto para coletar, armazenar e analisar dados de mercado de skins do Counter-Strike 2.

## Estrutura

- `data/raw/`: dados brutos coletados das fontes externas.
- `data/processed/`: dados tratados para analises.
- `scripts/`: scripts executaveis de coleta e analise.
- `src/`: codigo reutilizavel do projeto.
- `notebooks/`: experimentos e analises exploratorias.
- `dashboards/`: dashboards e visualizacoes.
- `reports/`: relatorios gerados.
- `docs/`: documentacao do projeto.
- `tests/`: testes automatizados.
- `infra/`: configuracoes de infraestrutura, banco e Docker.

## Scripts atuais

- `scripts/collect_skin_price.py`: coleta preco e volume da skin AK-47 Redline no Steam Market e salva em `data/raw/skins_data.csv`.
- `scripts/analyze_skin_price.py`: script de analise criado para o projeto.

## Como executar

```bash
python scripts/collect_skin_price.py
```

## Dependencias iniciais

```bash
pip install requests
```
