import subprocess

class ServerNTP:
    @staticmethod
    def alterar_servidor_ntp():
        # Methodo de setar servidor NTP
        comando_powershell = r'''
        $novoServidorNTP = "a.st1.ntp.br"
        $caminhoRegistro = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\DateTime\Servers"
        Set-ItemProperty -Path $caminhoRegistro -Name 0 -Value $novoServidorNTP
        Write-Host "Servidor NTP alterado para: $novoServidorNTP"
        '''
        # Executa o comando PowerShell
        subprocess.run(["powershell", "-Command", comando_powershell], shell=True, check=True)

class RenameHost:
    @staticmethod
    def renomear_computador():
        # Methodo de alterar o novo nome do computador
        novo_nome_computador = "TI001"

        # Comando PowerShell para renomear o computador
        comando_powershell = rf'''
        # Define o novo nome do computador
        $novoNomeComputador = "{novo_nome_computador}"

        # Renomeia o computador e reinicia
        Rename-Computer -NewName $novoNomeComputador -Force -Restart
        '''

        # Executa o comando PowerShell
        subprocess.run(["powershell", "-Command", comando_powershell], shell=True, check=True)
        
        
ServerNTP.alterar_servidor_ntp()
RenameHost.renomear_computador()