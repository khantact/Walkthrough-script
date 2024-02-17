from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from datetime import date
import csv

def setup(path, formLink):
    chrome_options = Options() 
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--user-data-dir="+path)

    web = webdriver.Chrome(options=chrome_options)
    web.get(formLink)
    return web
# login 
def login(username, password, web):
    usern = web.find_element('xpath', '//*[@id="identifierId"]')
    usern.send_keys(username)

    continuebutton = web.find_element('xpath', '//*[@id="identifierNext"]/div/button')
    continuebutton.click()

    time.sleep(2)
    passEntry =  web.find_element(By.CSS_SELECTOR, ("input[type='password']"))
    passEntry.send_keys(password)

    continuebutton = web.find_element('xpath','//*[@id="passwordNext"]/div/button')
    continuebutton.click()
    # Wait for 2 factor
    time.sleep(10)

def firstPageForm(request, apartmentXPaths, web):

    emailConfirm = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span').click()

    walkThruNames = request['CL Name(s)']
    clNames = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    clNames.send_keys(walkThruNames)

    # time.sleep(2)
    today = date.today()
    currentDay = (today.strftime("%m/%d/%Y"))
    findDate = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    findDate.send_keys(currentDay)

    findApartment = web.find_element('xpath', apartmentXPaths[request['Residential Area']])
    findApartment.click()

    apartment = request['Apartment']
    findApartmentRoom = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    findApartmentRoom.send_keys(apartment)

    walkThruType = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span'
    web.find_element('xpath',walkThruType).click()

    nextPage = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

def secondPageForm(request, web):
    exteriorCommonAreas = request['Exterior Common Areas']
    web.find_element('xpath', "/html[@class='HB1eCd-UMrnmb']/body[@class='D8bnZd ']/div[@class='Uc2NEf']/div[@class='teQAzf']/form[@id='mG61Hd']/div[@class='RH5hzf RLS9Fe']/div[@class='lrKTG']/div[@class='o3Dpx']/div[@class='Qr7Oae'][1]/div/div[@class='geS5n']/div[@class='AgroKb']/div[@class='edhGSc zKHdkd kRy7qc RdH0ib yqQS1']/div[@class='RpC4Ne oJeWuf']/div[@class='Pc9Gce Wic03c']/textarea[@class='KHxj8b tL9Q4c']").send_keys(exteriorCommonAreas)
    exteriorBuildingCond = request['Exterior Building Condition']
    web.find_element('xpath', "/html[@class='HB1eCd-UMrnmb']/body[@class='D8bnZd ']/div[@class='Uc2NEf']/div[@class='teQAzf']/form[@id='mG61Hd']/div[@class='RH5hzf RLS9Fe']/div[@class='lrKTG']/div[@class='o3Dpx']/div[@class='Qr7Oae'][2]/div/div[@class='geS5n']/div[@class='AgroKb']/div[@class='edhGSc zKHdkd kRy7qc RdH0ib yqQS1']/div[@class='RpC4Ne oJeWuf']/div[@class='Pc9Gce Wic03c']/textarea[@class='KHxj8b tL9Q4c']").send_keys(exteriorBuildingCond)
    emergencyRoutes = request['Emergency Routes']
    web.find_element('xpath', "/html[@class='HB1eCd-UMrnmb']/body[@class='D8bnZd ']/div[@class='Uc2NEf']/div[@class='teQAzf']/form[@id='mG61Hd']/div[@class='RH5hzf RLS9Fe']/div[@class='lrKTG']/div[@class='o3Dpx']/div[@class='Qr7Oae'][3]/div/div[@class='geS5n']/div[@class='AgroKb']/div[@class='edhGSc zKHdkd kRy7qc RdH0ib yqQS1']/div[@class='RpC4Ne oJeWuf']/div[@class='Pc9Gce Wic03c']/textarea[@class='KHxj8b tL9Q4c']").send_keys(emergencyRoutes)
    lighting = request['Lighting']
    web.find_element('xpath', "/html[@class='HB1eCd-UMrnmb']/body[@class='D8bnZd ']/div[@class='Uc2NEf']/div[@class='teQAzf']/form[@id='mG61Hd']/div[@class='RH5hzf RLS9Fe']/div[@class='lrKTG']/div[@class='o3Dpx']/div[@class='Qr7Oae'][4]/div/div[@class='geS5n']/div[@class='AgroKb']/div[@class='edhGSc zKHdkd kRy7qc RdH0ib yqQS1']/div[@class='RpC4Ne oJeWuf']/div[@class='Pc9Gce Wic03c']/textarea[@class='KHxj8b tL9Q4c']").send_keys(lighting)
    interiorCommonAreas = request['Interior Common Areas']
    web.find_element('xpath', "/html[@class='HB1eCd-UMrnmb']/body[@class='D8bnZd ']/div[@class='Uc2NEf']/div[@class='teQAzf']/form[@id='mG61Hd']/div[@class='RH5hzf RLS9Fe']/div[@class='lrKTG']/div[@class='o3Dpx']/div[@class='Qr7Oae'][5]/div/div[@class='geS5n']/div[@class='AgroKb']/div[@class='edhGSc zKHdkd kRy7qc RdH0ib yqQS1']/div[@class='RpC4Ne oJeWuf']/div[@class='Pc9Gce Wic03c']/textarea[@class='KHxj8b tL9Q4c']").send_keys(interiorCommonAreas)
    emergencyEquip = request['Emergency Equipment']
    web.find_element('xpath', "/html[@class='HB1eCd-UMrnmb']/body[@class='D8bnZd ']/div[@class='Uc2NEf']/div[@class='teQAzf']/form[@id='mG61Hd']/div[@class='RH5hzf RLS9Fe']/div[@class='lrKTG']/div[@class='o3Dpx']/div[@class='Qr7Oae'][6]/div/div[@class='geS5n']/div[@class='AgroKb']/div[@class='edhGSc zKHdkd kRy7qc RdH0ib yqQS1']/div[@class='RpC4Ne oJeWuf']/div[@class='Pc9Gce Wic03c']/textarea[@class='KHxj8b tL9Q4c']").send_keys(emergencyEquip)
    wDL = request['Windows, Doors, Locks']
    web.find_element('xpath', "/html[@class='HB1eCd-UMrnmb']/body[@class='D8bnZd ']/div[@class='Uc2NEf']/div[@class='teQAzf']/form[@id='mG61Hd']/div[@class='RH5hzf RLS9Fe']/div[@class='lrKTG']/div[@class='o3Dpx']/div[@class='Qr7Oae'][7]/div/div[@class='geS5n']/div[@class='AgroKb']/div[@class='edhGSc zKHdkd kRy7qc RdH0ib yqQS1']/div[@class='RpC4Ne oJeWuf']/div[@class='Pc9Gce Wic03c']/textarea[@class='KHxj8b tL9Q4c']").send_keys(wDL)
    residentEngage = request['Resident Engagement']
    web.find_element('xpath', "/html[@class='HB1eCd-UMrnmb']/body[@class='D8bnZd ']/div[@class='Uc2NEf']/div[@class='teQAzf']/form[@id='mG61Hd']/div[@class='RH5hzf RLS9Fe']/div[@class='lrKTG']/div[@class='o3Dpx']/div[@class='Qr7Oae'][8]/div/div[@class='geS5n']/div[@class='AgroKb']/div[@class='edhGSc zKHdkd kRy7qc RdH0ib yqQS1']/div[@class='RpC4Ne oJeWuf']/div[@class='Pc9Gce Wic03c']/textarea[@class='KHxj8b tL9Q4c']").send_keys(residentEngage)
    # Next page
    web.find_element('xpath', "/html[@class='HB1eCd-UMrnmb']/body[@class='D8bnZd ']/div[@class='Uc2NEf']/div[@class='teQAzf']/form[@id='mG61Hd']/div[@class='RH5hzf RLS9Fe']/div[@class='lrKTG']/div[@class='ThHDze']/div[@class='DE3NNc CekdCb']/div[@class='lRwqcd']/div[@class='uArJ5e UQuaGc YhQJj zo8FOc ctEux'][2]/span[@class='l4V7wb Fxmcue']/span[@class='NPEfkd RveJvd snByac']").click()


