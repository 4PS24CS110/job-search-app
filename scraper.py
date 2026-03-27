import requests

def get_jobs(query, location, experience):
    url = "https://remotive.com/api/remote-jobs"
    data = requests.get(url).json()

    jobs = []
    query = query.lower()

    for job in data.get("jobs", []):
        title = job.get("title", "").lower()
        description = job.get("description", "").lower()

        # 🔥 smart matching
        if query in title or query in description:
            jobs.append({
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("candidate_required_location")
            })

    # 🔥 fallback so always results show
    if len(jobs) == 0:
        for job in data.get("jobs", [])[:15]:
            jobs.append({
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("candidate_required_location")
            })

    return jobs