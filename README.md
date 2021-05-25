# QuotationProject / Quotation Application For Motor Insurance

Web Application for creating Quotes in Motor Insurance.

# Getting Started:
Pre-requisites: Project is built and validated using the following software
Insall the below,
	* Python (v.3.8), 
	* HTML5, Javascript, Css, JQuery, Bootstrap
	* Django (v.3.2)
  * Docker(latest for windows/ubuntu)

# Setup
1. Clone the repository(By using git clone https://github.com/pachasaheb55/QuotationProject.git) or download it as zip file.
2. Navigate to QuoationProject directory and open a command prompt to execute the following command
      > docker-compose up --build  (or) docker-compose up 
   It will build all the containers/images. Check for below output in the log to ensure the build is successfull and everything is up and running
     For celery check  the output as --> celery_1  | [2021-05-25 05:56:37,617: INFO/MainProcess] celery@4b61c000b407 ready.
     For Django chech the ouptut as --> django    | System check identified no issues (0 silenced).
                                        django    | May 25, 2021 - 06:24:10
                                        django    | Django version 3.2, using settings 'QuoteProject.settings'
                                        django    | Starting development server at http://0.0.0.0:8000/
3. Once we see the above output, open any browser and navigate to link http://localhost:8000/quote/ to find the landing page.

Note: If any docker issues arise due to other softwares running in other dockers we can run the below
       >docker system prune -a   
      which will remove any containers or images running before and the we can run 
       >docker-compose up

# Work Flow
