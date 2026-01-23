# Excluir linhas com quantidade e valor vazios

#### Parte 1: Excluir Linhas com Quantidade e Valor Vazios

Esta seção do script processa uma tabela de fatura para remover quaisquer linhas onde tanto a quantidade quanto o valor total são zero ou não fornecidos.

* **Verificar INVOICE\_TABLE:** Começa verificando se a chave `INVOICE_TABLE` existe no dicionário `tables_dict`.
* **Iterar sobre Linhas:** Para cada linha na tabela, o script inicializa flags e variáveis para determinar se as colunas `TOTAL_AMOUNT` e `QUANTITY` existem e para capturar seus valores.
* **Verificar Nomes de Colunas:** Ao iterar por cada coluna em uma linha, procura colunas chamadas `TOTAL_AMOUNT` e `QUANTITY`.
  * Se `TOTAL_AMOUNT` for encontrado, captura o valor. Se este valor não for zero, converte-o para número de ponto flutuante.
  * Da mesma forma para `QUANTITY`, capturando e convertendo o valor se não for zero.
* **Marcar Linha para Exclusão:** Após verificar ambas as colunas em uma linha, se tanto o valor total quanto a quantidade forem efetivamente zero (seja por serem zero ou por não existirem), a linha é marcada para exclusão definindo `row['is_deleted']` como `True`.

#### Parte 2: Validar Total das Linhas contra Total da Fatura

Esta seção calcula o valor total de todas as linhas em uma fatura e compara com o total reportado da fatura para validar sua consistência.

* **Inicializar Total das Linhas:** Começa definindo uma variável `lines_total` como 0.0 para acumular o valor total de todas as linhas.
* **Somar Valores das Linhas:** Itera sobre cada linha na `INVOICE_TABLE`, extraindo o `TOTAL_AMOUNT` de cada uma e adicionando ao `lines_total`.
* **Recuperar e Converter Total da Fatura:** Obtém o valor total da fatura usando uma função auxiliar `get_field_value` e converte para número de ponto flutuante.
* **Comparar Totais:** Por fim, verifica se a diferença absoluta entre o total calculado das linhas (`lines_total`) e o total reportado da fatura (`total_amount`) excede um limite de 0,05. Se sim, marca o campo de total da fatura como inválido usando outra função auxiliar `set_field_as_invalid`, citando uma discrepância.

```python
##################################################
# Delete lines with empty quantity and amount
##################################################


if tables_dict.get('INVOICE_TABLE'):
    for row in tables_dict['INVOICE_TABLE']['rows']:
        amount_col_found = False
        quantity_col_found = False
        line_amount = 0.0
        line_quantity = 0.0
        for col in row['columns']:
            if col['name'] == 'TOTAL_AMOUNT':
                amount_col_found = True
                line_amount = col.get('value', 0)
                if line_amount:
                    line_amount = float(line_amount)
            if col['name'] == 'QUANTITY':
                quantity_col_found = True
                line_quantity = col.get('value', 0)
                if line_quantity:
                    line_quantity = float(line_quantity)
            if amount_col_found and quantity_col_found:
                break
        if amount_col_found and quantity_col_found and (not line_amount and not line_quantity or (line_amount + line_quantity) == 0):
            row['is_deleted'] = True

##################################################
# End: Delete lines with empty quantity and amount
##################################################

##################################################
# Validating Line total againg invoice total
##################################################
lines_total = 0.0
# Getting Lines Total
if tables_dict.get('INVOICE_TABLE'):
    for row in tables_dict['INVOICE_TABLE']['rows']:
        line_amount = 0.0
        for col in row['columns']:
            if col['name'] == 'TOTAL_AMOUNT':
                line_amount = col.get('value', 0)
                if line_amount:
                    line_amount = float(line_amount)
                break
        lines_total += line_amount

# Getting Invoice total
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
    total_amount = float(total_amount)

# Comparing lines total with invoice total
if abs(total_amount - lines_total) > 0.05:
    set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# End: Validating Line total againg invoice total
##################################################
```

#### Resumo

O script garante efetivamente a integridade dos dados através de:

1. Remoção de linhas de dados que não contribuem para o total financeiro da fatura devido a quantidades ou valores ausentes.
2. Validação da consistência entre a soma dos valores individuais das linhas e o total geral da fatura, destacando discrepâncias para ações adicionais.

Esta automatização ajuda a manter registros financeiros precisos e pode ser crucial para sistemas como ERP que requerem dados precisos para contabilidade e relatórios financeiros.
