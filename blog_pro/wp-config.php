<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'ngi_iearn_tech' );

/** MySQL database username */
define( 'DB_USER', 'ngi_user' );

/** MySQL database password */
define( 'DB_PASSWORD', 'NgiP@$$+' );

/** MySQL hostname */
define( 'DB_HOST', '18.144.19.26' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'Z_b_fBsoPp^Yn_B7j?dibr0Ql 1j^,cJ6YS`R$;H]g3{.W0rfE&zHdbM*5q$ x@y' );
define( 'SECURE_AUTH_KEY',  '<#4-EMZgs0b[Eqw`UN4,`j1(73+S#905-_Y]X$&/iB4rjGLpQ#ClkTnCh+p#=dA*' );
define( 'LOGGED_IN_KEY',    'U$DVb6qGbCLeZ<MvC1gtWl-s&hk `z*],&84oLQMEcDf&pB[%*fPK>p0`a>MAa+b' );
define( 'NONCE_KEY',        '2r.z>f9iXzWuYy3Bg1&OcK2nbcf]^`G)U2wPvSnr<aO:9XcwP$k_c)[$y[ry{AXS' );
define( 'AUTH_SALT',        's!!<f.[puX@]wPzik]P2xsd%+HTle3nMzpD{UH5?JJo?qP?7HfN+,zA[[ous+Huj' );
define( 'SECURE_AUTH_SALT', 'J*CW2RxX@ocz0.Kf=QN%RdAoWP_Z;FJD ;cs`eoU1}$!am?c!s1cG3g%WtYC]mXe' );
define( 'LOGGED_IN_SALT',   'j{%N^u]/|;>3b+Iu`-e9aJq!!!& iGY&%Q~j|w;<KgUD|E#WqODD7Q=$4wBs*BB7' );
define( 'NONCE_SALT',       '~Q!8pb/)VMOlT5Cmf*VDq[o?[VEvlnaw^?VoMciXrh=^s9~f2^g,9(z)6%ja%*,S' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'ngib_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
