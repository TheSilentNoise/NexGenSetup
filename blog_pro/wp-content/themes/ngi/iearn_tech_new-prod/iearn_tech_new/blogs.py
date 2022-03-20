from flask import render_template
from app import app
from models import *
from flask_login import current_user
from sqlalchemy import desc,func
from models import db


########## blogs #############


@app.route('/blogs')
def blogs():
    blogs = Blogs.query.with_entities(Blogs.id,
                                       Blogs.blog_name,
                                       Blogs.blog_url,
                                       Blogs.blog_description,
                                       Blogs.blog_category_id,
                                       Blogs.blog_author,
                                       Blogs.date_created
                                       ).order_by(desc(Blogs.date_created)).all()

    blogs_categories = Blog_category.query.with_entities(Blog_category.id,
                            Blog_category.blog_category_name).distinct().all()

    recentblogs = Blogs.query.with_entities(Blogs.id,Blogs.blog_name,Blogs.blog_url
                       ).order_by(desc(Blogs.date_created)).limit(10).all()

    blog_lists = []

    categorylist = []

    for blog in blogs:
        blog_lists.append(blog)

    for category in blogs_categories:
        categorylist.append(category)


    if current_user.is_authenticated:
      return render_template('blogs.html',
                             categorylist=categorylist,blog_lists=blog_lists,recentblogs=recentblogs)
    return render_template('blogs.html',categorylist=categorylist,blog_lists=blog_lists,recentblogs=recentblogs)


@app.route('/api-concepts')
def api_concepts():
    return render_template('blogs/api-concepts.html')


@app.route('/java-collection-cheatsheet')
def java_collection_cheatsheet():
    return render_template('blogs/java-collection-cheatsheet.html')


@app.route('/apache-common-chains')
def apache_common_chains():
    return render_template('blogs/apache-common-chains.html')



@app.route('/fetch-data-from-sql-server-using-spark-sql')
def fetch_data_from_sql_server_using_spark_sql():
    return render_template('blogs/fetch-data-from-sql-server-using-spark-sql.html')

@app.route('/big-data-skewed')
def big_data_skewed():
    return render_template('blogs/big-data-skewed.html')


@app.route('/repartitioning-and-coalesce-in-spark')
def repartitioning_and_coalesce_in_spark():
    return render_template('blogs/repartitioning-and-coalesce-in-spark.html')


@app.route('/configuring-virtualenv')
def configuring_virtualenv():
    return render_template('blogs/configuring-virtualenv.html')


@app.route('/gpu-db-concepts')
def gpu_db_concepts():
    return render_template('blogs/gpu-db-concepts.html')

@app.route('/mapd-on-docker')
def mapd_on_docker():
    return render_template('blogs/mapd-on-docker.html')

@app.route('/aws-rds-installation')
def aws_rds_installation():
    return render_template('blogs/aws-rds-installation.html')
