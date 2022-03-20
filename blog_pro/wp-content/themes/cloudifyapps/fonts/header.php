<?php
/**
 * The header for our theme
 *
 * This is the template that displays all of the <head> section and everything up until <div id="content">
 *
 * @link https://developer.wordpress.org/themes/basics/template-files/#template-partials
 *
 * @package CloudifyApps
 */

?>
<!doctype html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>IEarn.Tech</title>
    <meta name="description" content="Learn Today...Earn Tomorrow">
	<?php wp_head(); 
	//echo url();
	//echo common_get();
?>


    <link rel="stylesheet" type="text/css" href="<?php echo url(); ?>/wp-content/themes/cloudifyapps/css/font.css">
    <link rel="stylesheet" type="text/css" href="<?php echo url(); ?>/wp-content/themes/cloudifyapps/css/font-awesome.min.css">
    <link rel="stylesheet" type="text/css" href="<?php echo url(); ?>/wp-content/themes/cloudifyapps/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="<?php echo url(); ?>/wp-content/themes/cloudifyapps/css/editor.css">
    <link rel="stylesheet" type="text/css" href="<?php echo url(); ?>/wp-content/themes/cloudifyapps/css/imagehover.min.css">
    <link rel="stylesheet" type="text/css" href="<?php echo url(); ?>/wp-content/themes/cloudifyapps/css/style.css">
  	<link rel="stylesheet" type="text/css" href="<?php echo url(); ?>/wp-content/themes/cloudifyapps/css/custom.css">
      <link rel="stylesheet" type="text/css" href="<?php echo url(); ?>/wp-content/themes/cloudifyapps/css/jquery.dataTables.min.css">


                       <!--Start of Tawk.to Script-->
            <script type="text/javascript">
            var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
            (function(){
            var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
            s1.async=true;
            s1.src='https://embed.tawk.to/5b1abe2010b99c7b36d4c236/default';
            s1.charset='UTF-8';
            s1.setAttribute('crossorigin','*');
            s0.parentNode.insertBefore(s1,s0);
            })();
            </script>
            <!--End of Tawk.to Script-->


      <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=UA-117491687-1"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());

          gtag('config', 'UA-117491687-1');
        </script>


</head>
<!--header part-->

<!--menu-->
  <body data-spy="scroll" data-offset="70" <?php body_class(); ?>>

	 <!-- header-->
    <nav class="navbar navbar-default navbar-fixed-top <?php if(is_front_page()){ echo ''; }else{ echo ' navbar-two'; }; ?>">
      <div class="container">
        <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
         <a class="navbar-brand" style="padding: 0px 0px 0px 9px;"><i class="fa fa-exclamation"></i>earn</a>
		 <?php  the_custom_logo(); ?>
        </div>
        <div class="collapse navbar-collapse" id="myNavbar" style="padding: 8px 70px 0px 0px;">
        <ul class="nav navbar-nav navbar-right">
            <li><a href="http://ngi.iearn.tech/">Home</a></li>
			<li><a href="http://ngi.iearn.tech/courses">Courses</a></li>
			<li><a href="http://ngi.iearn.tech/internships">Internships</a></li>
			<li><a href="http://ngi.iearn.tech/login" >Login</a></li>
			<li class="btn-trial"><a href="http://ngi.iearn.tech/signup">Sign up</a></li>
        </ul>
        </div>
      </div>
    </nav>
<!--/ header-->
<br/><br/>

<body>
    <div class="body">
	
<!--menu-->

