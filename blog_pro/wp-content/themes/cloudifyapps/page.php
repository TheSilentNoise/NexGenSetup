<?php
/**
 * The template for displaying all pages
 *
 * This is the template that displays all pages by default.
 * Please note that this is the WordPress construct of pages
 * and that other 'pages' on your WordPress site may use a
 * different template.
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/
 *
 * @package CloudifyApps
 */

get_header();
?>
      <header id="head" class="secondary">
          <div class="container">
              <div class="col-md-12"><?php the_title(); ?></div>
              <br/>
              <hr class="bottom-line">
          </div>
</header>


<section id ="pricing" class="section-padding">
  <div class="container">

	   

		<?php get_sideber(); ?>



	  <div class="col-md-9">

	

					<?php
					while ( have_posts() ) :
						the_post();

						get_template_part( 'template-parts/content', 'page' );

						//the_post_navigation();

						// If comments are open or we have at least one comment, load up the comment template.
						//if ( comments_open() || get_comments_number() ) :
							//comments_template();
						endif;

					endwhile; // End of the loop.
					?>


					
	  </div>

	</div>

  </div>
</section>
				
<?php
get_footer();
