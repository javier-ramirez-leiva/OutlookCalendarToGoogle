
import datetime
import sys
import os
from cal_setup import get_calendar_service





def main():
   calendarIDFile = os.path.join(sys.path[0]) +os.sep+ 'api_json' + os.sep + "CalendarID.txt"
   with open(calendarIDFile) as f:
      lines = f.readlines()
   ID = lines[0]
   print(ID)
   service = get_calendar_service()
   # Call the Calendar API
   now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
   print('Getting List o 100 events')
   events_result = service.events().list(
      calendarId=ID, timeMin=now,
      maxResults=100, singleEvents=True,
      orderBy='startTime').execute()
   events = events_result.get('items', [])

   if not events:
      print('No upcoming events found.')
   for event in events:
      start = event['start'].get('dateTime', event['start'].get('date'))
      print(start, event['summary'], event['id'])


if __name__ == '__main__':
       main()