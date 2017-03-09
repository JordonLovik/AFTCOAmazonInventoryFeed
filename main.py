###Step 1 retrieve files 01_Products.xml and 01_Inventory.txt from fullcirle at location: /v3/ex_web2/s
###Step 2 move these files into data folder in the project AFTCOInventoryParser at location: C:\Users\jordon.AFTCO\PycharmProjects\AFTCOInventoryParser\data
###Step 3 run script
###Step 4 review outputin excel
###Step 5 upload to Amazon
def main():
    import os
    from xml.etree import ElementTree

    inventoryfile = open('C:/Users/jordon.AFTCO/PycharmProjects/AFTCOInventoryParser/data/01_inventory.txt', 'r')
    searchfile = open('C:/Users/jordon.AFTCO/PycharmProjects/AFTCOInventoryParser/data/key.txt', 'r')
    amazonfile = open('C:/Users/jordon.AFTCO/PycharmProjects/AFTCOInventoryParser/data/AmazonUpload.txt', 'w')
    inventoryread = inventoryfile.readlines()
    keysread = searchfile.readlines()

    inventory = []
    keys = []

    def searchkeyfile(keylist, seachlist):
        """takes in one key list and returns the
                matches in search list as a list"""
        outputstring = []
        for key in keylist:  # for each key sku seachlist
            for x in seachlist:
                if x[0] == (key[0]):
                    # outputstring = key[0] + '\t' + x[1]
                    outputstring.append(x)
                else:
                    pass
        return outputstring
    def searchcombine(keylist, seachlist):
        """takes in one key list and returns the
                matches in search list as a list"""
        outputstring = []
        for key in keylist:  # for each key sku seachlist
            for x in seachlist:
                if x[0] == (key[0]):
                    outstring = key[0], key[2], x[1], key[1]
                    outputstring.append(outstring)
                else:
                    pass
        return outputstring
    #append inventoryread to inventory list
    for i in inventoryread: #split strings into list
        i.strip()
        t = i.split()
        for items in t:
            output = t[0] + t[2] + t[1]
            output2 = t[3]
            output3 = [output , output2]
            inventory.append(output3)
    #append keysread to keys list
    for j in keysread:
        keys.append(j.split())

    xml_data = ElementTree.parse('C:/Users/jordon.AFTCO/PycharmProjects/AFTCOInventoryParser/data/01_products.xml')
    product = xml_data.findall('product')

    product_parsed = [] #will hold parsed product data
    for items in product: #parses xml data
        try:
            sku = items.find('avail_sizes/sku').text
        except AttributeError:
            pass
        try:
            upc = items.find('avail_sizes/upc').text
        except AttributeError:
            pass
        try:
            msrp = items.find('msrp').text
        except AttributeError:
            pass
        temp = [sku, upc, msrp]
        product_parsed.append(temp)# holds list of product data

    inventoryoutput = searchkeyfile(keys, inventory)
    print(inventoryoutput)
    productoutput = searchkeyfile(keys, product_parsed)
    print(productoutput)
    print('\n')
    outputfinal = searchcombine(productoutput, inventoryoutput)
    print(outputfinal)
    b = [] #inicialize b
    for c in outputfinal:
        if b == c:#if c is equal to the previous list item dont write
            pass
        else:
            concant = c[0] + '\t' + c[1] + '\t' + c[2] + '\n'
            amazonfile.write(concant)
        b = [] #reset b membory
        b = c #give b the value of current list
        #amazonfile.write('\n')
    amazonfile.close()

#product_parsed is ready for combine function
if __name__ == "__main__":
    main()