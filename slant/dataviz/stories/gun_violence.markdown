Gun Deaths and Background Checks
================================

@author Andrew Milligan
@date Tue, 15 Aug 2017 02:05:59 -05
@outlet Slant
@djangotags static, shortcodes
@localimages dataviz/images/missouri_gun_deaths.svg

[[[ A lack of laws requiring criminal background checks for gun sales by
unlicensed vendors correlates with higher rates of gun deaths. ]]]


I gathered the data presented here from two sources: I got data on underlying
causes of death between 1999 and 2015 from the [CDC Wonder][1] web portal, and
I got data on state gun laws from the [Everytown Gun Law Navigator][2].

The graph below shows the rate of gun-related deaths per 100,000 people in the
state of Missouri from 1999 to 2015, as estimated by the Centers for Disease
Control and Prevention (CDC). According toe Everytown Research's Gun Navigator
and [the Washington Post][3] Missouri repealed laws requiring background checks
and licenses for all handgun owners. A [study][4] from the Johns Hopkins
Bloomberg School of Public Health found that the repeal led to a "sharp
increase" in Missouri's homicide rate, as the law was "associated with an
additional 55 to 63 murders per year in Missouri between 2008 and 2012" than
forcasts would have estimated had the law not been repealed.


{% graph img_path="dataviz/images/missouri_gun_deaths.svg" footnote="The dark line is the crude rate of all deaths in Missouri caused by firearms per 100,000 people as estimated by the CDC; the shaded area shows the 95% confidence interval. Get the data and code used [here](https://github.com/slantedlabs/gun_violence_data)." %}


A spike in crime within Missouri does not tell the entire story, however. The
same study found that police in neighboring states with harsher gun laws
recovered dramatically increasing numbers of guns that were originally
purchased in Missouri. As the study says:

> The number of guns sold in Missouri and later recovered by police in Illinois
> and Iowa, two border states with handgun purchaser licensing laws, increased
> 37% (from 133 to 182) from 2006 (just before Missouri’s [handgun licensing]
> law was repealed) to 2012 when the overall number of crime guns recovered by
> police in those states actually declined by 6%.

This trend does not manifest uniquely in Missouri. The graph below displays the
CDC's estimates of gun-related death rates per 100,000 people for each state
and the District of Columbia from 1999 to 2015. It also shows a statistical
smoothing of the data and the distributions of death rates for states with and
without background check laws each year. Since 1999, gun-related death rates
have trended up in general, though more so for states without background check
laws. Moreover, gun-related death rates are significantly higher in states
without these laws across the entire period, and the difference is only
increasing.


{% graphanim anim_id=0 img_paths='dataviz/images/national_gun_deaths_bg_checks_1999.svg dataviz/images/national_gun_deaths_bg_checks_2000.svg dataviz/images/national_gun_deaths_bg_checks_2001.svg dataviz/images/national_gun_deaths_bg_checks_2002.svg dataviz/images/national_gun_deaths_bg_checks_2003.svg dataviz/images/national_gun_deaths_bg_checks_2004.svg dataviz/images/national_gun_deaths_bg_checks_2005.svg dataviz/images/national_gun_deaths_bg_checks_2006.svg dataviz/images/national_gun_deaths_bg_checks_2007.svg dataviz/images/national_gun_deaths_bg_checks_2008.svg dataviz/images/national_gun_deaths_bg_checks_2009.svg dataviz/images/national_gun_deaths_bg_checks_2010.svg dataviz/images/national_gun_deaths_bg_checks_2011.svg dataviz/images/national_gun_deaths_bg_checks_2012.svg dataviz/images/national_gun_deaths_bg_checks_2013.svg dataviz/images/national_gun_deaths_bg_checks_2014.svg dataviz/images/national_gun_deaths_bg_checks_2015.svg'|seplist footnote="Each dot is a CDC-estimated crude rate of gun deaths per 100,000 people for a state. Lines are [LOESS smoothings](https://en.wikipedia.org/wiki/Local_regression) with 95% confidence intervals. The density graphs on the right show the distributions of death rates for states with and without background check laws (law data from Everytown Gun Law Navigator). Get the data and code used [here](https://github.com/slantedlabs/gun_violence_data)." %}


[1]: https://wonder.cdc.gov/
[2]: https://everytownresearch.org/navigator/
[3]: https://www.washingtonpost.com/blogs/govbeat/wp/2014/02/18/study-repealing-missouris-background-check-law-associated-with-a-murder-spike/?utm_term=.46dbb438ac60
[4]: https://link.springer.com/article/10.1007/s11524-014-9865-8
