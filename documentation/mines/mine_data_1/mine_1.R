library(tidyverse)
library(ggplot2)

dir.create("./documentation/mines/mine_data_1/plots")
mine <- read.csv("./documentation/mines/mine_data_1/mine_data_1.csv")

verify <- mine %>% count(floor_num)

col_names <- colnames(mine %>%
    summarise(across(where(is.numeric), sum)) %>%
    select(-c(
        attempt, mine_num, floor_num, no.rock, empty.tile, staircase.up
    )) %>%
    select(where(~ sum(.) > 0)))

mine <- mine %>%
    group_by(floor_num) %>%
    select(all_of(col_names), floor_num) %>%
    summarise(across(where(is.numeric), mean)) %>%
    mutate(across(where(is.numeric), round, 2))

for (col in col_names) {
    ggplot(data = mine, mapping = aes(x = floor_num)) +
        geom_bar(aes(weight = get(col))) +
        scale_x_continuous(breaks = 1:10) +
        labs(y = "Count", x = "Floor number")

    ggsave(
        file = paste0("./documentation/mines/mine_data_1/plots/", col, ".png"),
        width = 10,
        height = 5,
        dpi = 300
    )
}
