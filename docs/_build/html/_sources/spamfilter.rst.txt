User
=====================================

login
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/users/login
- **Parameter Location:** Request Body
- **Description:** Login to the Drill Platform

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "password": "string",
  "username": "string"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {"status":0, "token":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJzdW5pbDExMDExM0BbWFpbC5jb20iLCJhdXRob3JpdGllcyI6W3siYXV0aG9yaXR5IjoiU1VQRVJBRE1JTiJ9XSwiaWF0IjoxNjY0MjYwMDc2LCJleHAiOjE2NjQzMjMyMDB9.BcZRx2DPJxYUz7oJ6b2g_uhhA_iDemK-bDkN0gxCerHgScVfjasmRxjU6zNqfo883aP0RmwXV3w-YjR_VB6sVw", "userId":"null", "userDetails":{"uid":"8d72f798-c08b-42ef-82c1-2081d7e4764f","fullName":"Sunil Kumar","uemail":"sunil110113@gmail.com"}, "authorities":["SUPERADMIN"], "responseCode":200}




forgotpassword
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/users/forgotpassword
- **Parameter Location:** Request Body
- **Description:** API for forgot password and send the email to update password

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    Please check your email account for resetting password




loginattempt
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/users/loginattempt
- **Parameter Location:** Request Body
- **Description:** API to save a user's login atempt

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "attemptEmail": "string",
  "attemptStatus": "string",
  "attemptTime": datetime,
  "device": "string",
  "location": "string",
  "loginAttemptId": 0,
  "operatingSystem": "string"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "msg": "Login attempt saved"
}




register
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/users/register
- **Parameter Location:** Request Body
- **Description:** API to register users

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "active": true,
  "conditionAccepted": true,
  "fullName": "string",
  "jobfeed": true,
  "mentor": true,
  "password": "string",
  "resumeLink": "string",
  "ucontact": "string",
  "uemail": "string",
  "ugroup": "string",
  "uid": "string",
  "urole": "string",
  "userCreatedby": "string",
  "userCreatedts": "string",
  "userUpdatedby": "string",
  "userUpdatedts": "string",
  "username": "string",
  "utype": "string"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    tbd {"u_id":"4c989553-cc97-440f-823d-1c1ca2690f8a"}




resendverification
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/users/resendverification
- **Parameter Location:** Request Body
- **Description:** To resend verification email to user

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "headers": {},
  "body": {
    "msg": "You account is verified. Please click on Forgot Password or contact techsupport@wuelev8.tech for further support"
  },
  "statusCode": "INTERNAL_SERVER_ERROR",
  "statusCodeValue": 500
}




updatepassword
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/users/updatepassword
- **Parameter Location:** Request Body
- **Description:** To update password for user's account

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "emailid": "string",
  "newPassword": "string",
  "oldPassword": "string"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    tbd 




users
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/users
- **Parameter Location:** Request Body
- **Description:** To find details of a user as per given query

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [
  {
    "username": "abc@gmail.com",
    "fullName": "ABC XYZ",
    "email": "abc@gmail.com",
    "password": null,
    "userCreatedby": null,
    "mentor": true,
    "jobfeed": true,
    "resumeLink": "https://drive.google/",
    "userCreatedts": "2022-09-28T10:16:59.054+00:00",
    "userUpdatedby": null,
    "userUpdatedts": "2022-09-28T10:16:59.054+00:00",
    "active": true,
    "uid": "4c989553-cc97-440f-823d-1c1ca2690f8a",
    "conditionAccepted": true,
    "ucontact": "1234567890",
    "utype": "string",
    "urole": "USER",
    "ugroup": "GENERAL"
  }
]




search
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/users/search
- **Parameter Location:** Request Body
- **Description:** To find users' profiles according to given parameters

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "totalRecordCount": 1,
  "details": [
    {
      "uId": "4c989553-cc97-440f-823d-1c1ca2690f8a",
      "username": "abc@gmail.com",
      "fullName": "ABC XYZ",
      "uEmail": "abc@gmail.com",
      "uContact": "1234567890",
      "password": "$2a$10$SvBVrBDOFV1eUPCkw3a0ie13jctQQEm9Ccx/1JtSvkcTXAY1eiS3i",
      "uGroup": "GENERAL",
      "uRole": "USER",
      "isActive": true,
      "uType": "string",
      "isConditionAccepted": false,
      "resumeLink": null,
      "mentor": false,
      "jobfeed": false,
      "userCreatedby": null,
      "userUpdatedby": null,
      "userCreatedts": "2022-09-28T10:16:59.054+00:00",
      "userUpdatedts": "2022-09-28T10:16:59.054+00:00",
      "active": true,
      "uid": "4c989553-cc97-440f-823d-1c1ca2690f8a",
      "conditionAccepted": false,
      "ucontact": "1234567890",
      "utype": "string",
      "urole": "USER",
      "uemail": "abc@gmail.com",
      "ugroup": "GENERAL"
    }
  ]
}




login
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/users/verify/{encodedstring}
- **Parameter Location:** Request Body
- **Description:** tbd

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




accesses
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/users/{uId}/accesses/component
- **Parameter Location:** Request Body
- **Description:** To find if a user has access to a certain component

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




users
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/users/{userId}
- **Parameter Location:** Request Body
- **Description:** API to get a single user with uId

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "username": null,
  "fullName": null,
  "email": null,
  "password": null,
  "userCreatedby": null,
  "mentor": false,
  "jobfeed": false,
  "resumeLink": null,
  "userCreatedts": null,
  "userUpdatedby": null,
  "userUpdatedts": null,
  "uid": null,
  "active": false,
  "conditionAccepted": false,
  "ugroup": null,
  "urole": null,
  "utype": null,
  "ucontact": null
}




health
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/health
- **Parameter Location:** Request Body
- **Description:** tbd

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {"status": "UP"}




health
-----------------------------------------

- **Method:** DELETE
- **Request URL:** /api/v1/health
- **Parameter Location:** Request Body
- **Description:** tbd

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {"status": "UP"}




health
-----------------------------------------

- **Method:** HEAD
- **Request URL:** /api/v1/health
- **Parameter Location:** Request Body
- **Description:** tbd

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




health
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/health
- **Parameter Location:** Request Body
- **Description:** tbd

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {"status": "UP"}




health
-----------------------------------------

- **Method:** OPTIONS
- **Request URL:** /api/v1/health
- **Parameter Location:** Request Body
- **Description:** tbd

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




health
-----------------------------------------

- **Method:** PATCH
- **Request URL:** /api/v1/health
- **Parameter Location:** Request Body
- **Description:** tbd

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {"status": "UP"}




health
-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/health
- **Parameter Location:** Request Body
- **Description:** tbd

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {"status": "UP"}




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills
- **Parameter Location:** Request Body
- **Description:** To find details of a hackathon with drillid

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [
  {
    "active": true,
    "createdBy": "string",
    "createdTs": "2022-09-29T05:18:19.442Z",
    "drillApplicantCount": 0,
    "drillCoverImgUrl": "string",
    "drillCustUrl": "string",
    "drillEndDt": "2022-09-29T05:18:19.442Z",
    "drillHiringExp": "string",
    "drillHiringSkill": "string",
    "drillId": "string",
    "drillLogoUrl": "string",
    "drillMobileCoverImgSettings": "string",
    "drillName": "string",
    "drillNature": "string",
    "drillPageSettings": "string",
    "drillPartnerId": "string",
    "drillPartnerName": "string",
    "drillPurpose": "string",
    "drillRegistrationEndDt": "2022-09-29T05:18:19.442Z",
    "drillSectionComplete": "string",
    "drillSocialLinks": "string",
    "drillStartDt": "2022-09-29T05:18:19.442Z",
    "drillTeamSize": "string",
    "drillTimezone": "string",
    "drillType": "string",
    "updatedBy": "string",
    "updatedTs": "2022-09-29T05:18:19.442Z"
  }
]




drills
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills
- **Parameter Location:** Request Body
- **Description:** To add/update a new hackathon details

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "active": true,
  "createdBy": "string",
  "createdTs": "2022-09-29T05:18:19.274Z",
  "drillApplicantCount": 0,
  "drillCoverImgUrl": "string",
  "drillCustUrl": "string",
  "drillEndDt": "2022-09-29T05:18:19.274Z",
  "drillHiringExp": "string",
  "drillHiringSkill": "string",
  "drillId": "string",
  "drillLogoUrl": "string",
  "drillMobileCoverImgSettings": "string",
  "drillName": "string",
  "drillNature": "string",
  "drillPageSettings": "string",
  "drillPartnerId": "string",
  "drillPartnerName": "string",
  "drillPurpose": "string",
  "drillRegistrationEndDt": "2022-09-29T05:18:19.274Z",
  "drillSectionComplete": "string",
  "drillSocialLinks": "string",
  "drillStartDt": "2022-09-29T05:18:19.274Z",
  "drillTeamSize": "string",
  "drillTimezone": "string",
  "drillType": "string",
  "updatedBy": "string",
  "updatedTs": "2022-09-29T05:18:19.274Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "active": true,
  "createdBy": "string",
  "createdTs": "2022-09-29T05:18:19.274Z",
  "drillApplicantCount": 0,
  "drillCoverImgUrl": "string",
  "drillCustUrl": "string",
  "drillEndDt": "2022-09-29T05:18:19.274Z",
  "drillHiringExp": "string",
  "drillHiringSkill": "string",
  "drillId": "string",
  "drillLogoUrl": "string",
  "drillMobileCoverImgSettings": "string",
  "drillName": "string",
  "drillNature": "string",
  "drillPageSettings": "string",
  "drillPartnerId": "string",
  "drillPartnerName": "string",
  "drillPurpose": "string",
  "drillRegistrationEndDt": "2022-09-29T05:18:19.274Z",
  "drillSectionComplete": "string",
  "drillSocialLinks": "string",
  "drillStartDt": "2022-09-29T05:18:19.274Z",
  "drillTeamSize": "string",
  "drillTimezone": "string",
  "drillType": "string",
  "updatedBy": "string",
  "updatedTs": "2022-09-29T05:18:19.274Z"
}




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/participant/search
- **Parameter Location:** Request Body
- **Description:** To search users associated with a drill

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "totalRecordCount": 0,
  "details": []
}




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/participants
- **Parameter Location:** Request Body
- **Description:** To fetch participants with filter

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    []




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{custUrl}
- **Parameter Location:** Request Body
- **Description:** To get drillId from custom URL

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {"drillId":"{}"}




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{drillId}/common/participate
- **Parameter Location:** Request Body
- **Description:** To get drill specific common values

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "skills": [
    "Java",
    "reactJs",
    "Python",
    "NodeJs",
    "Docker",
    "DevOps",
    "Kubernetes",
    "Others"
  ],
  "knownPlatforms": "Facebook, LinkedIn, WUElev8, Twitter"
}




drills
-----------------------------------------

- **Method:** 
- **Request URL:** /api/v1/drills/{drillId}/participate
- **Parameter Location:** Request Body
- **Description:** To post details for registered user

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "aadharId": "string",
  "affiliatePlatform": "string",
  "clgName": "string",
  "clgPassingSemester": 0,
  "clgPassingYear": 0,
  "clgSpecialization": "string",
  "contact": "string",
  "createdBy": "string",
  "createdTs": "2022-09-29T05:18:19.277Z",
  "ctc": "string",
  "currentLoc": "string",
  "drillId": "string",
  "drillName": "string",
  "ectc": "string",
  "email": "string",
  "fullName": "string",
  "jobTitle": "string",
  "lastWorkingDay": "2022-09-29",
  "noticePeriod": "string",
  "notificationResponse": true,
  "organisation": "string",
  "pancardId": "string",
  "participantId": "string",
  "participantState": "string",
  "participantType": "string",
  "platformUId": "string",
  "preferredLoc": "string",
  "resumeLink": "string",
  "servingNoticePeriod": true,
  "skills": "string",
  "teamId": "string",
  "teamParticipationMessage": "string",
  "theme": "string",
  "updatedBy": "string",
  "updatedTs": "2022-09-29T05:18:19.277Z",
  "willingForJob": true,
  "yearsOfExperience": 0
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




