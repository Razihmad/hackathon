#Introduction
The submissions app allows authorized users to create and manage hackathons, as well as allow users to submit code or files as hackathon submissions. 
This documentation provides information on the API endpoints and parameters used in the submissions app.

#Authentication
All endpoints in the submissions app require authentication. Users must include a valid username and password in the request header.

#API Endpoints

Create Hackathon
Endpoint: /api/hackathons/
HTTP Method: POST


#Request Parameters:

    title (string): the title of the hackathon
    description (string): a brief description of the hackathon
    background_image (file): the background image for the hackathon
    hackathon_image (file): the image for the hackathon
    type_of_submission (string): the type of submission allowed (image, file, or link)
    start_datetime (string): the start date and time for the hackathon in ISO 8601 format
    end_datetime (string): the end date and time for the hackathon in ISO 8601 format
    reward_prize (integer): the reward prize for the hackathon in dollars

#Response Parameters:

    id (integer): the ID of the newly created hackathon
    title (string): the title of the hackathon
    description (string): a brief description of the hackathon
    background_image_url (string): the URL of the background image for the hackathon
    hackathon_image_url (string): the URL of the image for the hackathon
    type_of_submission (string): the type of submission allowed (image, file, or link)
    start_datetime (string): the start date and time for the hackathon in ISO 8601 format
    end_datetime (string): the end date and time for the hackathon in ISO 8601 format
    reward_prize (integer): the reward prize for the hackathon in dollars
  
 
#List Hackathons
#Endpoint: /api/hackathons/
#HTTP Method: GET

#Response Parameters:

    id (integer): the ID of the hackathon
    title (string): the title of the hackathon
    description (string): a brief description of the hackathon
    background_image_url (string): the URL of the background image for the hackathon
    hackathon_image_url (string): the URL of the image for the hackathon
    type_of_submission (string): the type of submission allowed (image, file, or link)
    start_datetime (string): the start date and time for the hackathon in ISO 8601 format
    end_datetime (string): the end date and time for the hackathon in ISO 8601 format
    reward_prize (integer): the reward prize for the hackathon in dollars
    
    
#Register for Hackathon
#Endpoint: /api/hackathons/register/
#HTTP Method: POST

#Request Parameters:

    hackathon (int id): the primary key of the hackathon that user want to register



#Submit Hackathon
#Endpoint: /api/hackathons/submit/
#HTTP Method: POST

#Request Parameters:

    name (string): the name of the submission
    summary (string): a summary of the submission
    submission_file (file): the file to the submission
    submission_image : the image to the submission
    submission_link: the link of the submission
    note-> any one of above three of submission 
    
 
#Response Parameters:

    id (integer): the ID of the submission
    name (string): the name of the submission
    summary (string): a summary of the submission
    
#Update Submitted Hackathon
#Endpoint: /api/hackathons/submit/{submission_id}/
#HTTP Method: POST

#Request Parameters:

    name (string): the name of the submission
    summary (string): a summary of the submission
    submission_file (file): the file to the submission
    submission_image : the image to the submission
    submission_link: the link of the submission
    note-> any one of above three of submission 

#Response Parameters:

    id (integer): the ID of the submission
    name (string): the name of the submission
    summary (string): a summary of the submission
    
    
    
  
#List Enrolled Hackathons
#Endpoint: /api/users/enrolled_hackathons/
#HTTP Method: GET

#Response Parameters:

    id (integer): the ID of the hackathon
    title (string): the title of the hackathon
    description (string): a brief description of the hackathon
    background_image_url (string): the URL of the background image for the hackathon
    hackathon_image_url (string): the URL of the image for the hackathon
    type_of_submission (string): the type of submission allowed (image, file, or link)
    start_datetime (string): the start date and time for the hackathon in ISO 8601 format
    end_datetime (string): the end date and time for the hackathon in ISO 8601 format
    reward_prize (integer): the reward prize for the hackathon in dollars



#List User Submissions
#Endpoint: /api/users/submissions/
#HTTP Method: GET

#Response Parameters:

    id (integer): the ID of the submission
    name (string): the name of the submission
    summary (string): a summary of the submission
    submission_url (string): the URL of the submission
    created_at (string): the date and time the submission was created in ISO 8601 format



#New User Registration
#Endpoint: /api/user/register/
#HTTP Method: POST

#Request parameter
            username: username of your choice
            email: your email
            password: password
            paswword2: should be same as password
   




Conclusion
That's it for the API documentation for the submissions app! You can use this as a starting point and expand upon it as needed. 
Don't forget to include information on the data models, API response codes, and other important information that developers may need to know. Good luck!
