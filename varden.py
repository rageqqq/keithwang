import pandas as pd
import numpy as np

hirers = pd.read_csv("hirers.csv", dtype={'my_tasks_ids': 'object'})
freelancers = pd.read_csv("freelancers.csv", dtype={'freelancer_usernames': 'object'})
tasks = pd.read_csv("tasks.csv", dtype={'task_id': 'object'})
user_pw = pd.read_csv("username_password.csv", dtype={'password': 'object'})

all_data = [hirers, freelancers, tasks, user_pw]


task_type_dict = {
    "household services": (
        "laundry", "sweeping", "mopping", "cooking",
        "plumbing", "clogs & chokes", "installation", "appliances repair",
        "leaks & tweaks", "air conditioner repair", "carpentry", "electrical",
        "ironing", "packing", "transporting", "vacuuming",
        "gardening", "child care", "car washing", "window cleaning",
        "dusting", "grocery shopping", "walk the dog", "elderly care",
        "sliding door repair", "furniture assembling", "replace door knob", "wall painting",
        "replace light fittings", "install heater", "delivery", "install basin",
        "replacing leaking pipe"
    ),

    "business admin": (
        "excel", "powerpoint", "word", "onenote",
        "filing", "minutes taking", "scanning", "printing",
        "data entry", "public relation", "bookkeeping", "faxing",
        "email", "inventory managment", "customer relation", "copywriting",
        "appointment setting", "answering telephones", "legal"
    ),

    "photography, design & editing": (
        "premiere pro", "after effects", "final cut pro", "imovie",
        "photoshop", "lightroom", "indesign", "illustrator",
        "canva", "UI", "UX", "wedding",
        "portrait", "branding", "packaging", "studio design",
        "animation", "events", "creative", "artistic",
        "colour", "aesthetic", "minimalistic", "typography",
        "logo", "commercial", "corporate training video", "music video",
        "feature film", "television program", "song production"
    )
}


def app():
    while True:
        print("### Welcome to MyWorld ###\n")
        username = signup_login()
        user_type = user_pw[user_pw["username"] == username]['user_type'].values[0]

        if user_type == "freelancer":
            freelancer_program(username)
        else:
            hirer_program(username)


def signup_login():
    while True:
        input_type = input("[1] Signup or [2] Login: ")
        if input_type == "1":
            return signup()
        elif input_type == "2":
            return login()


def login():
    is_authenticated = False
    while not is_authenticated:
        input_username = input("Enter your username (Type '0' to signup): ")
        if input_username == "0":
            return signup()

        input_pw = input("Enter your password (Type '0' to signup): ")
        if input_pw == "0":
            return signup()

        if (user_pw[user_pw["username"]==input_username]["password"]==input_pw).any():
            is_authenticated = True
            print()
        else:
            print("Your username or password is wrong. Please try again. (Type [0] to signup)")

    return input_username


def signup():
    input_usertype = freelancer_or_hirer()
    input_username = verify_username()
    input_pw = input("Choose your password: ")

    user_pw = all_data[3]
    user_pw.loc[len(user_pw)] = [
        input_username,
        input_pw,
        input_usertype,
    ]
    all_data[3] = user_pw
    user_pw.to_csv("username_password.csv", index=False)

    if input_usertype == "freelancer":
        return freelancer_signup(input_username)
    else:
        return hirer_signup(input_username)


def freelancer_or_hirer():
    while True:
        input_type = input("Are you signing up as a [1] Freelancer or [2] Hirer (Type '0' to login):  ")
        if input_type == "1":
            return "freelancer"
        elif input_type == "2":
            return "hirer"
        elif input_type == "0":
            return login()


def verify_username():
    user_pw = all_data[3]
    while True:
        input_username = input("Choose a username (Type '0' to login): ")
        if input_username == "0":
            return login()
        elif input_username not in user_pw["username"].values:
            return input_username

        else:
            print("Username is taken. Please input another username (Type [0] to signup).")


def hirer_signup(username):
    hirers = all_data[0]

    name = input("Please enter name: ")
    age = input("Please enter age: ")
    address = input("Please enter hiring address: ")
    hp = input("Please enter HP number: ")
    email = input("Please enter email: ")
    description = input("Please enter company description: ")
    hirers.loc[len(hirers)]= [
        username,
        name,
        age,
        address,
        hp,
        email,
        description,
        ''
    ]

    all_data[0] = hirers
    hirers.to_csv("hirers.csv", index =  False)
    return username


