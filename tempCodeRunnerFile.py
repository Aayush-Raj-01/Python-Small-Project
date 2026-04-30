
url = "http://172.16.16.16:8090/httpclient.html"


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get(url)
input("Press Enter to close...")