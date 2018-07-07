# for maintainability, we can separate web test cases by page name but I just listed every case in same array

def test_cases(number):
    return testCases[number]


testCases = [
    # [severity, description]
    ['Blocker', 'when user goes to main page, page should be loaded'],
    ['Blocker', 'In Main page, when user click "Sing in" button, he should see Sign in Page'],
    ['Blocker', 'In Login Page, when user login with a valid user, he should see Home Page'],
    ['Blocker', 'In Login Page, when user login with a in-valid user, he should see Error Message'],
    ['Blocker', 'In Home Page, when user clicks on choose project, he will see the projects and will choose the 6-12 option'],
    ['Blocker', 'In Home Page, After Logging in we will log out'],
]