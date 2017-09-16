Vital Signs of a Changing Planet
================================

@author Andrew Milligan
@date Thu, 17 Aug 2017 13:20:23 -05
@outlet Slant
@image dataviz/images/sea_transparent.png

[[[ NASA's Vital Signs of the Planet describe a planet that is changing
rapidly, with some of the values annually reaching new extremes over all of
human history.  ]]]


The National Aeronautics and Space Administration publishes [vital signs][1]
for the planet. These include measurements of temperature, atmospheric carbon
dioxide, sea level, and polar ice sheet mass&mdash;each of which tells the same
sobering story: the planet is changing.

The first graph below shows the change in average global temperature from a
baseline set at the average global temperature between 1950 and 1981. It shows
a dramatic rise in global temperatures. Further, the rate of that rise is also
increasing.

{@graph
  img_path = "dataviz/images/temp_timeseries.svg"
  footnote = "In grey are the global averages at each measurement; in red is
    the rolling 5-year average. Get the data and code used
    [here](https://github.com/slantedlabs/nasa_climate_change_data). See more
    from NASA
    [here](https://climate.nasa.gov/vital-signs/global-temperature/)."
}

The next graph shows the concentration in parts-per-million of carbon dioxide
in the atmosphere as measured at the Mauna Loa Observatory in Hawaii. Known as
the "[Keeling Curve][2]" after Charles David Keeling, who started the data
collection project, this graph shows a dramatic and unyielding increase in the
amount of carbon dioxide&mdash;an important heat-trapping greenhouse
gas&mdash;in the atmosphere.

{@graph
  img_path = "dataviz/images/co2_timeseries.svg"
  footnote = "In grey are the individual measurements; in red the trend with
    seasonal cycles removed. These data were collected at the Mauna Loa
    Observatory in Hawaii. Get the data and code used
    [here](https://github.com/slantedlabs/nasa_climate_change_data). See more
    from NASA [here](https://climate.nasa.gov/vital-signs/carbon-dioxide/)."
}

Sea level rise exhibits a similar unyielding advance. The graph below shows the
amount of sea level rise in millimeters from a 1993 baseline. Rising seas,
which [threaten][3] some of the largest U.S. cities, are [already dispacing][4]
island communities.


{% graph img_path="dataviz/images/sea_timeseries.svg" footnote="The area and dark blue line show the global mean sea level change from the start of the time series with annual and semiannual cycles removed; the jagged line includes these cycles. These data have Global Isostatic Adjustment applied to adjust for data collection methods. The dark line additionally has a 60-day Gaussian filter applied. Get the data and code used [here](https://github.com/slantedlabs/nasa_climate_change_data). See more from NASA [here](https://climate.nasa.gov/vital-signs/sea-level/)." %}


This final graph shows shrinkage of the Antarctic ice sheet. The shrinkage of
polar ice sheets, sea ice, and glaciers due to rising temperatures contribute
greatly to sea level rise and exacerbate temperature changes by altering the
planet's [albedo][5].


{% graph img_path="dataviz/images/ice_timeseries.svg" footnote="The dark line is a satellite etimate of ice sheet mass; the light region shows 1-&sigma; uncetainty. Get the data and code used [here](https://github.com/slantedlabs/nasa_climate_change_data). See more from NASA [here](https://climate.nasa.gov/vital-signs/land-ice/)." %}


All of these vital signs scream the same thing: we are rapidly&mdash;and
unintentionally&mdash;reshaping our world in dramatic ways, the full
consequences of which we can only wait to discover. While we often tear our
hair and cry that the planet is dying, this is not the case. It's simply
changing. The planet will be fine. It is humanity that is at risk of dying.



[1]: https://climate.nasa.gov/vital-signs/
[2]: https://en.wikipedia.org/wiki/Keeling_Curve
[3]: http://time.com/4257194/sea-level-rise-climate-change-miami/
[4]: https://www.scientificamerican.com/article/sea-level-rise-swallows-5-whole-pacific-islands/
[5]: https://en.wikipedia.org/wiki/Albedo
