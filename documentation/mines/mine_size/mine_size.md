# Mine size

Before exploring the values found on each floor of the mine, we must first determine what floor size should be used to get this data. Unfortunately, it does not seem feasible to allow the game to select the size randomly (as it would in normal gameplay) because to force a mine floor number (e.g. 3th mine, floor 365) in a script you must give it a mine location (aka mine size).

To do this, a random floor number was selected from each of the 4 mines and 1,000 floor were generated for each of the 4 possible sizes of the mine (14x7, 14x14, 29x14, 30x29). The data for each tile was collected (both the rocks and the tiled ground) and an average per generation was produced in the following 4 tables. Other than the "no rock" and "empty tile" growing with the size of the mine, most other value remains, on average, the same between each floor size. One thing to note is that generally, floor 100 of mine 2 is a larger floor, therefore some differences in the "junk ore" between the 14x7 and the other sizes may be due to the fact that the data generated "overflowed" beyond the 14x7 data array. There are also some indications that the number of "empty rock" and "junk ore" can be impacted by the size of the floor, but it does not seem that valuable rocks can be impacted.

**Therefore, the data collection for discovering the average number of item per floor should be done on the largest possible floor (30x29) to get the best data that includes both small and large floors.**

## Mine 1 (floor 9), average of 1000 attemps per floor size
|floor_size | no.rock| junk.ore| copper| silver| gold| mystrile| empty.tile| down.stairs| covered.hole| money.bag| black.grass|
|:----------|-------:|--------:|------:|------:|----:|--------:|----------:|-----------:|------------:|---------:|-----------:|
|1 - 14x7   |    69.9|      2.6|    1.1|    1.1| 19.4|      3.8|       42.3|        11.1|          2.1|      35.0|         7.5|
|2 - 14x14  |   165.9|      2.9|    1.3|    1.3| 20.4|      4.2|      139.8|        10.9|          2.0|      34.9|         7.4|
|3 - 29x14  |   374.2|      3.2|    1.4|    1.4| 21.8|      4.0|      349.6|        11.0|          2.0|      35.0|         7.5|
|4 - 30x29  |   837.4|      3.4|    1.4|    1.4| 22.0|      4.4|      813.7|        11.0|          2.0|      35.0|         7.4|

## Mine 2 (floor 100), average of 1000 attemps per floor size
|floor_size | no.rock| empty.rock| junk.ore| moon.stone| sand.rose| diamond| emerald| empty.tile| down.stairs| covered.hole| lithograph|
|:----------|-------:|----------:|--------:|----------:|---------:|-------:|-------:|----------:|-----------:|------------:|----------:|
|1 - 14x7   |    66.1|        4.9|     10.6|        0.4|       0.4|    15.2|     0.5|       73.5|        22.5|            1|          1|
|2 - 14x14  |   161.0|        4.8|     12.6|        0.4|       0.4|    16.4|     0.4|      170.5|        22.5|            1|          1|
|3 - 29x14  |   369.3|        5.1|     13.7|        0.4|       0.4|    16.6|     0.5|      380.6|        22.4|            1|          1|
|4 - 30x29  |   831.9|        5.0|     14.5|        0.5|       0.5|    17.1|     0.5|      844.6|        22.4|            1|          1|

## Mine 3 (floor 365), average of 1000 attemps per floor size
|floor_size | no.rock| empty.rock| junk.ore| empty.tile| down.stairs| covered.hole| money.bag| black.grass|
|:----------|-------:|----------:|--------:|----------:|-----------:|------------:|---------:|-----------:|
|1 - 14x7   |    28.5|       42.1|     25.6|       61.4|           8|          0.5|      25.1|         3.0|
|2 - 14x14  |   106.3|       47.3|     39.8|      158.8|           8|          0.5|      24.6|         3.1|
|3 - 29x14  |   298.6|       52.7|     51.7|      368.5|           8|          0.5|      24.9|         3.0|
|4 - 30x29  |   754.5|       53.7|     58.6|      833.0|           8|          0.5|      24.7|         2.9|

## Mine 4 (floor 3526), average of 1000 attemps per floor size
|floor_size | no.rock| empty.rock| empty.tile| down.stairs| covered.hole| money.bag| black.grass| bronze.coin| silver.coin| gold.coin|
|:----------|-------:|----------:|----------:|-----------:|------------:|---------:|-----------:|-----------:|-----------:|---------:|
|1 - 14x7   |    86.2|       11.8|       16.0|        22.6|          2.1|       0.5|         4.1|         0.5|         2.1|      50.2|
|2 - 14x14  |   184.0|       12.0|      114.3|        22.3|          2.0|       0.5|         4.1|         0.5|         2.0|      49.4|
|3 - 29x14  |   393.6|       12.4|      323.9|        22.5|          2.0|       0.5|         4.1|         0.6|         2.0|      49.5|
|4 - 30x29  |   857.7|       12.3|      788.2|        22.4|          2.0|       0.5|         3.9|         0.5|         1.9|      49.6|