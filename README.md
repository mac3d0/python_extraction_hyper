# python_extraction_hyper

Script em Python 3 para trabalhar com artefatos do **Tableau**: descompacta arquivos `.tds`/`.tdsx` e converte extratos `.hyper` para **CSV**, facilitando a análise e a extração de dados durante avaliações e investigações.

## Requisitos

- Python 3

## Uso

Por padrão, o script busca a extensão `.hyper` dentro da pasta `Data` gerada a partir do arquivo informado.

```bash
# Extrair um .tds e converter o .hyper resultante
python3 hyper_extraction.py --extrair caminho/arquivo.tds --converter caminho/arquivo.hyper

# Apenas extrair um .tds
python3 hyper_extraction.py --extrair caminho/arquivo.tds -o nome_de_saida

# Apenas converter um .hyper para CSV
python3 hyper_extraction.py --converter caminho/arquivo.hyper -o nome_de_saida
```

| Argumento | Alias | Descrição |
|-----------|-------|-----------|
| `--extrair` | `-ex` | Caminho do arquivo `.tds` a ser descompactado |
| `--converter` | `-cv` | Converte o `.hyper` para `.csv` |
| `--output` | `-o` | Nome do arquivo de saída |

## Licença

Distribuído sob a licença incluída em [`LICENSE`](LICENSE).
