"""
https://www.reddit.com/r/learnpython/comments/xsghab/how_to_parse_the_data_under_div_tag/
"""

import json
import re

from pprint import pprint

SAMPLE = r'''
<div class="listing-quick-lead after-lead-parent after-lead_disabled " ng-controller="quickLeadController" ng-init='setSourceRoute("listing_slug");
            setIsAfterLeadEnabled("1");
            setListingDetail("3610087",{
                "section": "1",
                "sectionTitle": "For sale",
                "isProjectParent": "" ,
                "sellerPhones": [{&quot;number&quot;:&quot;%2b%32%30%31%30%31%30%34%33%37%31%34%32&quot;}],
                "sellerPhone": "%2b%32%30%31%30%31%30%34%33%37%31%34%32",
                "financeUrl":"https://i.aqarmap.com/mortgage/?listingId=3610087",
                "userEmail": &quot;&quot;,
                "financeFeatureValue": "1",
                "listingName" : "3610087",
                "listingTitle" : "Commercial For sale in October Gardens",
                "location": "7192",
                "locationTitle": "October Gardens",
                "propertyType": "29",
                "propertyTypeTitle": "Stores",
                "price": "3010000",
                "area": "43",
                "listingUser": {
                    "sellerName" : "alkayan real estate",
                    "sellerLogo": "",
                    "sellerUrl": "/en/user/2446874",
                    "joinedData":"2021",
                    "activeListingsCount": "667",
                    "leadsCount":"0"
                }
            });
            saveListingDataInWebEngage({
                "id": "3610087",
                "listingTitle" : "Commercial For sale in October Gardens",
                "location": "7192",
                "locationTitle": "October Gardens",
                "propertyType": "29",
                "propertyTypeTitle": "Stores",
                "sectionTitle": "For sale",
                "price": "3010000",
                "currency": "EGP",
                "area": "43",
                "isCompound": "",
                "image": "https://imgs.aqarmap.com/wompoo/aqarmap-media/search-thumb/2209/63360f0410ea4733079600.jpeg",
                "description": "Commercial For sale in October Gardens",
                "paymentMethodLabel": "Cash or Installments",
                "pricePerMeter": "70000",
                "sellerRole": "Agent",
                "floor": "",
                "baths": "",
                "rooms": "",
                "yearBuilt": "",
                "finishType": "WITHOUT_FINISH",
                "publishDate": "2022-09-30 12:15:56 AM",
                "view": "Main Street",
            });
            saveAddedListingInWebEngage("2" ,{
                "listingId":"3610087",
                "listingTitle" : "Commercial For sale in October Gardens",
                "locationTitle": "October Gardens",
                "propertyTypeTitle": "Stores",
                "sectionTitle": "For sale",
                "price": "3010000",
                "area": "43",
                "image": "https://imgs.aqarmap.com/wompoo/aqarmap-media/search-thumb/2209/63360f0410ea4733079600.jpeg",
                "description": "Commercial For sale in October Gardens",
                "paymentMethodLabel": "Cash or Installments",
                "floor": "",
                "baths": "",
                "rooms": "",
                "yearBuilt": "",
                "finishType": "WITHOUT_FINISH",
                "view": "Main Street",
                "status": "Live",
                "statusId": "2",
                "address" : "حدائق أكتوبر, حدائق أكتوبر",
                "createdAt": "2022-09-29 11:31:56 PM",
                "expiresAt": "2023-03-29 12:15:56 AM",
                "phone": "%2b%32%30%31%30%31%30%34%33%37%31%34%32"
            })'>
'''

PATTERN = re.compile(r"\([^{]*(\{.*?\})\)", flags=re.M)

sanitized = re.sub(",\s*}", "}",
    SAMPLE.replace("&quot;", '"').replace("\n", ""))
#print(sanitized)
#exit()

for m in PATTERN.finditer(sanitized):
    try:
        src = m[1]
        parsed = json.loads(src)
        pprint(parsed)
    except json.JSONDecodeError as e:
        print(f"ERROR:{e}\nMatch: {m}\n{src}")
        exit()
    print()