drills
-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/drills/{drillId}/participate/{participantId}/state/{participantState}
- **Parameter Location:** Request Body
- **Description:** To add/update state of participant

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




drills
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/{drillId}/participate/{participantId}/teams
- **Parameter Location:** Request Body
- **Description:** To add a new team

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "createdBy": "string",
  "createdTs": "2022-09-29T08:58:13.561Z",
  "drillId": "8af2b4c5-6bb5-4985-b557-abbec4a5a4b7",
  "participantId": "string",
  "participantValue": "string",
  "selectedTheme": "string",
  "teamCurrentSize": 0,
  "teamId": "string",
  "teamImgUrl": "string",
  "teamLeadParticipantId": "string",
  "teamName": "string",
  "updatedBy": "string",
  "updatedTs": "2022-09-29T08:58:13.561Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "teamId": "bb94384e-32b2-4624-8266-3927e6f6d1be",
  "drillId": "8af2b4c5-6bb5-4985-b557-abbec4a5a4b7",
  "teamName": "string",
  "teamImgUrl": "string",
  "selectedTheme": "string",
  "teamLeadParticipantId": "8af2b4c5-6bb5-4985-b557-abbec4a5a4b7",
  "teamCurrentSize": 1,
  "participantValue": null,
  "participantId": null,
  "createdTs": "2022-09-29T09:00:43.241+00:00",
  "updatedTs": "2022-09-29T09:00:43.376+00:00",
  "createdBy": "string",
  "updatedBy": "string"
}




drills
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/{drillId}/participate/{participantId}/teams/{teamId}
- **Parameter Location:** Request Body
- **Description:** To add a new team member

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "createdBy": "string",
  "createdTs": "2022-09-29T08:58:13.562Z",
  "drillId": "string",
  "id": 0,
  "participantId": "string",
  "participantValue": "string",
  "requestAccepted": true,
  "teamId": "string",
  "updatedBy": "string",
  "updatedTs": "2022-09-29T08:58:13.562Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{drillId}/participate/{participantId}/teams/{teamId}/accept
- **Parameter Location:** Request Body
- **Description:** To accept team member

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{drillId}/teams
- **Parameter Location:** Request Body
- **Description:** To seach teams with initial letters

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{drillId}/teams/name
- **Parameter Location:** Request Body
- **Description:** To check if a team name is available

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    TRUE




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{drillId}/teams/{teamId}
- **Parameter Location:** Request Body
- **Description:** To get drill teams

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    []




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{drillId}/users/{uId}
- **Parameter Location:** Request Body
- **Description:** To get all the information of a user

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    FALSE-tbd




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{drillId}/{section}
- **Parameter Location:** Request Body
- **Description:** To search drill section

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




drills
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/{section}
- **Parameter Location:** Request Body
- **Description:** To save section in drill

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    payload


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/mails/participantTypes
- **Parameter Location:** Request Body
- **Description:** To get types of participants

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [
  "Participant",
  "Shortlisted",
  "Fighters",
  "Winners:Participant",
  "Shortlisted",
  "Fighters",
  "Winners"
]




drills
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/{drillId}/mails
- **Parameter Location:** Request Body
- **Description:** To send mail to participants

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "listOfBcc": [
    "string"
  ],
  "listOfReceiver": [
    "string"
  ],
  "listofCc": [
    "string"
  ],
  "mailBody": "string",
  "mailSubject": "string",
  "templateName": "string",
  "userType": "string"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{drillId}/mails/templates
- **Parameter Location:** Request Body
- **Description:** To get mail templates

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




drills
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/{drillId}/mails/templates
- **Parameter Location:** Request Body
- **Description:** To add/update mail templates

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "createdBy": "string",
  "createdTs": "2022-09-29T08:58:13.560Z",
  "drillId": "string",
  "mailBody": "string",
  "mailSubject": "string",
  "mailTemplateId": "string",
  "templateDesc": "string",
  "templateName": "string",
  "updatedBy": "string",
  "updatedTs": "2022-09-29T08:58:13.560Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "mailTemplateId": "7b6348c6-8383-44dc-b9e8-88ed095d2725",
  "drillId": "8af2b4c5-6bb5-4985-b557-abbec4a5a4b7",
  "templateName": "string",
  "templateDesc": "string",
  "mailSubject": "string",
  "mailBody": "string",
  "createdTs": "2022-09-29T11:20:44.764+00:00",
  "updatedTs": "2022-09-29T11:20:44.764+00:00",
  "createdBy": "string",
  "updatedBy": "string"
}




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/submissionFields/default
- **Parameter Location:** Request Body
- **Description:** To get default submission fields

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [{
  "fieldId": "string",
  "fieldName": "string",
  "fieldDescription": "string",
  "fieldType": "string",
  "createdTs": "2022-09-29T11:33:24.073+00:00",
  "updatedTs": "2022-09-29T11:33:24.073+00:00",
  "createdBy": "string",
  "updatedBy": "string",
  "hidden": true,
  "required": true
}]




drills
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/submissionFields/default
- **Parameter Location:** Request Body
- **Description:** To add/update default submission fields

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "fieldId": "string",
  "fieldName": "string",
  "fieldDescription": "string",
  "fieldType": "string",
  "createdTs": "2022-09-29T11:33:24.073+00:00",
  "updatedTs": "2022-09-29T11:33:24.073+00:00",
  "createdBy": "string",
  "updatedBy": "string",
  "hidden": true,
  "required": true
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "fieldId": "string",
  "fieldName": "string",
  "fieldDescription": "string",
  "fieldType": "string",
  "createdTs": "2022-09-29T11:33:24.073+00:00",
  "updatedTs": "2022-09-29T11:33:24.073+00:00",
  "createdBy": "string",
  "updatedBy": "string",
  "hidden": true,
  "required": true
}




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{drillId}/submissionFields
- **Parameter Location:** Request Body
- **Description:** To get drill submission fields

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




drills
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/{drillId}/submissionFields/configure
- **Parameter Location:** Request Body
- **Description:** To add/update submission fields

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "createdBy": "string",
  "createdTs": "2022-09-29T08:58:13.562Z",
  "drillId": "string",
  "fields": "string",
  "guidelines": "string",
  "updatedBy": "string",
  "updatedTs": "2022-09-29T08:58:13.562Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "createdBy": "string",
  "createdTs": "2022-09-29T08:58:13.562Z",
  "drillId": "string",
  "fields": "string",
  "guidelines": "string",
  "updatedBy": "string",
  "updatedTs": "2022-09-29T08:58:13.562Z"
}




drills
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{drilId}/submissions
- **Parameter Location:** Request Body
- **Description:** To get submissions made under one drillId

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "totalRecordCount": 0,
  "data": []
}




drills
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/{drillId}/submissions
- **Parameter Location:** Request Body
- **Description:** To add or update submissions made under a drilId

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "createdBy": "string",
  "createdTs": "2022-09-29T08:58:13.562Z",
  "drillId": "string",
  "judgeId": "string",
  "otherSubmission": "string",
  "participantId": "string",
  "presentation": "string",
  "projectName": "string",
  "snapshots": "string",
  "sourceCode": "string",
  "submissionDescription": "string",
  "submissionId": "string",
  "teamId": "string",
  "theme": "string",
  "updatedBy": "string",
  "updatedTs": "2022-09-29T08:58:13.563Z",
  "video": "string"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "createdBy": "string",
  "createdTs": "2022-09-29T08:58:13.562Z",
  "drillId": "string",
  "judgeId": "string",
  "otherSubmission": "string",
  "participantId": "string",
  "presentation": "string",
  "projectName": "string",
  "snapshots": "string",
  "sourceCode": "string",
  "submissionDescription": "string",
  "submissionId": "string",
  "teamId": "string",
  "theme": "string",
  "updatedBy": "string",
  "updatedTs": "2022-09-29T08:58:13.563Z",
  "video": "string"
}




drills
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/{drillId}/submissions/{submissionId}/assignments
- **Parameter Location:** Request Body
- **Description:** To add/update assignment of judges

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




jobs
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/allJobs
- **Parameter Location:** Request Body
- **Description:** To search for jobs according to a query

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [
  {
    "createdBy": "string",
    "createdTs": "2022-09-30T04:48:46.151Z",
    "isActive": true,
    "isCompanyNameHidden": true,
    "isSalaryHidden": true,
    "jdLink": "string",
    "jobApplicantCount": 0,
    "jobCtcCurrency": "string",
    "jobDescription": "string",
    "jobDomain": "string",
    "jobEsopAcceptance": true,
    "jobId": "string",
    "jobImageLink": "string",
    "jobIndustryCategory": "string",
    "jobKeywords": "string",
    "jobLocation": "string",
    "jobMaxCtcRange": 0,
    "jobMaxYoe": 0,
    "jobMinCtcRange": 0,
    "jobMinYoe": 0,
    "jobMusthave": "string",
    "jobNoticePeriodAcceptable": "string",
    "jobNumberOfVacancies": 0,
    "jobPostedBy": "string",
    "jobPriority": "string",
    "jobRounds": "string",
    "jobScreeningQuestions": "string",
    "jobSkills": "string",
    "jobTitle": "string",
    "jobType": "string",
    "otherTags": "string",
    "partner": {
      "createdBy": "string",
      "createdTs": "2022-09-30T04:48:46.151Z",
      "partnerDescription": "string",
      "partnerEstablishmentDate": "string",
      "partnerId": "string",
      "partnerIndustry": "string",
      "partnerLogoPath": "string",
      "partnerName": "string",
      "partnerSocialLinks": "string",
      "partnerType": "string",
      "updatedBy": "string",
      "updatedTs": "2022-09-30T04:48:46.151Z"
    },
    "partnerId": "string",
    "partnerName": "string",
    "updatedBy": "string",
    "updatedTs": "2022-09-30T04:48:46.151Z"
  }
]




jobs
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/jobs
- **Parameter Location:** Request Body
- **Description:** To add a job 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    jobDto


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




jobs
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/jobs/headings
- **Parameter Location:** Request Body
- **Description:** To get all headings for jobs

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "jobLocation": [],
  "jobTitle": [],
  "jobType": []
}




jobs
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/jobs/search
- **Parameter Location:** Request Body
- **Description:** To get all jobs which fulfill the query parameters

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "data": [
    {
      "createdBy": "string",
      "createdTs": "2022-09-30T04:48:46.157Z",
      "isActive": true,
      "isCompanyNameHidden": true,
      "isSalaryHidden": true,
      "jdLink": "string",
      "jobApplicantCount": 0,
      "jobCtcCurrency": "string",
      "jobDescription": "string",
      "jobDomain": "string",
      "jobEsopAcceptance": true,
      "jobId": "string",
      "jobImageLink": "string",
      "jobIndustryCategory": "string",
      "jobLocation": "string",
      "jobMaxCtcRange": 0,
      "jobMaxYoe": 0,
      "jobMinCtcRange": 0,
      "jobMinYoe": 0,
      "jobMusthave": "string",
      "jobNoticePeriodAcceptable": "string",
      "jobNumberOfVacancies": 0,
      "jobPostedBy": "string",
      "jobPriority": "string",
      "jobRounds": "string",
      "jobScreeningQuestions": "string",
      "jobSkills": "string",
      "jobTitle": "string",
      "jobType": "string",
      "otherTags": "string",
      "partnerId": "string",
      "partnerName": "string",
      "salaryHidden": true,
      "updatedBy": "string",
      "updatedTs": "2022-09-30T04:48:46.157Z"
    }
  ],
  "totalRecordCount": 0
}




