<?php
/**
 * The template for displaying all single posts
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/#single-post
 *
 * @package CloudifyApps
 */

get_header();
?>
	
	<?php if(is_singular('post')): ?>
		<!-- Start Page Title Area -->
	<div class="jumbotron text-white">
		<div class="container pt-2">
			<h2 class="profile-heading">
				<?php echo get_the_title(); ?>
			</h2>
	<nav aria-label="breadcrumb">
      <ol class="breadcrumb subheader-list">
        <li class="breadcrumb-item"><a href="http://ngi.iearn.tech/">Home</a></li>
        <li class="breadcrumb-item active" aria-current="page">Blog</li>
      </ol>
    </nav>
      <div class="card search-card p-2 mb-3 col-lg-8">
            
              <?php get_search_form();?>
            
          </div>
  </div>
    
</div>
<?php endif; ?>

<section>
  <div class="container">

	 
<div class="row">


	  <div class="col-lg-8">
	
		        

						<?php
						while ( have_posts() ) :
							the_post();

							get_template_part( 'template-parts/content', get_post_type() );

							//the_post_navigation();

							// If comments are open or we have at least one comment, load up the comment template.
							if ( comments_open() || get_comments_number() ) :
								//comments_template();
							endif;

						endwhile; // End of the loop.
						?>
					
		            </div>
		            
	   <?php get_sidebar();?>

	</div>

  </div>
</section>
		<!-- End News Area -->

<?php
get_footer();
