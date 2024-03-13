# IDM ACL Updater

**Feature Description**

This is a feature which, every 6 hours, uses the ION-API file to connect to your Infor-IDM and check through the newest/latest documents of the IDM-document-type(s) the DocBits team has configured at your request, and if the document type has an incorrect ACL-Setting (for example public), it will then be changed to the ACL-Setting you want (for example private). The image below illustrates the configuration of the API performing this feature

![](https://lh7-us.googleusercontent.com/gbiyEstnxrMFjgBxepfmz4gbW9iR0ZWBp6st1r7PIuFNxY\_DP7-0D\_NaVRDQEKVIDIBDXQ\_BTvfqLfgWgMRtR6Qn64JOc2H4Xi2vZ7GIe\_K9i\_Q4ZLsN6wPVnKCeWip3H6C7BLMBVsL4SDbQhqLNYTU)

The API is called “DocBits-Error” and is situated at the end in the above dataflow. The endpoint mapped to the API (DocBits\_Import) is the endpoint that carries out the functions discussed earlier.

**How to enable the IDM ACL Updater**

To enable this feature, from the Dashboard, go to Settings.

![](https://lh7-us.googleusercontent.com/co1KucusJgLeC18EFMPzync56VE0yRHW5vDUYgPQUfrt\_ie5\_leKdzL2OzB85NbE7i58LeqF6O1DcSB5J1eGyiN3r1a9kjdzf1w4lF91AXrOjILb6Gou3pvYf5BkSwmwoeo-sxMlugQU9wP027y-g5o)

Navigate to Document processing → Module

![](https://lh7-us.googleusercontent.com/lBVVT59jgsgYF8HH14Jou8Gh4VCOt1cnvqtA55fXuHIgYKFwvAi4mypmPqaDcX6at8l\_VfbvxHu-9MZf1kzMPtEJFYr03fl2xvkSgNNY2zaCjJ16HmaI5EFOHauCxr7-gi37C8BBUisMxIqZKtxlndI)

Once in the Module menu, you will find the slider to enable the IDM ACL Updater at the bottom of the page.

![](https://lh7-us.googleusercontent.com/J5zSxHsVNAoVa24TsmOr8UOwL4MmaUzK7dCF\_\_Ax6lyFkrc1IEO4wkMJ4fOqpVaRGTkWtzQFc2E9OVqEYtcll5N-CAh0eMM5MAF6nuXUO6pTGy2lbwqLhEJXPm7gGwD-sy6NIx8LZ\_fIQr1Z940mA2Q)

Once enabled, you simply need to upload the corresponding ION API file in the space provided as well as other data (eg. the document type) from INFOR as indicated. This data can be added by pressing the ADD button.
