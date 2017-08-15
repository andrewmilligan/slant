Gun Deaths and Background Checks
================================

@author Andrew Milligan
@date Tue, 15 Aug 2017 02:05:59 Z
@outlet Slant
@djangotags static, shortcodes
@localimages dataviz/images/missouri_gun_deaths.svg

[[[ A lack of laws requiring criminal background checks for gun sales by
unlicensed vendors correlates with higher rates of gun deaths. ]]]

I gathered the data presented here from two sources: I got data on underlying
causes of death between 1999 and 2015 from the [CDC Wonder][1] web portal, and
I got data on state gun laws from the [Everytown Gun Law Navigator][2].

{% graph img_path="dataviz/images/missouri_gun_deaths.svg" footnote="The dark line is the crude rate of all deaths in Missouri caused by firearms per 100,000 people as estimated by the CDC; the shaded area shows the 95% confidence interval. Get the data and code used [here](https://github.com/slantedlabs/)." %}

{% graphanim anim_id=0 img_paths='dataviz/images/national_gun_deaths_bg_checks_1999.svg dataviz/images/national_gun_deaths_bg_checks_2000.svg dataviz/images/national_gun_deaths_bg_checks_2001.svg dataviz/images/national_gun_deaths_bg_checks_2002.svg dataviz/images/national_gun_deaths_bg_checks_2003.svg dataviz/images/national_gun_deaths_bg_checks_2004.svg dataviz/images/national_gun_deaths_bg_checks_2005.svg dataviz/images/national_gun_deaths_bg_checks_2006.svg dataviz/images/national_gun_deaths_bg_checks_2007.svg dataviz/images/national_gun_deaths_bg_checks_2008.svg dataviz/images/national_gun_deaths_bg_checks_2009.svg dataviz/images/national_gun_deaths_bg_checks_2010.svg dataviz/images/national_gun_deaths_bg_checks_2011.svg dataviz/images/national_gun_deaths_bg_checks_2012.svg dataviz/images/national_gun_deaths_bg_checks_2013.svg dataviz/images/national_gun_deaths_bg_checks_2014.svg dataviz/images/national_gun_deaths_bg_checks_2015.svg'|seplist footnote="Each dot is a CDC-estimated crude rate of gun deaths per 100,000 people for a state. Lines are LOESS smoothings with 95% confidence intervals. The density graphs on the right show the distributions of death rates for states with and without background check laws (law data from Everytown Gun Law Navigator). Get the data and code used [here](https://github.com/slantedlabs/)." %}


[1]: https://wonder.cdc.gov/
[2]: https://everytownresearch.org/navigator/
[3]: https://everytownresearch.org/