jobs
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/jobs/views/
- **Parameter Location:** Request Body
- **Description:** To create a job view

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "createdBy": "string",
  "createdTs": "2022-09-30T04:48:46.116Z",
  "dayOfWeek": "string",
  "deviceInfo": "string",
  "jobId": "string",
  "jobName": "string",
  "jobViewCount": 0,
  "latitude": "string",
  "location": "string",
  "longitude": "string",
  "monthOfYear": "string",
  "uid": "string",
  "year": 0
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "msg": "Job View successfully saved"
}




jobs
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/jobs/{jobId}
- **Parameter Location:** Request Body
- **Description:** To get a specific job details with jobid

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "createdBy": "string",
  "createdTs": "2022-09-30T04:48:46.165Z",
  "isActive": true,
  "isCompanyNameHidden": true,
  "isSalaryHidden": true,
  "jdLink": "string",
  "jobApplicantCount": 0,
  "jobCtcCurrency": "string",
  "jobDescription": "string",
  "jobDomain": "string",
  "jobEsopAcceptance": true,
  "jobId": "string",
  "jobImageLink": "string",
  "jobIndustryCategory": "string",
  "jobKeywords": "string",
  "jobLocation": "string",
  "jobMaxCtcRange": 0,
  "jobMaxYoe": 0,
  "jobMinCtcRange": 0,
  "jobMinYoe": 0,
  "jobMusthave": "string",
  "jobNoticePeriodAcceptable": "string",
  "jobNumberOfVacancies": 0,
  "jobPostedBy": "string",
  "jobPriority": "string",
  "jobRounds": "string",
  "jobScreeningQuestions": "string",
  "jobSkills": "string",
  "jobTitle": "string",
  "jobType": "string",
  "otherTags": "string",
  "partner": {
    "createdBy": "string",
    "createdTs": "2022-09-30T04:48:46.165Z",
    "partnerDescription": "string",
    "partnerEstablishmentDate": "string",
    "partnerId": "string",
    "partnerIndustry": "string",
    "partnerLogoPath": "string",
    "partnerName": "string",
    "partnerSocialLinks": "string",
    "partnerType": "string",
    "updatedBy": "string",
    "updatedTs": "2022-09-30T04:48:46.165Z"
  },
  "partnerId": "string",
  "partnerName": "string",
  "updatedBy": "string",
  "updatedTs": "2022-09-30T04:48:46.165Z"
}




jobs
-----------------------------------------

- **Method:** PATCH
- **Request URL:** /api/v1/jobs/{jobId}
- **Parameter Location:** Request Body
- **Description:** To update job status

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




jobs
-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/jobs/{jobId}
- **Parameter Location:** Request Body
- **Description:** To edit already posted job

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "createdBy": "string",
  "createdTs": "2022-09-30T04:48:46.116Z",
  "isActive": true,
  "isCompanyNameHidden": true,
  "isSalaryHidden": true,
  "jdLink": "string",
  "jobApplicantCount": 0,
  "jobCtcCurrency": "string",
  "jobDescription": "string",
  "jobDomain": "string",
  "jobEsopAcceptance": true,
  "jobId": "eefe9b05-5d89-4901-aae0-f94f9f3ce10a",
  "jobImageLink": "string",
  "jobIndustryCategory": "string",
  "jobKeywords": "string",
  "jobLocation": "string",
  "jobMaxCtcRange": 0,
  "jobMaxYoe": 0,
  "jobMinCtcRange": 0,
  "jobMinYoe": 0,
  "jobMusthave": "string",
  "jobNoticePeriodAcceptable": "string",
  "jobNumberOfVacancies": 0,
  "jobPostedBy": "string",
  "jobPriority": "string",
  "jobRounds": "string",
  "jobScreeningQuestions": "string",
  "jobSkills": "string",
  "jobTitle": "string",
  "jobType": "string",
  "otherTags": "string",
  "partner": {
    "createdBy": "string",
    "createdTs": "2022-09-30T04:48:46.116Z",
    "partnerDescription": "string",
    "partnerEstablishmentDate": "string",
    "partnerId": "string",
    "partnerIndustry": "string",
    "partnerLogoPath": "string",
    "partnerName": "string",
    "partnerSocialLinks": "string",
    "partnerType": "string",
    "updatedBy": "string",
    "updatedTs": "2022-09-30T04:48:46.116Z"
  },
  "partnerId": "string",
  "partnerName": "string",
  "updatedBy": "string",
  "updatedTs": "2022-09-30T04:48:46.116Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




jobs
-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/jobs/{jobId}/activate/{action}
- **Parameter Location:** Request Body
- **Description:** To activate a job

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    TRUE




jobs
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/jobs/{jobId}/applications
- **Parameter Location:** Request Body
- **Description:** To check if a user has registered for a job

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    TRUE




jobs
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/jobs/{jobId}/views
- **Parameter Location:** Request Body
- **Description:** To get total number of views on a job-tbd

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "data": [],
  "count": 0
}




squad
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/squad
- **Parameter Location:** Request Body
- **Description:** To fetch applications for squad program

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




squad
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/squad
- **Parameter Location:** Request Body
- **Description:** To register for squad program

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "content": "string",
  "createdby": "string",
  "createdts": "2022-09-30T04:48:46.117Z",
  "description": "string",
  "domain": "string",
  "endDate": "2022-09-30T04:48:46.117Z",
  "logoPath": "string",
  "managers": "string",
  "modeOfDelivery": "string",
  "numberOfDays": 0,
  "oneLiner": "string",
  "price": "string",
  "registrationLink": "string",
  "squadId": "string",
  "squadName": "string",
  "startDate": "2022-09-30T04:48:46.117Z",
  "tags": "string",
  "technology": "string",
  "updatedby": "string",
  "updatedts": "2022-09-30T04:48:46.118Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "msg": "Registered successfully. Welcome to Squad."
}




upload
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/uploadFiles
- **Parameter Location:** Request Body
- **Description:** To help users upload files for hackathon submissions

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




contact
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/contactus
- **Parameter Location:** Request Body
- **Description:** To get contact details of user

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    []




contact
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/contactus
- **Parameter Location:** Request Body
- **Description:** To post contact details of users

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "contact": "string",
  "createdby": "string",
  "createdts": "2022-09-30T04:48:46.110Z",
  "email": "string",
  "message": "string",
  "purposeToConnect": "string",
  "queryId": 0,
  "senderFullName": "string",
  "visible": true
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "contact": "string",
  "createdby": "string",
  "createdts": "2022-09-30T04:48:46.110Z",
  "email": "string",
  "message": "string",
  "purposeToConnect": "string",
  "queryId": 0,
  "senderFullName": "string",
  "visible": true
}




contact
-----------------------------------------

- **Method:** DELETE
- **Request URL:** /api/v1/contactus/{action}
- **Parameter Location:** Request Body
- **Description:** To delete contact details of users

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




certificate
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/certificates
- **Parameter Location:** Request Body
- **Description:** To save certificate details

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "certificateUrl": "string",
  "email": "string",
  "eventId": "string",
  "eventType": "string",
  "positionType": "string"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "msg": "Certificate details saved successfully"
}




event
-----------------------------------------

- **Method:** DELETE
- **Request URL:** /api/v1/events
- **Parameter Location:** Request Body
- **Description:** To delete an event

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    [
  {
    "address": "string",
    "agenda": "string",
    "endDateTime": "string",
    "eventCreatedby": "string",
    "eventId": 0,
    "eventUpdatedby": "string",
    "eventUpdatedts": "2022-09-30",
    "location": "string",
    "mode": "string",
    "owner": "string",
    "speaker": "string",
    "startDateTime": "string",
    "status": "string",
    "topic": "string",
    "type": "string"
  }
]


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA




event
-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/events
- **Parameter Location:** Request Body
- **Description:** To get event details 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [
  {
    "address": "string",
    "agenda": "string",
    "endDateTime": "string",
    "eventCreatedby": "string",
    "eventCreatedts": "2022-09-30T11:24:51.746Z",
    "eventId": 0,
    "eventUpdatedby": "string",
    "eventUpdatedts": "2022-09-30T11:24:51.746Z",
    "location": "string",
    "mode": "string",
    "owner": "string",
    "speaker": "string",
    "startDateTime": "string",
    "status": "string",
    "topic": "string",
    "type": "string"
  }
]




event
-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/events
- **Parameter Location:** Request Body
- **Description:** To add/update events

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "address": "string",
  "agenda": "string",
  "endDateTime": "string",
  "eventCreatedby": "string",
  "eventId": 0,
  "eventUpdatedby": "string",
  "eventUpdatedts": "2022-09-30",
  "location": "string",
  "mode": "string",
  "owner": "string",
  "speaker": "string",
  "startDateTime": "string",
  "status": "string",
  "topic": "string",
  "type": "string"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    1




event
-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/events
- **Parameter Location:** Request Body
- **Description:** To update events

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    [
  {
    "address": "string",
    "agenda": "string",
    "endDateTime": "string",
    "eventCreatedby": "string",
    "eventId": 0,
    "eventUpdatedby": "string",
    "eventUpdatedts": "2022-09-30",
    "location": "string",
    "mode": "string",
    "owner": "string",
    "speaker": "string",
    "startDateTime": "string",
    "status": "string",
    "topic": "string",
    "type": "string"
  }
]


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    SUCCESS





-----------------------------------------

- **Method:** 
- **Request URL:** 
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/jobs/application
- **Parameter Location:** Request Body
- **Description:** To fetch application status for a job for a particular uId

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [
  {
    "applicationId": 0,
    "appliedTs": "2022-09-30T11:24:51.803Z",
    "createdby": "string",
    "createdts": "2022-09-30T11:24:51.803Z",
    "currentStatus": "string",
    "jobId": "string",
    "uid": "string",
    "updatedby": "string",
    "updatedts": "2022-09-30T11:24:51.803Z"
  }
]







-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/jobs/application
- **Parameter Location:** Request Body
- **Description:** To apply for a job

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "applicationId": 0,
  "appliedTs": "2022-09-30T11:24:51.492Z",
  "createdBy": "string",
  "createdTs": "2022-09-30T11:24:51.492Z",
  "currentStatus": "string",
  "jobId": "string",
  "uid": "string",
  "updatedBy": "string",
  "updatedTs": "2022-09-30T11:24:51.492Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/jobs/application/filter
- **Parameter Location:** Request Body
- **Description:** To filter applications for a job 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [
  {
    "applicationId": 0,
    "applicationTrackId": 0,
    "feedback": "string",
    "status": "string",
    "updatedby": "string",
    "updatedts": "2022-09-30T11:24:51.810Z"
  }
]





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/jobs/application/stats
- **Parameter Location:** Request Body
- **Description:** To get the number of jobs applied to,applications pending,offers closed and interviews pending for a user

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "applicationPending": 0,
  "offersClosed": 0,
  "jobApplied": 0,
  "interviewsPending": 0
}





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/jobs/application/statusenum
- **Parameter Location:** Request Body
- **Description:** To get the status of all job listings available for a user-tbd

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [
  {
    "order": "1",
    "status": "APPLIED"
  },
  {
    "order": "2",
    "status": "SHORTLISTED"
  },
  {
    "order": "3",
    "status": "APPLICATION SENT"
  }]





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/jobs/application/{applicationId}
- **Parameter Location:** Request Body
- **Description:** To get a specific application for one job

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/jobs/application/{applicationId}
- **Parameter Location:** Request Body
- **Description:** To update application status

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    payload


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/jobs/completeapplication
- **Parameter Location:** Request Body
- **Description:** To get complete applications for a job

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [
  {
    "applicationId": 0,
    "appliedTs": "2022-09-30T11:24:51.823Z",
    "createdBy": "string",
    "createdTs": "2022-09-30T11:24:51.823Z",
    "currentStatus": "string",
    "jobId": "string",
    "jobImg": "string",
    "jobTitle": "string",
    "partnerName": "string",
    "resumeLink": "string",
    "updatedBy": "string",
    "updatedTs": "2022-09-30T11:24:51.823Z",
    "userFullName": "string",
    "userId": "string"
  }
]





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/notification
- **Parameter Location:** Request Body
- **Description:** To add/update a notification

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "createdby": "string",
  "createdts": "2022-09-30T11:24:51.493Z",
  "message": "string",
  "notificationId": 0,
  "notificationType": "string",
  "oneLiner": "string",
  "read": true,
  "receiverUid": "string",
  "senderUid": "string",
  "updatedby": "string",
  "updatedts": "2022-09-30T11:24:51.493Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {"msg":"{msg=Successful request}"}






