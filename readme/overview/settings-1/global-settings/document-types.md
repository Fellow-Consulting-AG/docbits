# Document Types

In DocBits you will find the SETTINGS menu in the upper bar on the DASHBOARD.

![](https://lh7-us.googleusercontent.com/Hymy6pYVMY-UIxQ6P7t8eB3MJd5e7uYeqr8e68goAaVnEsTR8B6y-aMPNaUX-ZydM3CJHWAgUlVsSFfkWxytFZysHnoHQEpHlhlAfPflLu3riif-7KqaJpB8Qka0pWVv-3K2xrrMIZI-p8-RsswmxrE)

If you are logged in to DocBits as an admin, you will find all fields of a document that can be extracted under the respective document type.

Open the menu for Document Types.

![](https://lh7-us.googleusercontent.com/6YuM3TiseSwLVZAsJa\_WoeeyfifzvmBB0x1Y3v901MDsJ6Mn6n9SeiN7\_ILuF43h1jbHAKelHeVRjtfCYaAYZjLz0wvJZkMq5QXHakatU-bk7SoX3GDyeXOUvp7kjAI8mZNd73BMuDHCGDxW820pljU)

In the following overview you will find all standard document types available for you

![](https://lh7-us.googleusercontent.com/Qh2CHliApuNiEeGh7-pHMzC72Wwy9OHKZMQVG-dx9AQcB-5agqouu0PZSpsSBV8wH83voHHkfkNF2zKs5Ihaw3q8mJP3NeEhpY0EWTaUFPsyW62g12ryMzfS2zKpo-nBRQ0c5XGuy9ZArJLkWpmf4GY)

**Activate/Extraction Type**

To the right of each document type, you will see Activate and Extraction Type sliders.

Activate: This document type is active in your DocBits environment.

Extraction Type: This slider allows you to enable or disable a set of predefined rules for the document type when it is processed by DocBits. By selecting the gear icon to the right of the slider, the following menu will appear.

![](https://lh7-us.googleusercontent.com/mqJUTD0pCtfVHpq9qOXYmmcJONgSQZqlhRP4tBYJKK8hZCFR8B6KXPpFY7xNqtc5PFIVWO-PJNf8vAtVVAdTVyuWOke4lSEX2Nnkx7sTvD3MW\_CRHBzSwBqnvwjqeJtI2uIaJnfZnwsmacpeBmWgXwI)

To see which fields can be extracted, for example from an invoice, click on FIELDS for this document type.

![](https://lh7-us.googleusercontent.com/0uGJvBvZ1WufvZb-TYU2VeVuZUNxK5o8Tqb40BdEJykNi\_f-nI-DGPHKlxHGLxXarN-uOO9I1Gjs0uiHe9TMgWjElHTWFhKA3a\_xlwHOoWOhEhRvAH6oBZw1RDuxytNQCvC7fTe\_7YSEoG8Lp0nk9pA)

**Field Settings**

Here you will find all the fields that can be extracted

![](https://lh7-us.googleusercontent.com/frAZqTF-cWw6Kh3HiXj4PRPvC56TNqgte5lPMgeSR6Q28O\_q9OsC79MAM3xyJiBeLe5CdAjyW1SNq7CHniPqTmzXUBPYOHIpFuF4g\_8TvpecdJAhld5HvzoRMcydafDISuwhSBZOXan7rfCWJ6cL1Fw)

You can also CREATE FIELDS like freight, postage or any field with an amount you want to extract from your invoices.

For each field you can check the boxes if they are:

* REQUIRED: Here you can define if the field must contain a value to continue.
* READ ONLY: Here you can define if a field can only be displayed but not edited.
* HIDDEN: Here you can define whether a field should be hidden or displayed in the extraction view.
* FORCE VALIDATION: Here you can define whether a field must always be validated manually, even if it has been read 100% by DocBits.
* OCR and MATCH SCORE: Setting as described below, per field.
* FORMULA: Creation of a formula per field.

![](https://lh7-us.googleusercontent.com/rbHBbTDrmeHwCLhd2KTlYxDNGH86CJNKm1y45smSdPBYR9POZmDGMQIjTakshbcJFo7k1TbZS1I9kC\_ERdldIRbM2NRNU76wWhbjslGjFzM6ZLaxS\_\_zET7aGAv1wqIKXbJ3CIHyD5ijIitWaLkdxI0)

If all settings are made and should be saved, please confirm this with the SAVE SETTINGS button at the bottom of the page, otherwise the settings will not be applied.

![](https://lh7-us.googleusercontent.com/0h\_MC9D2qYARH-EkL0iXXzjeoxZNspHCIj8FE3Nc6lE1jD6XAIxvnORDd\_XokRZ6FIb3UkkcNF1AS42qCRpid2YxCSnbfGrQPi7skbRuyuPcDELYddt1WPqd-knXP7uIsP4AdPIcStRle435ZWffZUY)

**Recognition Settings**

![](https://lh7-us.googleusercontent.com/ILcUUoTWZJRMU0IsCDOKfFuW7-R6WfozPCkl4kzGlpb\_DVRaMX1z\_0CJiyJdHzcqU1c8VDh4NZcdK-RsN0sB\_JR86oNqEX9d1QQzLM7B6pr1Q4gRWhHefnHEhOluCfkMAFggYQEyHpJqYzw61h4aeIk)

**OCR**

Here you can set the sensitivity of the OCR (Optical Character Recognition) function for all fields at once. This value determines the sensitivity with which a field is marked in red if it could not be extracted with 100% certainty (OCR related!).

**Match Score**

This is where you can set the sensitivity of the MATCH SCORE function for all fields at once. This value determines when a field is marked in red if DocBits has not extracted the field with 100% probability. In this case the field needs to be validated manually.

The button RESTORE DEFAULTS will set back both values to “50”.

**Profile**

Here you can define the profile that shall be used. Either Default or ZUGFeRD.\
In profile ZUGFeRD there are predefined fields that are mandatory for this type of invoice.\
If you do not explicitly use ZUGFeRD, please select “Default”.

![](https://lh7-us.googleusercontent.com/K-ECluYA9Y2JxRdxMsTEx02VhSSWWodeMojYbPMCxRJLlZ-TCgDPzcYQNTfxJgYXLH1lxvSIMpLLlFf15bD\_EixLi4dqmp5JLXJKSKMbdGtNTKZcX9lAlZ\_dIRnhNl2dWMP6MYWamidNCtabBUVW1Lo)
