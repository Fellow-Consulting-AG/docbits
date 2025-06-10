# Automatic Checks

## Overview

By default, specific fields in the field validation process are automatically checked by verifying their values using formulas based on other extracted values. On this page, you can find the forms used for these automatic calculations.

You can always verify the used formula by hovering over the info icon.

<figure><img src="../../../.gitbook/assets/info_icon (1).png" alt="" width="113"><figcaption></figcaption></figure>

## Formulars for automatic checks:

### Net amount:

```
Net amount = Tax amount * 100 / Vat rate 
```

### Vat rate:

```
Vat Rate = Tax amount * 100 / Net amount 
```

### Tax amount:

```
Tax amount = Net amount + Vat rate / 100
```

### Net amount reduced:

```
Net amount reduced = Tax amount reduced * 100 / Vat rate reduced
```

### Vat rate reduced:

```
Vat Rate reduced = Tax Amount reduced * 100 / Net amount reduced
```

### Tax amount reduced:

```
Tax amount reduced = Net Amount reduced + Vat rate reduced / 100
```

### Total net amount:

```
Total net amount = Net amount + Net amount reduced + Net amount free
```

### Total net amount US:

```
Total net amount US = Net amount + Shipping charges + Misc. charges + Additional amount
```

### Total tax amount:

```
Total tax amount = Tax amount + Tax amount reduced + Tax amount free 
```

### Total amount:

```
Total amount = Net amount + Tax Amount
```

<mark style="color:red;">**Note:**</mark> If the extracted Value and the checked value do not match you won't be able to process your document further and get an amounts mismatch error on the corresponding value
