Why We Need Affirmative Action
==============================

@author Andrew Milligan
@date Sun, 06 Aug 2017 11:27:34 -05
@outlet Slant
@image dataviz/images/usa_map_warhol.png

[[[ Black people are attending college at much lower rates than white
people. Completing any years of college has a measurable impact on lifetime
earnings; completing a four year degree can increase lifetime earnings by
nearly a million dollars. Racial disparity in college attendance perpetuates
a racial disparity in wealth distribution. ]]]

President Trump's [recent push][1] to have the Justice Department sue
universities over affirmative action policies has triggered a national debate
about racial discrimination against white students. Some, like [David Harsanyi
from The Federalist][2], hold that the federal government has no business
meddling in college admission policies, though any interference might as well
work to "undo institutional discrimination against white and Asian kids".
Others, like [Jelanie Cobb from The New Yorker][3], argue that by curbing
affirmative action, the administration is constructing a "racial protectionism"
that favors white people as the "unheralded disadvantaged class in America".

I dug into some data in order to provide some context for this debate. All of
the data analyzed were collected from [IPUMS-USA][4], a project from the
University of Minnesota.

The graph below shows the percentages of white and black people who had
completed four years of college between 1950 and 2015. Both white and black
people have been completing four years of college at increasing rates since
1950, but there has always been a racial disparity. Further, that disparity has
only been exacerbated over time as the rate of incrase for whites has
dramatically outpaced that for blacks. In 2015 white people were nearly **twice
as likely** as black people to complete four years of college.

{@graph
  img_path = "dataviz/images/race_college_timeseries.svg"
  footnote = "Data came from [IPUMS-USA](https://www.ipums.org/). Get the code
    used [here](https://github.com/slantedlabs/affirmative_action_data)."
}

Such a gap in college attendance could, in theory, be explained by a systematic
racial disparity in desire to go to college, but the assumption of such a
disparity is indisputably rooted in racism. If we assume that, all else being
equal, white and black people have, on average, the same desire and ability to
complete four years of college, then such a sharp difference in the rates at
which they do can only indicate the presence of systematic barriers that hinder
black people but do not encumber whites.

Perhaps, though, white and black people enter college at the same rate and
black people simply suffer a higher attrition rate. The graph below debunks
this hypothesis; it displays the percentages of the white and black populations
that completed each successive year of college between 1950 and 2015. The rates
of attrition from one year to the next are remarkably similar across the entire
time period. Yet again, we see that over time, the percentages of both whites
and black that complete each year of college have increased significantly, but
white people have always completed each successive year of college at much
higher rates than  black people.

{@graph
  img_path = 'dataviz/images/completion_year.gif'
  footnote = "Data came from [IPUMS-USA](https://www.ipums.org/). Get the code
    used [here](https://github.com/slantedlabs/affirmative_action_data)."
}

The fact that white people are, and have been, attending and completing college
at much higher rates than black people, coupled with the fact that these rates
have been increasing for whites much more rapidly than for blacks, indicates
that there are external factors inhibiting the collegiate achievements of black
people. Negating the effects of such factors&mdash;and, ideally, reversing their
historic effects&mdash;is exactly the purpose of affirmative action. Until
black people are able to attend college at the same rates as their white peers,
affirmative action policies are vital to the development of racial equality.



[1]: https://www.washingtonpost.com/world/national-security/justice-department-plans-new-project-to-sue-universities-over-affirmative-action-policies/2017/08/01/6295eba4-772b-11e7-8f39-eeb7d3a2d304_story.html?hpid=hp_hp-top-table-main_affirmative-1124pm-2-1:homepage/story&tid=a_inl&utm_term=.68f9da104827
[2]: https://thefederalist.com/2017/08/02/government-out-college-admissions/
[3]: http://www.newyorker.com/news/news-desk/in-trumps-world-whites-are-the-only-disadvantaged-class
[4]: https://www.ipums.org/
