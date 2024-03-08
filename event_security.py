import win32evtlog

server = 'localhost'
logtype = 'Security'  # Especificando o tipo de log como 'Security' para acessar os eventos de segurança
hand = win32evtlog.OpenEventLog(server, logtype)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
total = win32evtlog.GetNumberOfEventLogRecords(hand)

events = win32evtlog.ReadEventLog(hand, flags, 0)

for event in events:
    # Aqui você pode processar os eventos de segurança conforme necessário
    print(event.StringInserts)
    print(event.TimeGenerated)
    print(event.EventID)
    # Adicione outras propriedades conforme necessário
