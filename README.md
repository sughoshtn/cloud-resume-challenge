# cloud-resume-challenge
I am an IT professional with over 13 years of Experience in the field having a background in CRM applications design development including Siebel and Salesforce.I am also a tech enthusiast who wants to explore different technologies and continue to improve on my technical skills.

In 2021, I stumbled upon the Cloud Resume Challenge created by Forrest Brazeal and wanted to try my hands at it. This pushed me to know more in AWS. As my AWS Knowledge was limited, I Decided to take this as a challenge and prered myself for a Solution Architect Associate Certification.I was able to crack the Certification in around 3 months time.

However , its just not enough to have a certification and not have a hands on the technology. So, came along the Cloud Resume challenge to get a hands-on practice to apply the skills i was learning.

![image](https://user-images.githubusercontent.com/6101877/223347984-bded98e8-e819-451e-bc73-d9101f21e637.png)

The Cloud Resume Challenge

This one is already really old challenge for a lot of people now, however for those who are not aware below are the Objectives of hte Challenge :

1. Certification : 
Your Resume needs to have atleast 1 AWS ertification to start with.
2. HTML :
You would need a Resume to be written in HTML. Not a word file or a PDF.
3. CSS :
The Resume needs to be FOrmatted and Styled. It doesnt matter, if the Resume is not fancy, but should not be raw HTML.
4: Static Website
Your HTML resume should be deployed online as an Amazon S3 static website.
5. HTTPS
The S3 website URL should use HTTPS for security.
6. DNS 
Point a custom DNS domain name to the CloudFront distribution, so your resume can be accessed at something.I used my custom domain Name pointing to resume.sughoshnagarajan.com .
You can use Amazon Route 53 or any other DNS provider for this. A domain name usually costs about ten bucks to register. I registered myself on goDaddy.com for a Domain Name.
7. Javascript
Your resume webpage should include a visitor counter that displays how many people have accessed the site. You will need to write a bit of Javascript to make this happen.
Below is a snippet of how i have written the Java script: 
if (document.location.origin == "https://resume.sughoshnagarajan.com") {
            $(document).ready(function() {
                $.ajax({
                    url: "https://<URL to your API Service Running on AWS>/fn-site-visit-counter",
                    success: function(result) {
                        $("#counter").html(result);
                    }
                });
            });
        }


8. Database
The visitor counter will need to retrieve and update its count in a database somewhere.I have used Amazon’s DynamoDB for this.

9. API
Do not communicate directly with DynamoDB from your Javascript code. Instead, you will need to create an API that accepts requests from your web app and communicates with the database. 
I have used an AWS’s API Gateway and a Lambda services for this. 
(They are almost free for what we are doing.)

10. Python
As the purpose here is to explore and learn, Use Python here to Program a Lambda function. Include the boto3 library for AWS for the basic functions.
This script needs to be invoked from the API

11. Tests
You should also include some tests for your Python code.
Here is a simple test code :
{
        "key1": "value1",
		"key2": "value2",
		"key3": "value3"
}
12. Infrastructure as Code
The idea here is to make sure that we dont create all these components mentioned above manually by clicking around in the AWS Console but through a template.You can use CLoudFormation or Terraforming here, i have used a simple yaml template to do this.

13. Source Control
You do not want to be updating either your back-end API or your front-end website by making calls from your laptop, though. You want them to update automatically whenever you make a change to the code. This is done using a Github repository.

14. CI/CD (Back end)
Set up GitHub Actions such that when you push an update to your Serverless Application Model template or Python code, your Python tests get run. If the tests pass, the SAM application should get packaged and deployed to AWS.
	
