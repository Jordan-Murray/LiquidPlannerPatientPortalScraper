import requests
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

login_url = "https://app.liquidplanner.com/people/sign_in"
dashboard_url = "https://app.liquidplanner.com/space/98957/external_dashboards/198462"

# Create a session object to persist cookies
session = requests.Session()

login_page_response = session.get(login_url)
login_page_soup = BeautifulSoup(login_page_response.content, 'html.parser')

csrf_token = login_page_soup.find('meta', {'name': 'csrf-token'})['content']

payload = {
    'authenticity_token': csrf_token,
    'person[email]': os.getenv('LIQUIDPLANNER_EMAIL'),   
    'person[password]': os.getenv('LIQUIDPLANNER_PASSWORD'),  
    'person[remember_me]': '1' 
}

login_response = session.post(login_url, data=payload)

if login_response.ok and 'sign_in' not in login_response.url:
    response = session.get(dashboard_url)

    soup = BeautifulSoup(response.content, 'html.parser')

    tables = soup.find_all('table')

    with pd.ExcelWriter('patient_portal_data.xlsx', engine='xlsxwriter') as writer:
        table_count = 1

        for table in tables:
            header_row = table.find_all('th')
            headers = [header.text.strip() for header in header_row] if header_row else []

            patient_portal_rows = []

            rows = table.find_all('tr')
            for row in rows:
                if 'Patient Portal' in row.text:
                    row_data = [cell.text.strip() for cell in row.find_all(['td', 'th'])]
                    patient_portal_rows.append(row_data)

            if patient_portal_rows:
                if headers:
                    df = pd.DataFrame(patient_portal_rows, columns=headers)
                else:
                    df = pd.DataFrame(patient_portal_rows)  

                sheet_name = f'Table_{table_count}'
                df.to_excel(writer, sheet_name=sheet_name, index=False)

                # Auto-adjust the column width
                worksheet = writer.sheets[sheet_name]  
                for idx, col in enumerate(df.columns):
                    max_len = max(
                        df[col].astype(str).apply(len).max(),  # Length of the longest item in the column
                        len(col)  # Length of the column header
                    )
                    worksheet.set_column(idx, idx, max_len + 2)  # Add some padding to the width

                print(f"Data from table {table_count} saved to sheet '{sheet_name}' in 'patient_portal_data.xlsx'.")
                table_count += 1

else:
    print("Login failed. Please check your credentials.")
