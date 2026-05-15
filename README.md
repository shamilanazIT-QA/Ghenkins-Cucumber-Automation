# Ghenkins-Cucumber-Automation
# Data-Driven BDD Test Automation Framework

A professional behavior-driven development (BDD) test automation framework built using **Python**, **Behave (Gherkins)**, and **Selenium WebDriver**. 

This project demonstrates automated testing against a realistic web application (SauceDemo), utilizing data-driven testing templates, advanced synchronization (Explicit Waits), and an automated CI/CD pipeline via GitHub Actions.

## 🚀 Key Features
*   **Behavior-Driven Development:** Uses human-readable Gherkin syntax (`.feature` files) to map business requirements directly to executable automated test steps.
*   **Data-Driven Architecture:** Leverages Gherkin `Scenario Outlines` and `Examples` tables to run identical test flows against multiple user profiles and conditions simultaneously.
*   **Robust Synchronization:** Eliminates flaky tests by implementing Selenium `WebDriverWait` (Explicit Waits) to seamlessly handle web performance delays and asynchronous loading.
*   **CI/CD Integration:** Configured with a headless browser automation workflow (`GitHub Actions`) that triggers test suites automatically on every code push or pull request.

---

## 🛠️ Project Structure
```text
PythonProject3/
│
├── .github/
│   └── workflows/
│       └── behave_tests.yml   # GitHub Actions CI/CD configuration
├── features/
│   ├── steps/
│   │   └── login_steps.py     # Step definition implementations
│   ├── environment.py         # Hooks for browser setup (Local & CI/CD Headless)
│   └── login.feature          # Gherkin Scenario Outlines & Test Data
└── requirements.txt           # Project dependencies
