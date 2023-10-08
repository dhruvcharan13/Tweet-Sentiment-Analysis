# Tweet-Sentiment-Analysis
Analyzes the sentiment of a tweet and returns a doughnut chart representing the Positive, Negative and Neutral breakdown of the tweet.

#### Description:
This project is a web application developed using Python and the Flask framework, designed for sentiment analysis of tweets using the Twitter-RoBERTa base model. Users can input a tweet, and the app employs the model to analyze its sentiment, returning the results in the form of an interactive doughnut chart created with Chart.js. The project also includes styling and presentation using HTML and CSS to provide an elegant and user-friendly interface.

### Files and Components
- `app.py`: The main Flask application that handles the web server, form submission, and sentiment analysis.
- `index.html`: The HTML template for the input page where users can enter a tweet for sentiment analysis.
- `result.html`: The HTML template for the result page displaying the sentiment analysis chart and the analyzed data.
- `styles.css`: The CSS file containing styles for the web application's appearance and layout.
- `requirements.txt`: List of Python packages and dependencies required for the project.
- `static/`: Directory containing static assets such as stylesheets, JavaScript files, and fonts.
- `templates/`: Directory containing HTML templates used by Flask.

### Installation and Usage
1. Clone this repository.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Run the Flask application with `python app.py`.
4. Access the application in your web browser at `http://localhost:5000`.

### Project Video Demo
Watch the project video demo [here](URL HERE).

### Acknowledgments
- Twitter-RoBERTa model for sentiment analysis: [Link to Model](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)

### Contact
For questions or inquiries, please contact Dhruv Charan at charanbik1976@gmail.com.
