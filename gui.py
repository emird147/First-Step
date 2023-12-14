from utils import enhance_internship_description
from utils import enhance_project_description
import tkinter as tk
from tkinter import ttk

def collect_data(callback):
    def submit_data():
        internship_description = enhance_internship_description(internship_entry.get("1.0", tk.END).strip())
        proj_description = enhance_project_description(project_entry.get("1.0", tk.END).strip())

        data = {
            "personal_info": {
                "name": name_entry.get(),
                "email": email_entry.get(),
                "linkedin": linkedin_entry.get(),
                "github": github_entry.get(),
                "location": location_entry.get()
            },
            "education": {
                "school": school_entry.get(),
                "school_location": school_location_entry.get(),
                "degree": degree_entry.get(),
                "major": major_entry.get(),
                "graduation_date": graduation_date_entry.get(),
                "gpa": gpa_entry.get(),
                "relevant_courses": relevant_courses_entry.get(),
            },
            "internship_info": {
                "internship_company": internship_company_entry.get(),
                "internship_position": internship_position_entry.get(),
                "internship_location": internship_location_entry.get(),
                "internship_date": internship_date_entry.get(),
                "internship_description": internship_description,
            },
            "internship": internship_entry.get("1.0", tk.END).strip(),
            "proj_info": {
                "proj_name": proj_name_entry.get(),
                "proj_url": proj_url_entry.get(),
                "proj_date": proj_date_entry.get(),
                "proj_description": proj_description,
            },
            "skills_info": {
                'prog_languages': prog_languages_entry.get(),
                'applications': applications_entry.get(),
                'os': os_entry.get(),
                'design_software': design_software_entry.get()
                },
        }

        callback(data)

    root = tk.Tk()
    root.title("Resume Generator")
    
    # Personal Information Section
    personal_info_frame = ttk.LabelFrame(root, text="Personal Information")   # container 
    ttk.Label(personal_info_frame, text="Name:").grid(row=0, column=0, sticky=tk.W)   # label widget
    name_entry = ttk.Entry(personal_info_frame)         # accompanying entry widget for user to input the necessary information
    name_entry.grid(row=0, column=1)        # grid method to position the entry's display

    ttk.Label(personal_info_frame, text="Email:").grid(row=0, column=5, sticky=tk.W)
    email_entry = ttk.Entry(personal_info_frame)
    email_entry.grid(row=0, column=6)

    ttk.Label(personal_info_frame, text="LinkedIn:").grid(row=0, column=11, sticky=tk.W)
    linkedin_entry = ttk.Entry(personal_info_frame)
    linkedin_entry.grid(row=0, column=12)

    ttk.Label(personal_info_frame, text="GitHub:").grid(row=0, column=17, sticky=tk.W)
    github_entry = ttk.Entry(personal_info_frame)
    github_entry.grid(row=0, column=18)

    ttk.Label(personal_info_frame, text="Location:").grid(row=1, column=0, sticky=tk.W)
    location_entry = ttk.Entry(personal_info_frame)
    location_entry.grid(row=1, column=1)

    personal_info_frame.pack(fill="both", expand="yes", padx=10, pady=10)

    
    
    
    # Education Section
    education_frame = ttk.LabelFrame(root, text="Education")
    education_frame.pack(fill='both', expand=True)

    ttk.Label(education_frame, text="School:").grid(row=3, column=0, sticky=tk.W)
    school_entry = ttk.Entry(education_frame)
    school_entry.grid(row=3, column=1)

    ttk.Label(education_frame, text="School Location:").grid(row=3, column=5, sticky=tk.W)
    school_location_entry = ttk.Entry(education_frame)
    school_location_entry.grid(row=3, column=6)

    ttk.Label(education_frame, text="Degree:").grid(row=3, column=11, sticky=tk.W)
    degree_entry = ttk.Entry(education_frame)
    degree_entry.grid(row=3, column=12)

    ttk.Label(education_frame, text="Major:").grid(row=4, column=0, sticky=tk.W)
    major_entry = ttk.Entry(education_frame)
    major_entry.grid(row=4, column=1)

    ttk.Label(education_frame, text="Graduation Date:").grid(row=4, column=5, sticky=tk.W)
    graduation_date_entry = ttk.Entry(education_frame)
    graduation_date_entry.grid(row=4, column=6)

    ttk.Label(education_frame, text="GPA:").grid(row=4, column=11, sticky=tk.W)
    gpa_entry = ttk.Entry(education_frame)
    gpa_entry.grid(row=4, column=12)

    ttk.Label(education_frame, text="Relevant Courses:").grid(row=3, column=17, sticky=tk.W)
    relevant_courses_entry = ttk.Entry(education_frame)
    relevant_courses_entry.grid(row=3, column=18)

    
    
    
    # Experience Section
    internship_frame = ttk.LabelFrame(root, text="Experience")
    internship_frame.pack(fill="both", expand="yes")
    
    ttk.Label(internship_frame, text="Company Name:").grid(row=5, column=0, sticky=tk.W)
    internship_company_entry = ttk.Entry(internship_frame)
    internship_company_entry.grid(row=5, column=1)

    ttk.Label(internship_frame, text="Position:").grid(row=5, column=5, sticky=tk.W)
    internship_position_entry = ttk.Entry(internship_frame)
    internship_position_entry.grid(row=5, column=6)

    ttk.Label(internship_frame, text="Location:").grid(row=5, column=11, sticky=tk.W)
    internship_location_entry = ttk.Entry(internship_frame)
    internship_location_entry.grid(row=5, column=12)

    ttk.Label(internship_frame, text="Dates:").grid(row=5, column=16, sticky=tk.W)
    internship_date_entry = ttk.Entry(internship_frame)
    internship_date_entry.grid(row=5, column=17)
    
    ttk.Label(internship_frame, text="Description:").grid(row=6, column=0, sticky=tk.W)
    internship_entry = tk.Text(internship_frame, height=5, width=40)
    internship_entry.grid(row=7, column=0, columnspan=19, sticky=tk.EW)
    

    
    
    # Projects Section
    projects_frame = ttk.LabelFrame(root, text="Projects")
    projects_frame.pack(fill="both", expand="yes")
    
    ttk.Label(projects_frame, text="Project Name:").grid(row=14, column=0, sticky=tk.W)
    proj_name_entry = ttk.Entry(projects_frame)
    proj_name_entry.grid(row=14, column=1)

    ttk.Label(projects_frame, text="Project Date:").grid(row=14, column=6, sticky=tk.W)
    proj_date_entry = ttk.Entry(projects_frame)
    proj_date_entry.grid(row=14, column=7)

    ttk.Label(projects_frame, text="Project URL:").grid(row=14, column=12, sticky=tk.W)
    proj_url_entry = ttk.Entry(projects_frame)
    proj_url_entry.grid(row=14, column=13)
    
    ttk.Label(projects_frame, text="Project Description:").grid(row=15, column=0, sticky=tk.W)
    project_entry = tk.Text(projects_frame, height=5, width=40)
    project_entry.grid(row=16, column=0, columnspan=28, sticky=tk.EW)







    # Technical Skills Section
    technical_skills_frame = ttk.LabelFrame(root, text="Technical Skills")
    technical_skills_frame.pack(fill="both", expand="yes")

    ttk.Label(technical_skills_frame, text="Programming Languages:").grid(row=1, column=0, sticky=tk.W)
    prog_languages_entry = ttk.Entry(technical_skills_frame, width=75)
    prog_languages_entry.grid(row=1, column=1)

    ttk.Label(technical_skills_frame, text="Applications:").grid(row=3, column=0, sticky=tk.W)
    applications_entry = ttk.Entry(technical_skills_frame, width=75)
    applications_entry.grid(row=3, column=1)

    ttk.Label(technical_skills_frame, text="Operating Systems:").grid(row=5, column=0, sticky=tk.W)
    os_entry = ttk.Entry(technical_skills_frame, width=75)
    os_entry.grid(row=5, column=1)

    ttk.Label(technical_skills_frame, text="Design Software:").grid(row=7, column=0, sticky=tk.W)
    design_software_entry = ttk.Entry(technical_skills_frame, width=75)
    design_software_entry.grid(row=7, column=1)



    # Submit Button
    submit_button = ttk.Button(root, text="Submit", command=submit_data)
    submit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":

    collect_data()
