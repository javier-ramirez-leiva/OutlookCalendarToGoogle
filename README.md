# OutlookCalendarToGoogle
Send Outlook Calendar appointments to Google Calendar. Synchronization  tool for you to not to check your meetings on your pro laptop.

It creates a copy of your Outook Calendar to your Gmail Calendar (weekly).Please create a specific calendar for this purpose The steps are:
1. Export Outlook calendar (ics file)
2. Clean you dedicated pro calendar (to not to have duplicates or deleted meetings)
3. Add your meetings of the week (no description will be added to your personal account, let's keep it confidental)

It's nice to automate launch of the .bat so that you don't have to launch it everyday.

To install:
  * Create a google api for your calendar "Google Calendar API" (https://docs.simplecalendar.io/google-api-key/)
  * Add your google api json to api_json
  * Fill your "api_json/CalendarID.txt" with your calendar ID "you can use getCalendarIDs to retrieve all your calendars"
