import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

columnArray = ['上市、上櫃股名代碼表', 'Unnamed: 2', 'Unnamed: 4', 'Unnamed: 6', 'Unnamed: 8', 'Unnamed: 10', 'Unnamed: 12', 'Unnamed: 14', 'Unnamed: 16', 'Unnamed: 18', 'Unnamed: 20', 'Unnamed: 22', 'Unnamed: 24', 'Unnamed: 26', 'Unnamed: 28', 'Unnamed: 30', 'Unnamed: 32', 'Unnamed: 34', 'Unnamed: 36', 'Unnamed: 38']
stockNameArray = ['Unnamed: 1', 'Unnamed: 3', 'Unnamed: 5', 'Unnamed: 7', 'Unnamed: 9', 'Unnamed: 11', 'Unnamed: 13', 'Unnamed: 15', 'Unnamed: 17', 'Unnamed: 19', 'Unnamed: 21', 'Unnamed: 23', 'Unnamed: 25', 'Unnamed: 27', 'Unnamed: 29', 'Unnamed: 31', 'Unnamed: 33', 'Unnamed: 35', 'Unnamed: 37', 'Unnamed: 39']
stockCodeMatrix = []
stockNameMatrix = []

#print(DFOfStock)    # Check the whole form
checkFile = input('This Crawler need a supporting file "StockTable.xlsx" to fetch the code of securities, have you already downloaded it? The crawler would malfunction without this supporting file, type "Yes" to activate the cralwer. (Yes/No)')
if checkFile != 'Yes':
    print('Please download the necessary file and try to run the crawler again!')
    os._exit(0)
else:
    pathProg = os.path.abspath('.')
    DFOfStock = pd.read_excel(pathProg + '/Supporting Files/StockTable.xlsx')

for r in range(0, len(columnArray)):
    stockCode1 = DFOfStock[columnArray[r]][2:83]
    stockName = DFOfStock[stockNameArray[r]][2:83]

    for s in range(0, len(stockCode1.values)):
        try:
            stockCodeMatrix.append(int(stockCode1.values[s]))
            stockNameMatrix.append(str(stockName.values[s]))
        except:
            print("", end = '\t')

print(len(stockCodeMatrix))    # Check whether I have load and store all the codes into the array
print(len(stockNameMatrix))    # Check whether I have load and store all the names into the array

# The website I refered to: https://blog.csdn.net/chenKFKevin/article/details/62049060



nameArray = []
codeArray = []
closePriceArray = []
openPriceArray = []
differencePriceArray = []
startTime = time.time()

for m in range(0, len(stockCodeMatrix)):
    if len(nameArray) < len(stockCodeMatrix):
        url = 'https://tw.stock.yahoo.com/q/q?s='+ str(stockCodeMatrix[m])
        header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Cookie':'PSTM=1476231684; BIDUPSID=4F526560482E2A5E68D69CC8B0998806; plus_cv=1::m:92e3c68f; BAIDUID=C5A710455602AEA5BEC3D1B13B26321B:FG=1;'
                 ' BDUSS=W5zS3JSeVYwSHZjVm5SdTdjQjlKNC1FLWJqbklvaEptZjVZVkl2bXhMN1o1amhZSVFBQUFBJCQAAAAAAAAAAAEAAACj2nZjanVleWluZ3MAAAAAAAAAAAAAAAAAAAA'
                 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANlZEVjZWRFYT; BD_HOME=1; BD_UPN=12314353; sug=3; sugstore=0; ORIGIN=2; bdime=0;'
                 ' H_PS_645EC=78d5XI4%2Bj6NkSjLKSmkiYdx%2F5jHNa0c4UemYz6WwEpyczIPebiQwaLtzwnXd2gUHv28P; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1;'
                 ' PSINO=6; H_PS_PSSID=1448_18288_21112_17001_20241_21455_21406_21394_21377_21192_20929; BDSVRTM=0'
    }

        response = requests.get(url,headers=header)

        soup = BeautifulSoup(response.text, 'lxml')
        codeOfAllPrice = soup.find_all('td')
        codeOfTitle = soup.find_all('a')
        endTime = time.time()
        #print("test!!!!!!!!!!!!")
        #print(codeOfAllPrice)
        #print("test!!!!!!!!!!!!")
        #for i in range(1, 20):
        #    print(i)
        #    print(codeOfAllPrice[i].text)
        #    print("Next")
        #break

        closePrice = codeOfAllPrice[10].text
        openPrice = codeOfAllPrice[11].text
        highestPrice = codeOfAllPrice[12].text
        lowestPrice = codeOfAllPrice[13].text
        nameOfTarget = stockNameMatrix[m]
        codeOfTarget = stockCodeMatrix[m]

        try:
            float(closePrice)
            nameArray.append(nameOfTarget)
            codeArray.append(codeOfTarget)
            closePriceArray.append(closePrice)
            openPriceArray.append(openPrice)
            differencePriceArray.append(str(lowestPrice) + "-" + str(highestPrice))

            print('Download', str(len(nameArray)), 'th data of security.')
            print("Completition: " + str(int(((m + 1)/len(stockCodeMatrix))*100)) + "%")

            secondsPassed = endTime-startTime
            restSeconds = ((secondsPassed)/(m+1))*len(stockCodeMatrix)-secondsPassed
            restMinutes = int(round(restSeconds/60, 0))
            residualSeconds = round(restSeconds%60, 3)
            print("Estimated rest of the time:", restMinutes, "minutes", residualSeconds ,"seconds")

        except ValueError:
            print("The data of security no." + str(stockCodeMatrix[m]) + "is going wrong!")
            print("Completition: " + str(int(((m + 1)/len(stockCodeMatrix))*100)) + "%")

    elif len(nameArray) >= len(stockCodeMatrix):
        break

for e in range(0, len(nameArray)):
    print(str(codeArray[e]) + "\t" + nameArray[e] + "\t" + closePriceArray[e] + "\t" + openPriceArray[e] + "\t" + differencePriceArray[e])

#The tutorials about time I referred to:
#https://blog.csdn.net/ppdyhappy/article/details/78175547
#https://blog.csdn.net/Mr_Cat123/article/details/80681061


# Export the file
import datetime
today = datetime.date.today()    # Get the date

DFName = pd.DataFrame(nameArray)
DFCode = pd.DataFrame(codeArray)
DFClose = pd.DataFrame(closePriceArray)
DFOpen = pd.DataFrame(openPriceArray)
DFDifference = pd.DataFrame(differencePriceArray)
finalDF = pd.concat([DFCode, DFName, DFClose, DFOpen, DFDifference], axis = 1, ignore_index = True)
finalDF.columns = ['Code of Security', 'Name of Security', 'Close Price', 'Open Price', 'Price Range']
finalDF.to_excel('Output_of_Security_' + str(today) + '.xlsx', index = False)

# The website I refered to: http://blog.alarmchang.com/?p=230
