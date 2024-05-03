# Doc Script

If you want to use scripts that, for example, convert currency characters or written-out currency names into ISO codes.

Go to the desired document type. Once here, select the Scripts option.

![](https://lh7-us.googleusercontent.com/P1V7wiiuXITAhPs7gyf52WBCWoBxztvCFTkZQxqQFIFwiORjXpYEMDxsRy5xiIGCI0sHw07ZyOdK9mWv1i-BQnjjjOlmzdZuNE5UNAnICi6zWVy69e5UCg5oVElInLDKWJVHGi4hGy8ikanZvV9VD-M)

You will be taken to the Scripts Menu. Once here, click on +NEW.

![](https://lh7-us.googleusercontent.com/KfYgsUtkYfxMqeuh3s7rHftLO1YPAeDcT2YzXRKkvDWpNRtiPDTRI7ZOo2aKaqObdG6deV8yph59TYIo33GBN3EVHnMA\_OJ2wwyMiWUg-aiFaUh1ZLTzsgXBnAPpxBwW2auwK5sfxSAg94n2BfkJHQA)

From here you have the choice of a Label, the document type, when the script for the document type should be triggered and also a specific sub document type if necessary. After adding the script in the provided area, click on SAVE.

For example:

currency\_map = {

&#x20;   "€": "EUR",

&#x20;   "EURO": "EUR",

&#x20;   "$": "USD",

&#x20;   "£": "GBP"

}

currency\_value = get\_field\_value(fields\_dict, "currency", None)

if currency\_value:

&#x20;   currency\_value = currency\_value.upper()

&#x20;   if currency\_value in currency\_map:

&#x20;       currency\_value = currency\_map\[currency\_value]

&#x20;   set\_field\_value(fields\_dict, "currency", currency\_value)

In the next step, upload a document with one of the following criteria: “€”, “EURO”, “$” or “£”.

When the document is ready for validation, open this and click in the Currency validation field. You will be prompted to select the appropriate area on the image. Now do this with the € sign.

You will then immediately see that € is converted to EUR by the script. The same is done by the script when you mark EURO on the invoice.

\