-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/notification/
- **Parameter Location:** Request Body
- **Description:** To fetch only particular type of notifications

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/notification/{action}
- **Parameter Location:** Request Body
- **Description:** To get list of notifications-tbd

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "createdby": "string",
  "createdts": "2022-09-30T11:24:51.494Z",
  "message": "string",
  "notificationId": 0,
  "notificationType": "string",
  "oneLiner": "string",
  "read": true,
  "receiverUid": "string",
  "senderUid": "string",
  "updatedby": "string",
  "updatedts": "2022-09-30T11:24:51.494Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "msg": "All notifications read successfully"
}





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/notification/{receiverUid}
- **Parameter Location:** Request Body
- **Description:** To get list of notifications for a user/receiver

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "data": [],
  "count": 0
}





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/partners
- **Parameter Location:** Request Body
- **Description:** To get partner details

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [
  {
    "createdBy": "string",
    "createdTs": "2022-10-01T04:39:54.900Z",
    "partnerDescription": "string",
    "partnerEstablishmentDate": "string",
    "partnerId": "string",
    "partnerIndustry": "string",
    "partnerLogoPath": "string",
    "partnerName": "string",
    "partnerSocialLinks": "string",
    "partnerType": "string",
    "updatedBy": "string",
    "updatedTs": "2022-10-01T04:39:54.900Z"
  }
]





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/partners
- **Parameter Location:** Request Body
- **Description:** To save partner details

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "createdBy": "string",
  "createdTs": "2022-10-01T04:39:54.739Z",
  "partnerDescription": "string",
  "partnerEstablishmentDate": "string",
  "partnerId": "string",
  "partnerIndustry": "string",
  "partnerLogoPath": "string",
  "partnerName": "string",
  "partnerSocialLinks": "string",
  "partnerType": "string",
  "updatedBy": "string",
  "updatedTs": "2022-10-01T04:39:54.739Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "partnerId": "a8030704-abab-46f5-845e-b2d40aedc96f",
  "partnerName": "string",
  "partnerDescription": "string",
  "partnerSocialLinks": "string",
  "partnerType": "string",
  "partnerIndustry": "string",
  "partnerEstablishmentDate": "string",
  "partnerLogoPath": "string",
  "createdTs": "2022-10-01T04:39:54.739+00:00",
  "updatedTs": "2022-10-01T04:39:54.739+00:00",
  "createdBy": "string",
  "updatedBy": "string"
}





-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/partners/{partnerId}
- **Parameter Location:** Request Body
- **Description:** To update patners details

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "createdBy": "string",
  "createdTs": "2022-10-01T04:39:54.739Z",
  "partnerDescription": "string",
  "partnerEstablishmentDate": "string",
  "partnerId": "a8030704-abab-46f5-845e-b2d40aedc96f",
  "partnerIndustry": "string",
  "partnerLogoPath": "string",
  "partnerName": "string",
  "partnerSocialLinks": "string",
  "partnerType": "string",
  "updatedBy": "string",
  "updatedTs": "2022-10-01T04:39:54.739Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** 
- **Request URL:** 
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/platformintegration
- **Parameter Location:** Request Body
- **Description:** To check if a user's profile is integrated with other platforms

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [
  {
    "platformIntegrationId": 0,
    "platformName": "string",
    "profileIntegrated": true,
    "profileLink": "string",
    "profileVerified": true,
    "uid": "string",
    "userCreatedby": "string",
    "userCreatedts": "2022-10-01T04:39:54.904Z",
    "userUpdatedby": "string",
    "userUpdatedts": "2022-10-01T04:39:54.904Z"
  }
]





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/platformintegration
- **Parameter Location:** Request Body
- **Description:** To add/update platform integration details

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "platformIntegrationId": 0,
  "platformName": "string",
  "profileIntegrated": true,
  "profileLink": "string",
  "profileVerified": true,
  "uid": "string",
  "userCreatedby": "string",
  "userCreatedts": "2022-10-01T04:39:54.739Z",
  "userUpdatedby": "string",
  "userUpdatedts": "2022-10-01T04:39:54.739Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "platformIntegrationId": 1,
  "platformName": "string",
  "profileLink": "string",
  "profileVerified": true,
  "userCreatedby": "string",
  "userCreatedts": "2022-10-01T07:18:52.252+00:00",
  "userUpdatedby": "string",
  "userUpdatedts": "2022-10-01T07:18:52.252+00:00",
  "profileIntegrated": true,
  "uid": "8af2b4c5-6bb5-4985-b557-abbec4a5a4b7"
}





-----------------------------------------

- **Method:** DELETE
- **Request URL:** /api/v1/skills/
- **Parameter Location:** Request Body
- **Description:** To delete skills

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/skills/
- **Parameter Location:** Request Body
- **Description:** To fetch skills

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [
  "string"
]





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/skills/
- **Parameter Location:** Request Body
- **Description:** To add/update a new skill

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "createdby": "string",
  "createdts": "2022-10-01T04:39:54.740Z",
  "skillId": 0,
  "skillName": "string",
  "skillTags": "string",
  "updatedby": "string",
  "updatedts": "2022-10-01T04:39:54.740Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    Skill saved/updated successfully





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/stats
- **Parameter Location:** Request Body
- **Description:** To get statistics

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [
  {
    "joiningsDone": 0,
    "numberOfColleges": 0,
    "numberOfFresherDrives": 0,
    "numberOfFresherHired": 0,
    "numberOfFreshersUsers": 0,
    "numberOfHackathons": 0,
    "numberOfInternsHired": 0,
    "numberOfJobPosted": 0,
    "numberOfPartners": 0,
    "numberOfProfessionalsUsers": 0,
    "numberOfSquadPrograms": 0,
    "numberOfStudentsInSquad": 0,
    "numberOfUsersOnPlatform": 0,
    "numberOfmeetups": 0,
    "recordInsertedts": "2022-10-01T04:39:54.915Z",
    "statsId": 0,
    "userUpdatedby": "string"
  }
]





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/stats/cumulative
- **Parameter Location:** Request Body
- **Description:** tbd

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "numberOfActiveJobs": "0",
  "numberOfUsers": "1",
  "numberofJobViews": "1",
  "numberOfJobs": "0",
  "numberofSiteViews": "0"
}





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/stats/drills/participants
- **Parameter Location:** Request Body
- **Description:** To get list of participants in hackathons

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "data": [],
  "countOfDrillParticipants": 0,
  "countOfUserNotInDrill": 0
}





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/stats/landingpage
- **Parameter Location:** Request Body
- **Description:** To get platform statistics

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "joiningsDone": 0,
  "numberOfColleges": 0,
  "numberOfFresherDrives": 0,
  "numberOfFresherHired": 0,
  "numberOfFreshersUsers": 0,
  "numberOfHackathons": 0,
  "numberOfInternsHired": 0,
  "numberOfJobPosted": 0,
  "numberOfPartners": 0,
  "numberOfProfessionalsUsers": 0,
  "numberOfSquadPrograms": 0,
  "numberOfStudentsInSquad": 0,
  "numberOfUsersOnPlatform": 0,
  "numberOfmeetups": 0,
  "recordInsertedts": "2022-10-01T04:39:54.917Z",
  "statsId": 0,
  "userUpdatedby": "string"
}





-----------------------------------------

- **Method:** 
- **Request URL:** 
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/stats/landingpage
- **Parameter Location:** Request Body
- **Description:** To save platform statistics

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "joiningsDone": 0,
  "numberOfColleges": 0,
  "numberOfFresherDrives": 0,
  "numberOfFresherHired": 0,
  "numberOfFreshersUsers": 0,
  "numberOfHackathons": 0,
  "numberOfInternsHired": 0,
  "numberOfJobPosted": 0,
  "numberOfPartners": 0,
  "numberOfProfessionalsUsers": 0,
  "numberOfSquadPrograms": 0,
  "numberOfStudentsInSquad": 0,
  "numberOfUsersOnPlatform": 0,
  "numberOfmeetups": 0,
  "recordInsertedts": "2022-10-01T04:39:54.740Z",
  "statsId": 0,
  "userUpdatedby": "string"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    TRUE





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/subscription
- **Parameter Location:** Request Body
- **Description:** To get subscriptions

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [
  {
    "active": true,
    "component": "string",
    "componentId": "string",
    "createdby": "string",
    "createdts": "2022-10-01T04:39:54.920Z",
    "subscriptionEndDt": "2022-10-01T04:39:54.920Z",
    "subscriptionId": "string",
    "subscriptionStartDt": "2022-10-01T04:39:54.920Z",
    "uid": "string",
    "unsubscribtionDt": "2022-10-01T04:39:54.920Z",
    "updatedBy": "string",
    "updatedTs": "2022-10-01T04:39:54.920Z"
  }
]





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/subscription
- **Parameter Location:** Request Body
- **Description:** To add/update subscriptions

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "active": true,
  "component": "string",
  "componentId": "string",
  "createdby": "string",
  "createdts": "2022-10-01T04:39:54.740Z",
  "subscriptionEndDt": "2022-10-01T04:39:54.740Z",
  "subscriptionId": "string",
  "subscriptionStartDt": "2022-10-01T04:39:54.740Z",
  "uid": "string",
  "unsubscribtionDt": "2022-10-01T04:39:54.740Z",
  "updatedBy": "string",
  "updatedTs": "2022-10-01T04:39:54.740Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "active": true,
  "component": "string",
  "componentId": "string",
  "createdby": "string",
  "createdts": "2022-10-01T04:39:54.740Z",
  "subscriptionEndDt": "2022-10-01T04:39:54.740Z",
  "subscriptionId": "string",
  "subscriptionStartDt": "2022-10-01T04:39:54.740Z",
  "uid": "string",
  "unsubscribtionDt": "2022-10-01T04:39:54.740Z",
  "updatedBy": "string",
  "updatedTs": "2022-10-01T04:39:54.740Z"
}





-----------------------------------------

- **Method:** DELETE
- **Request URL:** /api/v1/subscription/{subscriptionId}
- **Parameter Location:** Request Body
- **Description:** To delete subscription

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    Deleted Successfully





