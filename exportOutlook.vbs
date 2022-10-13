' -------------------------------------------------
' Modify this \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
Const myEmailAddress = "jaramil92@gmail.com"
Const includePrivateDetails = True
Const howManyDaysToDisplay = 7
' Modify this /////////////////////////////////////
' -------------------------------------------------
Const olFreeBusyAndSubject = 1
Const olFullDetails = 2
Const olFolderCalendar = 9
ExportCalendar Date, (Date + (howManyDaysToDisplay - 1))

Sub ExportCalendar(datBeg, datEnd)
   Dim olkApp, olkSes, olkCal, olkExp, olkMsg
   Set olkApp = CreateObject("Outlook.Application")
   Set olkSes = OlkApp.GetNameSpace("MAPI")
   olkSes.Logon olkApp.DefaultProfileName
   Set olkCal = olkSes.GetDefaultFolder(olFolderCalendar)
   Set olkExp = olkCal.GetCalendarExporter
   With olkExp
   .CalendarDetail = olFreeBusyAndSubject
   .IncludePrivateDetails = includePrivateDetails
   .RestrictToWorkingHours = False
   .StartDate = datBeg
   .EndDate = datEnd
   End With
   scriptdir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
   olkExp.SaveAsICal scriptdir+"\temp\Calendar.ics" 
   Wscript.Echo "Exported To" +scriptdir+"\temp\Calendar.ics" 
   Set olkCal = Nothing
   Set olkExp = Nothing
   Set olkMsg = Nothing
   olkSes.Logoff
   Set olkSes = Nothing
   Set olkApp = Nothing
End Sub