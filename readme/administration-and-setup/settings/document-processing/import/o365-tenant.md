# O365 Tenant

> Migrated from Confluence (page: "O365 Tenant"). Images referenced in the original page remain linked to Confluence blob URLs. If you want the images embedded locally in the repository, I can download the attachments and place them in a nearby `assets/` folder and update the image links. See the notes at the end.

# Register App on Azure AD

**Note:** The permissions may require authorization from an administrator.

1. Sign in to the [Azure Portal](https://portal.azure.com/) using your credentials.
2. From Azure services, locate and open Azure Active Directory (also known as Azure AD).

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=f7983629-4559-4ef6-b611-c0d0723ae7be&&collection=contentId-2430631937&height=93&occurrenceKey=null&width=96&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
3. Under the **Manage** section, select **App registrations**.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=31b99024-56c1-4c81-ba55-022420c67d0a&&collection=contentId-2430631937&height=471&occurrenceKey=null&width=230&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
4. In the App registrations screen, click **+ New registration**.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=efe090f2-39b1-435f-ad90-816eec912ba4&&collection=contentId-2430631937&height=30&occurrenceKey=null&width=143&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
5. The **Register an application** screen displays. Enter the user-facing display name for the App in **Name**.

6. ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9cef067d-7100-437f-a331-8b65f5f0ff2d&&collection=contentId-2430631937&height=101&occurrenceKey=null&width=828&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)

	Select one of the following account types depending on your needs:

* **Accounts in any organizational directory (Any Azure AD directory – Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)**

* ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=139e40e5-e0e7-459a-b050-03013c473824&&collection=contentId-2430631937&height=149&occurrenceKey=null&width=809&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)

	**Accounts in any organizational directory (Any Azure AD directory – Multitenant)** 

7. ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=8ac58cb6-cf49-4595-8c3e-276cad31dd6b&&collection=contentId-2430631937&height=236&occurrenceKey=null&width=1103&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)

	Leave the option **Redirect URI (optional)** as is.

8. Click **Register** to complete the App registration. This will return you to the screen for the new App.

9. ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=9d368861-8da3-4eb0-9881-7d2bb7dd9c7a&&collection=contentId-2430631937&height=73&occurrenceKey=null&width=387&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)

	In the App screen, locate the **Application (client) ID**. Copy it to be used when configuring email import for Docbits.

10. ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=16692f74-cae7-4398-a251-4264bc7a1469&&collection=contentId-2430631937&height=114&occurrenceKey=null&width=534&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)

	From left panel, select **Certificates & secrets**:

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a32b4fec-6970-40ca-b328-39430c9e8ff4&&collection=contentId-2430631937&height=51&occurrenceKey=null&width=200&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
11. In the **Certificates & secrets** screen, click on **+ New client secret** button under **Client secrets** section:

12. ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=ac2b11e5-f9f3-4f32-ac81-e33923ee3c90&&collection=contentId-2430631937&height=170&occurrenceKey=null&width=818&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)

	In the **Add a client secret** dialog box, click the **Add** button:

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=32a37673-74e5-4db0-b3d1-aa72fe8de4cc&&collection=contentId-2430631937&height=314&occurrenceKey=null&width=309&__contextId=null&__displayType=null&__external=false&__fileMimeType,null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)
It is recommended to fill in a description to identify this secret among many (as of now the limit is 2 secrets per App).  
**Note:** Select this expiration date according to your company policy. Once expired, a new client secret will need to be created and specified for each email configuration where it was used previously.

13. The newly generated client secret will be visible. Copy this client secret to be used when configuring email import for DocBits

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1a502147-3462-4574-98e0-563435a8439a&&collection=contentId-2430631937&height=188&occurrenceKey=null&width=1119&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId,null&url=null)
**Important:** Ensure that you have copied the client secret as the client secret will not display again once it is closed.

14. Select **Authentication** on the left panel. This will present the **Authentication** screen on the right-hand side.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=1d36c5f6-e350-479d-9786-1d20f2fb9735&&collection=contentId-2430631937&height=42&occurrenceKey=null&width=271&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId,null&url=null)
15. In the **Advanced settings** section, click **Yes** for **Default client type**.

16. ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=dee3ca45-c7be-4dfa-a203-a2a52e1b30af&&collection=contentId-2430631937&height=211&occurrenceKey=null&width=708&__contextId=null&__displayType=null&__external=false&__fileMimeType,null&__fileName=null&__fileSize=null&__mediaTraceId,null&url=null)

	Click **Save** to confirm changes.

	![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a2cb2317-a006-4062-b953-c93d75588b6a&&collection=contentId-2430631937&height=141&occurrenceKey=null&width=308&__contextId=null&__displayType=null&__external=false&__fileMimeType,null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)

17. Select **API permissions** on the left panel. This will present the API permissions screen.

	![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=36647871-c0b4-44c5-8be6-df46422921c2&&collection=contentId-2430631937&height=40&occurrenceKey=null&width=202&__contextId=null&__displayType=null&__external=false&__fileMimeType,null&__fileName=null&__fileSize=null&__mediaTraceId,null&url=null)

18. By default the **User.Read** permission from **Microsoft Graph** is present, leave this as is.

	![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=afe43dea-71c0-4e8c-899f-e7d50af43d52&&collection=contentId-2430631937&height=106&occurrenceKey=null&width=543&__contextId=null&__displayType=null&__external=false&__fileMimeType,null&__fileName=null&__fileSize=null&__mediaTraceId,null&url=null)

**Note:** This is a required permission. If this permission is not available, then add the permission with the steps mentioned below for **Mail.ReadWrite** permission.

19. Click **+ Add a permission**.This will open the **Request API permissions** panel.

	![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=5854db17-ab2a-486b-8eef-88bc17a0e39d&&collection=contentId-2430631937&height=197&occurrenceKey=null&width=309&__contextId=null&__displayType=null&__external=false&__fileMimeType,null&__fileName=null&__fileSize=null&__mediaTraceId,null&url=null)

20. ![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=ddee3cb0-c0ed-4f3e-adff-d41f914d555e&&collection=contentId-2430631937&height=346&occurrenceKey=null&width=840&__contextId=null&__displayType=null&__external=false&__fileMimeType,null&__fileName=null&__fileSize=null&__mediaTraceId,null&url=null)

	Click **Microsoft Graph**.

21. From the two sub-categories, select **Delegated permissions**.

	![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=94c0df46-824d-4238-a561-3c3fb85cb118&&collection=contentId-2430631937&height=202&occurrenceKey=null&width=797&__contextId=null&__displayType=null&__external=false&__fileMimeType,null&__fileName=null&__fileSize=null&__mediaTraceId,null&url=null)

22. Type **Mail.ReadWrite** in the search box. Select the **Mail.ReadWrite** checkbox for the permission.

	![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=a80ee8fd-76ab-48e2-9d22-6c095b89cf76&&collection=contentId-2430631937&height=511&occurrenceKey=null&width=408&__contextId=null&__displayType=null&__external=false&__fileMimeType,null&__fileName=null&__fileSize=null&__mediaTraceId,null&url=null)

23. This will enable the **Add permissions** button at the bottom of the panel. Click **Add permissions**.

	![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=7ab5c649-8a06-46cb-bf49-5db87e68c745&&collection=contentId-2430631937&height=574&occurrenceKey=null&width=413&__contextId=null&__displayType,null&__external=false&__fileMimeType,null&__fileName=null&__fileSize=null&__mediaTraceId,null&url=null)

24. This will add the **Mail.ReadWrite** permission to the list of **Configured permissions** for the App.  
  **Note:** Administrator permissions may be required. The administrator will have to authorize the App for using these permissions. Once authorized the granted status will be indicated as follows:

	![](blob:https://media.staging.atl-paas.net/?type=file&localId=null&id=44c76000-366d-4968-8ccd-c656fd156f68&&collection=contentId-2430631937&height=263&occurrenceKey=null&width=1028&__contextId,null&__displayType,null&__external=false&__fileMimeType,null&__fileName=null&__fileSize=null&__mediaTraceId,null&url=null)