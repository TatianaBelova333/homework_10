import json


def load_candidates_info(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates


def get_candidate_profile(candidate: dict):
    candidate_info: str = ''
    candidate_name = candidate.get('name', 'информация отсутствует')
    candidate_position = candidate.get('position', 'информация отсутствует')
    candidate_skills = candidate.get('skills', 'информация отсутствует')
    candidate_info += f"Имя кандидата - {candidate_name}\n" \
                      f"Позиция кандидата - {candidate_position}\n" \
                      f"Навыки - {candidate_skills}\n\n"
    return candidate_info
