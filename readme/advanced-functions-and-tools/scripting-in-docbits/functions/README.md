# Funções

## **Documentação Funcional**

Este módulo contém funções para manipular dados de documentos e realizar várias operações relacionadas a campos de documentos.

## **Funções**

### **set\_field\_value()**

Define o valor de um campo nos dados do documento.

```python
po_number = get_field_value(fields_dict, 'purchase_order', None)
if not po_number:
    po_number = ''
    
if po_number:
    set_field_value(fields_dict, "invoice_sub_type", 'Purchase Invoice')
else:
    set_field_value(fields_dict, "invoice_sub_type", 'Cost Invoice')
```

#### Parâmetros:

<table><thead><tr><th width="177">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome do campo a ser definido</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>O valor a ser definido para o campo</td></tr></tbody></table>

### **set\_date\_value()**

Define o valor de um campo de data nos dados do documento.

```python
invoice_date = get_field_value(document_data, 'invoice_date', None)
    
if not document_json.get("script_executed", False):
    if invoice_date:
        set_date_value(document_data, "accounting_date", invoice_date)
        document_json["script_executed"] = True
```

#### Parâmetros:

<table><thead><tr><th width="229">Nome</th><th width="138">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome do campo a ser definido</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O valor da data a ser definido no formato ISO (por exemplo, "2020-12-31").</td></tr><tr><td>add_days (opcional)</td><td><code>int</code></td><td>Adiciona dias adicionais à data dada<br>O padrão é 0</td></tr><tr><td>skip_weekend (opcional)</td><td><code>bool</code></td><td>Ignora a data se cair no final de semana<br>O padrão é <code>False</code></td></tr></tbody></table>

### **set\_amount\_value()**

