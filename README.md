# QuotationProject / Quotation Application For Motor Insurance

Web Application for creating Quotes in Motor Insurance.

# Getting Started:
Pre-requisites: Project is built and validated using the following software
Insall the below,
- Python (v.3.8), 
- HTML5, Javascript, Css, JQuery, Bootstrap
- Django (v.3.2)
- Docker(latest for windows/ubuntu)

# Setup
1. Clone the repository(By using git clone https://github.com/pachasaheb55/QuotationProject.git) or download it as zip file.
2. Navigate to QuoationProject directory and open a command prompt to execute the following command

     ```sh 
     PATH\QuotaionProject>docker-compose up --build  (or) docker-compose up
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
2. Create Quote- By clicking on QUICK QUOTE button customer will navigated to http://localhost:8000/quote/createQuote/ and cansee the create quote page with all the 3 forms.
 
	<img width="750" alt="create-quote" src="https://user-images.githubusercontent.com/80810225/119462202-17467100-bd5e-11eb-8c66-3da44e49ec5d.PNG">
   
   Now user can enter the required details for the quote to create and click on the GET QUTOE button for getting the quotation price. Below are the example screensshots
   
   >ScreenShot 1: Successful Quote 
   	
	![example2](https://user-images.githubusercontent.com/80810225/119464558-79a07100-bd60-11eb-90ea-ee0faa5992a3.png)

   >Screenshot 2: successful Quote
   
   	![exampl-1](https://user-images.githubusercontent.com/80810225/119464670-99d03000-bd60-11eb-82f2-2b9348388ade.png)
	
   >Screenshot 3: Validation message for the email input field

	![example-3 (1)](https://user-images.githubusercontent.com/80810225/119466611-6c848180-bd62-11eb-99e0-ee13b12c93b1.png)

   >Screenshot 4: Validation message for the coverage field

	![example-3 (2)](https://user-images.githubusercontent.com/80810225/119466645-760de980-bd62-11eb-8c5d-e6255d32cb8d.png)
	
   Note:
   	a. Each field in the form consists of validations.
	b. Provided a checkbox field Get Summary By Email, and its value will be saved in Quotation Table. For now havent implemented the mail send from customer side. Only 		insurance agent who can login and can send the email.





