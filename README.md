# Selenium-Google-Form
## Using selenium to fill a google form 
### (**for learning & personal purposes**, use it wisely)

---

### Explanation & Reference:
- Explanation blog post: [My Medium Blog](https://albertosanjaya.medium.com/using-selenium-web-driver-to-automatic-filling-a-google-form-3bf85fb6ce25)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
---  
## On used:
- Python 3.10.6
- Pip 22.2.2
- Selenium Web Driver - Chrome Version 104 ([Download here](https://chromedriver.chromium.org/downloads))\*
- Google form without requirement to sign in 
  
\* Make sure to download the same version as your chrome, won't work if different version.

---
## Scenario that covered with this program:
- textbox input
- radio button input
- checkbox input
- linear scale input
- next button (each section) & submit button (multi-section form)

 
---
### To install requirement
``` pip install -r requirement.txt ```

### To only use one time 
1. Clone this repository
2. Change the webdriver executable_path
3. Change the google form link
4. Change the input format (radio button, textbox, submit button, etc.)
5. Execute in terminal with ``` python autogform.py ```

### To only more than one time 
1. Clone this repository
2. Change the webdriver executable_path
3. Change the google form link
4. Change the input format (radio button, textbox, submit button, etc.)
5. Change how much time the goggle form to be submit (inside auto-spam.py)
6. Execute in terminal with ``` python auto-spam.py ```