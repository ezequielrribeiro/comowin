import win32evtlog
import datetime

# Obtém a hora atual do sistema
hora_atual = datetime.datetime.now()

# Define o intervalo de tempo desejado (últimas 12 horas)
hora_inicial = hora_atual - datetime.timedelta(hours=12)
hora_final = hora_atual

# Abre o log de eventos de segurança
server = 'localhost'
logtype = 'Security'
hand = win32evtlog.OpenEventLog(server, logtype)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
total = win32evtlog.GetNumberOfEventLogRecords(hand)

# Lê os eventos de segurança
events = win32evtlog.ReadEventLog(hand, flags, 0)

# Itera sobre os eventos e imprime aqueles que estão dentro do intervalo de tempo
for event in events:
    # Verifica se o evento está dentro do intervalo de tempo desejado
    if hora_inicial <= event.TimeGenerated <= hora_final:
        print("StringInserts:", event.StringInserts)
        print("TimeGenerated:", event.TimeGenerated)
        print("EventID:", event.EventID)
        print("EventCategory:", event.EventCategory)
        print("SourceName:", event.SourceName)
        print("ComputerName:", event.ComputerName)
        print("RecordNumber:", event.RecordNumber)
        print("TimeWritten:", event.TimeWritten)
        print("EventType:", event.EventType)
        print()
