## Learn Flask

This is the simple REST API using flask.

## Install and run

To run this application, you need to install python3 and flask first. You can read this documentation: http://flask.pocoo.org/docs/0.12/installation/

Add executable privilege to run-server.sh

    $ chmod +x run-server.sh
    
Then run run-server.sh

    $ ./run-server.sh

## API Reference

- [GET] /items

    To show all items on the store.
- [POST] /add_item

    To insert item into store. If item name is already in the store, it will add item qty. Below are sample json format for input item.
 
json:

    {
        "name": "item name",
        "description": "item description",
        "price": (item price in integer),
        "qty": (item quantity in number),
        "category": "item category"
     }


- [DELETE] /items/{name}

    To remove item from the store. Just need to call the item name for deleting it.
    Example for deleting "buku tulis", the path is "/items/buku tulis".