-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/subscription/{subscriptionId}/{action}
- **Parameter Location:** Request Body
- **Description:** To update a subscription

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** DELETE
- **Request URL:** /api/v1/testimonial
- **Parameter Location:** Request Body
- **Description:** To delete testimonials

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/testimonial
- **Parameter Location:** Request Body
- **Description:** To get testimonials

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    [
  {
    "postedByUserDesignation": "string",
    "postedByUsername": "string",
    "postedContent": "string",
    "postedDate": "2022-10-01T04:39:54.925Z",
    "recordInsertedts": "2022-10-01T04:39:54.925Z",
    "testimonialPostId": 0,
    "userUpdatedby": "string"
  }
]





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/testimonial
- **Parameter Location:** Request Body
- **Description:** To add/update testimonials

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "postedByUserDesignation": "string",
  "postedByUsername": "string",
  "postedContent": "string",
  "postedDate": "2022-10-01T04:39:54.740Z",
  "recordInsertedts": "2022-10-01T04:39:54.740Z",
  "testimonialPostId": 0,
  "userUpdatedby": "string"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "testimonialPostId": 1,
  "postedDate": "2022-10-01T04:39:54.740+00:00",
  "postedByUsername": "string",
  "postedByUserDesignation": "string",
  "postedContent": "string",
  "userUpdatedby": "string",
  "recordInsertedts": "2022-10-01T12:01:28.843+00:00"
}





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/common/college
- **Parameter Location:** Request Body
- **Description:** To get college details

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "college": [
    "{id=1, college=string, tags=string,m,n,o,p, createdts=2022-09-26 13:47:30.847, updatedts=2022-09-26 13:47:30.847, createdby=string, updatedby=string}",
    "{id=2, college=string, tags=string, createdts=2022-09-28 11:54:30.374, updatedts=2022-09-28 11:54:30.374, createdby=string, updatedby=string}"
  ]
}





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/common/college
- **Parameter Location:** Request Body
- **Description:** To add/update college details

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "college": "string",
  "createdby": "string",
  "createdts": "2022-10-01T04:39:54.731Z",
  "id": 0,
  "tags": "string",
  "updatedby": "string",
  "updatedts": "2022-10-01T04:39:54.731Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "id": 3,
  "college": "string",
  "tags": "string",
  "createdts": "2022-10-01T12:37:08.117+00:00",
  "updatedts": "2022-10-01T12:37:08.117+00:00",
  "createdby": "string",
  "updatedby": "string"
}





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/common/company
- **Parameter Location:** Request Body
- **Description:** To get company details

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "company": [
    "{id=1, company=string, tags=string, createdts=2022-09-26 13:48:10.215, updatedts=2022-09-26 13:48:10.215, createdby=string, updatedby=string,p,q,r}"
  ]
}





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/common/company
- **Parameter Location:** Request Body
- **Description:** To add/update company details

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "company": "string",
  "createdby": "string",
  "createdts": "2022-10-01T04:39:54.731Z",
  "id": 0,
  "tags": "string",
  "updatedby": "string",
  "updatedts": "2022-10-01T04:39:54.731Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "id": 2,
  "company": "string",
  "tags": "string",
  "createdts": "2022-10-01T12:39:44.161+00:00",
  "updatedts": "2022-10-01T12:39:44.161+00:00",
  "createdby": "string",
  "updatedby": "string"
}





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/common/jobdesignation
- **Parameter Location:** Request Body
- **Description:** To get job designation details

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "job designation": [
    "{id=1, jobdesignation=string,b,c,d,e, tags=string, createdts=2022-09-26 13:48:37.304, updatedts=2022-09-26 13:48:37.304, createdby=string, updatedby=string}"
  ]





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/common/jobdesignation
- **Parameter Location:** Request Body
- **Description:** To add/update job designation details

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "createdby": "string",
  "createdts": "2022-10-01T04:39:54.731Z",
  "id": 0,
  "jobdesignation": "string",
  "tags": "string",
  "updatedby": "string",
  "updatedts": "2022-10-01T04:39:54.731Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "id": 2,
  "jobdesignation": "string",
  "tags": "string",
  "createdts": "2022-10-01T12:42:23.055+00:00",
  "updatedts": "2022-10-01T12:42:23.055+00:00",
  "createdby": "string",
  "updatedby": "string"
}





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/common/location
- **Parameter Location:** Request Body
- **Description:** To get location details

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    []





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/common/location
- **Parameter Location:** Request Body
- **Description:** To add/update location details

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "city": "string",
  "countryCode": "string",
  "createdts": "2022-10-01T04:39:54.732Z",
  "id": 0,
  "locality": "string",
  "state": "string",
  "updatedts": "2022-10-01T04:39:54.732Z",
  "zipcode": "string"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "id": 1,
  "countryCode": "string",
  "state": "string",
  "city": "string",
  "locality": "string",
  "zipcode": "string",
  "createdts": "2022-10-01T12:47:22.188+00:00",
  "updatedts": "2022-10-01T12:47:22.188+00:00"
}





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/common/pages
- **Parameter Location:** Request Body
- **Description:** To save page view

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "clientIpaddress": "string",
  "createdTs": "2022-10-03T02:36:19.625Z",
  "dayOfWeek": "string",
  "deviceInfo": "string",
  "latitude": "string",
  "location": "string",
  "longitude": "string",
  "monthOfYear": "string",
  "pageViewCount": 0,
  "page_name": "string",
  "uid": "string",
  "utmCampaign": "string",
  "utmContent": "string",
  "utmId": "string",
  "utmMedium": "string",
  "utmSource": "string",
  "utmTerm": "string",
  "year": 0
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "msg": "Page view saved"
}





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/common/technology
- **Parameter Location:** Request Body
- **Description:** To get technology options

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "technology": [
    "{id=1, technology=xyz,abc, tags=xyz, createdts=2022-09-22 16:54:12.335, updatedts=2022-09-22 16:54:12.335, createdby=string, updatedby=string}"
  ]
}





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/common/technology
- **Parameter Location:** Request Body
- **Description:** To add/update new technology options

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "createdby": "string",
  "createdts": "2022-10-03T02:36:19.625Z",
  "id": 0,
  "tags": "string",
  "technology": "string",
  "updatedby": "string",
  "updatedts": "2022-10-03T02:36:19.625Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "id": 2,
  "technology": "string",
  "tags": "string",
  "createdts": "2022-10-03T02:40:21.687+00:00",
  "updatedts": "2022-10-03T02:40:21.687+00:00",
  "createdby": "string",
  "updatedby": "string"
}





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/common/timezones
- **Parameter Location:** Request Body
- **Description:** To get timezones

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {
  "Africa/Abidjan": "(UTC+00:00)",
  "Africa/Accra": "(UTC+00:00)",
  "Africa/Addis_Ababa": "(UTC+03:00)",
  "Africa/Algiers": "(UTC+01:00)",
  "Africa/Asmara": "(UTC+03:00)",
  "Africa/Asmera": "(UTC+03:00)",
  "Africa/Bamako": "(UTC+00:00)",
  "Africa/Bangui": "(UTC+01:00)",
  "Africa/Banjul": "(UTC+00:00)",
  "Africa/Bissau": "(UTC+00:00)",
  "Africa/Blantyre": "(UTC+02:00)",
  "Africa/Brazzaville": "(UTC+01:00)",
  "Africa/Bujumbura": "(UTC+02:00)",
  "Africa/Cairo": "(UTC+02:00)",
  "Africa/Casablanca": "(UTC+01:00)",
  "Africa/Ceuta": "(UTC+02:00)",
  "Africa/Conakry": "(UTC+00:00)",
  "Africa/Dakar": "(UTC+00:00)",
  "Africa/Dar_es_Salaam": "(UTC+03:00)",
  "Africa/Djibouti": "(UTC+03:00)",
  "Africa/Douala": "(UTC+01:00)",
  "Africa/El_Aaiun": "(UTC+01:00)",
  "Africa/Freetown": "(UTC+00:00)",
  "Africa/Gaborone": "(UTC+02:00)",
  "Africa/Harare": "(UTC+02:00)",
  "Africa/Johannesburg": "(UTC+02:00)",
  "Africa/Juba": "(UTC+02:00)",
  "Africa/Kampala": "(UTC+03:00)",
  "Africa/Khartoum": "(UTC+02:00)",
  "Africa/Kigali": "(UTC+02:00)",
  "Africa/Kinshasa": "(UTC+01:00)",
  "Africa/Lagos": "(UTC+01:00)",
  "Africa/Libreville": "(UTC+01:00)",
  "Africa/Lome": "(UTC+00:00)",
  "Africa/Luanda": "(UTC+01:00)",
  "Africa/Lubumbashi": "(UTC+02:00)",
  "Africa/Lusaka": "(UTC+02:00)",
  "Africa/Malabo": "(UTC+01:00)",
  "Africa/Maputo": "(UTC+02:00)",
  "Africa/Maseru": "(UTC+02:00)",
  "Africa/Mbabane": "(UTC+02:00)",
  "Africa/Mogadishu": "(UTC+03:00)",
  "Africa/Monrovia": "(UTC+00:00)",
  "Africa/Nairobi": "(UTC+03:00)",
  "Africa/Ndjamena": "(UTC+01:00)",
  "Africa/Niamey": "(UTC+01:00)",
  "Africa/Nouakchott": "(UTC+00:00)",
  "Africa/Ouagadougou": "(UTC+00:00)",
  "Africa/Porto-Novo": "(UTC+01:00)",
  "Africa/Sao_Tome": "(UTC+00:00)",
  "Africa/Timbuktu": "(UTC+00:00)",
  "Africa/Tripoli": "(UTC+02:00)",
  "Africa/Tunis": "(UTC+01:00)",
  "Africa/Windhoek": "(UTC+02:00)",
  "America/Adak": "(UTC-09:00)",
  "America/Anchorage": "(UTC-08:00)",
  "America/Anguilla": "(UTC-04:00)",
  "America/Antigua": "(UTC-04:00)",
  "America/Araguaina": "(UTC-03:00)",
  "America/Argentina/Buenos_Aires": "(UTC-03:00)",
  "America/Argentina/Catamarca": "(UTC-03:00)",
  "America/Argentina/ComodRivadavia": "(UTC-03:00)",
  "America/Argentina/Cordoba": "(UTC-03:00)",
  "America/Argentina/Jujuy": "(UTC-03:00)",
  "America/Argentina/La_Rioja": "(UTC-03:00)",
  "America/Argentina/Mendoza": "(UTC-03:00)",
  "America/Argentina/Rio_Gallegos": "(UTC-03:00)",
  "America/Argentina/Salta": "(UTC-03:00)",
  "America/Argentina/San_Juan": "(UTC-03:00)",
  "America/Argentina/San_Luis": "(UTC-03:00)",
  "America/Argentina/Tucuman": "(UTC-03:00)",
  "America/Argentina/Ushuaia": "(UTC-03:00)",
  "America/Aruba": "(UTC-04:00)",
  "America/Asuncion": "(UTC-03:00)",
  "America/Atikokan": "(UTC-05:00)",
  "America/Atka": "(UTC-09:00)",
  "America/Bahia": "(UTC-03:00)",
  "America/Bahia_Banderas": "(UTC-05:00)",
  "America/Barbados": "(UTC-04:00)",
  "America/Belem": "(UTC-03:00)",
  "America/Belize": "(UTC-06:00)",
  "America/Blanc-Sablon": "(UTC-04:00)",
  "America/Boa_Vista": "(UTC-04:00)",
  "America/Bogota": "(UTC-05:00)",
  "America/Boise": "(UTC-06:00)",
  "America/Buenos_Aires": "(UTC-03:00)",
  "America/Cambridge_Bay": "(UTC-06:00)",
  "America/Campo_Grande": "(UTC-04:00)",
  "America/Cancun": "(UTC-05:00)",
  "America/Caracas": "(UTC-04:00)",
  "America/Catamarca": "(UTC-03:00)",
  "America/Cayenne": "(UTC-03:00)",
  "America/Cayman": "(UTC-05:00)",
  "America/Chicago": "(UTC-05:00)",
  "America/Chihuahua": "(UTC-06:00)",
  "America/Coral_Harbour": "(UTC-05:00)",
  "America/Cordoba": "(UTC-03:00)",
  "America/Costa_Rica": "(UTC-06:00)",
  "America/Creston": "(UTC-07:00)",
  "America/Cuiaba": "(UTC-04:00)",
  "America/Curacao": "(UTC-04:00)",
  "America/Danmarkshavn": "(UTC+00:00)",
  "America/Dawson": "(UTC-07:00)",
  "America/Dawson_Creek": "(UTC-07:00)",
  "America/Denver": "(UTC-06:00)",
  "America/Detroit": "(UTC-04:00)",
  "America/Dominica": "(UTC-04:00)",
  "America/Edmonton": "(UTC-06:00)",
  "America/Eirunepe": "(UTC-05:00)",
  "America/El_Salvador": "(UTC-06:00)",
  "America/Ensenada": "(UTC-07:00)",
  "America/Fort_Nelson": "(UTC-07:00)",
  "America/Fort_Wayne": "(UTC-04:00)",
  "America/Fortaleza": "(UTC-03:00)",
  "America/Glace_Bay": "(UTC-03:00)",
  "America/Godthab": "(UTC-02:00)",
  "America/Goose_Bay": "(UTC-03:00)",
  "America/Grand_Turk": "(UTC-04:00)",
  "America/Grenada": "(UTC-04:00)",
  "America/Guadeloupe": "(UTC-04:00)",
  "America/Guatemala": "(UTC-06:00)",
  "America/Guayaquil": "(UTC-05:00)",
  "America/Guyana": "(UTC-04:00)",
  "America/Halifax": "(UTC-03:00)",
  "America/Havana": "(UTC-04:00)",
  "America/Hermosillo": "(UTC-07:00)",
  "America/Indiana/Indianapolis": "(UTC-04:00)",
  "America/Indiana/Knox": "(UTC-05:00)",
  "America/Indiana/Marengo": "(UTC-04:00)",
  "America/Indiana/Petersburg": "(UTC-04:00)",
  "America/Indiana/Tell_City": "(UTC-05:00)",
  "America/Indiana/Vevay": "(UTC-04:00)",
  "America/Indiana/Vincennes": "(UTC-04:00)",
  "America/Indiana/Winamac": "(UTC-04:00)",
  "America/Indianapolis": "(UTC-04:00)",
  "America/Inuvik": "(UTC-06:00)",
  "America/Iqaluit": "(UTC-04:00)",
  "America/Jamaica": "(UTC-05:00)",
  "America/Jujuy": "(UTC-03:00)",
  "America/Juneau": "(UTC-08:00)",
  "America/Kentucky/Louisville": "(UTC-04:00)",
  "America/Kentucky/Monticello": "(UTC-04:00)",
  "America/Knox_IN": "(UTC-05:00)",
  "America/Kralendijk": "(UTC-04:00)",
  "America/La_Paz": "(UTC-04:00)",
  "America/Lima": "(UTC-05:00)",
  "America/Los_Angeles": "(UTC-07:00)",
  "America/Louisville": "(UTC-04:00)",
  "America/Lower_Princes": "(UTC-04:00)",
  "America/Maceio": "(UTC-03:00)",
  "America/Managua": "(UTC-06:00)",
  "America/Manaus": "(UTC-04:00)",
  "America/Marigot": "(UTC-04:00)",
  "America/Martinique": "(UTC-04:00)",
  "America/Matamoros": "(UTC-05:00)",
  "America/Mazatlan": "(UTC-06:00)",
  "America/Mendoza": "(UTC-03:00)",
  "America/Menominee": "(UTC-05:00)",
  "America/Merida": "(UTC-05:00)",
  "America/Metlakatla": "(UTC-08:00)",
  "America/Mexico_City": "(UTC-05:00)",
  "America/Miquelon": "(UTC-02:00)",
  "America/Moncton": "(UTC-03:00)",
  "America/Monterrey": "(UTC-05:00)",
  "America/Montevideo": "(UTC-03:00)",
  "America/Montreal": "(UTC-04:00)",
  "America/Montserrat": "(UTC-04:00)",
  "America/Nassau": "(UTC-04:00)",
  "America/New_York": "(UTC-04:00)",
  "America/Nipigon": "(UTC-04:00)",
  "America/Nome": "(UTC-08:00)",
  "America/Noronha": "(UTC-02:00)",
  "America/North_Dakota/Beulah": "(UTC-05:00)",
  "America/North_Dakota/Center": "(UTC-05:00)",
  "America/North_Dakota/New_Salem": "(UTC-05:00)",
  "America/Nuuk": "(UTC-02:00)",
  "America/Ojinaga": "(UTC-06:00)",
  "America/Panama": "(UTC-05:00)",
  "America/Pangnirtung": "(UTC-04:00)",
  "America/Paramaribo": "(UTC-03:00)",
  "America/Phoenix": "(UTC-07:00)",
  "America/Port-au-Prince": "(UTC-04:00)",
  "America/Port_of_Spain": "(UTC-04:00)",
  "America/Porto_Acre": "(UTC-05:00)",
  "America/Porto_Velho": "(UTC-04:00)",
  "America/Puerto_Rico": "(UTC-04:00)",
  "America/Punta_Arenas": "(UTC-03:00)",
  "America/Rainy_River": "(UTC-05:00)",
  "America/Rankin_Inlet": "(UTC-05:00)",
  "America/Recife": "(UTC-03:00)",
  "America/Regina": "(UTC-06:00)",
  "America/Resolute": "(UTC-05:00)",
  "America/Rio_Branco": "(UTC-05:00)",
  "America/Rosario": "(UTC-03:00)",
  "America/Santa_Isabel": "(UTC-07:00)",
  "America/Santarem": "(UTC-03:00)",
  "America/Santiago": "(UTC-03:00)",
  "America/Santo_Domingo": "(UTC-04:00)",
  "America/Sao_Paulo": "(UTC-03:00)",
  "America/Scoresbysund": "(UTC+00:00)",
  "America/Shiprock": "(UTC-06:00)",
  "America/Sitka": "(UTC-08:00)",
  "America/St_Barthelemy": "(UTC-04:00)",
  "America/St_Johns": "(UTC-02:30)",
  "America/St_Kitts": "(UTC-04:00)",
  "America/St_Lucia": "(UTC-04:00)",
  "America/St_Thomas": "(UTC-04:00)",
  "America/St_Vincent": "(UTC-04:00)",
  "America/Swift_Current": "(UTC-06:00)",
  "America/Tegucigalpa": "(UTC-06:00)",
  "America/Thule": "(UTC-03:00)",
  "America/Thunder_Bay": "(UTC-04:00)",
  "America/Tijuana": "(UTC-07:00)",
  "America/Toronto": "(UTC-04:00)",
  "America/Tortola": "(UTC-04:00)",
  "America/Vancouver": "(UTC-07:00)",
  "America/Virgin": "(UTC-04:00)",
  "America/Whitehorse": "(UTC-07:00)",
  "America/Winnipeg": "(UTC-05:00)",
  "America/Yakutat": "(UTC-08:00)",
  "America/Yellowknife": "(UTC-06:00)",
  "Antarctica/Casey": "(UTC+11:00)",
  "Antarctica/Davis": "(UTC+07:00)",
  "Antarctica/DumontDUrville": "(UTC+10:00)",
  "Antarctica/Macquarie": "(UTC+11:00)",
  "Antarctica/Mawson": "(UTC+05:00)",
  "Antarctica/McMurdo": "(UTC+13:00)",
  "Antarctica/Palmer": "(UTC-03:00)",
  "Antarctica/Rothera": "(UTC-03:00)",
  "Antarctica/South_Pole": "(UTC+13:00)",
  "Antarctica/Syowa": "(UTC+03:00)",
  "Antarctica/Troll": "(UTC+02:00)",
  "Antarctica/Vostok": "(UTC+06:00)",
  "Arctic/Longyearbyen": "(UTC+02:00)",
  "Asia/Aden": "(UTC+03:00)",
  "Asia/Almaty": "(UTC+06:00)",
  "Asia/Amman": "(UTC+03:00)",
  "Asia/Anadyr": "(UTC+12:00)",
  "Asia/Aqtau": "(UTC+05:00)",
  "Asia/Aqtobe": "(UTC+05:00)",
  "Asia/Ashgabat": "(UTC+05:00)",
  "Asia/Ashkhabad": "(UTC+05:00)",
  "Asia/Atyrau": "(UTC+05:00)",
  "Asia/Baghdad": "(UTC+03:00)",
  "Asia/Bahrain": "(UTC+03:00)",
  "Asia/Baku": "(UTC+04:00)",
  "Asia/Bangkok": "(UTC+07:00)",
  "Asia/Barnaul": "(UTC+07:00)",
  "Asia/Beirut": "(UTC+03:00)",
  "Asia/Bishkek": "(UTC+06:00)",
  "Asia/Brunei": "(UTC+08:00)",
  "Asia/Calcutta": "(UTC+05:30)",
  "Asia/Chita": "(UTC+09:00)",
  "Asia/Choibalsan": "(UTC+08:00)",
  "Asia/Chongqing": "(UTC+08:00)",
  "Asia/Chungking": "(UTC+08:00)",
  "Asia/Colombo": "(UTC+05:30)",
  "Asia/Dacca": "(UTC+06:00)",
  "Asia/Damascus": "(UTC+03:00)",
  "Asia/Dhaka": "(UTC+06:00)",
  "Asia/Dili": "(UTC+09:00)",
  "Asia/Dubai": "(UTC+04:00)",
  "Asia/Dushanbe": "(UTC+05:00)",
  "Asia/Famagusta": "(UTC+03:00)",
  "Asia/Gaza": "(UTC+03:00)",
  "Asia/Harbin": "(UTC+08:00)",
  "Asia/Hebron": "(UTC+03:00)",
  "Asia/Ho_Chi_Minh": "(UTC+07:00)",
  "Asia/Hong_Kong": "(UTC+08:00)",
  "Asia/Hovd": "(UTC+07:00)",
  "Asia/Irkutsk": "(UTC+08:00)",
  "Asia/Istanbul": "(UTC+03:00)",
  "Asia/Jakarta": "(UTC+07:00)",
  "Asia/Jayapura": "(UTC+09:00)",
  "Asia/Jerusalem": "(UTC+03:00)",
  "Asia/Kabul": "(UTC+04:30)",
  "Asia/Kamchatka": "(UTC+12:00)",
  "Asia/Karachi": "(UTC+05:00)",
  "Asia/Kashgar": "(UTC+06:00)",
  "Asia/Kathmandu": "(UTC+05:45)",
  "Asia/Katmandu": "(UTC+05:45)",
  "Asia/Khandyga": "(UTC+09:00)",
  "Asia/Kolkata": "(UTC+05:30)",
  "Asia/Krasnoyarsk": "(UTC+07:00)",
  "Asia/Kuala_Lumpur": "(UTC+08:00)",
  "Asia/Kuching": "(UTC+08:00)",
  "Asia/Kuwait": "(UTC+03:00)",
  "Asia/Macao": "(UTC+08:00)",
  "Asia/Macau": "(UTC+08:00)",
  "Asia/Magadan": "(UTC+11:00)",
  "Asia/Makassar": "(UTC+08:00)",
  "Asia/Manila": "(UTC+08:00)",
  "Asia/Muscat": "(UTC+04:00)",
  "Asia/Nicosia": "(UTC+03:00)",
  "Asia/Novokuznetsk": "(UTC+07:00)",
  "Asia/Novosibirsk": "(UTC+07:00)",
  "Asia/Omsk": "(UTC+06:00)",
  "Asia/Oral": "(UTC+05:00)",
  "Asia/Phnom_Penh": "(UTC+07:00)",
  "Asia/Pontianak": "(UTC+07:00)",
  "Asia/Pyongyang": "(UTC+09:00)",
  "Asia/Qatar": "(UTC+03:00)",
  "Asia/Qostanay": "(UTC+06:00)",
  "Asia/Qyzylorda": "(UTC+05:00)",
  "Asia/Rangoon": "(UTC+06:30)",
  "Asia/Riyadh": "(UTC+03:00)",
  "Asia/Saigon": "(UTC+07:00)",
  "Asia/Sakhalin": "(UTC+11:00)",
  "Asia/Samarkand": "(UTC+05:00)",
  "Asia/Seoul": "(UTC+09:00)",
  "Asia/Shanghai": "(UTC+08:00)",
  "Asia/Singapore": "(UTC+08:00)",
  "Asia/Srednekolymsk": "(UTC+11:00)",
  "Asia/Taipei": "(UTC+08:00)",
  "Asia/Tashkent": "(UTC+05:00)",
  "Asia/Tbilisi": "(UTC+04:00)",
  "Asia/Tehran": "(UTC+03:30)",
  "Asia/Tel_Aviv": "(UTC+03:00)",
  "Asia/Thimbu": "(UTC+06:00)",
  "Asia/Thimphu": "(UTC+06:00)",
  "Asia/Tokyo": "(UTC+09:00)",
  "Asia/Tomsk": "(UTC+07:00)",
  "Asia/Ujung_Pandang": "(UTC+08:00)",
  "Asia/Ulaanbaatar": "(UTC+08:00)",
  "Asia/Ulan_Bator": "(UTC+08:00)",
  "Asia/Urumqi": "(UTC+06:00)",
  "Asia/Ust-Nera": "(UTC+10:00)",
  "Asia/Vientiane": "(UTC+07:00)",
  "Asia/Vladivostok": "(UTC+10:00)",
  "Asia/Yakutsk": "(UTC+09:00)",
  "Asia/Yangon": "(UTC+06:30)",
  "Asia/Yekaterinburg": "(UTC+05:00)",
  "Asia/Yerevan": "(UTC+04:00)",
  "Atlantic/Azores": "(UTC+00:00)",
  "Atlantic/Bermuda": "(UTC-03:00)",
  "Atlantic/Canary": "(UTC+01:00)",
  "Atlantic/Cape_Verde": "(UTC-01:00)",
  "Atlantic/Faeroe": "(UTC+01:00)",
  "Atlantic/Faroe": "(UTC+01:00)",
  "Atlantic/Jan_Mayen": "(UTC+02:00)",
  "Atlantic/Madeira": "(UTC+01:00)",
  "Atlantic/Reykjavik": "(UTC+00:00)",
  "Atlantic/South_Georgia": "(UTC-02:00)",
  "Atlantic/St_Helena": "(UTC+00:00)",
  "Atlantic/Stanley": "(UTC-03:00)",
  "Australia/ACT": "(UTC+11:00)",
  "Australia/Adelaide": "(UTC+10:30)",
  "Australia/Brisbane": "(UTC+10:00)",
  "Australia/Broken_Hill": "(UTC+10:30)",
  "Australia/Canberra": "(UTC+11:00)",
  "Australia/Currie": "(UTC+11:00)",
  "Australia/Darwin": "(UTC+09:30)",
  "Australia/Eucla": "(UTC+08:45)",
  "Australia/Hobart": "(UTC+11:00)",
  "Australia/LHI": "(UTC+11:00)",
  "Australia/Lindeman": "(UTC+10:00)",
  "Australia/Lord_Howe": "(UTC+11:00)",
  "Australia/Melbourne": "(UTC+11:00)",
  "Australia/NSW": "(UTC+11:00)",
  "Australia/North": "(UTC+09:30)",
  "Australia/Perth": "(UTC+08:00)",
  "Australia/Queensland": "(UTC+10:00)",
  "Australia/South": "(UTC+10:30)",
  "Australia/Sydney": "(UTC+11:00)",
  "Australia/Tasmania": "(UTC+11:00)",
  "Australia/Victoria": "(UTC+11:00)",
  "Australia/West": "(UTC+08:00)",
  "Australia/Yancowinna": "(UTC+10:30)",
  "Brazil/Acre": "(UTC-05:00)",
  "Brazil/DeNoronha": "(UTC-02:00)",
  "Brazil/East": "(UTC-03:00)",
  "Brazil/West": "(UTC-04:00)",
  "CET": "(UTC+02:00)",
  "CST6CDT": "(UTC-05:00)",
  "Canada/Atlantic": "(UTC-03:00)",
  "Canada/Central": "(UTC-05:00)",
  "Canada/Eastern": "(UTC-04:00)",
  "Canada/Mountain": "(UTC-06:00)",
  "Canada/Newfoundland": "(UTC-02:30)",
  "Canada/Pacific": "(UTC-07:00)",
  "Canada/Saskatchewan": "(UTC-06:00)",
  "Canada/Yukon": "(UTC-07:00)",
  "Chile/Continental": "(UTC-03:00)",
  "Chile/EasterIsland": "(UTC-05:00)",
  "Cuba": "(UTC-04:00)",
  "EET": "(UTC+03:00)",
  "EST5EDT": "(UTC-04:00)",
  "Egypt": "(UTC+02:00)",
  "Eire": "(UTC+01:00)",
  "Etc/GMT": "(UTC+00:00)",
  "Etc/GMT+0": "(UTC+00:00)",
  "Etc/GMT+1": "(UTC-01:00)",
  "Etc/GMT+10": "(UTC-10:00)",
  "Etc/GMT+11": "(UTC-11:00)",
  "Etc/GMT+12": "(UTC-12:00)",
  "Etc/GMT+2": "(UTC-02:00)",
  "Etc/GMT+3": "(UTC-03:00)",
  "Etc/GMT+4": "(UTC-04:00)",
  "Etc/GMT+5": "(UTC-05:00)",
  "Etc/GMT+6": "(UTC-06:00)",
  "Etc/GMT+7": "(UTC-07:00)",
  "Etc/GMT+8": "(UTC-08:00)",
  "Etc/GMT+9": "(UTC-09:00)",
  "Etc/GMT-0": "(UTC+00:00)",
  "Etc/GMT-1": "(UTC+01:00)",
  "Etc/GMT-10": "(UTC+10:00)",
  "Etc/GMT-11": "(UTC+11:00)",
  "Etc/GMT-12": "(UTC+12:00)",
  "Etc/GMT-13": "(UTC+13:00)",
  "Etc/GMT-14": "(UTC+14:00)",
  "Etc/GMT-2": "(UTC+02:00)",
  "Etc/GMT-3": "(UTC+03:00)",
  "Etc/GMT-4": "(UTC+04:00)",
  "Etc/GMT-5": "(UTC+05:00)",
  "Etc/GMT-6": "(UTC+06:00)",
  "Etc/GMT-7": "(UTC+07:00)",
  "Etc/GMT-8": "(UTC+08:00)",
  "Etc/GMT-9": "(UTC+09:00)",
  "Etc/GMT0": "(UTC+00:00)",
  "Etc/Greenwich": "(UTC+00:00)",
  "Etc/UCT": "(UTC+00:00)",
  "Etc/UTC": "(UTC+00:00)",
  "Etc/Universal": "(UTC+00:00)",
  "Etc/Zulu": "(UTC+00:00)",
  "Europe/Amsterdam": "(UTC+02:00)",
  "Europe/Andorra": "(UTC+02:00)",
  "Europe/Astrakhan": "(UTC+04:00)",
  "Europe/Athens": "(UTC+03:00)",
  "Europe/Belfast": "(UTC+01:00)",
  "Europe/Belgrade": "(UTC+02:00)",
  "Europe/Berlin": "(UTC+02:00)",
  "Europe/Bratislava": "(UTC+02:00)",
  "Europe/Brussels": "(UTC+02:00)",
  "Europe/Bucharest": "(UTC+03:00)",
  "Europe/Budapest": "(UTC+02:00)",
  "Europe/Busingen": "(UTC+02:00)",
  "Europe/Chisinau": "(UTC+03:00)",
  "Europe/Copenhagen": "(UTC+02:00)",
  "Europe/Dublin": "(UTC+01:00)",
  "Europe/Gibraltar": "(UTC+02:00)",
  "Europe/Guernsey": "(UTC+01:00)",
  "Europe/Helsinki": "(UTC+03:00)",
  "Europe/Isle_of_Man": "(UTC+01:00)",
  "Europe/Istanbul": "(UTC+03:00)",
  "Europe/Jersey": "(UTC+01:00)",
  "Europe/Kaliningrad": "(UTC+02:00)",
  "Europe/Kiev": "(UTC+03:00)",
  "Europe/Kirov": "(UTC+03:00)",
  "Europe/Lisbon": "(UTC+01:00)",
  "Europe/Ljubljana": "(UTC+02:00)",
  "Europe/London": "(UTC+01:00)",
  "Europe/Luxembourg": "(UTC+02:00)",
  "Europe/Madrid": "(UTC+02:00)",
  "Europe/Malta": "(UTC+02:00)",
  "Europe/Mariehamn": "(UTC+03:00)",
  "Europe/Minsk": "(UTC+03:00)",
  "Europe/Monaco": "(UTC+02:00)",
  "Europe/Moscow": "(UTC+03:00)",
  "Europe/Nicosia": "(UTC+03:00)",
  "Europe/Oslo": "(UTC+02:00)",
  "Europe/Paris": "(UTC+02:00)",
  "Europe/Podgorica": "(UTC+02:00)",
  "Europe/Prague": "(UTC+02:00)",
  "Europe/Riga": "(UTC+03:00)",
  "Europe/Rome": "(UTC+02:00)",
  "Europe/Samara": "(UTC+04:00)",
  "Europe/San_Marino": "(UTC+02:00)",
  "Europe/Sarajevo": "(UTC+02:00)",
  "Europe/Saratov": "(UTC+04:00)",
  "Europe/Simferopol": "(UTC+03:00)",
  "Europe/Skopje": "(UTC+02:00)",
  "Europe/Sofia": "(UTC+03:00)",
  "Europe/Stockholm": "(UTC+02:00)",
  "Europe/Tallinn": "(UTC+03:00)",
  "Europe/Tirane": "(UTC+02:00)",
  "Europe/Tiraspol": "(UTC+03:00)",
  "Europe/Ulyanovsk": "(UTC+04:00)",
  "Europe/Uzhgorod": "(UTC+03:00)",
  "Europe/Vaduz": "(UTC+02:00)",
  "Europe/Vatican": "(UTC+02:00)",
  "Europe/Vienna": "(UTC+02:00)",
  "Europe/Vilnius": "(UTC+03:00)",
  "Europe/Volgograd": "(UTC+03:00)",
  "Europe/Warsaw": "(UTC+02:00)",
  "Europe/Zagreb": "(UTC+02:00)",
  "Europe/Zaporozhye": "(UTC+03:00)",
  "Europe/Zurich": "(UTC+02:00)",
  "GB": "(UTC+01:00)",
  "GB-Eire": "(UTC+01:00)",
  "GMT": "(UTC+00:00)",
  "GMT0": "(UTC+00:00)",
  "Greenwich": "(UTC+00:00)",
  "Hongkong": "(UTC+08:00)",
  "Iceland": "(UTC+00:00)",
  "Indian/Antananarivo": "(UTC+03:00)",
  "Indian/Chagos": "(UTC+06:00)",
  "Indian/Christmas": "(UTC+07:00)",
  "Indian/Cocos": "(UTC+06:30)",
  "Indian/Comoro": "(UTC+03:00)",
  "Indian/Kerguelen": "(UTC+05:00)",
  "Indian/Mahe": "(UTC+04:00)",
  "Indian/Maldives": "(UTC+05:00)",
  "Indian/Mauritius": "(UTC+04:00)",
  "Indian/Mayotte": "(UTC+03:00)",
  "Indian/Reunion": "(UTC+04:00)",
  "Iran": "(UTC+03:30)",
  "Israel": "(UTC+03:00)",
  "Jamaica": "(UTC-05:00)",
  "Japan": "(UTC+09:00)",
  "Kwajalein": "(UTC+12:00)",
  "Libya": "(UTC+02:00)",
  "MET": "(UTC+02:00)",
  "MST7MDT": "(UTC-06:00)",
  "Mexico/BajaNorte": "(UTC-07:00)",
  "Mexico/BajaSur": "(UTC-06:00)",
  "Mexico/General": "(UTC-05:00)",
  "NZ": "(UTC+13:00)",
  "NZ-CHAT": "(UTC+13:45)",
  "Navajo": "(UTC-06:00)",
  "PRC": "(UTC+08:00)",
  "PST8PDT": "(UTC-07:00)",
  "Pacific/Apia": "(UTC+13:00)",
  "Pacific/Auckland": "(UTC+13:00)",
  "Pacific/Bougainville": "(UTC+11:00)",
  "Pacific/Chatham": "(UTC+13:45)",
  "Pacific/Chuuk": "(UTC+10:00)",
  "Pacific/Easter": "(UTC-05:00)",
  "Pacific/Efate": "(UTC+11:00)",
  "Pacific/Enderbury": "(UTC+13:00)",
  "Pacific/Fakaofo": "(UTC+13:00)",
  "Pacific/Fiji": "(UTC+12:00)",
  "Pacific/Funafuti": "(UTC+12:00)",
  "Pacific/Galapagos": "(UTC-06:00)",
  "Pacific/Gambier": "(UTC-09:00)",
  "Pacific/Guadalcanal": "(UTC+11:00)",
  "Pacific/Guam": "(UTC+10:00)",
  "Pacific/Honolulu": "(UTC-10:00)",
  "Pacific/Johnston": "(UTC-10:00)",
  "Pacific/Kanton": "(UTC+13:00)",
  "Pacific/Kiritimati": "(UTC+14:00)",
  "Pacific/Kosrae": "(UTC+11:00)",
  "Pacific/Kwajalein": "(UTC+12:00)",
  "Pacific/Majuro": "(UTC+12:00)",
  "Pacific/Marquesas": "(UTC-09:30)",
  "Pacific/Midway": "(UTC-11:00)",
  "Pacific/Nauru": "(UTC+12:00)",
  "Pacific/Niue": "(UTC-11:00)",
  "Pacific/Norfolk": "(UTC+12:00)",
  "Pacific/Noumea": "(UTC+11:00)",
  "Pacific/Pago_Pago": "(UTC-11:00)",
  "Pacific/Palau": "(UTC+09:00)",
  "Pacific/Pitcairn": "(UTC-08:00)",
  "Pacific/Pohnpei": "(UTC+11:00)",
  "Pacific/Ponape": "(UTC+11:00)",
  "Pacific/Port_Moresby": "(UTC+10:00)",
  "Pacific/Rarotonga": "(UTC-10:00)",
  "Pacific/Saipan": "(UTC+10:00)",
  "Pacific/Samoa": "(UTC-11:00)",
  "Pacific/Tahiti": "(UTC-10:00)",
  "Pacific/Tarawa": "(UTC+12:00)",
  "Pacific/Tongatapu": "(UTC+13:00)",
  "Pacific/Truk": "(UTC+10:00)",
  "Pacific/Wake": "(UTC+12:00)",
  "Pacific/Wallis": "(UTC+12:00)",
  "Pacific/Yap": "(UTC+10:00)",
  "Poland": "(UTC+02:00)",
  "Portugal": "(UTC+01:00)",
  "ROK": "(UTC+09:00)",
  "Singapore": "(UTC+08:00)",
  "SystemV/AST4": "(UTC-04:00)",
  "SystemV/AST4ADT": "(UTC-03:00)",
  "SystemV/CST6": "(UTC-06:00)",
  "SystemV/CST6CDT": "(UTC-05:00)",
  "SystemV/EST5": "(UTC-05:00)",
  "SystemV/EST5EDT": "(UTC-04:00)",
  "SystemV/HST10": "(UTC-10:00)",
  "SystemV/MST7": "(UTC-07:00)",
  "SystemV/MST7MDT": "(UTC-06:00)",
  "SystemV/PST8": "(UTC-08:00)",
  "SystemV/PST8PDT": "(UTC-07:00)",
  "SystemV/YST9": "(UTC-09:00)",
  "SystemV/YST9YDT": "(UTC-08:00)",
  "Turkey": "(UTC+03:00)",
  "UCT": "(UTC+00:00)",
  "US/Alaska": "(UTC-08:00)",
  "US/Aleutian": "(UTC-09:00)",
  "US/Arizona": "(UTC-07:00)",
  "US/Central": "(UTC-05:00)",
  "US/East-Indiana": "(UTC-04:00)",
  "US/Eastern": "(UTC-04:00)",
  "US/Hawaii": "(UTC-10:00)",
  "US/Indiana-Starke": "(UTC-05:00)",
  "US/Michigan": "(UTC-04:00)",
  "US/Mountain": "(UTC-06:00)",
  "US/Pacific": "(UTC-07:00)",
  "US/Samoa": "(UTC-11:00)",
  "UTC": "(UTC+00:00)",
  "Universal": "(UTC+00:00)",
  "W-SU": "(UTC+03:00)",
  "WET": "(UTC+01:00)",
  "Zulu": "(UTC+00:00)"
}





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/common/{title}
- **Parameter Location:** Request Body
- **Description:** To get teams page

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/users/profile/common/{section}
- **Parameter Location:** Request Body
- **Description:** To fetch common fields in a section

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/users/profile/completion/{uId}
- **Parameter Location:** Request Body
- **Description:** To get the completion percentage of a user profile

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    0





