from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(q.get('text'), q.get('answer')) for q in question_data]
qb = QuizBrain(question_list=question_bank)

while qb.still_has_questions():
    qb.next_question()
