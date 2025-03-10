# Table Extraction for costing Element

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-09-20 um 13.42.20.png" alt=""><figcaption></figcaption></figure>

In order to activate the table extraction for costing element you will have to import the m3costingelement table into DocBits.

From the M3 Homepage, type Command + r and search the “PPS280” prompt.

Select any of the lines displayed to you. On the next menu, select TOOLS and “Export to Excel”

![](https://lh7-us.googleusercontent.com/I8SYWm-JwpyYRHFUp2obGtXcsa7m_blJ_lTrnhczztRIXIN5gfxCt3eRw6ZI42fH6AwnsKyv4ux5-rhaT505PsyDFFI_anUNvmACFyx_ssgxaqWq25vLt_E5s310HNoiPPLf35qJlYtstjpj5Cc4aB4)

Select “Export all Rows” and then press EXPORT.

![](https://lh7-us.googleusercontent.com/wtjHI9L4YUhf-yJFjcPGu218Vis_zELtCIfpmkIUKgasfrdfNW-dr_J1DqXlfD-SBrnVduDrMLAIAQh6UTlzBqEP_JPXP48elGMyGj0ByZbX7TpqlnIfRZ4ZoD0pyCo-AKigeKjlHN6cFcdpeClZ9L4)

Once downloaded, you will need to alter the excel file before converting it into a CSV file.

You will need to open the excel file, it will look similar to what is shown below.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

From this excel sheet you need the columns A, B, H, J ,K and I, alter the excel sheet so that the end result looks as follows.

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Once this is done, save the file as a CSV.

Once you have your CSV file, go to the following webpage. This depends on which environment you are using:

* Prod: http://api.docbits.com/
* Sandbox: http://sandbox.api.docbits.com/
* Stage: http://stage.api.docbits.com/
* Demo: http://demo.api.docbits.com/
* Dev: http://dev.api.docbits.com/

Here you will manually upload the CostingElement table via an API. Click on the Authorise button.

![](https://lh7-us.googleusercontent.com/tyzOq3BR2QqTguQFKicxo0dE5j5hGsP-BhfVbS81O_mxN5bSVp40jYfgsVJcE_rBLFMDJNvbPkPIdjPqaqoNbHBBM-9hx0i-U4VAH9ISBYhpwKgqQeUEd67VV1E4izwNyxbAwwrhCmrAo1uIKhLherY)

Here you will need to insert the API Key from your DocBits environment. This is located in Settings under Integration.

![](https://lh7-us.googleusercontent.com/4ADnevq6kq_vbxUJpyPbHNcGvRvpO-l9Gwd8ZaYf_vO4uWhSl1jmKNpddmHGc9ZHMMbXCgLOElLDYbNwB3INmBDETecPrDnpI601IUOZQlT7tc7OLSPXwkooOJFNwML2i_gvBPuE8CvfwRpX-ZIlb_g)

Once complete, search for the API called master\_data\_lookup/import\_data and fill in the required information. Once complete, click EXECUTE to trigger the API.

## data\_type needs to be costing\_element

![](https://lh7-us.googleusercontent.com/8UD4FhFv2dRB4cMjCDL4G9ndjH7laVMKWqdeMaJGgEo48-UVvucB1uOydzNdfFy0yPM5bb66mZB4k9uJR7TTiEREGFaV2EqW01gxJpTyuUfGNh5QmBjySkyhZ56gWV8sYs8WI5RnHcENtXgjTU0vg0Q)

If done correctly, the M3CostingElement table should now be in your DocBits environment. Table extraction for costing elements has now been configured for your environment.
