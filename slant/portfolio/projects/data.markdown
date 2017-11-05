Data
====

@djangotags static
@image portfolio/projects/data_dotplot.png

[[[ Check out the data products behind the Slant. Created primarily with R. ]]]


In an increasingly data-driven world, vast amounts of information are at our
fingertips&mdash;but that information is only as good as our ability to
interpret it. When dealing with complex data sets, and even sometimes with
seemingly simple data sets, the task of extracting a clear and concise story
from the data can be immense. Often, expecting a reader to spend time and
effort to understand the complexities and nuances of a dataset is unrealistic,
and, when faced with such a task, the reader will simply move on. This is
especially true in data-driven stories that attempt to reach the general public
rather than a more technical audience. Thus, it is the job of the data
scientist not only to discover compelling stories encased in opaque data, but
to present the data in a way that clearly, intuitively, and beautifully conveys
those stories immediately and without studious inspection.

{@quote
  quote = "The commonality between science and art is in trying to see
    profoundly&mdash;to develop strategies of seeing and showing."
  name = "Edward Tufte"
}

Below are several of the data visualization projects I have done for the
articles in the [Slant](/). I did all of the data processing and analysis as
well as the visualization itself in R unless explicitly noted otherwise. Each
visualization provides a link to the code that created it, and, when possible,
the data as well.

{@break }

### Racial Disparities

The graph below is from the Slant article on both the over-representation of
white people in income received and the over-representation of black people in
those killed by the police. In 49 states and the District of Columbia, white
people receive a larger percentage of all household income than they represent
demographically. The disparity is 5 points in the average state, but it ranges
up to 20 points in DC, where white people make up 40% of the population, but
take home 60% of the income.

The entirety of this graph was made in R. I retrieved all of the data from
[IPUMS][ipums] in a CSV format, and then processed, analyzed, and visualized it
using the [R Tidyverse][tidyverse] packages. Three key aspects that make this
graph effective are:

* the sorting of the states by white income disparity rather than
  alphabetically;
* the color-coded textual labels that explain the graph; and
* the quantile labeling of the y-axis, which allows numerical interpretation,
  but prevents cluttering the graph with excessive grid lines.

{@graph
  img_path = "portfolio/projects/data/income_disparity.svg"
  footnote = "Data from [IPUMS USA](https://usa.ipums.org/usa/) using total
    family income, race, and state from 2013 to 2015. Get the data and code
    used [here](https://github.com/slantedlabs/whites_paid_blacks_killed)."
}

The map below is from the same story; it shows the geographical distribution of
the disparity between the representation of black people in those killed by the
police and the representation of black people in the population.

I collected these data from [Mapping Police Violence][mpv], a project working
to "provide greater transparency and accountability for police departments".
I made the tile map with the [tilemapr][tilemapr] library, which is an
open-source library for making tile and hextile maps of the US. Tile maps are
effective when the geographical area of a state is not important; here, we only
care about the disparity in each state and, roughly, where each state is
located regionally. In this map, the fact that several New England states have
some of the highest disparities jumps out; that fact could easily be lost in a
traditional choropleth map because these states have some of the smallest
geographical areas.

{@graph
  img_path = "portfolio/projects/data/death_disparity_map.svg"
  footnote = "Data from
    [Mapping Police Violence](https://mappingpoliceviolence.org/), who
    constructed a database of police killings from 2013 to the present. Get the
    data and code used
    [here](https://github.com/slantedlabs/whites_paid_blacks_killed)."
}

{@break }

### National Gun Deaths

This next graph pivots to the issue of gun-related deaths in the United States
from 1999 to 2015. In it we can see clearly that gun-related deaths are, on
average, more frequent in states that do not have background check laws.
Moreover, the difference has increased over time.

Taken simply as groups of points, the death rates in the different states are
not meaningful. Adding a LOESS smoothing, we can immediately see that red
states have higher rates of gun deaths. Finally, the density plots on the right
make it clear that, while gun death rates have increased across the board, the
distribution of red states is increasingly separating itself from the
distribution of black states.

{@graph
  img_path = "portfolio/projects/data/national_gun_deaths_bg_checks.gif"
	footnote = "Each point shows the crude rate of all deaths in a state in a
    given year as estimated by the CDC; black and red states do and don't have
    background check laws, respectively. The lines show LOESS fitting the two
    classes of states with 95% confidence intervals. The density plots at the
    right show the distributions of rates for states with (black) and without
    (red) background check laws. Get the data and code used
    [here](https://github.com/slantedlabs/gun_violence_data)."
}

This graph was also made entirely with R.

{@break }

### Simulated Foraging

This final graph departs from the theme and displays foraging patterns in
simulated ants. Some of my work in the Adaptive Computation Lab at UNM has
involved abstracting and modeling swarms of interacting agents, ranging from
foraging ants to users of social media. This has included developing ways to
abstract swarm behaviors as distributed methods of approximating unknown prior
distributions. Here, we see a swarm of simulated ants approximating an unknown
distribution of seeds with their spatial distribution of foraging effort. It is
clear from the graph that the seeds were distributed throughout the environment
in clusters of varying size.

One of the technical challenges of creating this graph&mdash;and one of the
things that makes it so visually effective&mdash;was applying a high-pass
filter to the two-dimensional histogram. In the graph we can see the ghostly
paths where a small number of ants have foraged; in order to prevent this from
obfuscating the meaningful data, I applied a progressive alpha gradient to the
lowest ranges of the data, making insignificant rarities less visually
confusing.

{@graph
  img_path = "portfolio/projects/data/foraging_map_power.png"
  footnote = "Get the data and code used
    [here](https://github.com/slantedlabs/ants_data)."
}


[ipums]: https://usa.ipums.org/usa/
[mpv]: https://mappingpoliceviolence.org/
[tilemapr]: https://github.com/EmilHvitfeldt/tilemapr
[tidyverse]: https://www.tidyverse.org/
