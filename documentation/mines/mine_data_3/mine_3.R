library(tidyverse)
library(ggplot2)
library(ggtext)
library(ggrepel)

dir.create("./documentation/mines/mine_data_3/plots")
mine <- read.csv("./documentation/mines/mine_data_3/mine_data_3.csv")

verify <- mine %>% count(floor_num)

col_names <- colnames(mine %>%
    summarise(across(where(is.numeric), sum)) %>%
    select(-c(attempt, mine_num, floor_num, no.rock, empty.tile)) %>%
    select(where(~ sum(.) > 0)))

mine <- mine %>%
    group_by(floor_num) %>%
    select(all_of(col_names), floor_num) %>%
    summarise(across(where(is.numeric), mean)) %>%
    mutate(across(where(is.numeric), round, 1))

for (col in col_names) {
    mine_item <- mine %>%
        select(col, floor_num) %>%
        mutate(
            lab = case_when(
                col == "black.grass" ~
                    case_when(
                        get(col) > 20 ~ paste0(floor_num)
                    ),
                col == "down.stairs" ~
                    case_when(
                        get(col) > 20 ~ paste0(floor_num)
                    )
            ),
            lab2 = case_when(
                col == "cursed.accessory" ~
                    case_when(
                        get(col) > 0 ~ paste0(floor_num)
                    ),
                col == "cursed.tool" ~
                    case_when(
                        get(col) > 0 ~ paste0(floor_num)
                    ),
                col == "fall.sun" ~
                    case_when(
                        floor_num < 50 & get(col) > 0 ~ paste0(floor_num)
                    ),
                col == "spring.sun" ~
                    case_when(
                        floor_num < 50 & get(col) > 0 ~ paste0(floor_num)
                    ),
                col == "summer.sun" ~
                    case_when(
                        floor_num < 50 & get(col) > 0 ~ paste0(floor_num)
                    ),
                col == "copper" ~
                    case_when(
                        floor_num < 50 & get(col) > 10 ~ paste0(floor_num)
                    ),
                col == "gold" ~
                    case_when(
                        floor_num < 50 & get(col) > 10 ~ paste0(floor_num)
                    ),
                col == "mystrile" ~
                    case_when(
                        floor_num < 50 & get(col) > 10 ~ paste0(floor_num)
                    ),
                col == "silver" ~
                    case_when(
                        floor_num < 50 & get(col) > 10 ~ paste0(floor_num)
                    ),
            )
        )

    ggplot(data = mine_item, mapping = aes(x = floor_num)) +

        # The data
        geom_bar(aes(weight = get(col))) +
        scale_y_continuous(expand = expansion(mult = c(0, .1))) +
        scale_x_continuous(expand = expansion(mult = c(0, .02))) +

        # Text
        geom_richtext(
            data = subset(mine_item, !is.na(lab)),
            aes(y = get(col), label = lab),
            vjust = -0.2,
            size = 3.5,
            label.padding = unit(1, "pt"),
        ) +
        # Text (all)
        geom_label_repel(
            data = subset(mine_item, !is.na(lab2)),
            aes(y = get(col), label = lab2),
            size = 3.5,
            min.segment.length = 0,
            max.overlaps = 20
        ) +
        labs(y = "Count", x = "Floor number")

    ggsave(
        file = paste0("./documentation/mines/mine_data_3/plots/", col, ".png"),
        width = 10,
        height = 5,
        dpi = 300
    )
}
