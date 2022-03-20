<?php
/**
 * CloudifyApps functions and definitions
 *
 * @link https://developer.wordpress.org/themes/basics/theme-functions/
 *
 * @package CloudifyApps
 */
define('GOOGLE_API_KEY', 'AIzaSyBXhRkC6lQGc3RDvn_b6wk8sFj09Sr7XIg');

if ( ! function_exists( 'cloudifyapps_setup' ) ) :
	/**
	 * Sets up theme defaults and registers support for various WordPress features.
	 *
	 * Note that this function is hooked into the after_setup_theme hook, which
	 * runs before the init hook. The init hook is too late for some features, such
	 * as indicating support for post thumbnails.
	 */
	function cloudifyapps_setup() {
		/*
		 * Make theme available for translation.
		 * Translations can be filed in the /languages/ directory.
		 * If you're building a theme based on CloudifyApps, use a find and replace
		 * to change 'cloudifyapps' to the name of your theme in all the template files.
		 */
		load_theme_textdomain( 'cloudifyapps', get_template_directory() . '/languages' );

		// Add default posts and comments RSS feed links to head.
		add_theme_support( 'automatic-feed-links' );

		/*
		 * Let WordPress manage the document title.
		 * By adding theme support, we declare that this theme does not use a
		 * hard-coded <title> tag in the document head, and expect WordPress to
		 * provide it for us.
		 */
		add_theme_support( 'title-tag' );

		/*
		 * Enable support for Post Thumbnails on posts and pages.
		 *
		 * @link https://developer.wordpress.org/themes/functionality/featured-images-post-thumbnails/
		 */
		add_theme_support( 'post-thumbnails' );

		// This theme uses wp_nav_menu() in one location.
		
		register_nav_menus( array(
			'menu-1' => esc_html__( 'Primary', 'cloudifyapps' ),
		) );
		

		

		/*
		 * Switch default core markup for search form, comment form, and comments
		 * to output valid HTML5.
		 */
		add_theme_support( 'html5', array(
			'search-form',
			'comment-form',
			'comment-list',
			'gallery',
			'caption',
		) );

		// Set up the WordPress core custom background feature.
		add_theme_support( 'custom-background', apply_filters( 'cloudifyapps_custom_background_args', array(
			'default-color' => 'ffffff',
			'default-image' => '',
		) ) );

		// Add theme support for selective refresh for widgets.
		add_theme_support( 'customize-selective-refresh-widgets' );

		/**
		 * Add support for core custom logo.
		 *
		 * @link https://codex.wordpress.org/Theme_Logo
		 */
		add_theme_support( 'custom-logo', array(
			'height'      => 50,
			'width'       => 50,
			'flex-width'  => true,
			'flex-height' => true,
		) );


		add_shortcode( 'template_dir', function( $atts ){
			return get_template_directory_uri() . '/img/' . $atts['image'];
		});
	}
endif;
add_action( 'after_setup_theme', 'cloudifyapps_setup' );

// function awesome_theme_setup() {
// 	add_theme_support('menus');

// 	register_nav_menus('primary', 'Primary Header Navigation');
// }

// add_action('init', 'awesome_theme_setup');

/**
 * Set the content width in pixels, based on the theme's design and stylesheet.
 *
 * Priority 0 to make it available to lower priority callbacks.
 *
 * @global int $content_width
 */
function cloudifyapps_content_width() {
	// This variable is intended to be overruled from themes.
	// Open WPCS issue: {@link https://github.com/WordPress-Coding-Standards/WordPress-Coding-Standards/issues/1043}.
	// phpcs:ignore WordPress.NamingConventions.PrefixAllGlobals.NonPrefixedVariableFound
	$GLOBALS['content_width'] = apply_filters( 'cloudifyapps_content_width', 640 );
}
add_action( 'after_setup_theme', 'cloudifyapps_content_width', 0 );

/**
 * Register widget area.
 *
 * @link https://developer.wordpress.org/themes/functionality/sidebars/#registering-a-sidebar
 */
