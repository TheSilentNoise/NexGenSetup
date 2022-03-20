<?php
/**
 * Template part for displaying posts
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/
 *
 * @package CloudifyApps
 */

?>

<article>
	
			<div class="filterDiv">
				<div class="portfolio-item">
				   <div class="portfolio-desc align-center">
						    <div class="inner blog-border">
							<?php if(has_post_thumbnail()): ?>
								<img src="<?php echo get_the_post_thumbnail_url(); ?>" alt="<?php echo get_the_title(); ?>">
							<?php else: ?>
								<img src="<?php echo get_template_directory_uri() . '/img/blog-details.jpg'; ?>" alt="<?php echo get_the_title(); ?>">
							<?php endif; ?>
							
								<h3><?php echo get_the_title(); ?></h3>
								
									<i>Posted By: <?php the_author(); ?></i>
									<div class="date">
										<span><?php the_date('j F'); ?></span>
									</div>
									<li><a href="#postCommentArea"><i class="icofont-comment"></i> <?php echo get_comments_number(); ?></a></li>
								
							
									<p><?php the_content(); ?></p>
								
									<div class="tags">
										<?php the_tags('','',''); ?>
									</div>
								
								
						</div>
					</div>
				</div>
			</div>
	
</article>

<?php /* ?>
<article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
	<header class="entry-header">
		<?php
		if ( is_singular() ) :
			the_title( '<h1 class="entry-title">', '</h1>' );
		else :
			the_title( '<h2 class="entry-title"><a href="' . esc_url( get_permalink() ) . '" rel="bookmark">', '</a></h2>' );
		endif;

		if ( 'post' === get_post_type() ) :
			?>
			<div class="entry-meta">
				<?php
				cloudifyapps_posted_on();
				cloudifyapps_posted_by();
				?>
			</div><!-- .entry-meta -->
		<?php endif; ?>
	</header><!-- .entry-header -->

	<?php cloudifyapps_post_thumbnail(); ?>

	<div class="entry-content">
		<?php
		the_content( sprintf(
			wp_kses(
				// translators: %s: Name of current post. Only visible to screen readers 
				__( 'Continue reading<span class="screen-reader-text"> "%s"</span>', 'cloudifyapps' ),
				array(
					'span' => array(
						'class' => array(),
					),
				)
			),
			get_the_title()
		) );

		wp_link_pages( array(
			'before' => '<div class="page-links">' . esc_html__( 'Pages:', 'cloudifyapps' ),
			'after'  => '</div>',
		) );
		?>
	</div><!-- .entry-content -->

	<footer class="entry-footer">
		<?php cloudifyapps_entry_footer(); ?>
	</footer><!-- .entry-footer -->
</article><!-- #post-<?php the_ID(); ?> -->
<?php */ ?>