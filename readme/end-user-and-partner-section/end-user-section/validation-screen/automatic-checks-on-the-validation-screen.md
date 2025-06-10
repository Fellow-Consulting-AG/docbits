# Automatyczne Kontrole na Ekranie Walidacji

## Przegląd

Domyślnie, określone pola w procesie walidacji pól są automatycznie sprawdzane poprzez weryfikację ich wartości za pomocą formuł opartych na innych wyekstrahowanych wartościach. Na tej stronie można znaleźć formularze używane do tych automatycznych obliczeń.

Zawsze możesz zweryfikować używaną formułę, najeżdżając kursorem na ikonę informacji.

<figure><img src="../../../.gitbook/assets/automatic_checks_1.png" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**Uwaga:**</mark> Ikona informacji jest widoczna tylko wtedy, gdy wartość została wyekstrahowana dla odpowiadającego pola.

## Formularze do automatycznych kontroli:

### Kwota netto:

```
Net amount = Tax amount * 100 / Vat rate 
```

### Stawka VAT:

```
Vat rate = Tax amount * 100 / Net amount 
```

### Kwota podatku:

```
Tax amount = Net amount + Vat rate / 100
```

### Kwota netto po obniżeniu:

```
Net amount reduced = Reduced Tax amount * 100 / Vat rate reduced
```

### Stawka VAT po obniżeniu:

```
Vat rate reduced = Reduced Tax amount * 100 / Net amount reduced
```

### Kwota podatku po obniżeniu:

```
Tax amount reduced = Reduced Tax amount + Vat rate reduced / 100
```

### Całkowita kwota netto:

```
Total net amount = Net amount + Reduced Tax amount + Net amount free
```

### Całkowita kwota netto w USA:

```
Total net amount US = Net amount + Shipping charges + Misc. charges + Additional amount
```

### Całkowita kwota podatku:

```
Total tax amount = Tax amount + Reduced Tax amount + Tax amount free 
```

### Całkowita kwota:

```
Total amount = Net amount + Tax Amount
```

<mark style="color:red;">**Uwaga:**</mark> Jeśli wyekstrahowana wartość i zweryfikowana wartość się nie zgadzają, dokument nie może być przetwarzany dalej. Pojawi się błąd **Amounts Mismatch** dla odpowiadającego pola.
