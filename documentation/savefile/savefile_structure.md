# HMDS Savefile structure

The savefiles for HMDS are split into two halves. First half goes from 0x00000010 to 0x00008BFF and the second half goes from 0x00008C00 to 0x000119FF.

The table below is applies to both EU (1.0) and NA (1.0). The second half of the table does not apply to JP (1.0), the first half of the sav is correct

### Structure of the save file
| range                   | Length | Item                                                          	|
|-------------------------|--------|----------------------------------------------------------------|
| 0x00000205              | 6      | Name of the farm                                              	|
| 0x00000215              | 6      | Name of the player                                            	|
| 0x00000245              | 6      | Name of the horse                                             	|
| 0x00000255              | 6      | Name of the dog                                               	|
| 0x00000265              | 6      | Name of the cat                                               	|
| 0x00000275 - 0x00000425 | 6      | Name of the farm animals                                      	|
| 0x00000465              | 16     | The season and the year                                       	|
| 0x00008E05              | 6      | Name of the farm                                              	|
| 0x00008E15              | 6      | Name of the player                                            	|
| 0x00008E45              | 6      | Name of the horse                                             	|
| 0x00008E55              | 6      | Name of the dog                                               	|
| 0x00008E65              | 6      | Name of the cat                                               	|
| 0x00008E75 - 0x00009025 | 6      | Name of the farm animals                                      	|
| 0x00009065              | 16     | The season and the year                                       	|

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
