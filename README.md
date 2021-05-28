# python_extraction_hyper
Script em Python3 que descompacta arquivos com extenções .tds e faz a conversão de arquivos .hyper para .csv

EXEMPLOS DE USO

Por padrão ele faz uma busca pela extenção .hyper dentro da pasta Data que é gerada usando o primeiro argumento. 
$ python3 hyper_extraction.py --extrair caminho_do-arquivo.tds --converter caminho_do.hyper

Pode apenas extrair um .tds usando apenas o argumento --extrair
$ python3 hyper_extraction.py --extrair caminho_do-arquivo.tds -o nome_de_renomeação

fazer conversão do arquivo .hyper usando o --converter
$ python3 hyper_extraction.py --converter caminho_do-arquivo.hyper -o nome_de_renomeação
