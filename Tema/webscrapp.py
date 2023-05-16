import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta

def get_data(driver, url):
    driver.get(url)
    try:
        table = driver.find_element(By.XPATH, "//table")

        rows = table.find_elements(By.XPATH, ".//tr[position()>1]")
        data = []
        for row in rows:
            row_data = row.find_elements(By.XPATH, ".//td")
            data.append([cell.text for cell in row_data[:3]])

        return pd.DataFrame(data, columns=['NR. CRT.', 'JUDEȚ', 'NUMĂR DE CAZURI CONFIRMATE (total)'])
    except NoSuchElementException:
        return None

driver = webdriver.Chrome()  # or use another driver, e.g. webdriver.Firefox()
final_df = pd.DataFrame(columns=['NR. CRT', 'Judet', '01.03', '02.03', '03.03', '04.03', '05.03'])
base_url = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{}-ora-13-00-2/"
dates = ['1-martie', '2-martie', '3-martie', '4-martie', '5-martie']
column_dates = ['01.03', '02.03', '03.03', '04.03', '05.03']
for date, column_date in zip(dates, column_dates):
    url = base_url.format(date)
    data = get_data(driver, url)

    if data is not None:
        data = data[['NR. CRT.', 'JUDEȚ', 'NUMĂR DE CAZURI CONFIRMATE (total)']]
        data.columns = ['NR. CRT', 'Judet', column_date]
        final_df = final_df.merge(data, on=['NR. CRT', 'Judet'], how='outer')
    else:
        print(f"No data found for {column_date}")

driver.quit()
final_df.to_excel("covid_data.xlsx", index=False)
