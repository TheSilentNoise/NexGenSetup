<?php
/**
 * The template for displaying search forms in CloudifyApps
 *
 * @package CloudifyApps
 */
?>
<!--form role="search" method="get" class="search-form" action="<?php echo esc_url( home_url( '/' ) ); ?>">
	<label>
		<input type="search" class="search-field" placeholder="<?php echo esc_attr_x( 'Search...', 'placeholder', 'CloudifyApps' ); ?>" value="<?php echo esc_attr( get_search_query() ); ?>" name="s">
	</label>
	<input type="submit" class="search-submit" value="<?php echo esc_attr_x( 'Search', 'submit button', 'CloudifyApps' ); ?>">
</form-->

<form role="search" method="get" class="search-form" action="<?php echo esc_url( home_url( '/' ) ); ?>">
			<div class="form-row input-group-borderless">
			<div class="col-sm">
                <input type="text"  name="s" class="form-control shadow-none search-box-input" id="course-search-box" placeholder="<?php echo esc_attr_x( 'Search our lastest article here...', 'placeholder', 'CloudifyApps' ); ?>" value="<?php echo esc_attr( get_search_query() ); ?>" aria-label="Search our lastest article here...">
              </div>
              <div class="col-sm-auto">
                <button type="submit" class="btn btn-block btn-primary search-btn">
                  <i class="fas fa-search"></i>
                  <span class="d-sm-none ml-1">Search</span>
                </button>
              </div>
			</div>
</form>
<?php //get_search_form();
?>