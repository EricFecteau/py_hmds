library(tidyverse)
library(ggplot2)

bins <- c(-2147483648, seq(-2147483648 + 97483648, 2147483647 - 97483647, by = 100000000), 2147483647)

rng <- read.csv("./documentation/mechanics/rng/rng.csv") %>%
    mutate(RNG_bin = cut(RNG_Value, breaks = bins, dig.lab = 10)) %>%
    group_by(RNG_bin) %>%
    summarise(n = n())

ggplot(data = rng, mapping = aes(y = RNG_bin)) +
    geom_bar(aes(weight = n)) +
    theme(axis.title.y = element_blank(), axis.title.x = element_blank())

ggsave(file = "./documentation/mechanics/rng/rng.png", width = 6, height = 5, dpi = 300)
