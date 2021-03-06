library(tidyverse)
library(ggplot2)
library(ggtext)
library(ggrepel)

dir.create("./documentation/mines/mine_data_2/plots")
mine <- read.csv("./documentation/mines/mine_data_2/mine_data_2.csv")

verify <- mine %>% count(floor_num)

col_names <- colnames(mine %>%
    summarise(across(where(is.numeric), sum)) %>%
    select(-c(
        attempt, mine_num, floor_num, no.rock, empty.tile,
        staircase.up
    )) %>%
    select(where(~ sum(.) > 0)))

mine <- mine %>%
    group_by(floor_num) %>%
    select(all_of(col_names), floor_num) %>%
    summarise(across(where(is.numeric), mean)) %>%
    mutate(across(where(is.numeric), round, 2))

for (col in col_names) {
    mine_item <- mine %>%
        select(col, floor_num) %>%
        mutate(
            lab = case_when(
                col == "alexandrite" ~
                    case_when(
                        get(col) > 0 ~ paste0(floor_num)
                    ),
                col == "diamond" ~
                    case_when(
                        get(col) > 15 ~ paste0(floor_num)
                    ),
                col == "down.stairs" ~
                    case_when(
                        get(col) > 20 & floor_num > 20 ~ paste0(floor_num)
                    ),
                col == "junk.ore" ~
                    case_when(
                        get(col) > 14 ~ paste0(floor_num)
                    ),
                col == "money.bag" ~
                    case_when(
                        get(col) > 50 ~ paste0(floor_num)
                    ),
                col == "lithograph" ~
                    case_when(
                        floor_num %% 50 == 0 ~ paste0(floor_num)
                    )
            ),
            lab2 = case_when(
                col == "black.grass" ~
                    case_when(
                        get(col) > 20 & get(col) < 30 ~ paste0(floor_num),
                        get(col) > 30 & floor_num %in% c(3, 6, 9, 12) ~
                            paste0(floor_num)
                    ),
                col == "agate" ~
                    case_when(
                        get(col) > 5 ~ paste0(floor_num),
                        floor_num == 255 ~ paste0(floor_num)
                    ),
                col == "amethyst" ~
                    case_when(
                        get(col) > 5 ~ paste0(floor_num),
                        floor_num == 255 ~ paste0(floor_num)
                    ),
                col == "emerald" ~
                    case_when(
                        get(col) > 5 ~ paste0(floor_num),
                        floor_num == 255 ~ paste0(floor_num)
                    ),
                col == "fluorite" ~
                    case_when(
                        get(col) > 5 ~ paste0(floor_num),
                        floor_num == 255 ~ paste0(floor_num)
                    ),
                col == "moon.stone" ~
                    case_when(
                        get(col) > 5 ~ paste0(floor_num),
                        floor_num == 255 ~ paste0(floor_num)
                    ),
                col == "peridot" ~
                    case_when(
                        get(col) > 5 ~ paste0(floor_num),
                        floor_num == 255 ~ paste0(floor_num)
                    ),
                col == "ruby" ~
                    case_when(
                        get(col) > 5 ~ paste0(floor_num),
                        floor_num == 255 ~ paste0(floor_num)
                    ),
                col == "sand.rose" ~
                    case_when(
                        get(col) > 5 ~ paste0(floor_num),
                        floor_num == 255 ~ paste0(floor_num)
                    ),
                col == "topaz" ~
                    case_when(
                        get(col) > 5 ~ paste0(floor_num),
                        floor_num == 255 ~ paste0(floor_num)
                    ),
                col == "pink.diamond" ~
                    case_when(
                        floor_num %in% c(
                            102, 123, 153, 183,
                            201, 204, 207, 213,
                            222, 225, 231, 234,
                            237, 243, 252, 105, 108
                        ) ~
                            paste0(floor_num)
                    ),
            )
        )

    ggplot(data = mine_item, mapping = aes(x = floor_num, label = lab)) +

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
        file = paste0("./documentation/mines/mine_data_2/plots/", col, ".png"),
        width = 10,
        height = 5,
        dpi = 300
    )
}
