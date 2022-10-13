
import datetime
import sys
import os
from cal_setup import get_calendar_service





def main():
   calendarIDFile = os.path.join(sys.path[0]) +os.sep+ 'api_json' + os.sep + "CalendarID.txt"
   with open(calendarIDFile) as f:
      lines = f.readlines()
   ID = lines[0]
   service = get_calendar_service()
   # Call the Calendar API
   yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
   yesterdayiso = yesterday.isoformat() + 'Z' # 'Z' indicates UTC time
   events_result = service.events().list(
      calendarId=ID, timeMin=yesterdayiso,
      maxResults=100, singleEvents=True,
      orderBy='startTime').execute()
   events = events_result.get('items', [])

   for event in events:
      service.events().delete(calendarId=ID,eventId=event['id'],).execute()
      
   print("Calendar cleaned")

if __name__ == '__main__':
       main()