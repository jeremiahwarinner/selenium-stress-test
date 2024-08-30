from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, UnexpectedAlertPresentException
import time
import statistics
import os
import random
import string
import json
from time import sleep
from concurrent.futures import ThreadPoolExecutor

def generate_random_username():
    return ''.join(random.choices(string.ascii_lowercase, k=8))

def generate_random_email():
    return f"{generate_random_username()}@example.com"

def generate_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def run_test(url, num_iterations):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    iteration_results = []
    for _ in range(num_iterations):
        iteration_data = {}

        try:
            page_start_time = time.time()
            driver.get(url)
            page_end_time = time.time()
            iteration_data['page_load_time'] = page_end_time - page_start_time
#click login link in header
            login_click_start_time = time.time()
            login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_button.click()
            login_click_end_time = time.time()
            iteration_data['login_click_time'] = login_click_end_time - login_click_start_time
#click create account button 
            create_account_click_start_time = time.time()
            create_account_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create new account')]")))
            create_account_button.click()
            create_account_click_end_time = time.time()
            iteration_data['create_account_click_time'] = create_account_click_end_time - create_account_click_start_time
#generate random login credentials
            username = generate_random_username()
            email = generate_random_email()
            password = generate_random_password()
#fill out form for account creation
            form_fill_start_time = time.time()
            username_field = wait.until(EC.presence_of_element_located((By.ID, "uname")))
            email_field = driver.find_element(By.ID, "email")
            password_field = driver.find_element(By.ID, "password")
            username_field.send_keys(username)
            email_field.send_keys(email)
            password_field.send_keys(password)
            form_fill_end_time = time.time()
            iteration_data['form_fill_time'] = form_fill_end_time - form_fill_start_time
#press create account
            create_account_submit_start_time = time.time()
            create_account_submit = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Account')]")
            create_account_submit.click()
            create_account_submit_end_time = time.time()
            iteration_data['create_account_submit_time'] = create_account_submit_end_time - create_account_submit_start_time
#handle alert
            alert_wait_start_time = time.time()
            try:
                WebDriverWait(driver, 10).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                alert_text = alert.text
                print(f"Alert present with text: {alert_text}")
                alert.accept()
                print("Alert accepted")
            except TimeoutException:
                print("No alert present")
            alert_wait_end_time = time.time()
            iteration_data['alert_wait_time'] = alert_wait_end_time - alert_wait_start_time
#navigate to login 
            login_click_start_time_1 = time.time()
            login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_button.click()
            login_click_end_time_1 = time.time()
            iteration_data['login_click_time_1'] = login_click_end_time_1 - login_click_start_time_1
#filling out login form
            form_fill_start_time_1 = time.time()
            username_field = wait.until(EC.presence_of_element_located((By.ID, "uname")))
            password_field = driver.find_element(By.ID, "password")
            username_field.send_keys(username)
            password_field.send_keys(password)
            form_fill_end_time_1 = time.time()
            iteration_data['form_fill_time_1'] = form_fill_end_time_1 - form_fill_start_time_1
#login button press
            login_form_button_click_start_time = time.time()
            login_form_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]")))
            login_form_button.click()
            login_form_button_click_end_time = time.time()
            iteration_data['login_form_button_click_time'] = login_form_button_click_end_time - login_form_button_click_start_time
#click quotes link
            quote_click_start_time = time.time()
            quote_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Quotes")))
            quote_button.click()
            quote_click_end_time = time.time()
            iteration_data['quote_click_time'] = quote_click_end_time - quote_click_start_time
#click buy by href 
            buy_button_click_start_time = time.time()
            buy_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/Trade/buy/A']")))
            driver.execute_script("arguments[0].click();", buy_button)
            buy_button_click_end_time = time.time()
            iteration_data['buy_button_click_time'] = buy_button_click_end_time - buy_button_click_start_time
#click place order 
            place_button_click_start_time = time.time()
            place_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Place Order')]")))
            place_button.click()
            place_button_click_end_time = time.time()
            iteration_data['place_button_click_time'] = place_button_click_end_time - place_button_click_start_time
#handle alert
            alert_wait_start_time = time.time()
            try:
                WebDriverWait(driver, 10).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                alert_text = alert.text
                print(f"Alert present with text: {alert_text}")
                alert.accept()
                print("Alert accepted")
            except TimeoutException:
                print("No alert present")
            alert_wait_end_time = time.time()
            iteration_data['alert_wait_time'] = alert_wait_end_time - alert_wait_start_time

