# O365 Tenant

> Migrated from Confluence (page: "O365 Tenant"). Images referenced in the original page remain linked to Confluence blob URLs. If you want the images embedded locally in the repository, I can download the attachments and place them in a nearby `assets/` folder and update the image links. See the notes at the end.

---
migrated-from: "Confluence - O365 Tenant"
migration-ticket: DOCB-8610
date: 2025-11-03
---

# O365 Tenant

> Migrated from Confluence (page: "O365 Tenant"). Images have been moved to `.gitbook/assets/o365-tenant/`. Use the included script `scripts/download_o365_attachments.sh` to fetch the files from Confluence into that folder (needs Atlassian username + API token).

## Register App on Azure AD

**Note:** The permissions may require authorization from an administrator.

1. Sign in to the [Azure Portal](https://portal.azure.com/) using your credentials.
2. From Azure services, locate and open Azure Active Directory (also known as Azure AD).

![](.gitbook/assets/o365-tenant/image-20251030-093427.png)
3. Under the **Manage** section, select **App registrations**.

![](.gitbook/assets/o365-tenant/image-20251030-093406.png)
4. In the App registrations screen, click **+ New registration**.

![](.gitbook/assets/o365-tenant/image-20251030-093346.png)
5. The **Register an application** screen displays. Enter the user-facing display name for the App in **Name**.

![](.gitbook/assets/o365-tenant/image-20251030-093234.png)

Select one of the following account types depending on your needs:

* **Accounts in any organizational directory (Any Azure AD directory – Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)**

![](.gitbook/assets/o365-tenant/image-20251030-093227.png)

**Accounts in any Azure AD directory – Multitenant**

![](.gitbook/assets/o365-tenant/image-20251030-093220.png)

Leave the option **Redirect URI (optional)** as is.

8. Click **Register** to complete the App registration. This will return you to the screen for the new App.

![](.gitbook/assets/o365-tenant/image-20251030-093213.png)

In the App screen, locate the **Application (client) ID**. Copy it to be used when configuring email import for Docbits.

![](.gitbook/assets/o365-tenant/image-20251030-093203.png)

From left panel, select **Certificates & secrets**:

![](.gitbook/assets/o365-tenant/image-20251030-093128.png)
11. In the **Certificates & secrets** screen, click on **+ New client secret** button under **Client secrets** section:

![](.gitbook/assets/o365-tenant/image-20251030-093117.png)

In the **Add a client secret** dialog box, click the **Add** button:

![](.gitbook/assets/o365-tenant/image-20251030-093435.png)

It is recommended to fill in a description to identify this secret among many (as of now the limit is 2 secrets per App).  
**Note:** Select this expiration date according to your company policy. Once expired, a new client secret will need to be created and specified for each email configuration where it was used previously.

The newly generated client secret will be visible. Copy this client secret to be used when configuring email import for DocBits

![](.gitbook/assets/o365-tenant/image-20251030-093414.png)
**Important:** Ensure that you have copied the client secret as the client secret will not display again once it is closed.

Select **Authentication** on the left panel. This will present the **Authentication** screen on the right-hand side.

![](.gitbook/assets/o365-tenant/word-image-34.png)
15. In the **Advanced settings** section, click **Yes** for **Default client type**.

![](.gitbook/assets/o365-tenant/word-image-33.png)

Click **Save** to confirm changes.

![](.gitbook/assets/o365-tenant/word-image-32.png)

17. Select **API permissions** on the left panel. This will present the API permissions screen.

![](.gitbook/assets/o365-tenant/word-image-31.png)

18. By default the **User.Read** permission from **Microsoft Graph** is present, leave this as is.

![](.gitbook/assets/o365-tenant/word-image-30.png)

**Note:** This is a required permission. If this permission is not available, then add the permission with the steps mentioned below for **Mail.ReadWrite** permission.

19. Click **+ Add a permission**.This will open the **Request API permissions** panel.

![](.gitbook/assets/o365-tenant/word-image-29.png)

Click **Microsoft Graph**.

![](.gitbook/assets/o365-tenant/word-image-28.png)

From the two sub-categories, select **Delegated permissions**.

![](.gitbook/assets/o365-tenant/word-image-27.png)

Type **Mail.ReadWrite** in the search box. Select the **Mail.ReadWrite** checkbox for the permission.

![](.gitbook/assets/o365-tenant/word-image-26.png)

This will enable the **Add permissions** button at the bottom of the panel. Click **Add permissions**.

![](.gitbook/assets/o365-tenant/word-image-25.png)

This will add the **Mail.ReadWrite** permission to the list of **Configured permissions** for the App.  
**Note:** Administrator permissions may be required. The administrator will have to authorize the App for using these permissions. Once authorized the granted status will be indicated as follows:

![](.gitbook/assets/o365-tenant/word-image-24.png)
