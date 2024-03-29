 <?php
/**
 * The Header for our theme.
 *
 * Displays all of the <head> section and everything up till <div id="content">
 *
 * @package Yogasana Lite
 */
?><!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width">
<link rel="profile" href="http://gmpg.org/xfn/11">
<link rel="pingback" href="<?php bloginfo( 'pingback_url' ); ?>">
<?php wp_head(); ?>
</head>

<body <?php body_class(); ?>>
<?php
	//wp_body_open hook from WordPress 5.2
	if ( function_exists( 'wp_body_open' ) ) {
	    wp_body_open();
	}else{
		do_action( 'wp_body_open' ); 
	}
?>
<a class="skip-link screen-reader-text" href="#sitemain"><?php _e( 'Skip to content', 'yogasana-lite' ); ?></a>
<?php if(get_theme_mod('phone-txt') != '' || get_theme_mod('email-txt') != '') { ?>
<div id="topbar">
			<div class="top-inner">				
				<div class="top-left">
                	<?php if(get_theme_mod('phone-txt') != '') { ?>
                		<p><i class="fa fa-phone"></i><?php echo esc_html(get_theme_mod('phone-txt')); ?></p>
                    <?php } ?>
                    </div><!-- top-left -->
                    <div class="top-right">
                    <?php if(get_theme_mod('email-txt') != '') { ?>
						<p><i class="fa fa-envelope"></i><a href="<?php echo esc_attr(esc_html('mailto:','yogasana-lite').get_theme_mod('email-txt')); ?>"><?php echo esc_attr(get_theme_mod('email-txt')); ?></a></p>
                    <?php } ?>
				</div><!-- top-right --><div class="clear"></div> 
			</div><!--top-inner-->			
		</div><!-- topbar -->
<?php } ?>
        
<div id="header">
            <div class="header-inner">	
				<div class="logo">
					<?php yogasana_lite_the_custom_logo(); ?>
						<h1><a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home"><?php esc_attr(bloginfo( 'name' )); ?></a></h1>

					<?php $description = get_bloginfo( 'description', 'display' );
					if ( $description || is_customize_preview() ) : ?>
						<p><?php echo esc_html($description); ?></p>
					<?php endif; ?>
				</div>
                  
				<div class="toggle">
						<a class="toggleMenu" href="#"><?php esc_html_e('Menu','yogasana-lite'); ?></a>
				</div> 						
				<div class="main-nav">
						<?php wp_nav_menu( array('theme_location' => 'primary') ); ?>							
				</div>						
				<div class="clear"></div>				
            </div><!-- header-inner -->               
		</div><!-- header -->