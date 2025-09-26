import PySimpleGUI as sg
import requests
import os

# Função para baixar imagens
def download_image(url, folder, name):
    os.makedirs(folder, exist_ok=True)
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        with open(os.path.join(folder, name), "wb") as f:
            f.write(r.content)
        return f"✅ {name} baixado com sucesso!"
    except requests.exceptions.HTTPError:
        return f"⚠️ Imagem não encontrada: {name}"
    except Exception as e:
        return f"❌ Erro em {name}: {e}"

# Layout da interface
layout = [
    [sg.Text("Nome da coleção:"), sg.Input(key="nome")],
    [sg.Text("Código da coleção:"), sg.Input(key="cod")],
    [sg.Text("Sigla:"), sg.Input(key="sigla")],
    [sg.Text("Número da carta inicial:"), sg.Input(key="ncartas")],
    [sg.Text("Número máximo de cartas:"), sg.Input(key="nmax")],
    [sg.Button("Baixar Imagens"), sg.Button("Sair")],
    [sg.Output(size=(60, 20))]
]

# Criar janela
window = sg.Window("Downloader de Imagens - Coleções", layout)

# Loop da interface
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Sair"):
        break

    if event == "Baixar Imagens":
        try:
            nome = values["nome"].strip()
            cod = values["cod"].strip()
            sigla = values["sigla"].strip()
            ncartas = int(values["ncartas"])
            nmax = int(values["nmax"])

            pasta = os.path.join("imagens_salvas", nome)

            print(f"\n📥 Iniciando download da coleção '{nome}'...\n")

            for n in range(1, nmax + 1):
                url = f"https://dz3we2x72f7ol.cloudfront.net/expansions/{nome}/pt-br/{cod}{n}.png"
                nome_arq = f"{str(n).zfill(3)}-{ncartas} {sigla}.png"
                print(download_image(url, pasta, nome_arq))

            print("\n✅ Download concluído!")

        except Exception as e:
            print(f"❌ Erro: {e}")

window.close()
