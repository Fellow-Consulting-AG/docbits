# Example Script

Here are simple examples of how you can use different functions in small scripts.

**Verbose Examples**

#### **set\_field\_value(document\_data, field\_name, value)**

```python
iban_fuzzy = get_field_value(document_data, 'supplier_iban', None)
iban_extracted = get_field_value(document_data, 'iban_extracted', None)

if iban_extracted:
    iban_extracted = iban_extracted.replace(' ','')

if iban_fuzzy and iban_extracted and iban_fuzzy != iban_extracted:
    set_field_as_invalid(document_data, "supplier_iban", "There is a difference in the IBAN", "INVALID_VALUE")
elif iban_fuzzy and not iban_extracted: 
    set_field_as_invalid(document_data, "supplier_iban", "There is a difference in the IBAN", "INVALID_VALUE")
elif iban_extracted and not iban_fuzzy:
    set_field_as_invalid(document_data, "supplier_iban", "There is a difference in the IBAN", "INVALID_VALUE")
```

1.  **set\_date\_value(document\_data, field\_name, value, add\_days=0, skip\_weekend=False)**

    ```python
    genehmigungs_stufe = get_field_value(document_data, 'genehmigungs_stufe', None)
    genehmigung_user_1 = get_field_value(document_data, 'genehmigung_user_1', None)
    genehmigung_user_2 = get_field_value(document_data, 'genehmigung_user_2', None)
    genehmigung_user_3 = get_field_value(document_data, 'genehmigung_user_3', None)
    genehmigung_user_4 = get_field_value(document_data, 'genehmigung_user_4', None)


    try:
        current_status = str(document_json['status'])
    except:
        current_status = None

    first_approver = get_field_value(document_data, 'first_approver', None)
    if first_approver and current_status == "ready_for_validation":
        first_approver_name = str(get_user_by_id(first_approver).first_name+" "+get_user_by_id(first_approver).last_name) 
        set_field_value(document_data, "first_approver", None)
        if genehmigungs_stufe == "1" and genehmigung_user_1 =="LEER":
            set_field_value(document_data, "genehmigung_user_1", first_approver_name)
            set_date_value(document_data, "genehmigungsdatum_1", None, add_days=0)
            set_field_value(document_data, "genehmigungs_stufe", "2")
            update_document_status_with_doc_id(document_json['doc_id'], user, document_json['org_id'], "validated_pending_approval")
        elif genehmigungs_stufe == "2" and genehmigung_user_2 == "LEER":
            set_field_value(document_data, "genehmigung_user_2", first_approver_name)
            set_date_value(document_data, "genehmigungsdatum_2", None, add_days=0)
            set_field_value(document_data, "genehmigungs_stufe", "3")
            update_document_status_with_doc_id(document_json['doc_id'], user, document_json['org_id'], "validated_pending_approval")
        elif genehmigungs_stufe == "3" and genehmigung_user_3 == "LEER":
            set_field_value(document_data, "genehmigung_user_3", first_approver_name)
            set_date_value(document_data, "genehmigungsdatum_3", None, add_days=0)
            set_field_value(document_data, "genehmigungs_stufe", "4")
            update_document_status_with_doc_id(document_json['doc_id'], user, document_json['org_id'], "validated_pending_approval")
        elif genehmigungs_stufe == "4" and genehmigung_user_4 == "LEER":
            set_field_value(document_data, "genehmigung_user_4", first_approver_name)
            set_date_value(document_data, "genehmigungsdatum_4", None, add_days=0)
            set_field_value(document_data, "genehmigungs_stufe", "5")
            update_document_status_with_doc_id(document_json['doc_id'], user, document_json['org_id'], "validated_pending_approval")
    ```
2.  **set\_amount\_value(document\_data, field\_name, value)**

    ```python
    lines_total = 0.0
    if tables_dict.get('INVOICE_TABLE'):
        for row in tables_dict['INVOICE_TABLE']['rows']:
            line_amount = 0.0
            for col in row['columns']:
                if col['name'] == 'TOTAL_AMOUNT':
                    line_amount = col.get('value', 0)
                    if line_amount:
                        line_amount = float(line_amount)
                elif col['name'] == 'NET_AMOUNT':
                    line_amount = col.get('value', 0)
                    if line_amount:
                        line_amount = float(line_amount)
                    break
            if line_amount:
                lines_total += line_amount
    total_amount = get_field_value(document_data, "net_amount")
    if not total_amount:
        lines_total = float(lines_total)
        set_amount_value(document_data, "net_amount",str(lines_total))
    ```