-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/users/profile/education
- **Parameter Location:** Request Body
- **Description:** To add education details for a user's profile

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "boardName": "string",
  "cgpaPercentage": 0,
  "courseType": "string",
  "createdby": "string",
  "createdts": "2022-10-03T02:36:19.640Z",
  "degree": "string",
  "eduInfoCount": 0,
  "gradingSystem": "string",
  "instituteName": "string",
  "passingOutYear": 0,
  "pursuing": true,
  "qualification": "string",
  "schoolMedium": "string",
  "schoolName": "string",
  "specialization": "string",
  "uid": "string",
  "universityName": "string",
  "updatedby": "string",
  "updatedts": "2022-10-03T02:36:19.640Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {"msg":"Education Details Saved"}





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/users/profile/other/{section}
- **Parameter Location:** Request Body
- **Description:** To fetch user details in a given section

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/users/profile/other/{section}
- **Parameter Location:** Request Body
- **Description:** To add details to profile in a section

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "certification": "string",
  "createdby": "string",
  "createdts": "2022-10-03T02:36:19.640Z",
  "extraCurricular": "string",
  "otherDetailsCount": 0,
  "patent": "string",
  "uid": "string",
  "updatedby": "string",
  "updatedts": "2022-10-03T02:36:19.640Z",
  "whitePaper": "string",
  "workToHighlight": "string"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {"msg":"User Other details Saved"}





