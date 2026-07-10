# python_extraction_hyper

Um script em Python 3 para trabalhar com artefatos do Tableau. Ele descompacta arquivos .tds e .tdsx e converte extratos .hyper para CSV, o que ajuda na análise e na extração de dados durante avaliações e investigações.

## Requisitos

Python 3.

## Uso

Por padrão o script procura a extensão .hyper dentro da pasta Data que é gerada a partir do arquivo informado.

```bash
python3 hyper_extraction.py --extrair caminho/arquivo.tds --converter caminho/arquivo.hyper
```

Para só descompactar um .tds:

```bash
python3 hyper_extraction.py --extrair caminho/arquivo.tds -o nome_de_saida
```

Para só converter um .hyper em CSV:

```bash
python3 hyper_extraction.py --converter caminho/arquivo.hyper -o nome_de_saida
```

O `--extrair` ou `-ex` recebe o .tds a ser descompactado. O `--converter` ou `-cv` converte o .hyper para .csv. O `--output` ou `-o` define o nome do arquivo de saída.

## Licença

Distribuído sob a licença que está no arquivo LICENSE.
