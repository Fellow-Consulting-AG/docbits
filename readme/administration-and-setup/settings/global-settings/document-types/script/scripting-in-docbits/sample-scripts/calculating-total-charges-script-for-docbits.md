# Skrypt Obliczania Całkowitych Opłat dla DocBits

### Przegląd

Skrypt „Calculating Total Charges" jest istotnym narzędziem automatyzacji w DocBits, zaprojektowanym w celu uproszczenia procesu obliczania łącznych opłat na fakturze. Automatycznie sumuje wszystkie pozycje zawierające słowo „charge" w ich nazwie, zapewniając dokładne i efektywne przetwarzanie danych finansowych.

### Cel

Głównym celem tego skryptu jest automatyzacja obliczania łącznych opłat na dokumencie faktury poprzez sumowanie wartości wszystkich pól zawierających „charge" w nazwie. To zmniejsza liczbę błędów przy ręcznym wprowadzaniu danych i przyspiesza obieg dokumentów.

### Implementacja Skryptu

#### Fragment Kodu

```python
# Calculate total charges by summing all fields containing 'charge' in their name
total_charges = 0
for field_name in fields_dict:
    if 'charge' in field_name.lower():
        total_charges += get_field_value(fields_dict, field_name, 0)

# Set the total charges field
set_field_value(fields_dict, 'total_charges', total_charges)
```
