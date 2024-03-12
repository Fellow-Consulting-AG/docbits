# Calculation of Material and Energy Surcharges (MTZ and ETZ)

This guide provides a basic overview of how to calculate the material surcharge (MTZ) and energy surcharge (ETZ) for products or services. These surcharges are applied to account for fluctuations in material and energy costs.

## Material Surcharge (MTZ)

The material surcharge is calculated based on the current cost of materials used in the production of a product or the delivery of a service. To calculate the MTZ:

1. **Determine the base cost of materials**: This is the cost before any surcharges are applied.
2. **Apply the material surcharge rate**: This rate can vary based on contracts or current market conditions.

Example calculation:
```plaintext
Material Cost = €100
Material Surcharge Rate = 5%

MTZ = Material Cost * Material Surcharge Rate
    = €100 * 0.05
    = €5

Energy Cost = €50
Energy Surcharge Rate = 10%

ETZ = Energy Cost * Energy Surcharge Rate
    = €50 * 0.10
    = €5
```


{% swagger src="https://api.docbits.com/openapi.json" path="/table_extraction/calculate_mtz_and_etz" method="post" %}
[https://api.docbits.com/openapi.json](https://api.docbits.com/openapi.json)
{% endswagger %}
