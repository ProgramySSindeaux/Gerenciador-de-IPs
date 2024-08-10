#Usando Netmiko para Dispositivos de Rede
#Instale o Netmiko:
#pip install netmiko


import socket
import time
import os
import re

def verifica_conexao():
    try:
        # Tenta se conectar ao servidor do Google para verificar a conexão com a internet
        socket.create_connection(("www.google.com", 80), 2)
        return True
    except OSError:
        # Retorna False se não conseguir se conectar
        return False

def obter_informacoes_rede():
    # Executa o comando ipconfig e captura a saída
    resultado = os.popen('ipconfig /all').read()
    
    # Expressões regulares para capturar IP, máscara de sub-rede, gateway e DNS
    ip_pattern = re.compile(r'IPv4 Address.*: (\d+\.\d+\.\d+\.\d+)')
    subnet_pattern = re.compile(r'Subnet Mask.*: (\d+\.\d+\.\d+\.\d+)')
    gateway_pattern = re.compile(r'Default Gateway.*: (\d+\.\d+\.\d+\.\d+)')
    dns_pattern = re.compile(r'DNS Servers.*: (\d+\.\d+\.\d+\.\d+)')
    
    # Busca as informações na saída do comando ipconfig
    ip = ip_pattern.search(resultado)
    subnet = subnet_pattern.search(resultado)
    gateway = gateway_pattern.search(resultado)
    dns = dns_pattern.search(resultado)
    
    # Retorna um dicionário com as informações encontradas
    return {
        'IP': ip.group(1) if ip else 'Não encontrado',
        'Máscara de Sub-rede': subnet.group(1) if subnet else 'Não encontrado',
        'Gateway': gateway.group(1) if gateway else 'Não encontrado',
        'DNS': dns.group(1) if dns else 'Não encontrado'
    }

def configurar_rede(ip, mascara_subrede, gateway, dns):
    try:
        # Configura o endereço IP e a máscara de sub-rede
        os.system(f'netsh interface ip set address name="Ethernet" static {ip} {mascara_subrede} {gateway}')
        
        # Configura os servidores DNS
        os.system(f'netsh interface ip set dns name="Ethernet" static {dns}')
        
        print("Configuração de rede aplicada com sucesso.")
    except Exception as e:
        # Exibe uma mensagem de erro em caso de falha
        print(f"Erro ao configurar a rede: {e}")

def configurar_proxy(proxy_endereco, proxy_porta):
    try:
        # Configura o proxy
        os.system(f'netsh winhttp set proxy {proxy_endereco}:{proxy_porta}')
        
        print("Configuração de proxy aplicada com sucesso.")
    except Exception as e:
        # Exibe uma mensagem de erro em caso de falha
        print(f"Erro ao configurar o proxy: {e}")

def alternar_configuracao(conexao_estavel):
    if conexao_estavel:
        # Configuração 1: Rede principal
        configurar_rede("192.168.1.100", "255.255.255.0", "192.168.1.1", "8.8.8.8")
        configurar_proxy("proxy.exemplo.com", "8080")
    else:
        # Configuração 2: Rede alternativa
        configurar_rede("192.168.1.101", "255.255.255.0", "192.168.1.1", "8.8.4.4")
        configurar_proxy("proxy.alternativo.com", "8081")

while True:
    # Verifica a conexão com a internet
    conexao_estavel = verifica_conexao()
    if conexao_estavel:
        print("Conectado à internet.")
        # Obtém e imprime as informações da rede
        info_rede = obter_informacoes_rede()
        print(f"IP: {info_rede['IP']}")
        print(f"Máscara de Sub-rede: {info_rede['Máscara de Sub-rede']}")
        print(f"Gateway: {info_rede['Gateway']}")
        print(f"DNS: {info_rede['DNS']}\n\n")
    else:
        print("Sem conexão com a internet. Alternando configuração de rede...\n\n")
        # Alterna a configuração de rede em caso de queda de conexão
        alternar_configuracao(conexao_estavel)
    
    # Aguarda 10 segundos antes de verificar novamente
    time.sleep(10)