3.  **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**

    <pre class="language-python"><code class="lang-python"><strong>vpo_number = get_field_value(document_data, 'purchase_order', None)
    </strong>
    if po_number:
        clean_po_number = po_number.replace('PO', '')
        set_field_value(document_data, "purchase_order", clean_po_number)
    </code></pre>
4.  **create\_new\_field(field\_name, value="")**

    ```python
    currency = get_field_value(document_data, 'currency', None)

    if not currency:
        if 'currency' not in fields_dict:
            new_field = create_new_field('currency','')
            fields_dict['currency'] = new_field
            document_json['fields'].append(new_field)
        set_field_value(document_data, "currency", "USD")
        
    elif currency == "USD US Dollar" or currency == "U.S. Dollars":
        set_field_value(document_data, "currency", "USD")
        
    if currency != "USD" and currency != "EUR" and currency != "GBP" and currency != "CAD" and currency != "AUD" and currency != "CHF":
        set_field_as_invalid(document_data, "currency", "Currency is not valid")
    else:
        set_field_attribute(document_data, "currency", "is_valid", True)
        set_field_attribute(document_data, "currency", "validation_message","")
    ```
5.  **delete\_field(document\_data, field\_name)**

    ```python
    fields = [
        "shipping_charges",
        "fuel_surcharge",
        "handling_charge",
        "steel_surcharge",
        "tariff",
        "hazardous_mater",
        "core_charge",
        "wg_rebate",
        "make_ready_fee",
        "pl_transport",
        "import_duty",    
    ]
    for field_name in fields:
        if field_name in fields_dict:
            field_amount = get_field_value(document_data, field_name)
            if not field_amount:
                delete_field(document_data, fields_dict, field_name)
            else:
                field_amount = float(field_amount)
                if field_amount == 0:
                    delete_field(document_data, fields_dict, field_name)
    ```
6.  **set\_is\_required(document\_data, field\_name, value)**

    ```python
    net_amount   = get_field_value(document_data, "net_amount", None)
    if net_amount:
        set_is_required(document_data, "tax_country", True)
        set_is_required(document_data, "tax_code_without_country", True)
        net_amount__1 = get_field_value(document_data, "net_amount__1", None)
        if net_amount__1:
            set_is_required(document_data, "tax_country__1", True)
            set_is_required(document_data, "tax_code_without_country__1", True)
            net_amount__2 = get_field_value(document_data, "net_amount__2", None)
            if net_amount__2 :
                set_is_required(document_data, "tax_country__2", True)
                set_is_required(document_data, "tax_code_without_country__2", True)
                net_amount__3 = get_field_value(document_data, "net_amount__3", None)
                if net_amount__3:
                    set_is_required(document_data, "tax_country__3", True)
                    set_is_required(document_data, "tax_code_without_country__3", True)
                else:
                    set_is_required(document_data, "tax_country__3", False)
                    set_is_required(document_data, "tax_code_without_country__3", False)
            else:
                set_is_required(document_data, "tax_country__2", False)
                set_is_required(document_data, "tax_code_without_country__2", False)
        else:
            set_is_required(document_data, "tax_country__1", False)
            set_is_required(document_data, "tax_code_without_country__1", False)
    else:
        set_is_required(document_data, "tax_country", False)
        set_is_required(document_data, "tax_code_without_country", False)
    ```
7.  **set\_force\_validation(document\_data, field\_name, value)**

    ```python
    purchase_order = get_field_value(document_data, 'purchase_order', None)
    supplier_id = get_field_value(document_data, 'supplier_id', None)

    extra_data = document_json.get('extra_data', {})
    old_supplier_id = extra_data.get('supplier_id_new')

    extra_data['old_supplier_id_new'] = old_supplier_id
    extra_data['supplier_id_new'] = supplier_id

    document_json['extra_data'] = extra_data

    reset_validation = False
    if old_supplier_id is None or (old_supplier_id is not None and supplier_id is not None and supplier_id != old_supplier_id):
        reset_validation = True

    if not purchase_order:
        
        supplier_to_check = get_lov_values(org_id, 'BlacklistSupplier', return_type="list_of_values")
        
        if supplier_id in supplier_to_check:
            set_force_validation(document_data, 'purchase_order', True, reset_validation=reset_validation)
    ```
