After completing some basic Selenium with Python courses, I wanted to see and understand how an entire Selenium framework works together. So, I found this Youtube channel called Qtomation, which has a very good training playlist with a project built from scratch.
In this project, pytest was used as the testing framework along with the Page Object Model (POM) folder structure. Initially, I followed the project on the channel, but I encountered a captcha issue with the website used in the training. So, I switched to automationteststore.com as my testing site.

The project includes several test cases:
• Test Create Account: 
This test verifies that an account is created successfully when valid information is entered in the form.

• Test Login:
This test verifies the title of the login page and tests both valid and invalid login scenarios.

• Test Login (Data-Driven):
This test performs login tests using data from an Excel file, which I managed with OpenPyXL and utility methods for Excel.

• Test Shopping Cart:
This test ensures that items added to the shopping cart from the product page are accurate.

I also learned how to:
• Run tests in parallel using the pytest-xdist plugin,
• Mark tests for regression or sanity testing,
• Run tests via a .bat file,
• Improve my debugging skills,
• Generate HTML reports and modify their metadata,
• Capture logs and screenshots,
• Run tests on different browsers by using the parser adoption function and Pytest fixtures.

This project has given me a much better understanding of how all the pieces of a Selenium framework fit together. I will definitely continue to explore, learn more, and create additional test cases to enhance my skills further.
