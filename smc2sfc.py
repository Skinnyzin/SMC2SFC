import os
import customtkinter as ctk
from tkinter import filedialog, messagebox

# ==========================================
# CONFIGURAÇÃO DE TEMA DO CUSTOMTKINTER
# ==========================================
ctk.set_appearance_mode("System")  # Segue o tema do sistema (Dark/Light)
ctk.set_default_color_theme("blue")  # Tema de cores dos botões

def selecionar_pasta():
    """Abre uma janela para o usuário escolher o diretório base."""
    pasta = filedialog.askdirectory(initialdir=os.getcwd(), title="Selecione a pasta raiz")
    if pasta:
        entrada_pasta.delete(0, 'end')
        entrada_pasta.insert(0, pasta)

def log_mensagem(mensagem):
    """Adiciona uma mensagem à caixa de texto e rola para o final."""
    caixa_texto.insert('end', mensagem + "\n")
    caixa_texto.see('end')
    janela.update_idletasks()

def converter_smc_para_sfc():
    """Função principal de conversão."""
    pasta_principal = entrada_pasta.get()
    
    if not os.path.isdir(pasta_principal):
        messagebox.showerror("Erro", "Por favor, selecione uma pasta válida.")
        return

    # Limpa a caixa de texto antes de começar e desativa o botão
    caixa_texto.delete('1.0', 'end')
    btn_converter.configure(state="disabled", text="Convertendo...")
    arquivos_renomeados = 0

    log_mensagem(f"Iniciando busca em:\n{pasta_principal}\n")
    log_mensagem("Vasculhando subpastas...\n" + "-"*40)

    for raiz, diretorios, arquivos in os.walk(pasta_principal):
        for arquivo in arquivos:
            if arquivo.lower().endswith('.smc'):
                nome_base = os.path.splitext(arquivo)[0]
                novo_nome = nome_base + ".sfc"
                
                caminho_antigo = os.path.join(raiz, arquivo)
                caminho_novo = os.path.join(raiz, novo_nome)
                
                os.rename(caminho_antigo, caminho_novo)
                
                caminho_relativo = os.path.relpath(caminho_novo, pasta_principal)
                log_mensagem(f"✓ {caminho_relativo}")
                arquivos_renomeados += 1

    # Resumo final
    log_mensagem("-" * 40)
    if arquivos_renomeados == 0:
        log_mensagem("\nNenhum arquivo .smc encontrado.")
    else:
        log_mensagem(f"\nSucesso! {arquivos_renomeados} arquivo(s) convertido(s).")
    
    # Restaura o botão
    btn_converter.configure(state="normal", text="Iniciar Conversão")

# ==========================================
# CONSTRUÇÃO DA INTERFACE
# ==========================================

janela = ctk.CTk()
janela.title("Conversor SMC > SFC")
janela.geometry("650x500")
janela.resizable(False, False)

# Título no topo
titulo = ctk.CTkLabel(janela, text="Conversor de ROMs (.smc para .sfc)", font=ctk.CTkFont(size=20, weight="bold"))
titulo.pack(pady=(20, 10))

# Frame para agrupar o input e o botão de busca
frame_pasta = ctk.CTkFrame(janela, fg_color="transparent")
frame_pasta.pack(pady=10, padx=20, fill="x")

entrada_pasta = ctk.CTkEntry(frame_pasta, placeholder_text="Selecione ou cole o caminho da pasta...", width=450, height=35)
entrada_pasta.insert(0, os.getcwd())
entrada_pasta.pack(side="left", padx=(0, 10))

btn_procurar = ctk.CTkButton(frame_pasta, text="Procurar", command=selecionar_pasta, width=100, height=35, fg_color="transparent", border_width=2, text_color=("black", "white"))
btn_procurar.pack(side="right")

# Botão de Ação Principal
btn_converter = ctk.CTkButton(janela, text="Iniciar Conversão", command=converter_smc_para_sfc, height=40, font=ctk.CTkFont(size=14, weight="bold"))
btn_converter.pack(pady=15)

# Caixa de texto (Console Log)
caixa_texto = ctk.CTkTextbox(janela, width=610, height=250, font=ctk.CTkFont(family="Consolas", size=12))
caixa_texto.pack(padx=20, pady=(0, 20))
caixa_texto.insert('1.0', "Aguardando inicialização...\nSelecione a pasta acima e clique em 'Iniciar Conversão'.")

if __name__ == "__main__":
    janela.mainloop()