from datetime import datetime, timedelta
from cal_setup import get_calendar_service
from icalendar import Calendar, Event
import icalendar
from icalendar import vDatetime
import sys
import os


def main():
   calendarIDFile = os.path.join(sys.path[0]) +os.sep+ 'api_json' + os.sep + "CalendarID.txt"
   with open(calendarIDFile) as f:
      lines = f.readlines()
   ID =lines[0]
   service = get_calendar_service()
   
   ICSFile = open(os.path.join(sys.path[0]) +os.sep+ 'temp'+ os.sep +'Calendar.ics', 'rb')
   ICSCalendar = icalendar.Calendar.from_ical(ICSFile.read())
   for component in ICSCalendar.walk():
       
       noFormatStart = component.get('dtstart')
       noFormatEnd = component.get('dtend')
       if(noFormatStart is not None and noFormatEnd is not None):
         summary = component.get('summary')
         start = vDatetime.from_ical(noFormatStart.to_ical())
         end = vDatetime.from_ical(noFormatEnd.to_ical())
         print("Import event: ", summary, start, end)
         event_result = service.events().insert(calendarId=ID,
         body={
          "summary": summary,
          "start": {"dateTime": start.isoformat(), "timeZone": 'Europe/Paris'},
          "end": {"dateTime": end.isoformat(), "timeZone": 'Europe/Paris'},
         },).execute()
       
   
   


if __name__ == '__main__':
   main()