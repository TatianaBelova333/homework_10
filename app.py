from flask import Flask
import utils

candidates = utils.load_candidates_info('candidates.json')

app = Flask(__name__)



@app.route("/")
def main_page():
    all_candidates = ''
    for candidate in candidates:
        candidate_info = utils.get_candidate_profile(candidate)
        all_candidates += candidate_info
    return f"<pre>{all_candidates}</pre>"


@app.route("/candidate/<int:id>")
def candidate_profile(id):
    last_id = candidates[-1]['id']
    if id <= last_id:
        candidate = candidates[id - 1]
        candidate_info = utils.get_candidate_profile(candidate)
        image_link = candidate.get('picture')
        return f"<img src={image_link}>\n" \
               f'<pre>{candidate_info}</pre>'
    return "Такого кандидата нет"


@app.route("/skill/<skill>")
def candidate_skills(skill):
    candidates_with_skill = ''
    for candidate in candidates:
        if skill in candidate.get('skills', 'not applicable').lower():
            candidate_info = utils.get_candidate_profile(candidate)
            candidates_with_skill += candidate_info
    return f'<pre>{candidates_with_skill}</pre>'


app.run()
