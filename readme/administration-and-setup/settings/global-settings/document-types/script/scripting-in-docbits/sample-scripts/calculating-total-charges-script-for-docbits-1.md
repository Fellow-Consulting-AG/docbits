# Script de Cálculo de Encargos Totais para Docbits

O script "Calculating Total Charges" automatiza o processo de soma de vários encargos e valores adicionais dentro de documentos de fatura. Este guia orienta você através da configuração, lógica e aplicação do script para garantir cálculos precisos de encargos totais em seus documentos.

### Propósito

Este script visa fornecer uma forma dinâmica de calcular os encargos totais em uma fatura somando diferentes tipos de encargos, como encargos base, frete (Fracht) e embalagem (Verpackung). Em seguida, atualiza o campo de encargos totais da fatura com a soma calculada, garantindo informações de faturamento precisas.

### Visão Geral do Script

O script recupera valores de campos especificados, converte-os em números de ponto flutuante, soma-os e então atualiza o campo `total_charges` com o resultado. Se o campo `total_charges` não existir, o script cria este campo e define seu valor de acordo.

#### Trecho de Código

```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Initialize total to 0
total = 0

# Add fracht to total if it exists
if fracht:
    fracht = float(fracht)
    total += fracht

# Add verpackung to total if it exists
if verpackung:
    verpackung = float(verpackung)
    total += verpackung

# Formatting the total to two decimal places
formatted_total = "{0:.2f}".format(total)

# Checking if the total_charges field exists and updating or creating accordingly
if 'total_charges' not in fields_dict:
    new_field = create_new_field('total_charges', formatted_total)
    fields_dict['total_charges'] = new_field
    document_json['fields'].append(new_field)
else:
    set_field_value(fields_dict, 'total_charges', formatted_total)
```
