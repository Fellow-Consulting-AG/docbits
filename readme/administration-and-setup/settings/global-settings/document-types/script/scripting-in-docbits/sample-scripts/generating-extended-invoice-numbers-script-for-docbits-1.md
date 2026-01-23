# Script de Geração de Números de Fatura Estendidos para Docbits

Este documento detalha o script "Generating Extended Invoice Numbers", que automatiza a criação de números de fatura estendidos no Docbits. Números de fatura estendidos combinam múltiplos identificadores de documentos, como o ID da fatura e o número do pedido de compra, em um único identificador abrangente. Este script melhora a rastreabilidade de documentos e simplifica a manutenção de registros.

### Propósito

O propósito deste script é otimizar o processo de geração de números de fatura estendidos concatenando automaticamente o ID da fatura e o número do pedido de compra, proporcionando assim um identificador unificado e único para cada documento de fatura.

### Visão Geral do Script

O script verifica a presença dos campos ID da fatura e número do pedido de compra dentro do documento, concatena seus valores se ambos estiverem presentes (separados por um hífen), e atualiza ou cria um novo campo para armazenar o valor combinado.

#### Trecho de Código

```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Combining invoice ID and purchase order number with a hyphen separator
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check if there is an extended number to set
if extended_number:
    # Updating the 'invoice_extended_number' field with the combined value
    if not 'invoice_extended_number' in fields_dict:
        new_field = create_new_field('invoice_extended_number', extended_number)
        fields_dict['invoice_extended_number'] = new_field
        document_json['fields'].append(new_field)
    else:
        set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```
