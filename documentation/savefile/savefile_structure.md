# HMDS Savefile structure


The savefiles for HMDS are split into two halves. First half goes from 0x00000010 to 0x00008BFF and the second half goes from 0x00008C00 to 0x000119FF.

### Structure of the save file
| range         	        | Item                                                          	|
|---------------------------|----------------------------------------------------------------	|
| 0x00000000 - 0x0000000F 	| Checksum                                                      	|
| 0x00000205            	| Name of the farm                                              	|
| 0x00000215            	| Name of the player                                              	|
| 0x00000245            	| Name of the horse                                              	|
| 0x00000255            	| Name of the dog                                               	|
| 0x00000265            	| Name of the cat                                                	|
| 0x00000275 - 0x00000425  	| Name of the farm animals                                         	|
| 0x00000465            	| The season and the year                                          	|
| 0x00008E05            	| Name of the farm                                              	|
| 0x00008E15            	| Name of the player                                              	|
| 0x00008E45            	| Name of the horse                                              	|
| 0x00008E55            	| Name of the dog                                               	|
| 0x00008E65            	| Name of the cat                                                	|
| 0x00008E75 - 0x00009025  	| Name of the farm animals                                         	|
| 0x00009065            	| The season and the year                                          	|

## Regional differences

### EU

0x3FFF0F End of file EU
6 character names

### NA

0x7FFF0F End of file NA
6 character names

### JP

0x7FFF0F End of file NA
5 character names

Uses Shift-JIS Encoding for text
