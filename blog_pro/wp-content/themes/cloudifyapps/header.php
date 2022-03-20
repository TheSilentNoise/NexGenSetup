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

  <link rel="shortcut icon" href="<?php bloginfo('template_url'); ?>/img/favicon.png" type="image/x-icon">
    <script src="https://kit.fontawesome.com/a076d05399.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Work+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="<?php echo url(); ?>/wp-content/themes/cloudifyapps/css/app.css">
     <link rel="stylesheet" type="text/css" href="<?php echo url(); ?>/wp-content/themes/cloudifyapps/css/subpage-header.css">
   
   

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
  <body data-spy="scroll" data-offset="70" <?php body_class(); ?> style="background:#fff!important">

	 <!-- header-->
   <!-- <nav class="navbar navbar-default navbar-fixed-top <?//php if(is_front_page()){ echo ''; }else{ echo ' navbar-two'; }; ?>">
      <div class="container">
        <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
         <a class="navbar-brand" style="padding: 0px 0px 0px 9px;"><i class="fa fa-exclamation"></i>earn</a>
		 <?//php  the_custom_logo(); ?>
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
    </nav>-->
<!--/ header-->
<header>
  <nav class="navbar navbar-expand-xl  navbar-dark fixed-top">
         <a class="navbar-brand px-lg-4" href="http://ngi.iearn.tech/"><?php  the_custom_logo(); ?><img src="<?php bloginfo('template_url'); ?>/img/logo-3.png" id="my_image"><spna class="pl-2 logo-name d-lg-inline-block d-xl-inline-block">Next generation innovation</spna></a>
		 
         <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
           <span class="navbar-toggler-icon"></span>
         </button>
       
         <div class="collapse navbar-collapse" id="navbarSupportedContent">
           <ul class="navbar-nav ml-auto px-4 main-menu">
            <li class="nav-item">
               <a class="nav-link" href="http://ngi.iearn.tech/">Home</a>
             </li> 
            <!--  <li class="nav-item dropdown">
               <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Services <i class="fas fa-chevron-down dropdown-icon"></i>
               </a>
               <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                 <a class="dropdown-item" href="#">Online Tutorials</a>
                 <div class="dropdown-divider"></div>
                 
                 <a class="dropdown-item" href="#">Internships</a>
               </div>
             </li>
              -->
              
               <li class="nav-item">
                  
                 <a class="nav-link" href="http://ngi.iearn.tech/courses">Tutorials</a>
               </li>
<!--               <li class="nav-item">-->
<!--                 <a class="nav-link" href="/internships">Internship</a>-->
<!--               </li>-->
               
               <li class="nav-item">
                 <a class="nav-link" href="http://ngi.iearn.tech/testimonials">Testimonials</a>
               </li>


               
          


               
               <li class="nav-item"><a class="nav-link" href="http://ngi.iearn.tech/login" >Login</a></li>
               <li cla
               
               ss="nav-item"><a  class="nav-link reg-btn ml-4" id="btn-reg" href="http://ngi.iearn.tech/signup">Registration</a></li>
           


           
         </ul>
     
         </div>
       </nav>
    
         
    </header>
<body>
    <div class="body">
	
<!--menu-->

