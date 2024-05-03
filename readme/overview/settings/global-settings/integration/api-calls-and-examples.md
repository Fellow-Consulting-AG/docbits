# API Calls and Examples

**API Calls for Document Upload and Status Check**

API integration provides functions and services that connect applications and processes. In this guide, we will show you how to make API calls through api.polydocs.io for document upload and status check.

**Authentication**

To make API calls, authentication is the first step. Follow the steps below to authenticate:

1. Open doc2api.cloudintegration.eu/docs
2. Click on Authorize in the upper right corner.
3. Enter your API Key and confirm by clicking Authorize.

![](https://lh7-us.googleusercontent.com/wceNQu0C9bBsIGNVPNwhPIMnY6nHCb19lqTEveKZEKkQRj3nSbWmEifsYMoKRpWLr5oS0jOczALnqRVcFa2LIGYfKrh5iWgvKqRKjUMs-gp5WMUTX1dmZ6KDK\_nPYIeG5NV281DmS7hT58NE6kp1cfQ)

**Upload a Document**

To upload a document, follow the steps below:

* After authentication, scroll down to the POST /document/process endpoint.
* Open the tab and click on Try it out in the upper right corner.
* Enter the following value in the source field: email:{Pattern name}.
* Select the file you want to upload and click Execute.

Your document will be uploaded to your dashboard with the rules you set in DocBits.

![](https://lh7-us.googleusercontent.com/TSWOw9Xuvs7JH9UIfyAWVRLhHZuqvrl5pd1lIbtS66KTc7BQUbYn7OilucvxbvgbfEDFn8f2uFio6EdAZLnLNPjPR9HxqCpzxr3p58mS40RTmJGv6O7GyI-faHLLoRF2MJf3Z7aBpmPrdc2ZWrkqf0c)

![](https://lh7-us.googleusercontent.com/A-JoLxKSnX7\_\_59F\_tLHxy1Dj9KAp1ApYqUzvDcqEczkDy1R9VrK0mjGxR3sybWTdEsFSWs5S28a29z3IeALumD0J7xalvRU5RrST31i-ZHwrOGvBOhl5wVUH5cqztLj65XbVuAtl4D3NTXc\_xkBlbk)

**Document Status Check**

To check the status of a document, follow the steps below:

* After authentication, scroll down to the GET /document/status endpoint.
* Open the tab and click on Try it out in the upper right corner.
* Enter the document ID in the doc-id field. You can find the document ID when you open the document on the dashboard. This is the last part of the URL when the document is open.

![](https://lh7-us.googleusercontent.com/4iokWT\_cydakjt2P0GT6Kor4rOGhSpQVIR9opbFo9Ac-cIXZrDP-7E1Lm16GCG7pcN8bbifha5Iq5e1xpkK7UxkL-p6auJSjyx9z91wChxFrGe8GvWLhNAkE6RS2JT\_OwfnRW98mlN4jPkWfObPb9C8)

You will receive the following response

![](https://lh7-us.googleusercontent.com/w0xjyhtsAVnjHZ7NayWX1pPnNASSoqyy3h-2ml4EXrpfXBfmldf4CxFeyT3B4cVY785qSWXjtvN7qHfHP9XR3ddU-65D7SWzSP2ku\_wBht7-g3pFSt4Kle5m9k-AvbFvrn6Ix1m9oQh2mC7VVGbV49A)

If the status is “Ready For Validation,” it means that the user can check the document.

Uploading a Document with Metadata

To upload a document with metadata, follow the steps below:

* After authentication, scroll down to one of these endpoints: /document/process\_documents, /document/process, or /document/process\_base64.
* Open the tab and click on Try it out in the upper right corner.
* Enter the metadata in the metadata field. The metadata needs to be in a valid JSON format. An example of a metadata entry would be: {"custom-key": "the custom value", "custom\_doc\_id": "8a5cf33b-c923-4879-96ca-94d69965d508"}.
* Select a file to upload.
* Click Execute.
* Wait for the response. If the metadata field is not a valid JSON, an error message will appear. If “success”: true, then your document will be uploaded to your dashboard with the rules you set in DocBits.
