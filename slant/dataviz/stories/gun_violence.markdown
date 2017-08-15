Gun Deaths and Background Checks
================================

@author Andrew Milligan
@date Tue, 15 Aug 2017 02:05:59 Z
@outlet Slant
@djangotags static
@localimages dataviz/images/missouri_gun_deaths.svg

[[[ A lack of laws requiring criminal background checks for gun sales by
unlicensed vendors correlates with higher rates of gun deaths. ]]]

I gathered the data presented here from two sources: I got data on underlying
causes of death between 1999 and 2015 from the [CDC Wonder][1] web portal, and
I got data on state gun laws from the [Everytown Gun Law Navigator][2].

<div class="graph-wrapper">
  <img src="{% static 'dataviz/images/missouri_gun_deaths.svg' %}" width=100%>
</div>


<div class="graph-wrapper">
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_1999.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2000.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2001.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2002.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2003.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2004.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2005.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2006.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2007.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2008.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2009.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2010.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2011.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2012.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2013.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2014.svg' %}" width=100%>
  <img class="slide" src="{% static 'dataviz/images/national_gun_deaths_bg_checks_2015.svg' %}" width=100%>
</div>


[1]: https://wonder.cdc.gov/
[2]: https://everytownresearch.org/navigator/
[3]: https://everytownresearch.org/


<script>
	var slideIndex = 0;
	carousel();

	function carousel() {
			var i;
			var x = document.getElementsByClassName("slide");
			for (i = 0; i < x.length; i++) {
				x[i].style.display = "none"; 
			}
			slideIndex++;
			if (slideIndex > x.length) {slideIndex = 1} 
			x[slideIndex-1].style.display = "block"; 
			setTimeout(carousel, 500); // Change image every 0.5 second
	}
</script>
