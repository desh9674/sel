"""
Credit Excluding tax Adjustment July 21 to Aug 23

 

https://cenveo.service-now.com/x_cenve_credit_memo_list.do?sysparm_query=reason_for_credit_request!%3Denv10%5Esys_created_onBETWEENjavascript:gs.dateGenerate(%272021-07-01%27%2C%2700:00:00%27)@javascript:gs.dateGenerate(%272023-08-31%27%2C%2723:59:59%27)&sysparm_first_row=1&sysparm_view=

[2:50 PM] Harshal Sarnobat

Credit Tax Adjustment from Jan 2018 to Aug 23

 

https://cenveo.service-now.com/x_cenve_credit_memo_list.do?sysparm_query=reason_for_credit_request%3Denv10%5Esys_created_onBETWEENjavascript:gs.dateGenerate(%272018-01-01%27%2C%2700:00:00%27)@javascript:gs.dateGenerate(%272023-08-31%27%2C%2723:59:59%27)&sysparm_first_row=1&sysparm_view=

[2:52 PM] Harshal Sarnobat

Change Tickets without labels: 2342

 

https://cenveo.service-now.com/change_request_list.do?sysparm_query=cmdb_ciNOT%20LIKElabels%5Esys_created_onBETWEENjavascript:gs.dateGenerate(%272021-01-01%27%2C%2700:00:00%27)@javascript:gs.dateGenerate(%272023-08-31%27%2C%2723:59:59%27)&sysparm_first_row=1&sysparm_view=



"""
import os


downloadsPath = r"C:\Users\cammy\Downloads\attachments\2023"



"""
July 21 Dec 21

https://cenveo.service-now.com/incident_list.do?sysparm_query=sys_created_onBETWEENjavascript:gs.dateGenerate(%272021-07-01%27%2C%2700:00:00%27)@javascript:gs.dateGenerate(%272021-12-31%27%2C%2723:59:59%27)%5Ecategory!%3Dpassword%5Eshort_descriptionNOT%20LIKElabels%5Eshort_descriptionNOT%20LIKEPrint&sysparm_first_row=1&sysparm_view=


Jan 22 Dec 22

https://cenveo.service-now.com/incident_list.do?sysparm_query=sys_created_onBETWEENjavascript:gs.dateGenerate(%272022-01-01%27%2C%2700:00:00%27)@javascript:gs.dateGenerate(%272022-12-31%27%2C%2723:59:59%27)%5Ecategory!%3Dpassword%5Eshort_descriptionNOT%20LIKElabels%5Eshort_descriptionNOT%20LIKEPrint&sysparm_first_row=1&sysparm_view=


Jan 23 Aug 23

https://cenveo.service-now.com/incident_list.do?sysparm_query=sys_created_onBETWEENjavascript:gs.dateGenerate(%272023-01-01%27%2C%2700:00:00%27)@javascript:gs.dateGenerate(%272023-08-31%27%2C%2723:59:59%27)%5Ecategory!%3Dpassword%5Eshort_descriptionNOT%20LIKElabels%5Eshort_descriptionNOT%20LIKEPrint&sysparm_first_row=1&sysparm_view=

 


"""


# //*[@id="row_change_request_17c746f897dc71109d777d200153af7e"]/td[3]/a
# /html/body/div[1]/div[1]/span/div/div[7]/div[1]/table/tbody/tr{rowNum}/