def thirdPageForm(request, web):
    priorIssues = request['Prior Issues']
    web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(priorIssues)
    submit = web.find_element('xpath', "/html[@class='HB1eCd-UMrnmb']/body[@class='D8bnZd ']/div[@class='Uc2NEf']/div[@class='teQAzf']/form[@id='mG61Hd']/div[@class='RH5hzf RLS9Fe']/div[@class='lrKTG']/div[@class='ThHDze']/div[@class='DE3NNc CekdCb']/div[@class='lRwqcd']/div[@class='uArJ5e UQuaGc Y5sE8d VkkpIf QvWxOd']/span[@class='l4V7wb Fxmcue']/span[@class='NPEfkd RveJvd snByac']").click()
    time.sleep(2)
    web.find_element('xpath', "/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()
def main():
    # replace this with your google chrome profile path, or use the login function
    # You can find the google chrome profile path by going to chrome://version and copy the profile path bit
    userPath = 'paste user path in here'
    formLink = 'paste google form link in here'
    web = setup(userPath, formLink)
    # if the above does not work or you can't find it, put your username and password in here and also uncomment the bottom 3 lines of code
    # username = 'insert email here'
    # password = 'insert password here'
    # login(username, password, web)
    apartmentXPaths = {
        'University Court Apartments': '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[20]/label/div/div[2]/div/span',
        'Newell Apartments' : "/html[@class='HB1eCd-UMrnmb']/body[@class='D8bnZd ']/div[@class='Uc2NEf']/div[@class='teQAzf']/form[@id='mG61Hd']/div[@class='RH5hzf RLS9Fe']/div[@class='lrKTG']/div[@class='o3Dpx']/div[@class='Qr7Oae'][3]/div/div[@class='geS5n']/div[@class='oyXaNc']/div/div[@class='lLfZXe fnxRtf cNDBpf']/span[@class='H2Gmcc tyNBNd']/div[@class='SG0AAe']/div[@class='nWQGrd zwllIb'][18]/label[@class='docssharedWizToggleLabeledContainer ajBQVb']/div[@class='bzfPab wFGF8']/div[@class='YEVVod']/div[@class='ulDsOb']/span[@class='aDTYNe snByac OvPDhc OIC90c']",
        }
    with open('walkThrough.csv') as f:
        reader = csv.DictReader(f)
        for dictionary in reader:
            firstPageForm(dictionary, apartmentXPaths, web)
            time.sleep(2)
            secondPageForm(dictionary, web)
            time.sleep(2)
            thirdPageForm(dictionary, web)
            time.sleep(2)
    print("All done!")
            

main()