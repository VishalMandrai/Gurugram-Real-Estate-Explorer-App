def sort_sec(sector):                    # Sorting all the Sectors numerically....
        x = sector.split()[-1]
        if x[-1].isdigit():
            return int(x)
        elif x[-1] == 'A':
            return int(x[0:-1]) + 0.1
        elif x[-1] == 'B':
            return int(x[0:-1]) + 0.2
        elif x[-1] == 'C':
            return int(x[0:-1]) + 0.3
        elif x[-1] == 'D':
            return int(x[0:-1]) + 0.4

sectors = pd.Series(df[df['Sector_Locality'].str.startswith("Sector")]['Sector_Locality'].unique())
sector_order = sectors.apply(sort_sec)

## Sorted List of all the Sectors:
sector_list = list(pd.concat([sectors, sector_order], axis=1).sort_values(by=1)[0].values)

## Sorted List of all the localities other than Sectors:
localities = sorted(df[~ df['Sector_Locality'].str.startswith("Sector")]['Sector_Locality'].unique())

Sector_Locality = sector_list + localities   # list....