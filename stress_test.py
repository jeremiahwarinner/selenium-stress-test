from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, UnexpectedAlertPresentException
import time
import statistics
import csv
import os
import random
import string
import json

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

    load_times = []
    for _ in range(num_iterations):
        start_time = time.time()

        driver.get(url)

        # Click on the login button
        login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_button.click()

        # Click on "Create new account"
        create_account_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create new account')]")))
        create_account_button.click()

        # Fill in the sign-up form
        username = generate_random_username()
        email = generate_random_email()
        password = generate_random_password()

        username_field = wait.until(EC.presence_of_element_located((By.ID, "uname")))
        email_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")

        username_field.send_keys(username)
        email_field.send_keys(email)
        password_field.send_keys(password)

        # Click on "Create Account"
        create_account_submit = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Account')]")
        create_account_submit.click()

        # Handle the "Thanks for joining" alert
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"Alert present with text: {alert_text}")
            alert.accept()
            print("Alert accepted")
        except TimeoutException:
            print("No alert present")

        end_time = time.time()
        load_time = end_time - start_time
        load_times.append(load_time)

    driver.quit()
    return load_times

def stress_test(url, num_users, num_iterations):
    with ThreadPoolExecutor(max_workers=num_users) as executor:
        futures = [executor.submit(run_test, url, num_iterations) for _ in range(num_users)]
        results = [future.result() for future in futures]
    
    return [item for sublist in results for item in sublist]

def calculate_metrics(load_times):
    return {
        "avg_load_time": statistics.mean(load_times),
        "median_load_time": statistics.median(load_times),
        "95th_percentile": statistics.quantiles(load_times, n=20)[-1],
        "99th_percentile": statistics.quantiles(load_times, n=100)[-1],
        "max_load_time": max(load_times),
        "min_load_time": min(load_times)
    }

def main():
    url = os.environ.get('TEST_URL', 'https://c397team05dev.computerlab.online')
    num_users = int(os.environ.get('NUM_USERS', '100'))
    num_iterations = int(os.environ.get('NUM_ITERATIONS', '5'))

    print(f"Starting stress test with {num_users} concurrent users, {num_iterations} iterations each")
    
    output_data = {
        "test_parameters": {
            "url": url,
            "num_users": num_users,
            "num_iterations": num_iterations
        },
        "iterations": []
    }

    load_times = stress_test(url, num_users, num_iterations)
    
    for i, load_time in enumerate(load_times):
        output_data["iterations"].append({
            "user": (i // num_iterations) + 1,
            "iteration": (i % num_iterations) + 1,
            "load_time": load_time
        })

    metrics = calculate_metrics(load_times)
    output_data["insights"] = metrics

    # Print JSON output to terminal
    print(json.dumps(output_data, indent=2))

if __name__ == "__main__":
    main()
