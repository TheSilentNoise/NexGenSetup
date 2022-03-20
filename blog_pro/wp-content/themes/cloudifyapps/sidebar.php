<?php
/**
 * The sidebar containing the main widget area
 *
 * @link https://developer.wordpress.org/themes/basics/template-files/#template-partials
 *
 * @package CloudifyApps
 */

/*if ( ! is_active_sidebar( 'sidebar-1' ) ) {
	return;
}
?>

<aside id="secondary" class="widget-area">
	<?php dynamic_sidebar( 'sidebar-1' ); ?>
</aside><!-- #secondary -->*/
 

?>
<div class ="col-lg-4 pl-lg-5">

		<div class="holder">
				
				<div class="blog-recent">
					<h4>Blog Categories</h4>
					<hr/>
						
								<li ><a href="<?php echo url(); ?>" onclick="filterSelection('all')">All </a></li>
								<?php $categories = get_categories();
								foreach($categories as $category) {
								   echo '<li class="active"><a href="' . get_category_link($category->term_id) . '">' . $category->name . '</a></li>';
								}?>
								<!--start loop
								<li><a href="#" onclick="cat(1)">Cat1</a></li>
								<!--end loop-->
							
					</div>

					 <div class="blog-recent"><br/>
						<h4>Recently added ...</h4><hr/>
						  <!--start loop-->
						  <?php
                $args = array( 'post_type' => 'post', 'posts_per_page' => 5 );
                $loop = new WP_Query( $args );
                if($loop->have_posts()){
                while ( $loop->have_posts() ) : $loop->the_post();

                ?>
				<!--start loop-->
							
							<li><a href="<?php echo get_permalink(); ?>" ><?php the_title(); ?></a></li></br>
						  <!--end loop-->
						  <?php

                endwhile;
            }else{
                echo "<h3 style='text-align:center; width: 100%;'>No Recent Posts</h3>";
            }
            ?>

					 </div>

					<br/>


				</div>



		</div>
