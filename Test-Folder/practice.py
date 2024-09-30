def shipping_order(**cons):
    for key, value in cons.items():
        print(f"{key}: {value}")


shipping_order(sony="PS4",
               microsoft="XBOX1",
               nintendo="NSWITCH")
