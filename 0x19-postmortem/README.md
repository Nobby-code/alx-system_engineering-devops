SYSTEM OUTAGE ISSUE

Issue mummery

On Friday December 2, 2022, at around 7:00 am EAT, requests by users to use a specific API that updates a specific table of a Hospital Management System resulted into 500 error response messages. This therefore reduced the functionality of the application in that specific hospital and hence almost everything came into a stand still because other functionalities depend of the failed part. The root cause of this outage was an incomplete system update where changes made on the databases were not pushed.

Timeline (East African Time (EAT))

•	4:30 am: started to push system update to the server, and barely 30 minutes later all updates were complete

•	6:45am: API failure begins and the system could not be used optimally by the users

•	6:50am: On of the users alerted the Software Development team and posted the error message on the team’s WhatsApp group.

•	7:05am: Failed configuration rollback

•	7:30am: pushing new updates

•	7:45am: server restarted and 100% of traffic is back online with the error solved 

Route Cause

At 4:30 am (EAT), an update was released, and the system was updated to the newer version. The system users experienced a bug on API that accesses a specific table in the database. The error was because when updating the system, the developers slightly forgot to push the changes made on the database, since the database resides on s different location from the source system code.

Resolution and recovery

At 6:50am EAT: One of the users of the system experienced the problem and immediately escalated the issue to the Software development team, which the team quickly identified

At 7:05am EAT, the failed update was rolled back and immediately correctly updated to a newer version, to remove the error.

Preventive measures
•	Testing the actual updated system on the server just to check the flow

•	All updates to be pushed at once.
