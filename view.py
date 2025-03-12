from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Submission, Problem, CustomUser, Leaderboard
from .sandbox import run_code

@api_view(['POST'])
def submit_code(request):
    user = CustomUser.objects.get(id=request.data['user_id'])
    problem = Problem.objects.get(id=request.data['problem_id'])
    code = request.data['code']
    language = request.data['language']

    result = run_code(code, language)
    submission = Submission.objects.create(user=user, problem=problem, code=code, language=language, status=result)

    return Response({'message': 'Code submitted!', 'result': result})

@api_view(['GET'])
def leaderboard(request):
    scores = Leaderboard.objects.all().order_by('-score')
    return Response({'leaderboard': list(scores.values())})
