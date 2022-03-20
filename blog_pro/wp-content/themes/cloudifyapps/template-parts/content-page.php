<?php
/**
 * Template part for displaying page content in page.php
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/
 *
 * @package CloudifyApps
 */

?>

<article>
	<div class="col-lg-12 col-md-12">
	    <div class="blog-detailss">
	        <h3 class="mb-3"><?php echo get_the_title(); ?></h3>
	        <div class="blog-details-content">
	        	<?php the_content(); ?>
	        	<div class="blog-details-meta dgHidden">
                    <div class="tags">
                        <?php the_tags('','',''); ?>
                    </div>
                    
                    <!--<div class="share">
                        <ul>
                            <li class="title">Share:</li>
                            <li><a href="#"><i class="icofont-facebook"></i></a></li>
                            <li><a href="#"><i class="icofont-twitter"></i></a></li>
                            <li><a href="#"><i class="icofont-instagram"></i></a></li>
                            <li><a href="#"><i class="icofont-twitter"></i></a></li>
                        </ul>
                    </div>-->
                </div>
	        </div>
	    </div>
	</div>
</article>

<?php /*
<article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
	<header class="entry-header">
		<?php the_title( '<h1 class="entry-title">', '</h1>' ); ?>
	</header><!-- .entry-header -->

	<?php cloudifyapps_post_thumbnail(); ?>

	<div class="entry-content">
		<?php
		the_content();

		wp_link_pages( array(
			'before' => '<div class="page-links">' . esc_html__( 'Pages:', 'cloudifyapps' ),
			'after'  => '</div>',
		) );
		?>
	</div><!-- .entry-content -->

	<?php if ( get_edit_post_link() ) : ?>
		<footer class="entry-footer">
			<?php
			edit_post_link(
				sprintf(
					wp_kses(
						// translators: %s: Name of current post. Only visible to screen readers 
						__( 'Edit <span class="screen-reader-text">%s</span>', 'cloudifyapps' ),
						array(
							'span' => array(
								'class' => array(),
							),
						)
					),
					get_the_title()
				),
				'<span class="edit-link">',
				'</span>'
			);
			?>
		</footer><!-- .entry-footer -->
	<?php endif; ?>
</article><!-- #post-<?php the_ID(); ?> -->
<?php */ ?>