# Effects of climate change on species distribution

Data science project for the Erdös Institute data science boot camp fall 2024

Balthazar Charles, Kevin Specht, Spyridon Lentas

---

### Objectives

*Main objective:* discover trends of species repartition over time, measure possible correlation with historical meteorological data. Possibly, project using projected climate parameters.

1) Is there a significant northward creep for species previously only observed in the south ?
2) Do some species stay longer in the year ?
3) Other miscellaneous questions to our fantasy.

Possibly validate the trends by trying to predict the last years of data? And then project to the :star: future :star:.

### Datasets

The ArtPortalen is a Swedish website where users can report sightings of species on the Swedish territory. For (almost) each record, the species, date of sighting and coordinates are available. 80% of the entries are after 2001, almost all after 1981, but previous records have been added such that the database has records as far as 1641.

Pièce de résistance: [*Artpotalen dataset*](https://www.gbif.org/dataset/38b4c89f-584c-41bb-bd8f-cd1def33e92f) (beware, 58GB)

Meteorological Data: [*Nordic gridded temperature and precipitation data from 1961 to present derived from in-situ observations*](https://cds.climate.copernicus.eu/datasets/insitu-gridded-observations-nordic?tab=overview) 


### Stakeholders

- Sweden
- Mosquito real estate investors

### KPI

- Good question
- Less mosquitoes?

### Special difficulties:

The database logs 100M observation of over 40000 species, making it 58GB. It is very imbalanced between taxons. We should probably find a way to reduce to reduce the data for easier handling, without cherry-picking (such as concentrating on arthropods). Moreover, some fields are in swedish, which I do not talk.