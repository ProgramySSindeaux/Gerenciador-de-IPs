
import tkinter as tk


from tkinter import messagebox
import subprocess
import re

def obter_ip():
    
    try:
        resultado = subprocess.run(['ipconfig'], capture_output=True, text=True)
        saida = resultado.stdout
        ip_pattern = re.compile(r'IPv4 Address[^\n]*:\s*([0-9.]+)|Endereço IPv4[^\n]*:\s*([0-9.]+)')
        ip_local = ip_pattern.search(saida)

        if ip_local:
            ip_local = ip_local.group(1) if ip_local.group(1) else ip_local.group(2)
  
            entrada_ip.delete(0, tk.END)
            entrada_ip.insert(0, ip_local)

        else:
            raise ValueError("IP não encontrado na saída do comando")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível obter o IP: {e}")

janela_principal = tk.Tk()
janela_principal.title("Meu IP Local")
janela_principal.configure(bg="white")

largura_janela = 350
altura_janela = 200

largura_tela = janela_principal.winfo_screenwidth()
altura_tela = janela_principal.winfo_screenheight()

posicao_x = (largura_tela // 2) - (largura_janela // 2)
posicao_y = (altura_tela // 2) - (altura_janela // 2)
janela_principal.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

frame_principal = tk.Frame(janela_principal, bg="white")
frame_principal.pack(expand=True)

botao_obter_ip = tk.Button(frame_principal, 
                           text="Obter IP Local", 
                           command=obter_ip, 
                           font=('Helvetica', 12))
botao_obter_ip.pack(pady=20)

frame_ip = tk.Frame(frame_principal, bg="white")
frame_ip.pack(pady=10)

label_ip = tk.Label(frame_ip, 
                    text="IP Local:", 
                    bg="white", 
                    font=('Helvetica', 12))

label_ip.pack(side="left", padx=5)

entrada_ip = tk.Entry(frame_ip, width=30, font=('Helvetica', 14))
entrada_ip.pack(side="left", padx=5)

janela_principal.mainloop()
