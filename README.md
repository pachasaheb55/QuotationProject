# QuotationProject / Quotation Application For Motor Insurance

Web Application for creating Quotes in Motor Insurance.

# Getting Started:
Pre-requisites: Project is built and validated using the following software
Insall the below,
- Python (v.3.8), 
- Django (v.3.2)
- Docker(latest for windows/ubuntu)

# Setup
1. Clone the repository(By using git clone https://github.com/pachasaheb55/QuotationProject.git) or download it as zip file.
2. Navigate to QuoationProject directory and open a command prompt to execute the following command

     ```sh 
     PATH\QuotationProject>docker-compose up --build  (or) docker-compose up
     ``` 
   It will build all the containers/images. Check for below output in the log to ensure the build is successfull and everything is up and running
   >For celery check  the output as:
    ```sh
    celery_1  | [2021-05-25 05:56:37,617: INFO/MainProcess] celery@4b61c000b407 ready.
    ```
   >For Django check the ouptut as:
   ```sh
   django    | System check identified no issues (0 silenced).
   django    | May 25, 2021 - 06:24:10
   django    | Django version 3.2, using settings 'QuoteProject.settings'
   django    | Starting development server at http://0.0.0.0:8000/
   ```
3. Once we see the above output, open any browser and navigate to link http://localhost:8000/quote/ to find the landing page.
4. Please give the email settings in quoteapp/settings.py file for email sending actions. Please change the below settings accordingly
	```
	EMAIL_HOST = 'smtp.gmail.com'
	EMAIL_PORT = '587'
	EMAIL_HOST_USER = 'abcde@gmail.com'
	EMAIL_HOST_PASSWORD = 'abcde'
	```
5. SuperUser is already created for the admin login page at http://localhost:8000/quotations-admin/. Credentials for admin user are
	```
	username: admin
	password: admin
	```
Note: If any docker issues arise due to other softwares running in other dockers we can run the below
       ```
       docker system prune -a
       ```
   which will remove any containers or images running before and the we can run 
      ```
       docker-compose up
      ```

# Work Flow/Screen Flow
1. Home/Landing Page, navigate to url http://localhost:8000/quote/, where customer can see 3 options on right side

- Quick Quote
- View Quote
- Admin Login

	<img width="750" alt="home" src="https://user-images.githubusercontent.com/80810225/119461092-fe898b80-bd5c-11eb-8efa-16a9b4b020ff.PNG">
	
2. Create Quote- By clicking on QUICK QUOTE button customer will navigated to http://localhost:8000/quote/createQuote/ and can see the create quote page with all the 3 forms.
 
	<img width="750" alt="create-quote" src="https://user-images.githubusercontent.com/80810225/119462202-17467100-bd5e-11eb-8c66-3da44e49ec5d.PNG">
   
   Now user can enter the required details for the quote to create and click on the GET QUTOE button for getting the quotation price. Below are the example screenshots
   
   >Screenshot 1: Successful Quote 
   	
	![example2](https://user-images.githubusercontent.com/80810225/119464558-79a07100-bd60-11eb-90ea-ee0faa5992a3.png)

   >Screenshot 2: Successful Quote
   
   	![exampl-1](https://user-images.githubusercontent.com/80810225/119464670-99d03000-bd60-11eb-82f2-2b9348388ade.png)
	
   >Screenshot 3: Validation message for the email input field

	![example-3 (1)](https://user-images.githubusercontent.com/80810225/119466611-6c848180-bd62-11eb-99e0-ee13b12c93b1.png)

   >Screenshot 4: Validation message for the coverage field

	![example-3 (2)](https://user-images.githubusercontent.com/80810225/119466645-760de980-bd62-11eb-8c5d-e6255d32cb8d.png)
	
   Note:
   	- Each field in the form consists of validations.
	- Provided a checkbox field Get Summary By Email, and its value will be saved in Quotation Table. For now havent implemented the mail send from customer side. Only 		insurance agent who can login and can send the email.
	- Here user can select multiple coverages and quatation price will be calculated accordingly.
	
3. After updating required values and seeing the quote price displayed below, customer can click on SUMMARY button which acts as a submit for all the forms and quotaion gets 	created in the database. And screen will be automaticllay routed to Quote Summary Page as shown below at http://localhost:8000/quote/quoteSummary/1/
	
	![quote-summary](https://user-images.githubusercontent.com/80810225/119469940-7491f080-bd65-11eb-835c-4f83873a2fa3.png)
   
   Note: User can use links in the footer section to Navigagte to Home Page or Cusotmer Quote View Page.
   
4. In HOME PAGE VIEW QUOTES Button will navigate customer to a login page at url http://localhost:8000/quote/customer/ as shown below
	
	<img width="750" alt="login" src="https://user-images.githubusercontent.com/80810225/119485989-5af8a500-bd75-11eb-8f9a-4709b98f8b6c.PNG">

   This customer login page has its own validations. Now user can enter registered mail id and can login into application. See the below screens
   
   >Screenshot 1:
   
   	<img width="750" alt="invalid-email" src="https://user-images.githubusercontent.com/80810225/119486655-1de0e280-bd76-11eb-8a7c-cf0dc6dfd993.PNG">	
	
   >Screenshot 2:

	<img width="960" alt="email-validation" src="https://user-images.githubusercontent.com/80810225/119486677-26d1b400-bd76-11eb-832f-17ab1291cc4c.PNG">	

  After giving the correct email id and clicking on login will take to the customer dashboard screen where details are shown in an table format. For full detail customer can 	click on last row in the table, which route to summary page for full details
  		<img width="750" alt="logged-in" src="https://user-images.githubusercontent.com/80810225/119486707-2f29ef00-bd76-11eb-8d4e-74c431af7065.PNG">

  Note: For now we are taking email id as unique in database, so one customer with one email id can create only one quote.
	
5. Now Insurance Agent can Login as Admin with django admin at http://localhost:8000/quotations-admin/. Please enter the credentials as shown in Setup seciton step 5.
	
	<img width="750" alt="admin-login" src="https://user-images.githubusercontent.com/80810225/119495009-9009f500-bd7f-11eb-8b58-5c3fddf13127.PNG">

   Enter the Credetnial and click on login
   	<img width="750" alt="admin-coverages" src="https://user-images.githubusercontent.com/80810225/119495130-b3cd3b00-bd7f-11eb-9023-399c594ed2bc.PNG">

   Admin will have all the access to models/tables data as shown in the above screen. So insurance agent as an admin can edit the coverage values as needed.
6. Insurane Agent can now access Quotations model in Django admin portal and can select the required quotation object and can perform the django admin action of 'Send Email 	to Customer' displayed on the top by selecting and clicking 'GO' button.

	![Screenshot (48)](https://user-images.githubusercontent.com/80810225/119495668-4372e980-bd80-11eb-87ea-ec2903073862.png)

   Now the quotation selected is linked to a customer with respective email id will recieve a mail from the insurance agent with an attachment PDF of Quotation Summary with      the Customer Details, Vehicle Details, Coverage Details as shown below 
   	<img width="749" alt="email" src="https://user-images.githubusercontent.com/80810225/119496317-00fddc80-bd81-11eb-9091-74e4d1688e70.PNG">

	
# TASK COMPLETION:
1. Create an app called 'quotations'. 
- Created a Djnago project called 'QuotationProject', Djangoapp as 'quoteapp', docker-compose.yaml, DOcker file

2. Design and create models for 'Quotation'.
- Created models for Customer, Vehicle, CoverageInfo, Quotations in `QuotationProject\quoteapp\models.py`

3. Create Django admin with link `http://localhost:8000/quotations-admin/` for insurance agents to login and view the quotations data.
- Modified the admin site urls to above url in `QuoteProject\urls.py`
5.Create Django admin action on Quotation model admin for insurance agent to select on quotations and "send email to user".
- Created an admin action in `quoteapp\admin.py` file as send_email_to_customer()
6.Create a quotation formset page for users to submit the form and generate the quotation pricing.
- Created Forms for indiviudal models with validations in `quoteapp\forms.py`
7.Create quotation pdf generator function and send email function.
- Created celery task in `quoteapp\tasks.py` as pdf_generator_task() which will render an HTML to PDF.
8.Create a login page for users to login to view their created quotations.
- Created a Login Page for customer to view the created quote at `http://localhost:8000/quote/customer/`
- 
 Special requests:
1.      Setup the application with Docker. - Yes created a Python-Django, Celery, Redis based docker application 
2.      Generate the PDF with Celery. - Yes, written a celery task for pdf_generation
3.      Setup documentation. - Below setup document consists of steps from scratch and above setup section can be followed to run the app in any other machine.
		[step_creation.docx](https://github.com/pachasaheb55/QuotationProject/files/6539271/step_creation.docx)
		



  
  	
  