function cloudifyapps_widgets_init() {
	register_sidebar( array(
		'name'          => esc_html__( 'Sidebar', 'cloudifyapps' ),
		'id'            => 'sidebar-1',
		'description'   => esc_html__( 'Add widgets here.', 'cloudifyapps' ),
		'before_widget' => '<section id="%1$s" class="widget %2$s">',
		'after_widget'  => '</section>',
		'before_title'  => '<h2 class="widget-title">',
		'after_title'   => '</h2>',
	) );
}
add_action( 'widgets_init', 'cloudifyapps_widgets_init' );

/**
 * Enqueue scripts and styles.
 */
function cloudifyapps_scripts() {
	
	$cs=url();
	
	wp_enqueue_style('cloudifyapps-responsive',  $cs.'/css/font.css', '1.0', 'all');
    wp_enqueue_style('cloudifyapps-responsive',  $cs.'cloudifyapps/css/font-awesome.min.css', '1.0', 'all');
    wp_enqueue_style('cloudifyapps-responsive',  $cs.'cloudifyapps/css/bootstrap.min.css', '1.0', 'all');
    wp_enqueue_style('cloudifyapps-responsive',  $cs.'cloudifyapps/css/editor.css', '1.0', 'all');
    wp_enqueue_style('cloudifyapps-responsive',  $cs.'cloudifyapps/css/imagehover.min.css', '1.0', 'all');
    wp_enqueue_style('cloudifyapps-responsive',  $cs.'cloudifyapps/style.css', '1.0', 'all');
  	wp_enqueue_style('cloudifyapps-responsive',  $cs.'cloudifyapps/css/custom.css', '1.0', 'all');
    wp_enqueue_style('cloudifyapps-responsive',  $cs.'cloudifyapps/css/jquery.dataTables.min.css', '1.0', 'all');

	wp_enqueue_script( 'cloudifyapps-skip-link-focus-fix', get_template_directory_uri() . 'cloudifyapps/js/jquery.min.js', array(), '20151215', true );
    wp_enqueue_script( 'cloudifyapps-skip-link-focus-fix', get_template_directory_uri() . 'cloudifyapps/js/jquery.easing.min.js', array(), '20151215', true );
    wp_enqueue_script( 'cloudifyapps-skip-link-focus-fix', get_template_directory_uri() . 'cloudifyapps/js/bootstrap.min.js', array(), '20151215', true );
    wp_enqueue_script( 'cloudifyapps-skip-link-focus-fix', get_template_directory_uri() . 'cloudifyapps/js/editor.js', array(), '20151215', true );
    wp_enqueue_script( 'cloudifyapps-skip-link-focus-fix', get_template_directory_uri() . 'cloudifyapps/js/custom.js', array(), '20151215', true );
    wp_enqueue_script( 'cloudifyapps-skip-link-focus-fix', get_template_directory_uri() . 'cloudifyapps/js/jquery.dataTables.min.js', array(), '20151215', true );
    wp_enqueue_script( 'cloudifyapps-skip-link-focus-fix', get_template_directory_uri() . 'cloudifyapps/js/app-script.js', array(), '20151215', true );






	if ( is_singular() && comments_open() && get_option( 'thread_comments' ) ) {
		wp_enqueue_script( 'comment-reply' );
	}
	//echo get_template_directory_uri();
}
add_action( 'wp_enqueue_scripts', 'cloudifyapps_scripts' );

/**
 * Implement the Custom Header feature.
 */
require get_template_directory() . '/inc/custom-header.php';

/**
 * Custom template tags for this theme.
 */
require get_template_directory() . '/inc/template-tags.php';

/**
 * Functions which enhance the theme by hooking into WordPress.
 */
require get_template_directory() . '/inc/template-functions.php';

/**
 * Customizer additions.
 */
require get_template_directory() . '/inc/customizer.php';

/**
 * Load Jetpack compatibility file.
 */
if ( defined( 'JETPACK__VERSION' ) ) {
	require get_template_directory() . '/inc/jetpack.php';
}