8.  **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**

    ```python
    fuzzy_purchase_order = get_field_value(document_data, 'fuzzy_purchase_order', None)
    document_date = get_field_value(document_data, 'document_date', None)

    if fuzzy_purchase_order:
        if 'purchase_order' not in fields_dict:
            field = create_new_field('purchase_order','')
            document_json['fields'].append(field)
            fields_dict['purchase_order'] = field
        set_field_value(document_data, "purchase_order", fuzzy_purchase_order)
        
    if not document_date:
        set_field_as_invalid(document_data, "document_date", "Es ist kein Datum vorhanden", "INVALID_VALUE")

    ```
9.  **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**

    ```python
    po_supplier_id = get_field_value(document_data, 'purchase_order_supplier_id')
    invoice_supplier_id = get_field_value(document_data, 'supplier_id')
    purchase_order = get_field_value(document_data, 'purchase_order')

    if purchase_order:
        if po_supplier_id != invoice_supplier_id:
            set_field_as_invalid(document_data, "supplier_name", "Supplier is different from PO supplier")
        else:
            set_field_attribute(document_data, "supplier_name", "is_valid", True)
            set_field_attribute(document_data, "supplier_name", "validation_message","")
    ```
10. **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**

    ```python
    bool = is_supplier_valid(user, {"name": "Supplier Inc."})
    ```
11. **get\_document\_content(document\_data)**

    ```python
    document_content = get_document_content(doc)
    if document_content:
        document_content = document_content.lower()

    clean_document_content = document_content.replace(' ', '').replace('-', '').replace('.', '').lower()
    clean_document_content = ''.join(clean_document_content.splitlines())

    de_word_to_check = [
        "deutschland"
    ]

    for de_word in de_word_to_check:
        clean_word = de_word.replace(' ', '').replace('-', '').replace('.', '').lower()
        if clean_word in clean_document_content:
            if 'innerhalb_de' not in fields_dict:
                field = create_new_field('innerhalb_de','')
                document_json['fields'].append(field)
                fields_dict['innerhalb_de'] = field
            set_field_value(document_data, "innerhalb_de", True)
        else:
            set_field_value(document_data, "innerhalb_de", False)
    ```
12. **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**

    ```python
    genehmigung_user_1   = get_field_value(document_data, 'genehmigung_user_1', None)

    if genehmigung_user_1!="LEER":
        update_document_status_with_doc_id(document_json['doc_id'], user, document_json['org_id'], "validated_pending_approval")
    ```
13. **get\_lov\_values(org\_id, key, return\_type="list\_of\_objects", sub\_org\_id=None)**

    ```python
    if not document_json.get("script_executed", False):
        document_content = get_document_content(doc)
        if document_content:
            document_content = document_content.lower()
        
        clean_document_content = document_content.replace(' ', '').replace('-', '').replace('.', '').lower()
        clean_document_content = ''.join(clean_document_content.splitlines())
        
        reverse_charge_to_check = get_lov_values(org_id, 'Kosten', return_type="list_of_values")
        
        all_charges = ""
        set_field_value(document_data, "kostentraeger", reverse_charge_to_check[3])
        for reverse_charge in reverse_charge_to_check:
            clean_word = reverse_charge.replace(' ', '').replace('-', '').replace('.', '').lower()
            if clean_word in clean_document_content:
                if all_charges:
                    all_charges += ","
                all_charges += reverse_charge
                clean_word = clean_word[:3] + " " + clean_word[3:]
        set_field_value(document_data, "kostentraeger", all_charges)

    document_json["script_executed"] = True
    ```