-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/users/profile/personal
- **Parameter Location:** Request Body
- **Description:** To add personal details in profile

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "coverLetter": "string",
  "currentAddress": "string",
  "currentCity": "string",
  "currentState": "string",
  "dateOfBirth": "2022-10-03T02:36:19.640Z",
  "gender": "string",
  "govtIdLink": "string",
  "languagesKnown": "string",
  "lastWorkingDay": "2022-10-03T02:36:19.640Z",
  "maritalStatus": "string",
  "otherDetails": "string",
  "personalDetailsCount": 0,
  "profileCompletion": 0,
  "profileCreatedby": "string",
  "profileCreatedts": "2022-10-03T02:36:19.640Z",
  "profilePicLink": "string",
  "profileUpdatedby": "string",
  "profileUpdatedts": "2022-10-03T02:36:19.640Z",
  "resumeLink": "string",
  "servingNoticePeriod": true,
  "socialLinks": "string",
  "uid": "string",
  "zipcode": "string"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {"msg":"Personal Details Saved"}





-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/users/profile/project
- **Parameter Location:** Request Body
- **Description:** To add project details to profile

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "client": "string",
  "createdby": "string",
  "createdts": "2022-10-03T02:36:19.641Z",
  "currentlyWorking": true,
  "designation": "string",
  "endDate": "2022-10-03T02:36:19.641Z",
  "orgOrClgId": 0,
  "projectCount": 0,
  "projectDescription": "string",
  "projectLink": "string",
  "projectSite": "string",
  "projectTitle": "string",
  "roleinProject": "string",
  "skillsUsed": "string",
  "startDate": "2022-10-03T02:36:19.641Z",
  "teamSize": "string",
  "uid": "string",
  "updatedby": "string",
  "updatedts": "2022-10-03T02:36:19.641Z"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {"msg":"Project Details Saved"}





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/users/profile/resume
- **Parameter Location:** Request Body
- **Description:** To find if resume is uploaded by user

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    TRUE





