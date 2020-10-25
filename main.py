import csv


inputCSVfile = open("input\\main.csv")
input_data = csv.reader(inputCSVfile)


filteredCountry = open("output\\filteredCountry.csv", 'w')
output_writer = csv.writer(filteredCountry)
output_writer.writerow(['SKU', 'DESCRIPTION', 'YEAR', 'CAPACITY', 'URL',
                        'PRICE', 'SELLER_INFORMATION', 'OFFER_DESCRIPTION', 'COUNTRY'])
filteredDict = {}
counter = 0
for i in input_data:
    if 'usa' in i[8].lower():

        output_writer.writerow(i)
        try:
            price = float(i[5].replace('$', ''))
            if not i[0] in filteredDict:
                filteredDict[i[0]] = [price, None]
            else:
                if price < filteredDict[i[0]][0]:
                    filteredDict[i[0]][0] = price
                elif filteredDict[i[0]][1] is None:
                    filteredDict[i[0]][1] = price
                elif price < filteredDict[i[0]][1]:
                    filteredDict[i[0]][1] = price
        except:
            pass

        counter += 1
inputCSVfile.close()

lowestPrice = open("output\\lowestPrice.csv", 'w')
output_writer = csv.writer(lowestPrice)
output_writer.writerow(['SKU', 'FIRST_MINIMUM_PRICE', 'SECOND_MINIMUM_PRICE'])
for i in filteredDict:
    output_writer.writerow([i, filteredDict[i][0], filteredDict[i][1]])