def freelancer_signup(username):
    freelancers = all_data[1]

    name = input("Please enter name: ")
    age = input("Please enter age: ")
    address = input("Please enter your address: ")
    hp = input("Please enter HP number: ")
    email = input("Please enter email: ")
    education = input("Please enter highest education certification: ")
    job_history_title_1 = input("Please enter your 1st job history title: ")
    job_history_position_1 = input("Please enter your 1st job history position: ")
    job_history_tenure_1 = input("Please enter your 1st job history tenure: ")
    job_history_title_2 = input("Please enter your 2nd job history title: ")
    job_history_position_2 = input("Please enter your 2nd job history position: ")
    job_history_tenure_2 = input("Please enter your 2nd job history tenure: ")
    job_history_title_3 = input("Please enter your 3rd job history title: ")
    job_history_position_3 = input("Please enter your 3rd job history position: ")
    job_history_tenure_3 = input("Please enter your 3rd job history tenure: ")
    skill_1 = input("Please enter your 1st skill: ")
    skill_proficiency_1 = input("On a scale of 1-5, please enter your 1st skill proficiency (higher score means more proficient): ")
    skill_2 = input("Please enter your 2nd skill: ")
    skill_proficiency_2 = input("On a scale of 1-5, please enter your 2nd skill proficiency (higher score means more proficient): ")
    skill_3 = input("Please enter your 3rd skill: ")
    skill_proficiency_3 = input("On a scale of 1-5, please enter your 3rd skill proficiency (higher score means more proficient): ")
    language_1 = input("Please enter your 1st language: ")
    language_proficiency_1 = input("On a scale of 1-5, please enter your 1st language proficiency (higher score means more proficient): ")
    language_2 = input("Please enter your 2nd language: ")
    language_proficiency_2 = input("On a scale of 1-5, please enter your 2nd language proficiency (higher score means more proficient): ")
    language_3 = input("Please enter your 3rd language: ")
    language_proficiency_3 = input("On a scale of 1-5, please enter your 3rd language proficiency (higher score means more proficient): ")
    freelancers.loc[len(freelancers)] = [
        username,
        name,
        age,
        address,
        hp,
        email,
        education,
        job_history_title_1,
        job_history_position_1,
        job_history_tenure_1,
        job_history_title_2,
        job_history_position_2,
        job_history_tenure_2,
        job_history_title_3,
        job_history_position_3,
        job_history_tenure_3,
        skill_1,
        skill_proficiency_1,
        skill_2,
        skill_proficiency_2,
        skill_3,
        skill_proficiency_3,
        language_1,
        language_proficiency_1,
        language_2,
        language_proficiency_2,
        language_3,
        language_proficiency_3,
        ''
    ]

    all_data[1] = freelancers
    freelancers.to_csv("freelancers.csv", index = False)
    return username


def freelancer_program(username):
    while True:
        input_type = input("[1] View all available tasks or [2] Logout: ")
        if input_type == "1":
            view_available_tasks(username)

        elif input_type == "2":
            print("You have successfully logged out. Soon you again soon!\n")
            return


def view_available_tasks(username):
    tasks = all_data[2]

    available_tasks = tasks[tasks["task_status"] == "available"]
    if len(available_tasks) == 0:
        print("No task available.\n")
        return

    for index, task in available_tasks.iterrows():
        pretty_print_task(task)

    signup_task(username)


def pretty_print_task(task):
    i = f"Task ID: {task.task_id}\n"
    t = f"Title: {task.title}\n"
    d = f"Description: {task.description}\n"
    c = f"Compensation: {task.compensation}\n"
    s = f"Period: {task.startdate} to {task.enddate}"
    print()
    print(i+t+d+c+s)
    print()


def signup_task(username):
    while True:
        task_id = input("Please enter the Task ID of the task that you want to sign up for (Type '0' to return to main menu): ")
        if task_id == "0":
            return
        else:
            tasks = all_data[2]
            available_tasks = tasks[tasks["task_status"] == "available"]
            if available_tasks["task_id"].isin([task_id]).any():
                task_index = available_tasks[available_tasks["task_id"]==task_id].index[0]
                if pd.isnull(tasks.loc[task_index, 'freelancer_usernames']):
                    tasks.loc[task_index, "freelancer_usernames"] = username
                elif username in tasks.loc[task_index, "freelancer_usernames"]:
                    print("You have already sign up for this task.\n")
                    continue
                else:
                    tasks.loc[task_index, "freelancer_usernames"] = tasks.loc[task_index, "freelancer_usernames"] + ',' + username

                all_data[2] = tasks
                tasks.to_csv("tasks.csv", index =  False)
                print(f"You have successfully signed up for task {task_id}\n")
            else:
                print("The task ID you have entered is invalid. Please re-enter.\n")


