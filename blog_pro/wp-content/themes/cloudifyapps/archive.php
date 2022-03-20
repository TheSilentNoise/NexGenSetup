<?php
/**
 * The template for displaying archive pages
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/
 *
 * @package CloudifyApps
 */

get_header();
?>
<div class="jumbotron text-white">
<div class="container pt-2">
	<?php if ( have_posts() ) : ?>
		  <?php
				the_archive_title( '<h2 class="profile-heading">', '</h2>' );
				
				?>
<nav aria-label="breadcrumb">
      <ol class="breadcrumb subheader-list">
        <li class="breadcrumb-item"><a href="http://ngi.iearn.tech/">Home</a></li>
        <li class="breadcrumb-item active" aria-current="page"><a href="">Blog</a></li>
      </ol>
    </nav>
     <div class="card search-card p-2 mb-3 col-lg-8">
            
              <?php get_search_form();?>
            
          </div>
  </div>
    
</div>
<section>
  <div class="container">

	 
<div class="row">


	  <div class="col-lg-8">

	   
	

			<?php
			/* Start the Loop */
			while ( have_posts() ) :
			?>
			
				<?php the_post();

				/*
				 * Include the Post-Type-specific template for the content.
				 * If you want to override this in a child theme, then include a file
				 * called content-___.php (where ___ is the Post Type name) and that will be used instead.
				 */
				get_template_part( 'template-parts/content', get_post_type() ); ?>
												
			<?php endwhile;

			//the_posts_navigation();

		else :

			get_template_part( 'template-parts/content', 'none' );

		endif;
		?>

		</div>
		<?php get_sidebar();?>

		

	</div>

  </div>
</section>
<?php

get_footer();