14. **format\_decimal\_to\_locale(value, to\_locale="en\_US.UTF-8", max\_decimal\_places=4, min\_decimal\_places=2)**

    ```python
    tax_amount = get_field_value(document_data, 'tax_amount', None)
    county_tax = get_field_value(document_data, 'county_tax', None)
    city_tax = get_field_value(document_data, 'city_tax', None)

    total = 0

    if county_tax:
        county_tax = float(county_tax)
        total += county_tax
    if city_tax:
        city_tax = float(city_tax)
        total += city_tax
         
    if 'tax_amount' not in fields_dict:
        new_field = create_new_field('tax_amount','')
        fields_dict['tax_amount'] = new_field
        document_json['fields'].append(new_field)

    standard_value = "{0:.2f}".format(total)
    formatted_value = format_decimal_to_locale(
        standard_value, document_json['amount_format_locale']
    )
    fields_dict['tax_amount']['value'] = standard_value
    fields_dict['tax_amount']['formatted_value'] = formatted_value
    ```
15. **compare\_values(value1, value2)**

    ```python
    result = compare_values(10, "10")
    ```
16. **create\_document\_task( user, document\_data, title, description, priority,** **assigned\_to\_user\_id, assigned\_to\_group\_id, send\_email: bool)**

    ```python
    herkunftsland = get_field_value(document_data, 'herkunftsland', None)
    eu_country_codes = [
        "AT",
        "BE",
        "BG",
        "CY",
        "CZ",
        "DE",
        "DK",
        "EE",
        "ES",
        "FI",
        "FR",
        "GR",
        "HR",
        "HU",
        "IE",
        "IT",
        "LT",
        "LU",
        "LV",
        "MT",
        "NL",
        "PL",
        "PT",
        "RO",
        "SE",
        "SI",
        "SK",
    ]

    is_task_created = document_data["document_json"].get("country_check_task_created", False)

    if herkunftsland:
        if herkunftsland in eu_country_codes:
            set_field_value(document_data, "herkunftsland_checkbox", True)
        else:
            set_field_value(document_data, "herkunftsland_checkbox", False)
            if not is_task_created:
                create_document_task(user, document_data, "Herkunftsland außerhalb der EU", "Die Gelangensbestätigung kommt von einem Land außerhalb der EU. Bitte das MRN-Dokument anhängen.", "high", 1007, None, False)
                document_data["document_json"]["country_check_task_created"] = True
    else:
        set_field_value(document_data, "herkunftsland_checkbox", False)
    ```
