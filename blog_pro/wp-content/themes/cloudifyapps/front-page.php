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
      <!--<header id="head" class="secondary">
          <div class="container">
              <div class="col-md-12">Blogs</div>
              <br/>
              <hr class="bottom-line">
          </div>
</header>-->

<div class="jumbotron text-white">
<div class="container pt-2">
  <h2 class="profile-heading">Blog</h2>
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


<section>
  <div class="container">

	 
<div class="row">


	  <div class="col-lg-8">

		   <!--start loop-->
			<?php if(have_posts()): ?>
                        <?php while(have_posts()): ?>
                            <?php the_post(); ?>
								  <div class="filterDiv {{blogs[4]}}">
									  <div class="portfolio-item">
										  <div class="portfolio-desc align-center">
											  <div class="inner blog-border">
												  <a href="<?php the_permalink(); ?>" style="text-decoration:none; color:#212529;">
													  <h3 class="main-heading-blog"><?php echo get_the_title(); ?></h3>
												  </a> <h4 class="author-name">- Posted By <?php the_author(); ?></h4>
												  <span class="inline-block mb16">
													   </span>
												  </a>
												  <hr>
												  <p><?php echo get_the_excerpt(); ?> &#8230;</p>
												  <div class="pull-right">
												  <a class="btn btn-blog" href="<?php the_permalink(); ?>">ReadMore&rarr;</a> <br /> <br />
												  </div>
											  </div>
										  </div>
									  </div>
								  </div>
					<?php endwhile; ?>
                    <?php else: ?>
								<h3>No blog posts found.</h3>
                                <p><br><br><br><br><br><br></p>
					<?php endif; ?>


			   <!--end loop-->

	  </div>
	   
	     <?php get_sidebar();?>
   

	</div>

    </div>
</section>
		


<?php
//get_sidebar();
get_footer();
