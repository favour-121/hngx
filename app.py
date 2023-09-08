from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)


@app.route('/get_info', methods=['GET'])
def get_info():
    # Retrieve query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day of the week
    current_day = datetime.datetime.utcnow().strftime("%A")

    # Get current UTC time
    utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Validate UTC time (within +/-2 hours)
    current_utc_time = datetime.datetime.strptime(
        utc_time, "%Y-%m-%dT%H:%M:%SZ")
    two_hours_ago = datetime.datetime.utcnow() - datetime.timedelta(hours=2)
    two_hours_later = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    if two_hours_ago <= current_utc_time <= two_hours_later:
        status_code = 200
    else:
        status_code = 400  # Return a bad request status if outside the range

    # GitHub URLs
    github_file_url = "https://github.com/username/repo/blob/main/app.py"
    github_repo_url = "https://github.com/Seun-Ayela/hngx.git"

    # Create JSON response
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
