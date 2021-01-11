import gspread
from oauth2client.service_account import ServiceAccountCredentials
  
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Dream Land Data").sheet1  # Open the spreadhseet
sheet2 = client.open("All Sheets").sheet1  # Open the spreadhseet


data1 = [item for item in sheet.col_values(12) if item]
data2 = [item for item in sheet.col_values(8) if item]
s1 = [item for item in sheet2.col_values(3) if item]
s2 = [item for item in sheet2.col_values(5) if item]

for i in range(0,492) :
    s1[i]=s1[i].replace(' ','')
    if ' 'in s2[i]:
        s2[i]=s2[i].replace(' ','')
    if ' ' in data1[i]:
        data1[i]=data1[i].replace(' ','') 
    if ' ' in data2[i]:
        data2[i]=data2[i].replace(' ','')

for i in range(1,492):
    index = s1.index(data1[i])
    if data1[i] == data2[index] and data2[i] != s2[index]: 
        print('code in Dream land: ' +data1[i])
        print('price in Dream land: ' +data2[i])
        print('code in all sheet: ' +s1[index])
        print('prince in all sheet: ' +s2[index])
