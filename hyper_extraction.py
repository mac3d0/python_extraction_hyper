from datetime import datetime
import argparse, pantab, zipfile

parser = argparse.ArgumentParser('''

 /$$                                                                           /$$                                    /$$     /$$                    
| $$                                                                          | $$                                   | $$    |__/                    
| $$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$         /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$  /$$$$$$   /$$$$$$$ /$$$$$$   /$$  /$$$$$$  /$$$$$$$ 
| $$__  $$| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$       /$$__  $$|  $$ /$$/|_  $$_/   /$$__  $$|____  $$ /$$_____/|_  $$_/  | $$ /$$__  $$| $$__  $$
| $$  \ $$| $$  | $$| $$  \ $$| $$$$$$$$| $$  \__/      | $$$$$$$$ \  $$$$/   | $$    | $$  \__/ /$$$$$$$| $$        | $$    | $$| $$  \ $$| $$  \ $$
| $$  | $$| $$  | $$| $$  | $$| $$_____/| $$            | $$_____/  >$$  $$   | $$ /$$| $$      /$$__  $$| $$        | $$ /$$| $$| $$  | $$| $$  | $$
| $$  | $$|  $$$$$$$| $$$$$$$/|  $$$$$$$| $$            |  $$$$$$$ /$$/\  $$  |  $$$$/| $$     |  $$$$$$$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$
|__/  |__/ \____  $$| $$____/  \_______/|__/             \_______/|__/  \__/   \___/  |__/      \_______/ \_______/   \___/  |__/ \______/ |__/  |__/
           /$$  | $$| $$                                                                                                                             
          |  $$$$$$/| $$                                                                                                                             
           \______/ |__/                                                                                                                                                                                                                                                                                                                                                                                                                                       
Made by Rafael Macedo
''')

parser.add_argument('--extrair', '-ex', help='caminho do arquivo a ser extraido | se tiver na mesma pasta do arquivo não precisa por caminho apenas o nome', required=False)
parser.add_argument('--converter', '-cv', help="faz a conversão do .hyper para .csv | caminho padrão \Data\Extracts | argumento opcional", default="Data\Extracts\EXT_CHAT_CONSOLE_ATE_FDA.hyper", required=False)
parser.add_argument('--output', '-o', help='nomear o arquivo', required=False)
args = vars(parser.parse_args())

extrair = args['extrair']
converter = args['converter']
output = args['output']

def pacote():
    unzip = zipfile.ZipFile(extrair)
    unzip.extractall()
    unzip.close()

def extracao():
    get_tables_from_hyper = pantab.frames_from_hyper(converter)

    for index, item in enumerate(get_tables_from_hyper):
        formated_table_name = str(item.name).replace('"', '')
        timestamp = "{:%Y_%m_%d_%H_%M_%S}".format(datetime.now())

        extract_all_tables = pantab.frame_from_hyper(source=converter, table=item)
        extract_all_tables.to_csv(
            r"{}_tabela_{}_{}.csv".format(output, formated_table_name, timestamp),
            index=False,
            header=True,
        )

new_extrair = str(extrair)

if __name__ == '__main__':
    if extrair == new_extrair.endswith('tdsx'):#""[25:]: controla o tamanho do arquivo.
        pacote()
        extracao()
    elif extrair == None:
        extracao()
    elif extrair == extrair:
        pacote()
        extracao()
