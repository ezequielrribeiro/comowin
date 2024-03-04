import subprocess
import os
import datetime
from selenium import webdriver

class SistemaAtualizacao:
    def __init__(self):
        self.log_file = "atualizacao_log.txt"

    def _registrar_log(self, mensagem):
        with open(self.log_file, "a") as log:
            log.write(f"{mensagem}\n")

    def _executar_comando(self, comando):
        result = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self._registrar_log(f"Saída Padrão:\n{result.stdout.decode('utf-8')}")
        self._registrar_log(f"Erros:\n{result.stderr.decode('utf-8')}")

    def atualizar_chrome(self):
        self._registrar_log(f"Data e Hora da Atualização do Chrome: {datetime.datetime.now()}")
        try:
            driver = webdriver.Chrome()
            driver.get("chrome://settings/help")
            driver.implicitly_wait(10)
            driver.quit()
            self._registrar_log("Atualização do Chrome concluída com sucesso.")
            
            
            # Comando para atualizar o Chrome
            #comando = ['chrome_installer.exe', '--update']
            #self._executar_comando(comando)
            #self._registrar_log("Atualização do Chrome concluída com sucesso.")
        except subprocess.CalledProcessError:
            self._registrar_log("Erro ao atualizar o Chrome.")

    def atualizar_edge(self):
        self._registrar_log(f"Data e Hora da Atualização do Edge: {datetime.datetime.now()}")
        try:
            # Comando para atualizar o Edge
            comando = ['msedge_installer.exe', '--update']
            self._executar_comando(comando)
            self._registrar_log("Atualização do Edge concluída com sucesso.")
        except subprocess.CalledProcessError:
            self._registrar_log("Erro ao atualizar o Edge.")

    def atualizar_sistema(self):
        self._registrar_log(f"Data e Hora da Atualização do Sistema: {datetime.datetime.now()}")
        try:
            instalar_ps_windows_update()
            comando = ['powershell', '-Command', 'Install-Module -Name PSWindowsUpdate -Force -AllowClobber -Scope CurrentUser']
            subprocess.run(comando, check=True)
            print("Módulo PSWindowsUpdate instalado com sucesso.")
            # Comando para verificar e instalar atualizações no Windows
            comando = ['powershell', '-Command', 'Install-WindowsUpdate -AcceptAll -AutoReboot']
            subprocess.run(comando, check=True)
            print("Atualização do sistema concluída com sucesso.")
        except subprocess.CalledProcessError:
            self._registrar_log("Erro ao atualizar o sistema.")

def instalar_ps_windows_update():
    
    try:
        #Configurar a política de execução de scripts globalmente
        comando_powershell = 'Set-ExecutionPolicy RemoteSigned -Scope LocalMachine -Force'
        subprocess.run(['powershell', '-Command', comando_powershell], check=True)
        # Comando PowerShell para instalar o módulo PSWindowsUpdate sem interação
        comando = [
            'powershell',
            '-Command',
            'Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force -Scope CurrentUser; Install-Module -Name PSWindowsUpdate -Force -AllowClobber -Scope CurrentUser; Import-Module -Name PSWindowsUpdate -Force'
        ]
        subprocess.run(comando, check=True)
        print("Módulo PSWindowsUpdate instalado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro durante a instalação do módulo PSWindowsUpdate: {e}")
        
class SistemaLimpeza:
    def __init__(self):
        self.log_file = "limpeza_log.txt"

    def _registrar_log(self, mensagem):
        with open(self.log_file, "a") as log:
            log.write(f"{mensagem}\n")

    def _executar_comando(self, comando):
        result = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self._registrar_log(f"Saída Padrão:\n{result.stdout.decode('utf-8')}")
        self._registrar_log(f"Erros:\n{result.stderr.decode('utf-8')}")

    def limpar_memoria_temporaria(self):
        self._registrar_log(f"Data e Hora da Limpeza: {datetime.datetime.now()}")
        try:
            # Caminho para o executável cleanmgr.exe
            cleanmgr_path = r'C:\Windows\System32\cleanmgr.exe'
            # Argumentos para realizar a limpeza de memória temporária
            arguments = ['/sagerun:1']
            
            self._executar_comando([cleanmgr_path] + arguments)
            self._registrar_log("Limpeza de memória temporária concluída com sucesso.")
        except subprocess.CalledProcessError:
            self._registrar_log("Erro ao executar a Limpeza de Disco.")

    def limpar_navegadores(self):
        try:
            # Limpeza do Chrome
            os.system("start chrome --args --clear-logs")
            
            # Limpeza do Edge
            os.system("start msedge --args --clear-logs")
            
            self._registrar_log("Limpeza dos navegadores Chrome e Edge concluída com sucesso.")
        except Exception as e:
            self._registrar_log(f"Erro ao executar a limpeza dos navegadores: {str(e)}")

def main():
    #limpeza
    sistema_limpeza = SistemaLimpeza()
    sistema_limpeza.limpar_memoria_temporaria()
    sistema_limpeza.limpar_navegadores()

    #Atualizacao
    sistema_atualizacao = SistemaAtualizacao()
    sistema_atualizacao.atualizar_sistema()
    sistema_atualizacao.atualizar_chrome()
    sistema_atualizacao.atualizar_edge()
if __name__ == "__main__":
    main()
