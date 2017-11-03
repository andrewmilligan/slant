Spatial Distribution of Effort for Simulated Ants
=================================================

@author Andrew Milligan
@date Mon, 07 Aug 2017 13:24:01 -05
@outlet Slant
@image dataviz/images/power_transparent.png

[[[ Foraging ants distribute their foraging effort spatially throughout their
environment in a way that, over time, approximates the spatial distribution of
resources in their environment. This amounts to a surprisingly efficient
distributed algorithms computing an unknown and arbitrary distribution over
time. ]]]


Distributed foraging processes for discovering resources in unknown
environments are [used extensively in nature][1] and have inspired highly
effective artificial foraging algorithms. By distributing the process of
investigating, analyzing, and exploiting the surrounding environment across
many redundant, autonomous actors, each employing a simple set of rational
rules, foraging swarms are able to reach a surprisingly effective geographical
allocation of resources relatively quickly.

I simulated foraging ant swarms with the [Central Place Foraging Algorithm
(CPFA)][2] implemented in the ARGoS simulation environment, which is a prominent
implementation of ant swarm foraging strategies for use in robotic swarms. The
graphs below display the spatial distributions of effort employed by these
swarms in a variety of environments. I captured all the coordinates that each
ant in a swarm or 100 ants inspected for a seed. The graphs are two-dimensional
histograms of the distributions of these coordinates.

A *clustered environment* is one in which all seeds occur in large groups, or
clusters. There are only a few large clusters distributed randomly throughout
the environment. Each cluster is the same size, and consists of a set of seeds
laid out in a grid within the cluster. In the graph below, it is clear that the
ants identify these clusters and remember them using pheromone trails,
coordinating the swarm's efforts to focus on the clusters. Interestingly, the
ants exhibit a great deal of random wandering throughout the entire
environment; this is likely because, when wandering randomly, an ant has a much
lower chance of finding a cluster than it has of finding a seed in a more
randomly distributed environment.

{@graph
  img_path = "dataviz/images/foraging_map_clustered.png"
  footnote = "More saturated patches indicate greater forager concentration in
    that region of the simulation arena. Get the data and code used
    [here](https://github.com/slantedlabs/ants_data)."
}

A *random environment* is the exact opposite of a clustered one: all of the
seeds are distributed uniformly and independently at random throughout the
environment with no clustering whatsoever. The lack of a clear visual trend in
the distribution of dark areas in the graph below indicates that the ants are
not coordinating their efforts in any particular way, but rather distributing
their focus more or less evenly across the environment.

{@graph
  img_path = "dataviz/images/foraging_map_random.png"
  footnote = "Get the data and code used
    [here](https://github.com/slantedlabs/ants_data)."
}

Finally, a *power-law-distributed environment* is one in which the seeds are
distributed according to a [power law distribution][3], and it is somewhat of a
middle ground between the fully clustered distribution and the fully random
distribution. In a power-law-distributed environment, clusters are placed
randomly throughout the environment, but the size of each cluster is
proportional to how many clusters of that size there are in the environment
(i.e., there is one large cluster, several medium-sized clusters, and many
small clusters). Power law distributions generally follow the [80-20 rule][4],
in that, roughly, only 20% of the clusters contain 80% of the seeds.

{@graph
  img_path = "dataviz/images/foraging_map_power.png"
  footnote = "Get the data and code used
    [here](https://github.com/slantedlabs/ants_data)."
}

From these graphs, it is clear that the spatial distribution of the swarm's
foraging efforts adheres over time to the underlying distribution of the seeds
in the environment.

[1]: https://www.cs.unm.edu/~melaniem/Publications_files/LetendreMoses_Synergy_GECCO_2013.pdf
[2]: https://www.cs.unm.edu/~csgsa/2011-2012/papers/2012/JoshuaHecker.pdf
[3]: https://en.wikipedia.org/wiki/Power_law
[4]: https://en.wikipedia.org/wiki/Pareto_principle
