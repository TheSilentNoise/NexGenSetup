<?php
/**
 * The main template file
 *
 * This is the most generic template file in a WordPress theme
 * and one of the two required files for a theme (the other being style.css).
 * It is used to display a page when nothing more specific matches a query.
 * E.g., it puts together the home page when no home.php file exists.
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/
 *
 * @package CloudifyApps
 */

get_header();
?>
<header id="head" class="secondary">
          <div class="container">
              <div class="col-md-12">Blogs</div>
              <br/>
              <hr class="bottom-line">
          </div>
</header>


<section id ="pricing" class="section-padding">
  <div class="container">

	<?php get_sidebar();?>   



	  <div class="col-md-9">

		   <!--start loop-->

		  <div class="filterDiv {{blogs[4]}}">
			  <div class="portfolio-item">
				  <div class="portfolio-desc align-center">
					  <div class="inner blog-border">
						  <a href="#">
							  <h3>Blog Title</h3>
						  </a> <i>Posted</i>&nbsp;&nbsp;
						  <span class="inline-block mb16">
							   </span>
						  </a>
						  <hr>
						  <p> &#8230;</p>
						  <div class="pull-right">
						  <a class="btn btn-success" href="#">ReadMore&rarr;</a> <br /> <br />
						  </div>
					  </div>
				  </div>
			  </div>
		  </div>

			   <!--end loop-->

	  </div>

	</div>

  </div>
</section>
		
  

<?php
//get_sidebar();
echo common_get();
get_footer();
