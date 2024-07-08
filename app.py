from lookup_csv_entry import get_mapped_url
from flask import Flask, send_file, redirect, url_for, send_from_directory

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	try:
		my_resolved_url = get_mapped_url(path)
	except:
		return 'Not found: %s' % path
	else:
		return redirect(my_resolved_url, code=302)
