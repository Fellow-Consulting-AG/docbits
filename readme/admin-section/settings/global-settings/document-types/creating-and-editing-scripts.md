# Creating and Editing Scripts

## To create a new script in DocBits, follow these detailed instructions:

**Choose the scripting language:**&#x20;

First, you need to choose the scripting language you want to use. DocBits typically supports common scripting languages ​​such as Python, JavaScript, or SQL. The choice of language depends on the needs of your project and your own competency.

**Open the script development environment:**&#x20;

Log in to DocBits and navigate to the script development environment. This is in the administration area.

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-23 um 15.19.50.png" alt=""><figcaption></figcaption></figure>

**Create a new script:**&#x20;

Click the "+ New" button to open a new script editor.

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-23 um 15.21.58.png" alt=""><figcaption></figcaption></figure>

**Write the code:**&#x20;

Use the editor to write the code for your script. Start with the basic syntax of your chosen scripting language.&#x20;

For example, if you are using Python, your script might look like this:

## 1. Example script in Python

<figure><img src="../../../../.gitbook/assets/image (131).png" alt=""><figcaption></figcaption></figure>

## Function to clean patient names

def clean\_patient\_name(name): cleaned\_name = name.strip().title() # Remove spaces and apply capitalization

return cleaned\_name

## Main program

if **name** == "**main**": patient\_name = " john doe " cleaned\_name = clean\_patient\_name(patient\_name) print("Cleaned patient name:", cleaned\_name)&#x20;

## 2. Example script

<figure><img src="../../../../.gitbook/assets/image (132).png" alt=""><figcaption></figcaption></figure>

**Test the script:**&#x20;

Check the code for errors and test it in a test environment. Make sure the script produces the expected results and works correctly.

<figure><img src="../../../../.gitbook/assets/image (133).png" alt=""><figcaption></figcaption></figure>

**Save the script:**&#x20;

Save the script in DocBits and give it a meaningful name that describes the purpose of the script.

<figure><img src="../../../../.gitbook/assets/image (134).png" alt="" width="84"><figcaption></figcaption></figure>

**Mapping the script to document types:**&#x20;

An important step is mapping the script to the appropriate document types. This determines when and how the script is applied. This can usually be done through a configuration interface in DocBits, where you can assign the script to a specific document type and specify under which conditions it should be applied.

<figure><img src="../../../../.gitbook/assets/image (135).png" alt=""><figcaption></figcaption></figure>

**Review and publish:**&#x20;

After you have created, tested and mapped the script, check it again for errors and inconsistencies. If everything is OK, you can publish the script to the DocBits production environment.

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-23 um 15.29.18.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (136).png" alt=""><figcaption></figcaption></figure>

Through these steps, you can successfully create, test and implement a new script in DocBits to automate processes and improve the efficiency of medical documentation.


