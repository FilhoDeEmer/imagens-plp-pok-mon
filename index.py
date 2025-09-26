import tkinter as tk
from tkinter import scrolledtext, messagebox
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

# Função chamada ao clicar no botão
def start_download():
    try:
        nome = entry_nome.get().strip()
        cod = entry_cod.get().strip()
        sigla = entry_sigla.get().strip()
        ncartas = int(entry_ncartas.get().strip())
        nmax = int(entry_nmax.get().strip())

        pasta = os.path.join("imagens_salvas", nome)

        log_box.delete(1.0, tk.END)  # limpa o log
        log_box.insert(tk.END, f"\n📥 Iniciando download da coleção '{nome}'...\n\n")

        for n in range(1, nmax + 1):
            url = f"https://dz3we2x72f7ol.cloudfront.net/expansions/{nome}/pt-br/{cod}{n}.png"
            nome_arq = f"{str(n).zfill(3)}-{ncartas} {sigla}.png"
            msg = download_image(url, pasta, nome_arq)
            log_box.insert(tk.END, msg + "\n")
            log_box.see(tk.END)  # scroll automático

        log_box.insert(tk.END, "\n✅ Download concluído!\n")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# ------------------- INTERFACE -------------------
root = tk.Tk()
root.title("Downloader de Imagens - Coleções")
root.geometry("550x500")

# Labels e Entrys
tk.Label(root, text="Nome da coleção:").pack(anchor="w", padx=10, pady=2)
entry_nome = tk.Entry(root, width=50)
entry_nome.pack(padx=10)

tk.Label(root, text="Código da coleção:").pack(anchor="w", padx=10, pady=2)
entry_cod = tk.Entry(root, width=50)
entry_cod.pack(padx=10)

tk.Label(root, text="Sigla:").pack(anchor="w", padx=10, pady=2)
entry_sigla = tk.Entry(root, width=50)
entry_sigla.pack(padx=10)

tk.Label(root, text="Número da carta inicial:").pack(anchor="w", padx=10, pady=2)
entry_ncartas = tk.Entry(root, width=20)
entry_ncartas.pack(padx=10)

tk.Label(root, text="Número máximo de cartas:").pack(anchor="w", padx=10, pady=2)
entry_nmax = tk.Entry(root, width=20)
entry_nmax.pack(padx=10)

# Botão
btn = tk.Button(root, text="Baixar Imagens", command=start_download, bg="#007bff", fg="white")
btn.pack(pady=10)

# Caixa de log
log_box = scrolledtext.ScrolledText(root, width=70, height=15)
log_box.pack(padx=10, pady=10)

root.mainloop()
