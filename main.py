import collections
from types import SimpleNamespace

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

secret = {
  "type": "service_account",
  "project_id": "cl-py-script",
  "private_key_id": "bf34b9feb65301768f336fa8332f9ed0f3239c94",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCWi5pZzToeQUlX\n2n8cR2t4t/v4v8kCexycrJLVE8u/xwJ8XaMONd2IPQ8ab+UHgawk2P1sRFG6Cy1r\nYMxAAibiS5ZeAvpM+nSGxHwQx+2EwA5NQbaj6tJB7SZsGmVazExS1fef+w4hPUhQ\ngBp7mCwF3Puk3F3/PZ+l4L3ApYdUASv+yTClXBo0zdn/MWEkC/rHQAh9ncTtC459\nHgdupPz1RDTn38damHfLpkJsgIL4ICFhcZDonOB4H5n2IzckdFRvZoYsjzItMzV9\n3lCadr+I1qlG6vixqWQM9R83iTIH/8u+PvdW0zndANCOuwt0QclplbAquT3/FXJL\njo/qlPeLAgMBAAECggEAAKXhBL+QGI4H2y3DSWbYxHEDIKeDuIZa3YOPD5mQm340\n3nQdCbyldTd5pDFo8Ur8kCQkvkDymq7/Q5oUPbcGVyLZkovAya10FMkm7OurlaZY\n0CYM+DjAVj25/RwggFegFWu3jdgeZDa1LhrjrhSpuYdeC32jAnZPx/6ZnW4apTG5\n4Mzyyc7k/xIdDrM4+8VdYeTSrKh7Y+Ezfuk6d5vOXiquX9tOy7cZsb1I7LCYwe/P\nCm0Limv26xNlaAM1YFy2gJ4j6YujVQ5kunJ+duYWLXtxzRVF5sy8LGpYx5ixHZba\nTnYXYft5hd/mSDISHseyFLy7UGLw5eK8x0zGCqvm6QKBgQDPgSBirjywiilUCbzp\nt4umhAZgJNW6vTC6/0n6+AoK6yPEdqKx4Fsh1J7HgdmewUPKLq/VWv7AH+bqkbzG\nfxItkRIIK6rpS8Z1Vv8mHhcfxszv+HihkphJmlz9hoWyqcnH0Kh2b5hkUXkjIEJX\nay5fWSQMuhd1mxX3dncZEYCkCQKBgQC5uqV5zufAiTn2ERiQ44cXlJlFLbjUk3uT\nN27rfFoNphvXGqpH+AFaRBgY2lIVYe7SjhQWRDJ26DxzdSIj8SFceNFlYP+TBxMA\n4CTdUnwF491UzmpIJwPlgZMCxFY57KEOpy20NVYs2qcJado3gKIY0/mzPRmnu57e\nOQSSyv3r8wKBgFB9CN/eMAJWhTNo15Ncs9mySnrOruzRZ+6RCdRElDip/uS9E9yl\nZxQXUkOW9Z/j3XS2aVP8CObjOQHx5+Si850jMXhj39bAoslvJmdVsqiLx4Cpw7kA\nkPuz2bAplwC3ZWKRaFcQcG8xPyjF4ZXhKEqp3BbntCPVNU8Y75eUt25pAoGBAKy6\nzyanrJU9inA0mho14O+nPZw+14Sr3OOfTEMplT7YW1AD9pWUKv3eEmMat/g26jtb\n84Z5yk0X0xC1wRiYKySrIGMegNImZCAOVXqYOcvojXFPvzx3PIJ3rVeHbYHVdjwA\nctsEN67jczGoBlBUC2z3x2RQ0MlUDn4xnPVAYELNAoGAcauUu28sJBJmFPeeVUto\nvg6cPzwXo9UZdyba/y0uw1V1a9O7A1IChgwoyazNQPt1ArPXnTjaOwoha8bYH3KC\n/32rbnb9vzM3WuzzDzKdp1HzlWRJE+AOxVXUGnu6YrDN25ihnMdCr+xy1G1WYG33\nIIZsU907TNGlet+cYDVBWCY=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-ri5cf@cl-py-script.iam.gserviceaccount.com",
  "client_id": "104289145204165001238",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ri5cf%40cl-py-script.iam.gserviceaccount.com"
}

cred = credentials.Certificate(secret)
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://cl-py-script-default-rtdb.europe-west1.firebasedatabase.app/"
})

ref = db.reference('/words/')


def getSize():
    i = 0
    data = ref.get()
    for key in data:
        i = i + 1


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# open it, go to a website, and get results
driver = webdriver.Chrome(options=options)


driver.get("https://instaling.pl/teacher.php?page=login")
login = driver.find_element(By.ID, "log_email")
password = driver.find_element(By.ID, "log_password")
login.send_keys("###")
password.send_keys("###")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="main-container"]/div[3]/form/div/div[3]/button').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="student_panel"]/p[1]/a').click()


continueOrStart = driver.find_element(By.XPATH, '//*[@id="continue_session_page"]/div[1]').text
if "Sesja została rozpoczęta, ale nie została jeszcze dokończona." in continueOrStart:
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="continue_session_button"]/h4').click()
else:
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="start_session_button"]').click()


time.sleep(3)

wordDe = ""
word = ""

times = 20
while times != 1:
    wordDe = ""
    word = ""

    word = driver.find_element(By.XPATH, '//*[@id="question"]/div[2]/div[2]').text

    isAdded = False
    x = ref.get()
    print(ref.child("/" + word))
    # for key in x:
    #     if key["PL"] == word and len(word) != 0 and len(key["PL"]) != 0 and len(key["DE"]) != 0:
    #         isAdded = True
    #         wordDe = key["DE"]

    if isAdded:
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="answer"]').send_keys(wordDe)
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="check"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="next_word"]').click()
        times = times - 1
        time.sleep(2)
        wordDe = ""
        word = ""
    elif not isAdded:
        driver.find_element(By.XPATH, '//*[@id="check"]').click()
        time.sleep(2)
        text = driver.find_element(By.XPATH, '//*[@id="word"]').text
        if len(word) > 1 and len(text) > 1:
            box_ref = ref.child(str(getSize()))
            box_ref.update({
                'PL': word,
                'DE': text
            })
        wordDe = ""
        word = ""
        driver.find_element(By.XPATH, '//*[@id="nextword"]').click()
        time.sleep(3)


driver.close()
