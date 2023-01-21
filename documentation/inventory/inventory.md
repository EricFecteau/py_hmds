
# Inventory

## Important memory locations
Red slot: 0x023D6B10 (NA1.0) <br /> 
Green slot: 0x023D6B14 (NA1.0) <br />
Blue slot: 0x023D6B18 (NA1.0) <br />
Rest of bag (every 4 bytes): 0x023D6B28 (NA1.0) <br />
Item price table: 0x0215AB24 (NA1.0) <br />

## Inventory data array

The inventory data array is an array of words (4 bytes) for each item that is included in each slot. The first two bytes identify the item (see item table below), the next byte is the quality (if the item is a tool or accessory see quality table below) and the last byte is the quantity of the tool.

## Item price table

The price of the item is in 12 bytes chunks per item, the first 4 bytes is the price of the item. The remaining 8 bytes is unclear.

## Item table

|      	|                      	|      	|                      	|      	|                     	|
|------	|----------------------	|------	|----------------------	|------	|---------------------	|
| 0000 	| Axe                  	| 0001 	| Fishing Rod          	| 0002 	| Hammer              	|
| 0003 	| Hoe                  	| 0004 	| Sickle               	| 0005 	| Watering Can        	|
| 0006 	| Clipper              	| 0007 	| Milker               	| 0008 	| Legendary Sword     	|
| 0009 	| Animal Medicine      	| 000A 	| Bell                 	| 000B 	| Blue Feather        	|
| 000C 	| Brush                	| 000D 	| Rucksack             	| 000E 	| Big Rucksack        	|
| 000F 	| Fodder               	| 0010 	| H. Goddess’s Gift    	| 0011 	| Fish Bones          	|
| 0012 	| Book                 	| 0013 	| Boot                 	| 0014 	| Bottle              	|
| 0015 	| Empty Can            	| 0016 	| Junk ore             	| 0017 	| Fossil of Fish      	|
| 0018 	| Title Bonus          	| 0019 	| Lithograph           	| 001A 	| W. Princess's Gift  	|
| 001B 	| Coin                 	| 001C 	| Bird Feed            	| 001D 	| Cow Miracle Potion  	|
| 001E 	| Sheep Miracle Potion 	| 001F 	| 10K Ticket           	| 0020 	| 1M Ticket           	|
| 0021 	| Music disc*          	| 0022 	| Yellow Wonderful     	| 0023 	| Orange Wonderful    	|
| 0024 	| Blue Wonderful       	| 0025 	| Green Wonderful      	| 0026 	| Indigo Wonderful    	|
| 0027 	| Purple Wonderful     	| 0028 	| Red Wonderful        	| 0029 	| White Wonderful     	|
| 002A 	| Black Wonderful      	| 002B 	| Yarn S               	| 002C 	| Yarn M              	|
| 002D 	| Yarn L               	| 002E 	| Wool S               	| 002F 	| Wool M              	|
| 0030 	| Wool L               	| 0031 	| Bronze Coin          	| 0032 	| Silver Coin         	|
| 0033 	| Gold Coin            	| 0034 	| Copper               	| 0035 	| Silver              	|
| 0036 	| Gold                 	| 0037 	| Agate                	| 0038 	| Fluorite            	|
| 0039 	| Mystrile             	| 003A 	| Orichalc             	| 003B 	| Pirate Treasure     	|
| 003C 	| Mythic Stone         	| 003D 	| Adamantite           	| 003E 	| Moon Stone          	|
| 003F 	| Alexandrite          	| 0040 	| Alexandrite          	| 0041 	| Amethyst            	|
| 0042 	| Emerald              	| 0043 	| Ruby                 	| 0044 	| Topaz               	|
| 0045 	| Diamond              	| 0046 	| Peridot              	| 0047 	| Pink Diamond        	|
| 0048 	| Bracelet             	| 0049 	| Brooch               	| 004A 	| Dress               	|
| 004B 	| Earrings             	| 004C 	| Facial Pack          	| 004D 	| Choker              	|
| 004E 	| Perfume              	| 004F 	| Skin Lotion          	| 0050 	| Sun Block           	|
| 0051 	| Steamed Egg          	| 0052 	| Cheese Steamed Bun   	| 0053 	| Bamboo Dumplings    	|
| 0054 	| Curry Bun            	| 0055 	| Sponge Cake          	| 0056 	| Steamed Bun         	|
| 0057 	| Steamed Cake         	| 0058 	| Steamed Dumplings    	| 0059 	| Shaomai             	|
| 005A 	| Chinese Bun          	| 005B 	| Failed Dish          	| 005C 	| Bread               	|
| 005D 	| Dinner Roll          	| 005E 	| Curry Bread          	| 005F 	| Toast               	|
| 0060 	| French Toast         	| 0061 	| Raisin Bread         	| 0062 	| Jam Bun             	|
| 0063 	| Apple Pie            	| 0064 	| Cake                 	| 0065 	| Cheese Cake         	|
| 0066 	| Chocolate Cake       	| 0067 	| Pancake              	| 0068 	| Failed Dish         	|
| 0069 	| Candied Potato       	| 006A 	| Baked Yam            	| 006B 	| Sweet Potatoes      	|
| 006C 	| Chocolate Cookies    	| 006D 	| Cookies              	| 006E 	| Moon Dumplings      	|
| 006F 	| Green Dumplings      	| 0070 	| Apple Souffle        	| 0071 	| Baked Corn          	|
| 0072 	| French Fries         	| 0073 	| Popcorn              	| 0074 	| Doughnut            	|
| 0075 	| Buckwheat Ball       	| 0076 	| Shaved Ice           	| 0077 	| Ice Cream           	|
| 0078 	| Pudding              	| 0079 	| Pumpkin Pudding      	| 007A 	| Failed Dish         	|
| 007B 	| Failed Dish          	| 007C 	| Cheese Fondue        	| 007D 	| Corn Flakes         	|
| 007E 	| Stew                 	| 007F 	| Pumpkin Stew         	| 0080 	| Mountain Stew       	|
| 0081 	| Boiled Spinach       	| 0082 	| Egg Over Rice        	| 0083 	| Tempura Rice        	|
| 0084 	| Matsutake Rice       	| 0085 	| Mushroom Rice        	| 0086 	| Bamboo Rice         	|
| 0087 	| Buckwheat Chips      	| 0088 	| Stew*                	| 0089 	| Rice Soup           	|
| 008A 	| Noodles              	| 008B 	| Curry Noodles        	| 008C 	| Tempura Noodles     	|
| 008D 	| Tempura B. Noodles   	| 008E 	| Tempura              	| 008F 	| Buckwheat Noodles   	|
| 0090 	| Chirashi Sushi       	| 0091 	| Fried Thick Noodles  	| 0092 	| Fried Noodles       	|
| 0093 	| Dumplings            	| 0094 	| Doria                	| 0095 	| Gratin              	|
| 0096 	| Porridge             	| 0097 	| Risotto              	| 0098 	| Failed Dish         	|
| 0099 	| Boiled Egg           	| 009A 	| Fish Sticks          	| 009B 	| Happy Eggplant      	|
| 009C 	| Grilled Fish         	| 009D 	| Pickled Turnip       	| 009E 	| Pickled Cucumber    	|
| 009F 	| Sashimi              	| 00A0 	| Sushi                	| 00A1 	| Stir Fry            	|
| 00A2 	| Yellow Curry         	| 00A3 	| Orange Curry         	| 00A4 	| Blue Curry          	|
| 00A5 	| Green Curry          	| 00A6 	| Indigo Curry         	| 00A7 	| Purple Curry        	|
| 00A8 	| Red Curry            	| 00A9 	| White Curry          	| 00AA 	| Black Curry         	|
| 00AB 	| Curry Rice           	| 00AC 	| Fried Rice           	| 00AD 	| Rice Plate*         	|
| 00AE 	| Croquettes           	| 00AF 	| Savory Pancake       	| 00B0 	| Omelet              	|
| 00B1 	| Omelet Rice          	| 00B2 	| Scrambled Eggs       	| 00B3 	| Rice Plate*         	|
| 00B4 	| Pizza                	| 00B5 	| Rice Ball            	| 00B6 	| Toasted Rice Ball   	|
| 00B7 	| Rice Cake            	| 00B8 	| Roasted Rice Cake    	| 00B9 	| Salad               	|
| 00BA 	| Sandwich             	| 00BB 	| Pot Sticker          	| 00BC 	| Dry Curry           	|
| 00BD 	| Rainbow Curry        	| 00BE 	| Ultimate Curry       	| 00BF 	| Finest Curry        	|
| 00C0 	| Fish Stew            	| 00C1 	| Fruit Sandwich       	| 00C2 	| Blender*            	|
| 00C3 	| Pan*                 	| 00C4 	| Microwave*           	| 00C5 	| Pot*                	|
| 00C6 	| Big Pot*             	| 00C7 	| Turnip Seeds         	| 00C8 	| Potato Seeds        	|
| 00C9 	| Cucumber Seeds       	| 00CA 	| Strawberry Seeds     	| 00CB 	| Cabbage Seeds       	|
| 00CC 	| Tomato Seeds         	| 00CD 	| Corn Seeds           	| 00CE 	| Onion Seeds         	|
| 00CF 	| Pumpkin Seeds        	| 00D0 	| Pineapple Seeds      	| 00D1 	| Eggplant Seeds      	|
| 00D2 	| Carrot Seeds         	| 00D3 	| Yam Seeds            	| 00D4 	| Spinach Seeds       	|
| 00D5 	| Bell Pepper Seeds    	| 00D6 	| Moondrop Seeds       	| 00D7 	| Toyflower Seeds     	|
| 00D8 	| Pinkcat Seeds        	| 00D9 	| Magic Red Seeds      	| 00DA 	| Grass Seeds         	|
| 00DB 	| Peach Seeds          	| 00DC 	| Banana Seeds         	| 00DD 	| Orange Seeds        	|
| 00DE 	| Apple Seeds          	| 00DF 	| Grape Seeds          	| 00E0 	| Shiitake Seeds      	|
| 00E1 	| Matsutake Seeds      	| 00E2 	| Toadstool Seeds      	| 00E3 	| Turnip              	|
| 00E4 	| Potato               	| 00E5 	| Cucumber             	| 00E6 	| Strawberry          	|
| 00E7 	| Cabbage              	| 00E8 	| Tomato               	| 00E9 	| Corn                	|
| 00EA 	| Onion                	| 00EB 	| Pumpkin              	| 00EC 	| Pineapple           	|
| 00ED 	| Eggplant             	| 00EE 	| Carrot               	| 00EF 	| Yam                 	|
| 00F0 	| Spinach              	| 00F1 	| Bell Pepper          	| 00F2 	| Moondrop Flower     	|
| 00F3 	| Toyflower            	| 00F4 	| Pinkcat Flower       	| 00F5 	| Blue Magic Flower   	|
| 00F6 	| Red Magic Flower     	| 00F7 	| Peach                	| 00F8 	| Banana              	|
| 00F9 	| Orange               	| 00FA 	| Apple                	| 00FB 	| Grape               	|
| 00FC 	| Shiitake S           	| 00FD 	| Shiitake M           	| 00FE 	| Shiiitake L         	|
| 00FF 	| Matsutake S          	| 0100 	| Matsutake M          	| 0101 	| Matsutake L         	|
| 0102 	| Toadstool S          	| 0103 	| Toadstool M          	| 0104 	| Toadstool L         	|
| 0105 	| Yellow Grass         	| 0106 	| Orange Grass         	| 0107 	| Blue Grass          	|
| 0108 	| Green Grass          	| 0109 	| Indigo Grass         	| 010A 	| Purple Grass        	|
| 010B 	| Red Grass            	| 010C 	| White Grass          	| 010D 	| Black Grass         	|
| 010E 	| Elli Leaves          	| 010F 	| Bamboo Shoot         	| 0110 	| Wild Grape          	|
| 0111 	| †                    	| 0112 	| †                    	| 0113 	| †                   	|
| 0114 	| †                    	| 0115 	| †                    	| 0116 	| †                   	|
| 0117 	| †                    	| 0118 	| †                    	| 0119 	| †                   	|
| 011A 	| †                    	| 011B 	| †                    	| 011C 	| †                   	|
| 011D 	| †                    	| 011E 	| †                    	| 011F 	| †                   	|
| 0120 	| †                    	| 0121 	| †                    	| 0122 	| †                   	|
| 0123 	| †                    	| 0124 	| †                    	| 0125 	| Teleport Stone      	|
| 0126 	| Pedometer            	| 0127 	| Clock                	| 0128 	| Red Cloak           	|
| 0129 	| Slow Shoes           	| 012A 	| Truth Bangle         	| 012B 	| Love Bangle         	|
| 012C 	| Godhand              	| 012D 	| Miracle Gloves       	| 012E 	| Touch Screen Gloves 	|
| 012F 	| Necklace             	| 0130 	| H. Goddess Earrings  	| 0131 	| Kappa Earrings      	|
| 0132 	| Witch P Earrings     	| 0133 	| Friendship Pendant   	| 0134 	| H. Goddess Pendant  	|
| 0135 	| Kappa Pendant        	| 0136 	| Time Ring            	| 0137 	| Harvest Goddess Hat 	|
| 0138 	| Kappa Hat            	| 0139 	| Angler Fish          	| 013A 	| Coelacanth          	|
| 013B 	| Squid                	| 013C 	| Huchen               	| 013D 	| Carp                	|
| 013E 	| Spa Catfish          	| 013F 	| Fish S               	| 0140 	| Fish M              	|
| 0141 	| Fish L               	| 0142 	| Fish Card*           	| 0143 	| Fish Card*          	|
| 0144 	| Fish Card*           	| 0145 	| Fish Card*           	| 0146 	| Fish Card*          	|
| 0147 	| Fish Card*           	| 0148 	| Failed Dish          	| 0149 	| Hot Milk            	|
| 014A 	| Hot Chocolate        	| 014B 	| Relax Tea            	| 014C 	| Turbojolt           	|
| 014D 	| Bodigizer            	| 014E 	| Fruit Juice          	| 014F 	| Fruit Latte         	|
| 0150 	| Grape Juice          	| 0151 	| Milk                 	| 0152 	| Mix Juice           	|
| 0153 	| Mix Latte            	| 0154 	| Pineapple Juice      	| 0155 	| Strawberry Milk     	|
| 0156 	| Tomato Juice         	| 0157 	| Vegetable Juice      	| 0158 	| Vegetable Latte     	|
| 0159 	| Water                	| 015A 	| Peach Juice          	| 015B 	| Banana Juice        	|
| 015C 	| Orange Juice         	| 015D 	| Apple Juice          	| 015E 	| Turbojolt XL        	|
| 015F 	| Bodigizer XL         	| 0160 	| Wild Grape Wine      	| 0161 	| Wine                	|
| 0162 	| Apple Jam            	| 0163 	| Grape Jam            	| 0164 	| Strawberry Jam      	|
| 0165 	| Marmalade            	| 0166 	| Cheese S             	| 0167 	| Cheese M            	|
| 0168 	| Cheese L             	| 0169 	| Yogurt S             	| 016A 	| Yogurt M            	|
| 016B 	| Yogurt L             	| 016C 	| Mayonnaise S         	| 016D 	| Mayonnaise M        	|
| 016E 	| Mayonnaise L         	| 016F 	| Milk S               	| 0170 	| Milk M              	|
| 0171 	| Milk L               	| 0172 	| Chicken Egg S        	| 0173 	| Chicken Egg M       	|
| 0174 	| Chicken Egg L        	| 0175 	| Spa-Boiled Egg       	| 0176 	| Duck Egg S          	|
| 0177 	| Duck Egg M           	| 0178 	| Duck Egg L           	| 0179 	| Buckwheat Flour     	|
| 017A 	| Butter               	| 017B 	| Chocolate            	| 017C 	| Curry Powder        	|
| 017D 	| Dumpling Mix         	| 017E 	| Flour                	| 017F 	| Ketchup             	|
| 0180 	| Oil                  	| 0181 	| Relax Tea Leaves     	| 0182 	| Spring Sun          	|
| 0183 	| Summer Sun           	| 0184 	| Fall Sun             	| 0185 	| Winter Sun          	|
| 0186 	| Sand Rose            	| 0187 	| Ball                 	| 0188 	| Basket              	|
| 0189 	| Weed                 	| 018A 	| Branch               	| 018B 	| Stone               	|
| 018C 	| Mine Rock*           	| 018D 	| Lumber               	| 018E 	| Material Stone      	|
| 018F 	| Golden Lumber        	| 0190 	| Cat*                 	| 0191 	| Dog*                	|
| 0192 	| Chick*               	| 0193 	| Chicken*             	| 0194 	| Duckling*           	|
| 0195 	| Duck*                	| 0196 	|                      	| 0197 	|                     	|

\* These items have a sprite but do not have accompanying text. <br />
† These items crash the game when in your inventory.

## Quality Table (tool)
|    	|          	|    	|         	|
|----	|----------	|----	|---------	|
| 00 	| Basic    	| 05 	| Blessed 	|
| 01 	| Copper   	| 06 	| Cursed  	|
| 02 	| Silver   	| 07 	| Mythic  	|
| 03 	| Gold     	| 08 	| *       	|
| 04 	| Mystrile 	| 09 	|         	|

\* 0x08 gives you another red-looking axe without any text. It has the same power as the mythic level. It gives you a “copper” colour tool with the same power level as mythic for other tools.

## Quality Table (accessory)
|    	|          	|    	|         	|
|----	|----------	|----	|---------	|
| 00 	| Cursed   	| 01 	| Blessed 	|