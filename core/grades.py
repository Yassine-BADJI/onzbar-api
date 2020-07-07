from sqlalchemy import func

from extensions import db
from model import Grades


def add_new_grades(current_user, data, bar_id):
    new_grades = Grades(
        evaluation=data['evaluation'],
        user_id=current_user.id,
        bar_id=bar_id,
    )
    db.session.add(new_grades)
    db.session.commit()


def get_grades_average(bar_id):
    avg = db.session.query(func.avg(Grades.evaluation)).filter_by(bar_id=bar_id).first()
    return avg[0]
