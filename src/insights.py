from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    read_dict = read(path)
    job_types = []
    for index in read_dict:
        if index["job_type"] != "":
            if index["job_type"] not in job_types:
                job_types.append(index["job_type"])

    return job_types


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    read_dict = read(path)
    industries_types = []
    for index in read_dict:
        if index["industry"] != "":
            if index["industry"] not in industries_types:
                industries_types.append(index["industry"])

    return industries_types


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    read_dict = read(path)
    initial_value = 0
    max_salary = initial_value
    for index in read_dict:
        if index["max_salary"] != "" and index["max_salary"].isnumeric():
            if int(index["max_salary"]) > max_salary:
                max_salary = int(index["max_salary"])

    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    read_dict = read(path)
    max_salary = get_max_salary(path)
    min_salary = max_salary
    for index in read_dict:
        if index["min_salary"] != "" and index["min_salary"].isnumeric():
            if int(index["min_salary"]) < min_salary:
                min_salary = int(index["min_salary"])

    return min_salary


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    # https://www.programiz.com/python-programming/methods/built-in/filter
    return list(filter(lambda i: (job_type == i["job_type"]), jobs))


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return list(filter(lambda i: (industry == i["industry"]), jobs))


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        if job["min_salary"] > job["max_salary"]:
            raise ValueError("job min_salary must be less than max_salary")
        # elif "min_salary" not in job or "max_salary" not in job:
        #     raise ValueError("job must have min_salary and max_salary keys")
        # elif not (type(job["min_salary"]) or type(job["max_salary"])) == int:
        #     raise ValueError("job min_salary and max_salary must be int")
        # elif not type(salary) == int:
        #     raise ValueError("salary must be an integer")
        elif job["min_salary"] <= int(salary) <= job["max_salary"]:
            return True
        else:
            return False
    except (KeyError, TypeError):
        raise ValueError


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    jobs_list = []
    for index in jobs:
        try:
            if matches_salary_range(index, salary):
                jobs_list.append(index)
        except ValueError:
            pass

    return jobs_list
