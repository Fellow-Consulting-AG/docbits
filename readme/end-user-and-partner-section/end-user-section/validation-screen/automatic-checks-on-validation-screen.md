# Verificações Automáticas na Tela de Validação

## Visão Geral

Por padrão, campos específicos no processo de validação de campos são verificados automaticamente, validando seus valores usando fórmulas baseadas em outros valores extraídos. Nesta página, você pode encontrar os formulários usados para esses cálculos automáticos.

Você pode sempre verificar a fórmula utilizada passando o mouse sobre o ícone de informação.

<figure><img src="../../../.gitbook/assets/automatic_checks_1.png" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**Nota:**</mark> O ícone de informação só é visível se um valor tiver sido extraído para o campo correspondente.

## Formulários para verificações automáticas:

### Valor líquido:

```
Valor líquido = Valor do imposto * 100 / Taxa de VAT 
```

### Taxa de VAT:

```
Taxa de VAT = Valor do imposto * 100 / Valor líquido 
```

### Valor do imposto:

```
Valor do imposto = Valor líquido + Taxa de VAT / 100
```

### Valor líquido reduzido:

```
Valor líquido reduzido = Valor do imposto reduzido * 100 / Taxa de VAT reduzida
```

### Taxa de VAT reduzida:

```
Taxa de VAT reduzida = Valor do imposto reduzido * 100 / Valor líquido reduzido
```

### Valor do imposto reduzido:

```
Valor do imposto reduzido = Valor do imposto reduzido + Taxa de VAT reduzida / 100
```

### Valor total líquido:

```
Valor total líquido = Valor líquido + Valor do imposto reduzido + Valor líquido isento
```

### Valor total líquido EUA:

```
Valor total líquido EUA = Valor líquido + Custos de envio + Custos diversos + Valor adicional
```

### Valor total do imposto:

```
Valor total do imposto = Valor do imposto + Valor do imposto reduzido + Valor do imposto isento 
```

### Valor total:

```
Valor total = Valor líquido + Valor do imposto
```

<mark style="color:red;">**Nota:**</mark> Se o valor extraído e o valor validado não corresponderem, o documento não poderá ser processado. Um erro de **Incompatibilidade de Valores** aparecerá para o campo correspondente.
