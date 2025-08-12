Register a Submission Account
=============================

Before you can submit data to BioSamples you must register a Webin submission account.

To do so, please navigate to the Webin Portal and click the ‘Register’ button. You will be presented with the below interface:


Fill out the boxes, giving details of the group and centre for which you are submitting. The centre name for your account can be changed later: note that the value will be applied irrevocably to all submissions you make from this account. Always make sure your account’s centre name is correct before you perform a submission.

You must add at least one contact to the account. Names added here will be automatically included in certain types of submission, including those which are processed into the EMBL Flat File format. In addition, when contacting the helpdesk certain requests will only be considered from people named as account contacts. It is therefore advisable to add new members of your team to this account if they are likely to participate in submission activities.

For interactive submissions, you can login with your username and password to BioSamples to access the drag’n’drop uploader and validation services.


For programmatic submissions only: How to get a token
For programmatic submissions, BioSamples uses token based authentication. This means that once you have a WEBIN account, you can login with your username and password to receive a token. This is a piece of text that contains all the information we need to know about who you are and what data you are allowed to access. You present this information to the API every time you make a request.

The Webin authentication token lasts for 3 hours unless a long validity token is requested using the time-to-live (ttl) parameter, so if you have a long-running process, you may find the token expiring before the process completes. In this case, use the ttl parameter and set it to longer. You can obtain a token by following the instructions below or running the commands here.

