# Python script to Download all the attachments from every ticket in Servicenow from give url using Selenium

First pip intall selenium in virtual environment
Then change "downloadsPath" variable and "url", in given script
Also change both urls along with your company domain name
save and run script.

This script uses selenium to conrol asks of input "Y" untill you login in browser then loads given url, and goes to last page.
Then scans for all tickets elements in list view table and opens each in new tab, if it has. Reccomend to keep 10 tikcets in each table view.
Attachments then downloads all in zip file and renames adding INC number before the file name.

## This works for Change, problems and any custom module tickets as well

Then clicks back page button in navigation and repeats the process untill first page is reached.

This script can be useful for some project that is moving out of servicnow and switching to some other platform and needs all ticket attachments data but don't want to pay for servicenow API.
Contact me if you need help with any of the steps.
Very useful if you want to save money.
Good Luck!