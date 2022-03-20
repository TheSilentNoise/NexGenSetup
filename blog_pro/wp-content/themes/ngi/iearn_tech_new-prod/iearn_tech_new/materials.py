from flask import render_template,redirect,url_for,abort
from app import app
from models import *
from sqlalchemy import desc
from flask_login import login_required,current_user

####################################### course materials #######################################


############ python basics

@login_required
@app.route('/python-environment-setup')
def python_env_setup():
    if current_user.is_authenticated:
       return render_template('materials/python-env-setup.html')
    return redirect(url_for('login'))


@login_required
@app.route('/python-basics-material')
def python_basics():
    if current_user.is_authenticated:
       return render_template('materials/python-basics.html')
    return redirect(url_for('login'))



@login_required
@app.route('/python-algorithm-material')
def python_algorithm():
    if current_user.is_authenticated:
       return render_template('materials/python-algorithms.html')
    return redirect(url_for('login'))



@login_required
@app.route('/python-data-structure-algorithm-material')
def python_datastructure_algorithm_material():
    if current_user.is_authenticated:
       return render_template('materials/python-data-structure.html')
    return redirect(url_for('login'))



########## data analysis

@login_required
@app.route('/data-analysis-using-pandas-material')
def data_analysis_using_pandas_material():
    if current_user.is_authenticated:
       return render_template('materials/pandas.html')
    return redirect(url_for('login'))


@login_required
@app.route('/data-analysis-using-numpy-material')
def data_analysis_using_numpy_material():
    if current_user.is_authenticated:
       return render_template('materials/numpy.html')
    return redirect(url_for('login'))


@login_required
@app.route('/data-analysis-using-scipy-material')
def data_analysis_using_scipy_material():
    if current_user.is_authenticated:
       return render_template('materials/scipy.html')
    return redirect(url_for('login'))



@login_required
@app.route('/exploratory-data-analysis')
def exploratory_data_analysis():
    if current_user.is_authenticated:
       return render_template('materials/exploratory-data-analysis.html')
    return redirect(url_for('login'))


@login_required
@app.route('/exploratory-data-analysis-2')
def exploratory_data_analysis_2():
    if current_user.is_authenticated:
       return render_template('materials/exploratory-data-analysis-2.html')
    return redirect(url_for('login'))



@login_required
@app.route('/data-wrangling')
def data_wrangling():
    if current_user.is_authenticated:
       return render_template('materials/data-wrangling.html')
    return redirect(url_for('login'))


########### visualization ####

@login_required
@app.route('/data-visualization-using-seaborn-material')
def data_visualization_using_seaborn_material():
    if current_user.is_authenticated:
       return render_template('materials/seaborn.html')
    return redirect(url_for('login'))


@login_required
@app.route('/data-visualization-using-matplotlib-material')
def data_visualization_using_matplotlib_material():
    if current_user.is_authenticated:
       return render_template('materials/matplotlib.html')
    return redirect(url_for('login'))


@login_required
@app.route('/data-visualization-using-plotly-material')
def data_visualization_using_plotly_material():
    if current_user.is_authenticated:
       return render_template('materials/plotly.html')
    return redirect(url_for('login'))


@login_required
@app.route('/different-types-data-visualization')
def different_types_data_visualization():
    if current_user.is_authenticated:
       return render_template('materials/different-visualization.html')
    return redirect(url_for('login'))



######### flask

@login_required
@app.route('/flask-for-beginners-material')
def flask_for_beginners_material():
    if current_user.is_authenticated:
       return render_template('materials/flask-for-beginners.html')
    return redirect(url_for('login'))


@login_required
@app.route('/flask-templates-material')
def flask_templates():
    if current_user.is_authenticated:
       return render_template('materials/flask-templates.html')
    return redirect(url_for('login'))


## statistics

@login_required
@app.route('/probability-material')
def probability_material():
    if current_user.is_authenticated:
       return render_template('materials/probability.html')
    return redirect(url_for('login'))




@login_required
@app.route('/basic-statistics-material')
def basic_statistics_material():
    if current_user.is_authenticated:
       return render_template('materials/basic-statistics.html')
    return redirect(url_for('login'))


###################################### exercise & solution  #####################################



@login_required
@app.route('/pandas-excercise-solutions')
def pandas_excercise_solutions():
    if current_user.is_authenticated:
       return render_template('exercise_solutions/exercise-solution-pandas.html')
    return redirect(url_for('login'))


@login_required
@app.route('/pandas-excercise')
def pandas_excercise():
    if current_user.is_authenticated:
       return render_template('exercise_solutions/exercise-pandas.html')
    return redirect(url_for('login'))


@login_required
@app.route('/numpy-excercise')
def numpy_excercise():
    if current_user.is_authenticated:
       return render_template('exercise_solutions/exercise-numpy.html')
    return redirect(url_for('login'))

@login_required
@app.route('/numpy-excercise-solutions')
def numpy_excercise_solutions():
    if current_user.is_authenticated:
       return render_template('exercise_solutions/exercise-solution-numpy.html')
    return redirect(url_for('login'))

@login_required
@app.route('/exercise-matplotlib')
def exercise_matplotlib():
    if current_user.is_authenticated:
       return render_template('exercise_solutions/exercise-matplotlib.html')
    return redirect(url_for('login'))


@login_required
@app.route('/exercise-seaborn')
def exercise_seaborn():
    if current_user.is_authenticated:
       return render_template('exercise_solutions/exercise-seaborn.html')
    return redirect(url_for('login'))



@login_required
@app.route('/exercise-solution-matplotlib')
def exercise_solution_matplotlib():
    if current_user.is_authenticated:
       return render_template('exercise_solutions/exercise-solution-matplotlib.html')
    return redirect(url_for('login'))


@login_required
@app.route('/exercise-solution-seaborn')
def exercise_solution_seaborn():
    if current_user.is_authenticated:
       return render_template('exercise_solutions/exercise-solution-seaborn.html')
    return redirect(url_for('login'))


@login_required
@app.route('/exercise-solution-python-1')
def exercise_solution_python():
    if current_user.is_authenticated:
       return render_template('exercise_solutions/exercise-solution-python-1.html')
    return redirect(url_for('login'))


@login_required
@app.route('/exercise-python-1')
def exercise_python():
    if current_user.is_authenticated:
       return render_template('exercise_solutions/exercise-python-1.html')
    return redirect(url_for('login'))


@login_required
@app.route('/exercise-basic-stats')
def exercise_basic_stats():
    if current_user.is_authenticated:
       return render_template('exercise_solutions/exercise-basic-stats.html')
    return redirect(url_for('login'))


@login_required
@app.route('/exercise-solution-basic-stats')
def exercise_solution_basic_stats():
    if current_user.is_authenticated:
       return render_template('exercise_solutions/exercise-solution-basic-stats.html')
    return redirect(url_for('login'))



@login_required
@app.route('/data-structure-exercise')
def data_structure_excercise():
    if current_user.is_authenticated:
       return render_template('exercise_solutions/exercise-data-structure.html')
    return redirect(url_for('login'))


@login_required
@app.route('/data-structure-exercise-solution')
def data_structure_excercise_solutions():
    if current_user.is_authenticated:
       return render_template('exercise_solutions/exercise-solution-data-structure.html')
    return redirect(url_for('login'))