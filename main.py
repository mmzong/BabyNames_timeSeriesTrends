from SRC.babynames import BabyNames

if __name__ == "__main__":
    # Instantiates BabyNames class by creating object b1
    b1 = BabyNames()

    # Testing pandas DataFrame created in init with return print(self.names_df) in sort_data
    print(b1)

    # Testing m_f_names subsets, groups, and plots names_df correctly. Yes.
    print(b1.m_f_names(1880, 2022))
    print(b1.m_f_names(1920, 1950))

    # Testing most_popular_ever grouped, subset, and plot correctly. Yes.
    print(b1.most_popular_ever())

    # Testing unisex grouped, subset, and plot correctly. Yes
    print(b1.unisex())

    # Testing unisex_evolution
    print(b1.unisex_evolution())
