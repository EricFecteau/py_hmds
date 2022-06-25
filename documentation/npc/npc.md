# NPC and Sprites

## Important memory locations
Table of NPC information (new NPC every 40 bytes): 0x023DBD30 (NA1.0)
Table of NPC locations (new NPC every 8 bytes): 0x023D7AE0 (NA1.0)

## List of NPC in order for all tables of NPC (by row)
|                   	|           	|                	|         	|
|-------------------	|-----------	|----------------	|---------	|
| Player Character* 	| Celia     	| Muffy          	| Nami    	|
| Romana            	| Sebastian 	| Lumina         	| Wally   	|
| Chris             	| Grant     	| Kate           	| Hugh    	|
| Carter            	| Flora     	| Vesta          	| Marlin  	|
| Ruby              	| Rock      	| Dr. Hardy      	| Galen   	|
| Nina              	| Daryl     	| Cody           	| Gustafa 	|
| Griffin           	| Vans      	| Kassey         	| Patrick 	|
| Murrey            	| Takakura  	|                	|         	|
|                   	|           	|                	|         	|
|                   	|           	|                	| Kai     	|
|                   	|           	|                	|         	|
| Harvest Goddess   	| Thomas    	| Gotz           	|         	|
| Leia              	| Keira     	| Witch Princess 	| †       	|

\* Only the first few bytes work for the player character
† After this list is the list of Sprites (see next section)

## Byte information for the table of NPC information (40 bytes)
| Byte  	| Data                                                                 	|
|-------	|----------------------------------------------------------------------	|
| 1     	| Current location (see Map section for byte values)*                  	|
| 2     	| Entrance ID to the current location*                                 	|
| 3     	| Previous location (see Map section for byte values)*                 	|
| 4     	| Exit ID of previous location*                                        	|
| 5     	| Friendship points                                                    	|
| 6-7   	| Interaction (did you talk to the NPC today, did you give it a gift…) 	|
| 8-9   	|                                                                      	|
| 10-11 	| Love points                                                          	|
| 12-20 	|                                                                      	|
| 21-28 	| Path information                                                     	|
| 29-30 	| Timer waiting for next action along path                             	|
| 31-32 	|                                                                      	|
| 33-34 	| Waiting when character blocks them                                   	|
| 35-40 	|                                                                      	|

\* Only for Player Character (00 00 00 00 for everyone else)

## Table of NPC locations (new NPC every 8 bytes)
| Byte 	| Data                                               	|
|------	|----------------------------------------------------	|
| 1    	| Current location (see Map section for byte values) 	|
| 2-8  	|                                                    	|