def hirer_program(username):
    while True:
        input_type = input("[1] View all my tasks, [2] Add new task or [3] Logout: ")
        if input_type == "1":
            view_my_tasks(username)
        elif input_type == "2":
            add_new_task(username)
        elif input_type == "3":
            print("You have successfully logged out. Soon you again soon!\n")
            return


def add_new_task(username): #for hirer to add task
    tasks = all_data[2]
    hirers = all_data[0]

    title = input("Please enter job title: ")
    task_type = input("Please select task type:\n select from the following\nphotography, design & editing\nhousehold services\nbusiness admin")
    description = input("Please enter job description: ")
    compensation = input("Please enter compensation for the job: ")
    start_date = input("Please enter start date: ")
    end_date = input("Please enter end date: ")
    task_id = str(len(tasks) + 1)

    tasks.loc[len(tasks)] = [
        task_id,
        title,
        "available",
        task_type,
        description,
        compensation,
        start_date,
        end_date,
        ''
    ]
    all_data[2] = tasks
    tasks.to_csv("tasks.csv", index = False)

    hirer_index = hirers[hirers["username"] == username].index
    if hirers.loc[hirer_index, "my_tasks_ids"].any():
        hirers.loc[hirer_index, "my_tasks_ids"] = hirers.loc[hirer_index, "my_tasks_ids"] + ',' + task_id
    else:
        hirers.loc[hirer_index, "my_tasks_ids"] = task_id
        print(hirer_index)
        print(username)
    all_data[0] = hirers
    hirers.to_csv("hirers.csv", index = False)

    print("\nYou have successfully added a new task.\n")


def view_my_tasks(username):
    hirers = all_data[0]
    tasks = all_data[2]

    if hirers[hirers["username"] == username].my_tasks_ids.any():
        my_task_ids = hirers[hirers["username"] == username].my_tasks_ids.values[0]
        my_tasks = tasks[tasks["task_id"].isin(my_task_ids.split(","))]
        for index, my_task in my_tasks.iterrows():
            pretty_print_task(my_task)
            if pd.isnull(my_task['freelancer_usernames']):
                print("# No applicants yet. #\n")
                continue
            else:
                score(my_task)
                print()
    else:
        print("You have not added any task.\n")
        return


def score(my_task):
    freelancers = all_data[1]
    tasks = all_data[2]

    final_scores = []
    freelancer_usernames = my_task['freelancer_usernames'].split(',')
    for username in freelancer_usernames:
        user_info = freelancers[freelancers["username"] == username]
        proficiency_ratings = user_info[['skill_proficiency_1', 'skill_proficiency_2', 'skill_proficiency_3']].sum(axis=1).values[0]
        aggregated_ratings = proficiency_ratings/3
        skills_match = user_info[["skill_1", "skill_2", "skill_3"]].values[0].tolist()
        keywords = task_type_dict[my_task["task_type"]]
        score = 0
        for keyword in keywords:
            if keyword in skills_match:
                score += 1.25
        final_score = (0.5*aggregated_ratings) + (0.5*score)
        final_scores.append(final_score)

    f = np.array(final_scores)
    n = np.array(freelancer_usernames)
    sorted_index = f.argsort()[::-1] #get index of highest scores
    sorted_username = n[sorted_index]

    print("### These are the recommended candidates: ###\n")
    for username in sorted_username[:3]:
        user_info = freelancers[freelancers["username"] == username]
        pretty_print_freelancer(user_info)

    print("### End of recommendation ###\n")

    # return freelancers[freelancers["username"].isin(top_3)]


def pretty_print_freelancer(user_info):
    u = f"Username: {user_info.username.values[0]}\n"
    n = f"Name: {user_info.name.values[0]}\n"
    h = f"Contact Number: {user_info.hp.values[0]}\n"
    e = f"Email: {user_info.email.values[0]}\n"
    j = f"Past Experiences: {user_info.job_history_title_1.values[0]}, {user_info.job_history_title_2.values[0]}, {user_info.job_history_title_3.values[0]}\n"
    l = f"Past Experiences: {user_info.language_1.values[0]}, {user_info.language_2.values[0]}, {user_info.language_3.values[0]}\n"
    s = f"Past Experiences: {user_info.skill_1.values[0]}, {user_info.skill_2.values[0]}, {user_info.skill_3.values[0]}\n"

    print(u+n+h+e+j+l+s)