Define o valor de um campo de montante nos dados do documento.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount",str(lines_total))
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome do campo a ser definido</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O valor a ser definido para o campo (passar um número como string, por exemplo, "123456"</td></tr></tbody></table>

### **get\_field\_value()**

Obtém o valor de um campo dos dados do documento.

```python
total_amount = get_field_value(document_data, "net_amount")
lines_total = 0.0
set_amount_value(document_data, "net_amount", str(lines_total))
```

#### Parâmetros:

<table><thead><tr><th width="191">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome do campo a ser definido</td></tr><tr><td>default_value (opcional)</td><td><code>any</code></td><td>Retorna default_value se nenhum valor de campo for encontrado<br>O padrão é <code>None</code></td></tr><tr><td>is_clean (opcional)</td><td><code>bool</code></td><td>Converte o valor para maiúsculas e remove espaços extras<br>O padrão é <code>False</code></td></tr></tbody></table>

#### Retorna:

* Valor do campo especificado

### **create\_new\_field()**

Cria um novo campo com o nome e valor especificados.

```python
currency = get_field_value(document_data, 'currency', None)

if not currency:
    if 'currency' not in fields_dict:
        new_field = create_new_field('currency','')
        fields_dict['currency'] = new_field
        document_json['fields'].append(new_field)
    set_field_value(document_data, "currency", "USD")
```

#### Parâmetros:

<table><thead><tr><th width="140">Nome</th><th width="133">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>str</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>value (opcional)</td><td><code>any</code></td><td>O valor inicial para o campo<br>O padrão é <code>""</code></td></tr></tbody></table>

#### Retorna:

* Dicionário do novo campo criado

### **delete\_field()**

Exclui um campo dos dados do documento.

```python
field_amount = get_field_value(document_data, field_name)
    if not field_amount:
        delete_field(document_data, fields_dict, field_name)
    else:
        field_amount = float(field_amount)
        if field_amount == 0:
            delete_field(document_data, fields_dict, field_name)
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome do campo a ser excluído</td></tr></tbody></table>

#### Retorna:

* Document\_data como json e como dict após o campo ser excluído

### **set\_is\_required()**

Define o atributo 'is\_required' de um campo nos dados do documento.

```python
net_amount = get_field_value(document_data, "net_amount", None)
if net_amount:
    set_is_required(document_data, "tax_country", True)
    set_is_required(document_data, "tax_code_without_country", True)
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome do campo a ser definido</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>O valor a ser definido para o campo</td></tr></tbody></table>

### **set\_force\_validation()**

Define o atributo 'force\_validation' de um campo nos dados do documento.

```python
if supplier_id in supplier_to_check:
    set_force_validation(document_data, 'purchase_order', True, reset_validation=reset_validation)
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome do campo a ser definido</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>O valor a ser definido para o campo</td></tr><tr><td>reset_validation (opcional)</td><td><code>bool</code></td><td>Define o atributo "is_validated" para o valor especificado<br>O padrão é <code>False</code></td></tr></tbody></table>

### **set\_field\_as\_invalid()**

Marca um campo na tela de validação como inválido e o destaca.

```python
if not document_date:
    set_field_as_invalid(document_data, "document_date", "Es ist kein Datum vorhanden", "INVALID_VALUE")
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome do campo a ser marcado como inválido</td></tr><tr><td>message<mark style="color:red;">*</mark></td><td><code>string</code></td><td>A mensagem de validação para o campo</td></tr><tr><td>code (opcional)</td><td><code>string</code></td><td><p>Código de erro para a validação</p><p>O padrão é <code>None</code></p></td></tr></tbody></table>

### **set\_field\_attribute()**

Define um atributo personalizado de um campo nos dados do documento.

```python
if purchase_order:
    if po_supplier_id != invoice_supplier_id:
        set_field_as_invalid(document_data, "supplier_name", "Supplier is different from PO supplier")
    else:
        set_field_attribute(document_data, "supplier_name", "is_valid", True)
        set_field_attribute(document_data, "supplier_name", "validation_message","")
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>field_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome do campo a ser definido</td></tr><tr><td>attribute_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome do atributo a ser definido</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>O valor a ser definido para o atributo</td></tr></tbody></table>

### **is\_supplier\_valid()**

Verifica se um fornecedor é válido com base nos critérios fornecidos.

```python
bool = is_supplier_valid(user, {"name": "Supplier Inc."})
```

#### Parâmetros:

<table><thead><tr><th width="203">Nome</th><th width="216">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>user<mark style="color:red;">*</mark></td><td><code>UserAuthentication</code></td><td>O usuário autenticado</td></tr><tr><td>filter_data_json<mark style="color:red;">*</mark></td><td><code>json</code></td><td>Critérios de filtragem para validar o fornecedor</td></tr><tr><td>sub_org_id (opcional)</td><td><code>string</code></td><td>ID de sub-organização opcional para filtragem<br>O padrão é <code>None</code></td></tr></tbody></table>

#### Retorna:

* True, se o usuário for válido
* False se o usuário não for válido

### **get\_document\_content()**

Decodifica os dados do documento e os retorna como uma string.

```python
document_content = get_document_content(doc)
if document_content:
    document_content = document_content.lower()
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr></tbody></table>

#### Retorna:

* Dados do documento como uma string.

### **update\_document\_status\_with\_doc\_id()**

Atualiza o status de um documento com um ID específico para o status dado.

```python
genehmigung_user_1 = get_field_value(document_data, 'genehmigung_user_1', None)

if genehmigung_user_1 != "LEER":
    update_document_status_with_doc_id(document_json['doc_id'], user, document_json['org_id'], "validated_pending_approval")
```

#### Parâmetros:

<table><thead><tr><th width="228">Nome</th><th width="216">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>doc_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O ID do documento a ser atualizado</td></tr><tr><td>user<mark style="color:red;">*</mark></td><td>ou <code>user ID</code> ou <code>UserAuthentication</code> object</td><td>O usuário que está realizando a atualização</td></tr><tr><td>org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O ID da organização à qual o documento pertence</td></tr><tr><td>status<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O novo status do documento</td></tr><tr><td>message (opcional)</td><td><code>string</code></td><td>Mensagem opcional associada à atualização de status<br>O padrão é <code>None</code></td></tr><tr><td>doc_classification_class (opcional)</td><td><code>string</code></td><td>Classe de classificação de documento opcional<br>O padrão é <code>None</code></td></tr></tbody></table>

### **get\_lov\_values()**

Obtém os valores LOV de um org\_id e chave específicos.

```python
reverse_charge_to_check = get_lov_values(org_id, 'Kosten', return_type="list_of_values")
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O ID da organização à qual o documento pertence</td></tr><tr><td>key<mark style="color:red;">*</mark></td><td><code>string</code></td><td>A chave da Lista de Valores necessária</td></tr><tr><td>return_type (opcional)</td><td><code>string</code></td><td>O tipo no qual os dados devem ser retornados<br>O padrão é <code>'list_of_objects'</code></td></tr><tr><td>sub_org_id (opcional)</td><td><code>string</code></td><td>ID de sub-organização opcional para filtragem<br>O padrão é <code>None</code></td></tr></tbody></table>

#### Retorna:

* Valores LOV como uma lista de objetos ou como uma lista.

### **format\_decimal\_to\_locale()**

Formata um valor decimal para o formato en\_US.UTF-8.

```python
standard_value = "{0:.2f}".format(total)
formatted_value = format_decimal_to_locale(
    standard_value, document_json['amount_format_locale']
)
```

#### Parâmetros:

<table><thead><tr><th width="208">Nome</th><th width="187">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>value<mark style="color:red;">*</mark></td><td><code>float, decimal.Decimal, str</code></td><td>O ID da organização à qual o documento pertence</td></tr><tr><td>to_locale (opcional)</td><td><code>string</code></td><td>O tipo no qual os dados devem ser retornados<br>O padrão é <code>'en_US.UTF-8'</code></td></tr><tr><td>max_decimal_places (opcional)</td><td><code>int</code></td><td>ID de sub-organização opcional para filtragem<br>O padrão é <code>4</code></td></tr><tr><td>min_decimal_places (opcional)</td><td><code>int</code></td><td>O mínimo de casas decimais que devem ser consideradas<br>O padrão é <code>2</code></td></tr></tbody></table>

* value: O valor que deve ser formatado.
* to\_locale (opcional): O formato no qual o valor é transformado.
* max\_decimal\_places (opcional): O máximo de casas decimais que devem ser consideradas.
* min\_decimal\_places (opcional): O mínimo de casas decimais que devem ser consideradas.

#### Retorna:

* O valor formatado.

### **compare\_values()**

Compara dois valores para igualdade, lidando com vários tipos de dados.

```python
result = compare_values(10, "10")
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>value1<mark style="color:red;">*</mark></td><td><code>any</code></td><td>O primeiro valor a comparar</td></tr><tr><td>value2<mark style="color:red;">*</mark></td><td><code>any</code></td><td>O segundo valor a comparar</td></tr></tbody></table>

#### Retorna:

* True se os valores forem iguais e False se forem diferentes

### **create\_document\_task()**

Cria uma tarefa, atribui-a a um usuário ou grupo, define a prioridade e, opcionalmente, envia um e-mail.

```python
if not is_task_created:
            create_document_task(user, document_data, "Herkunftsland außerhalb der EU", "Die Gelangensbestätigung kommt von einem Land außerhalb der EU. Bitte das MRN-Dokument anhängen.", "high", 1007, None, False)
            document_data["document_json"]["country_check_task_created"] = True
```

#### Parâmetros:

<table><thead><tr><th width="216">Nome</th><th width="217">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>user<mark style="color:red;">*</mark></td><td>ou <code>user ID</code> ou <code>UserAuthentication</code> object</td><td>O usuário que está realizando a atualização</td></tr><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>title<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O título da tarefa</td></tr><tr><td>description<mark style="color:red;">*</mark></td><td><code>string</code></td><td>A descrição da tarefa</td></tr><tr><td>priority<mark style="color:red;">*</mark></td><td><code>string</code></td><td>A prioridade da tarefa</td></tr><tr><td>assigned_to_user_id<mark style="color:red;">*</mark></td><td><code>int</code></td><td>O id do usuário ao qual a tarefa deve ser atribuída</td></tr><tr><td>assigned_to_group_id<mark style="color:red;">*</mark></td><td><code>int</code></td><td>O id do grupo ao qual a tarefa deve ser atribuída</td></tr><tr><td>send_email<mark style="color:red;">*</mark></td><td><code>bool</code></td><td>Determina se um e-mail deve ser enviado ou não</td></tr></tbody></table>

#### Retorna:

* Dict que indica se o processo foi bem-sucedido ou não

### **set\_document\_sub\_org\_id()**

Define o sub\_org\_id dos dados do documento especificado.

```python
if sub_org_id != current_sub_org_id:
    document_data["document_json"]["sub_org_id4"] = sub_org_id
    set_document_sub_org_id(document_data, sub_org_id)
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>sub_org_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>ID de sub-organização opcional para filtragem</td></tr></tbody></table>

### **get\_user\_by\_id()**

Obtém o usuário com o ID de usuário correspondente.

```python
requester_mail = str(get_user_by_id(str(requester)).email.lower())
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>user_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O ID do usuário</td></tr></tbody></table>

#### Retorna:

* O usuário com o ID de usuário correspondente

### **get\_group\_by\_id()**

Obtém o grupo com o ID de grupo correspondente.

```python
group_name  = str(get_group_by_id(assigned_to_group_id))
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>group_id<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O ID do grupo</td></tr></tbody></table>

#### Retorna:

* O grupo com o ID de grupo correspondente

### **add\_table\_column()**

Adiciona uma coluna à tabela especificada.

```python
table = tables_dict.get("ORDER_CONFIRMATION_TABLE")

if table:
    add_table_column(table, "PROMISED_DELIVERY_DATE")
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>table<mark style="color:red;">*</mark></td><td><code>string</code></td><td>A tabela onde a coluna deve ser adicionada</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome da coluna</td></tr><tr><td>default_value (opcional)</td><td><code>any</code></td><td><p>O valor inicial para o campo</p><p>O padrão é <code>None</code></p></td></tr></tbody></table>

### **get\_column\_value()**

Obtém o valor de uma coluna especificada.

```python
for row in table['rows']:
        unit = get_column_value(row, "UNIT")
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>A linha onde o valor está localizado</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome da coluna</td></tr><tr><td>default_value (opcional)</td><td><code>any</code></td><td>O valor inicial para o campo<br>O padrão é <code>None</code></td></tr><tr><td>is_clean (opcional)</td><td><code>bool</code></td><td>Converte o valor para maiúsculas e remove espaços extras<br>O padrão é <code>False</code></td></tr></tbody></table>

#### Retorna:

* O valor da coluna especificada

### **set\_column\_value()**

Define o valor de uma coluna especificada.

```python
supplier_id = get_field_value(document_data, "supplier_id", "")

quote_table = tables_dict["QUOTE_TABLE"]

for row in quote_table.get('rows', []):
    set_column_value(row,"SUPPLIER_ID", supplier_id)
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>A linha onde o valor está localizado</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome da coluna</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>any</code></td><td>O valor que será definido na localização especificada</td></tr></tbody></table>

#### Retorna:

* True se a alteração foi bem-sucedida

### **set\_column\_date\_value()**

Define o valor de data de uma coluna especificada.

```python
set_column_date_value(document_data, row, "DELIVERY_DATE", "2020-12-31", add_days=2)
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>A linha onde o valor está localizado</td></tr><tr><td>col_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome da coluna</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O valor da data a ser definido no formato ISO (por exemplo, "2020-12-31")</td></tr><tr><td>add_days (opcional)</td><td><code>int</code></td><td>Adiciona dias adicionais à data dada<br>O padrão é <code>2</code></td></tr></tbody></table>

### **set\_column\_amount\_value()**

* Converte o valor para string e define o valor para a coluna
* Define o conteúdo da coluna para o valor
* Formata o valor de acordo com a localidade

```python
quantity = float(quantity) / 1000
set_column_amount_value(document_data, row, "QUANTITY", str(quantity))
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>row<mark style="color:red;">*</mark></td><td><code>string</code></td><td>A linha onde o valor está localizado</td></tr><tr><td>column_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome da coluna</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O valor a ser definido para o campo (passar um número como string, por exemplo, "123456")</td></tr></tbody></table>

### **remove\_rows\_from\_table()**

Remove linhas da tabela especificada.

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>table_name<mark style="color:red;">*</mark></td><td><code>string</code></td><td>O nome da tabela</td></tr><tr><td>count<mark style="color:red;">*</mark></td><td><code>int</code></td><td>Quantas linhas devem ser excluídas</td></tr><tr><td>start<mark style="color:red;">*</mark></td><td><code>int</code></td><td>O ponto de partida</td></tr></tbody></table>

### **remove\_all\_rows\_except\_one\_from\_table()**

Remove todas as linhas, exceto uma, da tabela especificada.

```python
count = 1
start = 1
remove_rows_from_table(document_data,"INVOICE_TABLE",count,start) 
```

#### Parâmetros:

<table><thead><tr><th width="173">Nome</th><th width="176">Tipo</th><th>Descrição</th></tr></thead><tbody><tr><td>document_data<mark style="color:red;">*</mark></td><td><code>dictionary</code></td><td>Os dados do documento contendo informações de campo</td></tr><tr><td>line_number<mark style="color:red;">*</mark></td><td><code>int</code></td><td>O número da linha que não deve ser removida</td></tr></tbody></table>

## Funções Internas do Python

Você também pode utilizar algumas das funções internas do python:

* abs(): Retorna o valor absoluto de um número.
* len(): Retorna o comprimento (número de itens) de um objeto, como uma lista ou string.
* isinstance(): Verifica se um objeto é uma instância de uma classe ou tipo específico.
* print(): Imprime a saída no console.
* round(): Arredonda um número de ponto flutuante para um número especificado de casas decimais.
* str\_to\_bool(): Converte uma string em um valor booleano (True ou False).
* type(): Retorna o tipo de um objeto.
* dict(): Cria um objeto dicionário.
* list(): Cria um objeto lista.
* str(): Converte um valor em uma string.
* float(): Converte um valor em um número de ponto flutuante.
* int(): Converte um valor em um inteiro.

Para mais detalhes, visite a documentação oficial do Python: [Funções Internas](https://docs.python.org/3.12/library/functions.html).

## Funções da Classe String

Você também pode usar essas funções especificamente para trabalhar com strings:

* lower(): Converte todos os caracteres em uma string para minúsculas.
* upper(): Converte todos os caracteres em uma string para maiúsculas.
* split(): Divide uma string em uma lista com base em um delimitador (por exemplo, espaço ou vírgula).
* startswith(): Verifica se uma string começa com um prefixo especificado.
* endswith(): Verifica se uma string termina com um sufixo especificado.
* strip(): Remove qualquer espaço em branco no início ou no final de uma string.

## Funções do Módulo Math do Python

Essas funções fazem parte do módulo math e são úteis para operações matemáticas:

* floor(): Retorna o maior inteiro menor ou igual a um número dado.
* ceil(): Retorna o menor inteiro maior ou igual a um número dado.

Para mais informações, confira a documentação oficial do Python: [Funções do Módulo Math](https://docs.python.org/3/library/math.html).

## Função de Expressão Regular

* re.search(): Procura um padrão dentro de uma string e retorna a primeira correspondência.

Veja mais detalhes aqui: [Documentação re.search](https://docs.python.org/3/library/re.html#re.search).

## Funções Externas

Aqui estão algumas funções úteis de bibliotecas externas:

* deepcopy(): Cria uma cópia de um objeto, incluindo objetos aninhados (do módulo copy).\
  [Documentação Deepcopy](https://docs.python.org/3/library/copy.html#copy.deepcopy).
* levenshtein\_distance(): Calcula o número de edições (inserções, exclusões, substituições) necessárias para mudar uma string em outra. Esta função está disponível na [biblioteca Jellyfish](https://jamesturk.github.io/jellyfish/functions/).

## Funções de Data e Hora

Você pode usar as seguintes funções para trabalhar com datas e horas:

* strptime(): Converte uma string em um objeto datetime com base em um formato especificado.
* strftime(): Formata um objeto datetime em uma string com base em um formato especificado.

Para mais informações, confira a documentação oficial:\
[Funções de Data e Hora](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).
