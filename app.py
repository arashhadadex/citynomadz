from flask import Flask, render_template, jsonify, redirect, url_for
from flask_compress import Compress
from flask_caching import Cache
import time

app = Flask(__name__)

# Configure Flask-Caching with Redis
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_HOST'] = 'localhost'
app.config['CACHE_REDIS_PORT'] = 6379
cache = Cache(app)

# This below command enables Gzip compression for the Flask app
# It compresses responses before sending them to clients,
# reducing data transfer and improving performance
Compress(app)

@app.route('/')
def index():
    start_time = time.time()
    response = render_template('index.html')
    end_time = time.time()
    app.logger.info(f"Index page rendering time: {end_time - start_time:.4f} seconds")
    return response

@app.route('/cities')
def cities_home():
    start_time = time.time()
    response = render_template('cities_home.html')
    end_time = time.time()
    app.logger.info(f"Cities home page rendering time: {end_time - start_time:.4f} seconds")
    return response

@app.route('/yerevan')
def old_yerevan_redirect():
    return redirect(url_for('yerevan'), code=301)


@app.route('/cities/yerevan')
def yerevan():
    return render_template('yerevan.html')


@app.route('/cities/dubai')
def dubai():
    return render_template('dubai.html')

@app.route('/cities/dubai/cost_of_living')
def dubai_cost_of_living():
    return render_template('dubai_cost_of_living.html')

@app.route('/cities/dubai/burj_khalifa')
def dubai_burj_khalifa():
    return render_template('dubai_burj_khalifa.html')

@app.route('/cities/yerevan/cost_of_living')
def yerevan_cost_of_living():
    return render_template('yerevan_cost_of_living.html')

@app.route('/cities/yerevan/<page_name>')
def yerevan_subpage(page_name):
    # This route will handle all subpages under /cities/yerevan/
    # It will try to render a template with the same name as the page_name
    return render_template(f'{page_name}.html')


@app.route('/blogs')
def blog_home():
    start_time = time.time()
    response = render_template('blog_home.html')
    end_time = time.time()
    app.logger.info(f"Blog home page rendering time: {end_time - start_time:.4f} seconds")
    return response

@app.route('/blogs/<blog_name>')
def blog_post(blog_name):
    return render_template(f'{blog_name}.html')

@app.route('/blogs/crypto-travel-article')
def crypto_travel_article():
    return render_template('crypto-travel-article.html')
@app.route("/blogs/Why_Camping_Might_Be_the_Answer")
def camping_blog():
    return render_template("Why_Camping_Might_Be_the_Answer.html")

@app.route("/blogs/yerevan_travel_experience")
def yerevan_travel_experience():
    return render_template("yerevan_travel_experience.html")

@app.route('/slow')
@cache.cached(timeout=60)
def slow():
    time.sleep(2)  # Simulate a slow response
    return jsonify(message="This request was slow!")

@app.route('/compress')
def compress_route():
    return "<h1>Welcome to the optimized Flask app !</h1>"

if __name__ == '__main__':
    app.run(debug=False)