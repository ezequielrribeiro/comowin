# do a script who reads windows logs and print the last 10 logs



# Path: main.py
import win32evtlog
import win32api
import win32con

server = 'localhost'
logtype = 'System'
hand = win32evtlog.OpenEventLog(server, logtype)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
total = win32evtlog.GetNumberOfEventLogRecords(hand)

events = win32evtlog.ReadEventLog(hand, flags, 0)
#events = [events]
for event in events:
    print(event.StringInserts)
    print(event.TimeGenerated)
    print(event.EventID)
    print(event.EventType)
    print(event.SourceName)
    print(event.ComputerName)
    print(event.RecordNumber)
    print(event.TimeWritten)
    print(event.TimeGenerated)
    print(event.EventCategory)
    print(event.StringInserts)
    print(event.Sid)
    print(event.Data)
    print(event.EventID)
    print(event.EventType)
    print(event.SourceName)
    print(event.StringInserts)
    print(event.ComputerName)
    print(event.RecordNumber)
    print(event.TimeWritten)
    print(event.TimeGenerated)
    print(event.EventCategory)
    print(event.Sid)
    print(event.Data)
    print(event.EventID)
    print(event.EventType)
    print(event.SourceName)
    print(event.StringInserts)
    print(event.ComputerName)
    print(event.RecordNumber)
    print(event.TimeWritten)
    print(event.TimeGenerated)
    print(event.EventCategory)
    print(event.Sid)
    print(event.Data)
    print(event.EventID)
    print(event.EventType)
    print(event.SourceName)
    print(event.StringInserts)
    print(event.ComputerName)
    print(event.RecordNumber)
    print(event.TimeWritten)
    print(event.TimeGenerated)
    print(event.EventCategory)
    print(event.Sid)
    print(event.Data)
    print(event.EventID)
    print(event.EventType)
    print(event.SourceName)
    print(event.StringInserts)
    print(event.ComputerName)
    print(event.RecordNumber)
    print(event.TimeWritten)
    print(event.TimeGenerated)
    print(event.EventCategory)
    print(event.Sid)
    print(event.Data)