17. **set\_document\_sub\_org\_id(document\_data, sub\_org\_id)**

    ```python
    location_id = get_field_value(document_data, "purchase_order_location_id")
    current_sub_org_id = document_data["document_json"]["sub_org_id"]
    sub_org_id = "3b5d42f5-388e-4dd6-926b-e4db476d41bf"
    po_type = get_field_value(document_data, "po_type")

    document_data["document_json"]["location_id"] = location_id

    if po_type and po_type == "do":
        sub_org_id = "f600527f-cab2-4362-ad95-1b3e1a50b9fe"
    elif location_id:
        if location_id == "AF":
            sub_org_id = "72eeb6cc-6d74-4f2e-ad8c-9ef2b8295291"
        elif location_id == "FR":
            sub_org_id = "e3fffe7b-99cb-46d6-a60b-9b99bb7b629f"
        elif location_id == "ED":
            sub_org_id = "333afb57-01fc-49f5-b0ef-55e248c8536d"
        elif location_id == "CB":
            sub_org_id = "d08b607f-1a45-450a-ab7d-4db06caa0d11"
        elif location_id == "DA":
            sub_org_id = "a43f3111-7023-416a-9bda-698237a346cd"
        elif location_id == "GU":
            sub_org_id = "dfbf062f-d0f7-4fee-81d2-035a1ccb8817"
        elif location_id == "GF":
            sub_org_id = "e72d74e9-cabe-4a69-bd69-b46461de9760"
        elif location_id == "SY":
            sub_org_id = "bf425eee-142b-4db8-b1af-59624a18bfe3"
        elif location_id == "TR":
            sub_org_id = "af61a5b4-2f25-4b9e-85a5-f86b0d677698"
        elif location_id == "MI":
            sub_org_id = "ae6a3209-0d34-43b9-860a-77489c8bc493"
        elif location_id == "ID":
            sub_org_id = "c5b918af-09d5-4ff8-ae37-9e868b229f43"
        elif location_id == "FV":
            sub_org_id = "04a830fe-6e6a-49f9-8c2f-fcdda1cd5254"
        elif location_id == "HA":
            sub_org_id = "6384766d-d40a-450a-b78e-cf29700bcc61"
        elif location_id == "NF":
            sub_org_id = "832bdee2-d924-4c95-bb24-b0276db2dd2f"
        elif location_id == "CG":
            sub_org_id = "58ce0620-86c5-4e77-baa5-580336067070"
        elif location_id == "NG":
            sub_org_id = "3c3b84d0-ede0-4b33-80ce-7761da939a55"
        elif location_id == "KI":
            sub_org_id = "ba0727fe-6227-47e5-a6b2-53b57437b780"
        elif location_id == "KV":
            sub_org_id = "bf5f4aff-869f-4b60-903f-2e36e49e5410"
        elif location_id == "OT":
            sub_org_id = "76fcf28a-6108-4b5a-a5cc-a9e6a5065dfd"
        elif location_id == "SU":
            sub_org_id = "b192a2c0-68df-4531-80e8-72f58933d63c"
        elif location_id == "TS":
            sub_org_id = "c8d20cd8-36e3-432f-ae36-6590c8ef2674"
        elif location_id == "VA":
            sub_org_id = "1c24f3c9-360b-4695-a139-7981af4cb471"
        elif location_id == "VR":
            sub_org_id = "49113034-e38f-4330-a693-8c2fad5958dc"
        elif location_id == "BW":
            sub_org_id = "dcce7ede-4ab9-4ebb-9b93-d7ada2f947aa"
        elif location_id == "WB":
            sub_org_id = "30a6a17b-294f-431e-a6ca-6b4f2d134b32"
        elif location_id == "LG":
            sub_org_id = "87a9ece9-88e5-4bfd-a9ef-b4b088d6545f"
        elif location_id == "WI":
            sub_org_id = "7c77692b-0cfe-4a3f-a5f8-8d8f8bb047dc"
        elif location_id == "YM":
            sub_org_id = "55fb1d81-3214-4c5f-acd8-9d5b06e44017"
        elif location_id == "AU":
            sub_org_id = "f2663c99-dd98-4070-83df-38a7c7ece5dd"
        elif location_id == "OS":
            sub_org_id = "02057d6b-8de4-4869-b0bd-1ae4087bac71"
        elif location_id == "CT":
            sub_org_id = "919c836e-caeb-48b3-a091-516a5c7f3ab0"
        elif location_id == "HX":
            sub_org_id = "9b83d84f-fd95-4bf2-a886-c6bfca31b867"
        elif location_id == "SJ":
            sub_org_id = "6d25b0d1-fb25-42e5-80a7-3baa8d505a5a"
        elif location_id == "SS":
            sub_org_id = "c13b0a91-3c85-408b-b0df-c24fc0160eef"
        elif location_id == "AB":
            sub_org_id = "c6aaaf24-0dcc-4776-8005-98eb47d84d06"
        elif location_id == "BH":
            sub_org_id = "d97b854a-8b70-4430-a849-3e4e0733ea15"
        elif location_id == "DM":
            sub_org_id = "8c744808-c171-4724-925b-2df399dcc21e"
        elif location_id == "MT":
            sub_org_id = "72606886-e9ff-40f0-8eea-ebb6096bb84f"

    if sub_org_id != current_sub_org_id:
        document_data["document_json"]["sub_org_id4"] = sub_org_id
        set_document_sub_org_id(document_data, sub_org_id)
    ```
18. **get\_user\_by\_id(user\_id)**

    ```python
    user_dict = {}
    for line in usercost.splitlines():
        try:
            user_dict[line.split(";")[0]] = line.split(";")[1]
        except:
            pass

    requester   = get_field_value(document_data, 'requester', None)
    cost_center = get_field_value(document_data, 'cost_center', None)
    if requester and not cost_center:
        requester_mail = str(get_user_by_id(str(requester)).email.lower())
        if requester_mail in user_dict.keys():
            set_field_value(document_data, "cost_center", user_dict[requester_mail])
        else:
            set_field_value(document_data, "cost_center", "Requester e-mail not in list")
    ```
