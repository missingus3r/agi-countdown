# CountdownToAi.com
# Road to AGI

Countdown for Artifical General Intelligence by Metaculus predictions.

After ~the death of~ https://aicountdown.com/ (now fixed and alive) i decided to make my own site:

  https://countdowntoai.com/

This project is a simple web application that displays a countdown timer to an estimated date of achieving Artificial General Intelligence (AGI). The estimated date is parsed from the [Metaculus question](https://www.metaculus.com/questions/3479/date-weakly-general-ai-is-publicly-known/) page.

## Prerequisites

- Python 3

Dependencies:

- BeautifulSoup4
- Requests

To install the dependencies, run the following command:

```bash
pip install beautifulsoup4 requests
```

## Usage

1. Run the web application using a WSGI server such as Gunicorn or cPanel:

```bash
gunicorn app:application
```

2. Open the `index.html` file in your web browser or host it using a static file server.

## How It Works

The application consists of two parts:

1. The frontend (HTML, CSS, and JavaScript) in `index.html` which displays the countdown to AGI.
2. The Python backend script `app.py` which fetches and parses the estimative date from the Metaculus question page.

The frontend fetches the estimative date from the Python backend and updates the countdown on the web page in real-time.

The python endpoint is '/date'