-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/users/profile/skill
- **Parameter Location:** Request Body
- **Description:** To add skills to profile

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "active": true,
  "createdby": "string",
  "createdts": "2022-10-03T02:36:19.641Z",
  "relevantExperience": 0,
  "skillLastUsed": "2022-10-03T02:36:19.641Z",
  "skillLevelName": "string",
  "skillName": "string",
  "uid": "string",
  "updatedby": "string",
  "updatedts": "2022-10-03T02:36:19.641Z",
  "userSkillId": 0
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {"msg":"User Skills Saved"}





-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/users/profile/work
- **Parameter Location:** Request Body
- **Description:** To add work profile

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
      "createdby": "string",
  "createdts": "2022-10-03T02:36:19.641Z",
  "currentSalary": "string",
  "currentlyWorking": true,
  "endDate": "2022-10-03T02:36:19.641Z",
  "expCount": 0,
  "jobDesignation": "string",
  "jobType": "string",
  "lastWorkingDay": "2022-10-03T02:36:19.641Z",
  "noticePeriod": "string",
  "organisationName": "string",
  "startDate": "2022-10-03T02:36:19.641Z",
  "uid": "string",
  "updatedby": "string",
  "updatedts": "2022-10-03T02:36:19.641Z",
  "workDescription": "string",
  "workLocation": "string",
  "workSkillsToHighlight": "string"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {"msg":"Work Profile Saved"}





-----------------------------------------

- **Method:** DELETE
- **Request URL:** /api/v1/users/profile/{section}
- **Parameter Location:** Request Body
- **Description:** To delete a section in a user's profile

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/users/profile/{section}
- **Parameter Location:** Request Body
- **Description:** To fetch a section in a user's profile

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/users/profile/{section}
- **Parameter Location:** Request Body
- **Description:** To add details to profile in a section

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    requestPayload


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    {"msg":"Work Profile Saved"}





-----------------------------------------

- **Method:** PUT
- **Request URL:** /api/v1/users/profile/{uId}/upload
- **Parameter Location:** Request Body
- **Description:** To upload resume in a profile

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    {
  "link": "string",
  "linkType": "string"
}


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/listDrill
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    #NAME?





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/users/{partnerId}/customer
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/users/login
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/commons
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/common/timezones
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{partnerId}/OVERVIEW
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/common/domain
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/common/technology
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{partnerId}/SCHEDULE
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{partnerId}/PRIZES
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{partnerId}/FAQ
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{partnerId}/COLLABORATORS
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{partnerId}/submissionFields
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/submissionFields/default
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{partnerId}/JUDGINGCRITERIA
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{partnerId}/THEMES
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{partnerId}/OPPORTUNITIES
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{partnerId}/RESOURCES
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{partnerId}/panels
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{partnerId}/submissions
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{partnerId}/submissions/evaluations/all
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/stats/drills/{partnerId}
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** GET
- **Request URL:** /api/v1/drills/{partnerId}/mails/templates
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/OVERVIEW
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/SCHEDULE
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/PRIZES
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/FAQ
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/COLLABORATORS
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/{partnerId}/submissionFields/configure
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/JUDGINGCRITERIA
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** DELETE
- **Request URL:** /api/v1/drills/{partnerId}/COLLABORATORS/{partnerId}
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** DELETE
- **Request URL:** /api/v1/drills/{partnerId}/JUDGINGCRITERIA/{partnerId}
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/THEMES
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** DELETE
- **Request URL:** /api/v1/drills/{partnerId}/THEMES/0ec1ec29-eacb-4ea8-a3c8-edc2ed9d5345
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/OPPORTUNITIES
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** DELETE
- **Request URL:** /api/v1/drills/{PartnerId}/OPPORTUNITIES/45af4cc1-41f5-4e42-91f1-1cbb73ba36bc
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/PROBLEMSTATEMENT
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/RESOURCES
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/{partnerId}/panels
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/{partnerId}/mails
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA





-----------------------------------------

- **Method:** POST
- **Request URL:** /api/v1/drills/{partnerId}/mails/templates
- **Parameter Location:** Request Body
- **Description:** 

**Request Parameters**
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::
 
    NA


**Response Object**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    NA