19. **get\_group\_by\_id(group\_id)**

    ```python
    assigned_to_group_id       = str(document_json["assigned_to_group_id"])
    group_name  = str(get_group_by_id(assigned_to_group_id))
    group_name_short = group_name[len(group_name.split("_")[0])+len(group_name.split("_")[1])+2:]
    group_name_shorter = group_name_short[:31]

    set_field_value(document_data, "grupo_aprobacion", group_name_shorter)
    set_field_value(document_data, "grupo_aprobacion_full", group_name_short)

    Date_of_approval = get_field_value(document_data, 'date_of_approval', None)
    try:
        first_approver       = document_json['first_approver']
    except:
        first_approver       = None

    if first_approver:
        first_approver_name  = str(get_user_by_id(first_approver).first_name+" "+get_user_by_id(first_approver).last_name) 
        set_date_value(document_data, "date_of_approval", None, add_days=0)
        set_field_value(document_data, "preapproved", True)
        set_field_value(document_data, "the_first_approver", first_approver_name)
    ```
20. **add\_table\_column(table, col\_name, default\_value=None)**

    ```python
    table = tables_dict.get("ORDER_CONFIRMATION_TABLE")

    if table:
        add_table_column(table, "PROMISED_DELIVERY_DATE")

    if promissed_delivery_date and table:
        pdd_field = fields_dict["promised_delivery_date"]
        rows = table.get("rows", [])
        for row in rows:
            for col in row.get("columns", []):
                if col["name"].upper() == "PROMISED_DELIVERY_DATE":
                    current_value = col.get("value")
                    col["is_mapped"] = True
                    #if not current_value or len(current_value) != 10 and '.' not in current_value:
                    if not current_value:
                        col["value"] = pdd_field["value"]
                        col["formatted_value"] = pdd_field["formatted_value"]
                    break
    ```
21. **get\_column\_value(row, column\_name, default\_value=None, is\_clean=False)**

    ```python
    table = tables_dict.get("INVOICE_TABLE")
    if table:
        
        unit_price_per = None
        for row in table['rows']:
            unit = get_column_value(row, "UNIT")
            if unit == 'TO':
                add_table_column(table, "UNIT_PRICE_PER")
                set_column_amount_value(document_data, row, "UNIT_PRICE_PER", str(1000))
    ```
22. **set\_column\_value(row, column\_name, value)**

    ```python
    supplier_id = get_field_value(document_data, "supplier_id", "")

    quote_table = tables_dict["QUOTE_TABLE"]

    for row in quote_table.get('rows', []):
        set_column_value(row,"SUPPLIER_ID", supplier_id)
    ```
23. **set\_column\_date\_value(document\_data, row, column\_name, value, add\_days=0)**

    ```python
    set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
    ```
24. **set\_column\_amount\_value(document\_data, row, column\_name, value)**

    ```python
    supplier_id = get_field_value(document_data, 'supplier_id', None)
    table = tables_dict.get("ORDER_CONFIRMATION_TABLE")

    if table and supplier_id == 'AVE626022':
        for row in table['rows']:
            ve = get_column_value(row, "VE")
            quantity = get_column_value(row, "QUANTITY")

            if ve and quantity:
                quantity = float(quantity) / 1000
                set_column_amount_value(document_data, row, "QUANTITY", str(quantity))
    ```
25. **remove\_rows\_from\_table(document\_data, table\_name, count, start)**

    ```python
    if __name__ == '__main__':
        count = 1
        start = 1
        remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
    ```
26. **remove\_all\_rows\_except\_one\_from\_table(document\_data, line\_number)**

    ```python
    supplier_id = get_field_value(document_data, 'supplier_id', None)
    total_net_amount = document_data["fields_dict"]["total_net_amount"]

    line_number = 1

    if supplier_id == '600283':
        if tables_dict.get('INVOICE_TABLE'):
            remove_all_rows_except_one_from_table(document_data, line_number)
            for row in tables_dict['INVOICE_TABLE']['rows']:
                for col in row['columns']:
                    if col['name'] == 'QUANTITY':
                        col['value'] = "1.00"
                        col['formatted_value'] = "1,00"
                    if col['name'] == 'UNIT_PRICE':
                        col['value'] = total_net_amount["value"]
                        col['formatted_value'] = total_net_amount["formatted_value"]
                    if col['name'] == 'NET_AMOUNT':
                        col['value'] = total_net_amount["value"]
                        col['formatted_value'] = total_net_amount["formatted_value"]
    ```
