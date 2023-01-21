# Mine data configuration

This page explores the configuration of the mine data in memory.

## Important memory locations
Mine floor number: 0x023DBD2E (NA1.0) | 0x023DBD2A (NA1.1) <br />
Floor x size: 0x022C3EC4 (NA1.0) | 0x022C6C84 (NA1.1) <br />
Floor y size: 0x022C3EC5 (NA1.0) | 0x022C6C86 (NA1.1) <br />
Floor data array (870 bytes):  0x023DB964 (NA1.0) | 0x023DB960 (NA1.1) <br />

## Floor data array
The floor data (e.g. what each 16 pixel by 16 pixel square contains on each floor of the mine) is stored in a 870 byte array (see location above). This array can fit the maximum floor of 30 tiles by 29 tiles. Each element of the array contain two pieces of information, the ore information (what can be extracted from a rock with a hammer) is stored in the Most Significant 4 bits (MSB) and buried information (what can be extracted by tilling the ground) is stored in the Least Significant 4 bits (LSB).

## Least Significant 4 bits
|    	| Mine 1         	| Mine 2         	| Mine 3            	| Mine 4         	|
|----	|----------------	|----------------	|-------------------	|----------------	|
| X0 	| Empty          	| Empty          	| Empty             	| Empty          	|
| X1 	| Down stairs*   	| Down stairs*   	| Down stairs*      	| Down stairs*   	|
| X2 	| Covered hole   	| Covered hole   	| Covered hole      	| Covered hole   	|
| X3 	| Money bag      	| Money bag      	| Money bag         	| Money bag      	|
| X4 	| Black grass    	| Black grass    	| Black grass       	| Bronze coin    	|
| X5 	|                	| Lithograph     	| Cursed tool†      	| Silver coin    	|
| X6 	|                	|                	| Cursed accessory† 	| Gold coin      	|
| X7 	|                	|                	|                   	| Black grass    	|
| X8 	|                	|                	|                   	| Lithograph     	|
| X9 	|                	|                	|                   	|                	|
| XA 	|                	|                	|                   	|                	|
| XB 	|                	|                	|                   	|                	|
| XC 	| Tiled square   	| Tiled square   	| Tiled square      	| Tiled square   	|
| XD 	| Unearthed hole 	| Unearthed hole 	| Unearthed hole    	| Unearthed hole 	|
| XE 	| Staircase up   	| Staircase up   	| Staircase up      	| Staircase up   	|
| XF 	| Staircase down 	| Staircase down 	| Staircase down    	| Staircase down 	|

\* The “potential down stairs” (LSB value X1) will only be revealed once. Once one down stair is revealed, no other down stairs will be uncovered. <br />
† The cursed items can only be found on an apparently random set of floors (24, 35, 48, 52, 68, 71, 87, 99, 106, 118, 124, 135, 142, 153, 162, 178, 185, and 197). When the player drops to one of these floors, there is a possibility that a cursed item will not be generated at all. In the case that it does, however, the game rolls a random number at the time the player mines the square containing the item to determine the specific item given. For the cursed tools, the player will not get any item if the roll would give the player a tool they’ve already obtained; for the cursed accessories, the player will always get the rolled item, regardless of the number of times the player has previously found it.

## Most Significant 4 bits
|    	| Mine 1     	| Mine 2       	| Mine 3        	| Mine 4            	|
|----	|------------	|--------------	|---------------	|-------------------	|
| 0X 	| No rock    	| No rock      	| No rock       	| No rock           	|
| 1X 	| Empty rock 	| Empty rock   	| Empty rock    	| Empty rock        	|
| 2X 	| Junk ore   	| Junk ore     	| Junk ore      	| Junk ore          	|
| 3X 	| Copper     	| Pink Diamond 	| Copper        	| Blue wonderful†   	|
| 4X 	| Silver     	| Alexandrite  	| Silver        	| Green wonderful†  	|
| 5X 	| Gold       	| Moon stone   	| Gold          	| Red wonderful†    	|
| 6X 	| Mystrile   	| Sand Rose    	| Mystrile      	| Yellow wonderful† 	|
| 7X 	|            	| Diamond      	| Spring sun    	| Orange wonderful† 	|
| 8X 	|            	| Emerald      	| Summer sun    	| Purple wonderful† 	|
| 9X 	|            	| Ruby         	| Fall sun      	| Indigo wonderful† 	|
| AX 	|            	| Topaz        	| Winter sun    	| Black wonderful†  	|
| BX 	|            	| Peridot      	| Mythic stone* 	| White wonderful†  	|
| CX 	|            	| Fluorite     	| Adamantite    	|                   	|
| DX 	|            	| Agate        	| Orichalc      	|                   	|
| EX 	|            	| Amethyst     	|               	|                   	|
| FX 	|            	|              	|               	|                   	|

\* The mythic stone generates on floors ending in 0 for floors 0 to 255, and floors ending in 5 for floors 256 to 999. No matter how many cursed tools the player has, the stone will always be generated; however, the player only obtains the stone when they break the rock if they have 6 blessed tools. <br />
† The wonderfuls only generate on floors ending in 0. Additionally, the player will only receive the wonderful if they don’t already have it. See the table below for further details.

## Wonderfuls
| Floor ending 	| Wonderful color 	| Floor ending 	| Wonderful color 	|
|--------------	|-----------------	|--------------	|-----------------	|
| 10           	| Blue            	| 60           	| Black           	|
| 20           	| Purple          	| 70           	| Yellow          	|
| 30           	| Green           	| 80           	| White           	|
| 40           	| Indigo          	| 90           	| Orange          	|
| 50           	| Red             	|              	|                 	|