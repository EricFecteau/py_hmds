library(tidyverse)
library(ggplot2)

mines <- read.csv("./documentation/mines/mine_size/mine_size.csv") %>%
    mutate(
        rownum = row_number() - 1,
        floor_size = case_when(
            rownum %% 4000 < 1000 ~ "1 - 14x7",
            rownum %% 4000 >= 1000 & rownum %% 4000 < 2000 ~ "2 - 14x14",
            rownum %% 4000 >= 2000 & rownum %% 4000 < 3000 ~ "3 - 29x14",
            rownum %% 4000 >= 3000 & rownum %% 4000 < 4000 ~ "4 - 30x29"
        )
    )

verify <- mines %>% count(floor_size, mine_num)

mine_nums <- 0:3

for (m_num in mine_nums) {

    # Keep only relevant mine
    mine_local <- mines %>%
        filter(mine_num == m_num)

    # Get the col names of the columns with data
    col_names <- colnames(mine_local %>%
        summarise(across(where(is.numeric), sum)) %>%
        select(-c(attempt, mine_num, floor_num, rownum)) %>%
        select(where(~ sum(.) > 0)))

    mine_mean <- mine_local %>%
        select(all_of(col_names), floor_size) %>%
        group_by(floor_size) %>%
        summarise(across(where(is.numeric), mean)) %>%
        mutate(across(where(is.numeric), round, 1))

    print(knitr::kable(mine_mean, "pipe"))
}