#click quotes link
            quote_click_start_time_1 = time.time()
            quote_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Quotes")))
            quote_button.click()
            quote_click_end_time_1 = time.time()
            iteration_data['quote_click_time_1'] = quote_click_end_time_1 - quote_click_start_time_1
#click sell by href using js 
            sell_button_click_start_time = time.time()
            sell_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/Trade/sell/A']")))
            driver.execute_script("arguments[0].click();", sell_button)
            sell_button_click_end_time = time.time()
            iteration_data['sell_button_click_time'] = sell_button_click_end_time - sell_button_click_start_time
#click place order 
            place_button_click_start_time_1 = time.time()
            place_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Place Order')]")))
            place_button.click()
            place_button_click_end_time_1 = time.time()
            iteration_data['place_button_click_time_1'] = place_button_click_end_time_1 - place_button_click_start_time_1
#handle alert
            alert_wait_start_time = time.time()
            try:
                WebDriverWait(driver, 10).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                alert_text = alert.text
                print(f"Alert present with text: {alert_text}")
                alert.accept()
                print("Alert accepted")
            except TimeoutException:
                print("No alert present")
            alert_wait_end_time = time.time()
            iteration_data['alert_wait_time'] = alert_wait_end_time - alert_wait_start_time
#click logout
            logout_click_start_time = time.time()
            logout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout ("+ str(username) +")")))
            driver.execute_script("arguments[0].click();", logout_button)
            logout_click_end_time = time.time()
            iteration_data['portfolio_click_time'] = logout_click_end_time - logout_click_start_time
#handle alert
            alert_wait_start_time = time.time()
            try:
                WebDriverWait(driver, 10).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                alert_text = alert.text
                print(f"Alert present with text: {alert_text}")
                alert.accept()
                print("Alert accepted")
            except TimeoutException:
                print("No alert present")
            alert_wait_end_time = time.time()
            iteration_data['alert_wait_time'] = alert_wait_end_time - alert_wait_start_time
#done
        except (TimeoutException, NoSuchElementException, UnexpectedAlertPresentException) as e:
            print(f"Error during test execution: {str(e)}")
            iteration_data['error'] = str(e)
            
        iteration_results.append(iteration_data)
        
    driver.quit()
    return iteration_results

def stress_test(url, num_users, num_iterations):
    with ThreadPoolExecutor(max_workers=num_users) as executor:
        futures = [executor.submit(run_test, url, num_iterations) for _ in range(num_users)]
        results = [future.result() for future in futures]
    
    return [item for sublist in results for item in sublist]

def calculate_metrics(results):
    load_times = {
        'page_load_time': [],
        'login_click_time': [],
        'create_account_click_time': [],
        'form_fill_time': [],
        'create_account_submit_time': [],
        'alert_wait_time': []
    }

    for result in results:
        for key in load_times.keys():
            if key in result:
                load_times[key].append(result[key])

    metrics = {}
    for key, times in load_times.items():
        if times:
            metrics[key] = {
                "avg_time": statistics.mean(times),
                "median_time": statistics.median(times),
                "95th_percentile": statistics.quantiles(times, n=20)[-1],
                "99th_percentile": statistics.quantiles(times, n=100)[-1],
                "max_time": max(times),
                "min_time": min(times)
            }

    return metrics

def main():
    url = os.environ.get('TEST_URL', 'https://c397team05dev.computerlab.online')
    num_users = int(os.environ.get('NUM_USERS', '100'))
    num_iterations = int(os.environ.get('NUM_ITERATIONS', '3'))

    print(f"Starting stress test with {num_users} concurrent users, {num_iterations} iterations each")
    
    output_data = {
        "test_parameters": {
            "url": url,
            "num_users": num_users,
            "num_iterations": num_iterations
        },
        "iterations": []
    }

    results = stress_test(url, num_users, num_iterations)
    
    for i, result in enumerate(results):
        output_data["iterations"].append({
            "user": (i // num_iterations) + 1,
            "iteration": (i % num_iterations) + 1,
            **result
        })

    metrics = calculate_metrics(results)
    output_data["insights"] = metrics

    print(json.dumps(output_data, indent=2))

if __name__ == "__main__":
    main()
