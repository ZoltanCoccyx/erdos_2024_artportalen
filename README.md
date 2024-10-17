# Effects of climate change on species distribution

Data science project for the Erdös Institute data science boot camp fall 2024

Balthazar Charles, Kevin Specht, Spyridon Lentas

---

### Objectives

*Main objective:* discover trends of species repartition over time, measure possible correlation with historical meteorological data. Possibly, project using projected climate parameters.

1) Is there a significant northward creep for species previously only observed in the south ?
2) Do some species stay longer in the year ?
3) Other miscellaneous questions to our fantasy.
    - Possibly use some CNN to produce year on year repartition maps ?
    - Clustering/Classifying species depending on their reaction (e.g. observing the repartition of a species over only one year, can we predict if it will be positively or negatively impacted by climate change ?)

Possibly validate the trends by trying to predict the last years of data? And then project to the :star: future :star:.

### Datasets

The ArtPortalen is a Swedish website where users can report sightings of species on the Swedish territory. For (almost) each record, the species, date of sighting and coordinates are available. 80% of the entries are after 2001, almost all after 1981, but previous records have been added such that the database has records as far as 1641.

Pièce de résistance: [*Artpotalen dataset*](https://www.gbif.org/dataset/38b4c89f-584c-41bb-bd8f-cd1def33e92f) (beware, 58GB)

Meteorological Data: [*Nordic gridded temperature and precipitation data from 1961 to present derived from in-situ observations*](https://cds.climate.copernicus.eu/datasets/insitu-gridded-observations-nordic?tab=overview)

Possibly a good idea to find a population density dataset to ponder to frequency of observations?


### Stakeholders

- Healthcare system through the monitoring and prediction of animal-borne disease repartition (via the vector species).
- Environmental protection from invasive species.
- Mosquito real estate investors (self explanatory)

### KPI

- If we produce projection maps, at least rmse with actual map repartition considered as a 2d function? (If we consider that we are producing density function for the proba of observation of a species, maybe something more fancy like cross entropy?).
- Idem for period of presence and latitudes.
- Idem for classifying species into positively impacted/negatively impacted/indifferent.


### Special difficulties:

The database logs 100M observation of over 40000 species, making it 58GB. It is very imbalanced between taxons. We should probably find a way to reduce to reduce the data for easier handling, without cherry-picking (such as concentrating on arthropods). Moreover, some fields are in swedish, which I do not talk.