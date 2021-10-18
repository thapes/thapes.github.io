"""
Summary
-------
The summary is a brief intro. You can put raw HTML into this field.
"""
summary = '<p>I started my career in tech during my first year in college and since then I have been working directly with customers through support or consulting roles for product issues. During this time, I also have directed my work to innovations by creating projects globally to automate and integrate internal systems mainly with Python language.</p>'


languages = [
        ['Portuguese', ' (Native)'],
        ['English', ' (Professional)'],
        ['Spanish', ' (Intermediate)']
        ]

education = [
        ['BSc in Information Systems', 'Unisinos', '2014 - 2021'],
        ['Technician in Computer Systems', 'Colégio Dom Feliciano', '2011 - 2012']
        ]

interests = ['Reading', 'Gaming', 'Watching series', 'Sports']

skills = [
        ['Python & Flask', '80%'],
        ['MySQL & PostgreSQL', '60%'],
        ['Pandas & Numpy', '60%'],
        ['Matplotlib & Seaborn', '40%'],
        ['Java', '50%'],
        ['Data Structure & Algorithms', '50%']
        ]

"""
Experience
----------
This should be a list of lists. Each sublist corresponds to a particular job
and is of the form:
    ['Title', 'Date range', 'Company name and location', 'Description of role']

The 'Description of role' field does not get escaped by the templating engine,
so you can put raw HTML in it if you like.
"""
experience = [
        ['Client Service Specialist',
            '2021 - Present',
            'SAP Concur, São Leopoldo',
            '<p>Responsible to provide assistance to clients regarding audit questions and issues. As a CSS, I am responsible directly for 32 clients globally, provinding to them analysis reports and recommendations on their product.</p>'
        ],
        ['Customer Support Specialist/Innovation Lead',
            '2016 - Present',
            'SAP Concur, São Leopoldo',
            '<p>As a USD Representative, I am responsible to provide technical and navigational support to users by phone and portal cases, solving issues in real time. Along with this task, I also create and maintain knowledge base articles and provide internal assistance to colleagues.</p> <p>Adding to the representative task, I am also an Innovation Lead who is responsible to develop projects globally. Mostly of these projects were developed by using Python language to automate tasks and integrate systems.</p>'
        ],
        ['Internship',
            '2015 - 2016',
            'SAP, São Leopoldo',
            '<p>Responsible for handling the incident queue, needing to maintain global contact with various agents to ensure compliance with SLAs. Besides that, responsible for handling security incidents.</p>'
        ]
    ]

"""
Projects
--------
The project_intro field is for a short introduction to your work.
Project are a list of lists, where each sublist refers to a specific project,
and is of the form:
    ['Title', 'Description', 'Link to project webpage']
"""
project_intro = '<p>You can list your side projects or open source libraries in this section. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum et ligula in nunc bibendum fringilla a eu lectus.</p>'
projects = [
        ['Velocity',
            'A responsive website template designed to help startups promote, market and sell their products.',
            '#hook'
        ],
        ['DevStudio',
            'A responsive website template designed to help startups promote, market and sell their products.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-web-development-agencies-devstudio/'
        ],
        ['Tempo',
            'A responsive website template designed to help startups promote their products or services and to attract users &amp; investors.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-for-startups-tempo/'
        ],
        ['Atom',
            'A comprehensive website template solution for startups/developers to market their mobile apps.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-mobile-apps-atom/'
        ],
        ['Delta',
            'A responsive Bootstrap one page theme designed to help app developers promote their mobile apps.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-for-mobile-apps-delta/'
        ]
    ]



"""
default_data
------------
This dictionary puts everything together. It will be read by the Flask app when
it is instantiated.
"""
default_data = {
    'site_title' : 'Responsive Resume/CV Template for Developers',
    'name' : 'Thales Stuczynski',
    'tagline' : 'Python Developer',
    'email' : 'stuczynski.thales@gmail.com',
    'phone' : '+55 51 9 8283-3251',
    'website' : 'thapes.github.io',
    'linkedin' : 'linkedin.com/in/thalesstuczynski',
    'github' : 'github.com/thapes',
    'languages' : languages,
    'education' : education,
    'interests' : interests,
    'skills' : skills,
    'summary' : summary,
    'experience' : experience,
    'project_intro' : project_intro,
    'projects' : projects
    }
