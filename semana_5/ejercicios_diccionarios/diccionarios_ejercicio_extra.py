"""Dada una lista de ventas con la siguiente información:
date
customer_email
items
Y cada item teniendo la siguiente información:
name
upc
unit_price
Cree un diccionario que guarde el total de ventas de cada UPC."""

sales =[
    {
        "date":"02/02/2024",
        "customer_email": "lperez@gmail.com",
        "items":[
            {
                "name":"laptop",
                "upc":"ITEM-200",
                "unit_price":200
            },
            {
                "name":"phone",
                "upc":"ITEM-300",
                "unit_price":150
            },
            {
                "name":"mouse",
                "upc":"ITEM-400",
                "unit_price":80
            }
        ]
    },
    {
        "date":"04/03/2024",
        "customer_email":"lperez@gmail.com",
        "items":[
            {
                "name":"laptop",
                "upc":"ITEM-200",
                "unit_price":200
            },
            {
                "name":"mouse",
                "upc":"ITEM-400",
                "unit_price":80 
            }
        ]
    },
    {
        "date":"04/04/2024",
        "customer_email":"kgomez@gmail.com",
        "items":[
            {
                "name":"laptop",
                "upc":"ITEM-200",
                "unit_price":200

            },
            {
                "name":"phone",
                "upc":"ITEM-300",
                "unit_price":150
            }
        ]
    }
]
#result={}
result=dict()
#ITEM-200 ->total = 600
#ITEM-300 ->total = 300
#ITEM-400 ->total = 160
#Nota : recordar guardar en variables los upc y los precios

for sale in sales:
    for item in sale["items"]:
        upc_codes=item["upc"]
        unit_price_total =item["unit_price"]
        if upc_codes in result:
            result[upc_codes]+=unit_price_total
        else:
            result[upc_codes]=unit_price_total
print(result)