/*** DG ***/
function bootstrap_pagination( \WP_Query $wp_query = null, $echo = true ) {
	if ( null === $wp_query ) {
		global $wp_query;
	}
	$pages = paginate_links( [
			'base'         => str_replace( 999999999, '%#%', esc_url( get_pagenum_link( 999999999 ) ) ),
			'format'       => '?paged=%#%',
			'current'      => max( 1, get_query_var( 'paged' ) ),
			'total'        => $wp_query->max_num_pages,
			'type'         => 'array',
			'show_all'     => false,
			'end_size'     => 3,
			'mid_size'     => 1,
			'prev_next'    => true,
			'prev_text'    => __( '<i class="icofont-double-left"></i>' ),
			'next_text'    => __( '<i class="icofont-double-right"></i>' ),
			'add_args'     => false,
			'add_fragment' => ''
		]
	);
	if ( is_array( $pages ) ) {
		//$paged = ( get_query_var( 'paged' ) == 0 ) ? 1 : get_query_var( 'paged' );
		$pagination = '<div class="paginations"><ul class="pagination justify-content-center">';
		foreach ( $pages as $page ) {
			$pagination .= '<li class="page-item '.(strpos($page, 'current') !== false ? 'active' : '').'"> ' . str_replace( 'page-numbers', 'page-link', $page ) . '</li>';
		}
		$pagination .= '</ul></div>';
		if ( $echo ) {
			echo $pagination;
		} else {
			return $pagination;
		}
	}
	return null;
}

add_image_size( 'blog-size', 370, 246, true );

function url(){
  return get_site_url();
	  /*sprintf(
    "%s://%s%s",
    isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] != 'off' ? 'https' : 'http',
    $_SERVER['SERVER_NAME'],
    $_SERVER['REQUEST_URI']
  );*/
}
function file_checker($file){
	$fileLOC=WP_CONTENT_URL;
	$file = str_replace($fileLOC,"",$file);
    
    $location = WP_CONTENT_URL;// you can edit this <=
    $location = str_replace("http://","",$location);
    $location = str_replace("https://","",$location);
    $location = str_replace($_SERVER['HTTP_HOST'],"",$location);
    $location = $_SERVER['DOCUMENT_ROOT'].$location;
	$file=str_replace($fileLOC,"",$file);
    $filename = $location.$file;
	//print_r($filename);
	//exit();
	
	//$filename="D:/wamp/www/blog_pro/wp-content/uploads/2021/01/p1.jpeg";
    if (file_exists($filename)) {

        return true;
    } else {
        return false;
    }
}
/*url();
function common_get(){ 
	$htmlcss='<link rel="stylesheet" type="text/css" href="'.url().'"/wp-content/themes/cloudifyapps/css/font.css">';
    $htmlcss.='<link rel="stylesheet" type="text/css" href="'.url().'"/wp-content/themes/cloudifyapps/css/font-awesome.min.css">';
    $htmlcss.='<link rel="stylesheet" type="text/css" href="'.url().'"/wp-content/themes/cloudifyapps/css/bootstrap.min.css">';
    $htmlcss.='<link rel="stylesheet" type="text/css" href="'.url().'"/wp-content/themes/cloudifyapps/css/editor.css">';
    $htmlcss.='<link rel="stylesheet" type="text/css" href="'.url().'"/wp-content/themes/cloudifyapps/css/imagehover.min.css">';
    $htmlcss.='<link rel="stylesheet" type="text/css" href="'.url().'"/wp-content/themes/cloudifyapps/css/style.css">';
  	$htmlcss.='<link rel="stylesheet" type="text/css" href="'.url().'"/wp-content/themes/cloudifyapps/css/custom.css">';
    $htmlcss.='<link rel="stylesheet" type="text/css" href="'.url().'"/wp-content/themes/cloudifyapps/css/jquery.dataTables.min.css">';
	$htmlcss.='<script src="'.url() .'"/wp-content/themes/cloudifyapps/js/jquery.min.js"></script>';
    $htmlcss.='<script src="'.url() .'"/wp-content/themes/cloudifyapps/js/jquery.easing.min.js"></script>';
    $htmlcss.='<script src="'.url() .'"/wp-content/themes/cloudifyapps/js/bootstrap.min.js"></script>';
    $htmlcss.='<script src="'.url() .'"/wp-content/themes/cloudifyapps/js/editor.js"></script>';
    $htmlcss.='<script src="'.url() .'"/wp-content/themes/cloudifyapps/js/custom.js"></script>';
    $htmlcss.='<script src="'.url() .'"/wp-content/themes/cloudifyapps/js/jquery.dataTables.min.js"></script>';
    $htmlcss.='<script src="'.url() .'"/wp-content/themes/cloudifyapps/js/app-script.js"></script>';
	return $htmlcss;

}*/