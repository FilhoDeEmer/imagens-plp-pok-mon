import requests
import os

# Função para baixar a imagem
def download_image(image_url, folder='imagens_salvas', image_name='image.png'):
    if not os.path.exists(folder):
        os.makedirs(folder)  # Cria a pasta se não existir
    
    try:
        # Fazendo a requisição HTTP para pegar a imagem
        response = requests.get(image_url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        # Salvando o conteúdo da imagem no arquivo
        image_path = os.path.join(folder, image_name)
        with open(image_path, 'wb') as file:
            file.write(response.content)
        print(f"Imagem salva com sucesso: {image_path}")

    except Exception as e:
        print(f"Erro ao baixar imagem: {e}")

# Início
nomeCollection = input("Informe o nome da coleção (Ex.: surging-sparks): ")
codCollection = input("Informe o código da coleção (Ex.: SV08_PTBR_): ")
siglaCollection = input("Informe a sigla da coleção (Ex.: SSP): ")
nCartas = int(input("Informe o numero de cartas:  "))
nMax = int(input("Informe número máximo de cartas da coleção (Ex.: 252): "))  # Convertendo para int

nomePasta = 'imagens_salvas'  # Pasta principal onde as coleções serão salvas

# Criando o nome da pasta da coleção dentro de 'imagens_salvas'
folder_name = os.path.join(nomePasta, nomeCollection)

# Criando a pasta principal e a pasta da coleção
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Laço para iterar de 1 até nMax
for n in range(1, nMax + 1):
    # Formatar a URL com o número da imagem
    image_url = f"https://dz3we2x72f7ol.cloudfront.net/expansions/{nomeCollection}/pt-br/{codCollection}{n}.png"
    
    # Formatando o nome da imagem com a numeração (3 dígitos) e a sigla
    image_name = f"{str(n).zfill(3)}-{nCartas} {siglaCollection}.png"
    
    # Chama a função para fazer o download da imagem
    download_image(image_url, folder_name, image_name)
