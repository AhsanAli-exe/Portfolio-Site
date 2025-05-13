# Ahsan Ali - Portfolio Website

A modern, responsive portfolio website with a superhero/gamer theme, built using Flask and Python.

![Portfolio Preview](static/images/cool-superhero-flying-towards-camera-260nw-2521138109.webp)

## Description

This portfolio website showcases Ahsan Ali's skills, projects, experience, and achievements in a modern, interactive interface. The website features:

- Modern and minimalistic UI with a superhero/gamer theme
- Fully responsive design for all device sizes
- Smooth animations and transitions
- Interactive project showcase with links to live demos
- Contact form for easy communication

## Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Libraries:**
  - AOS (Animate On Scroll)
  - Swiper.js
  - Font Awesome
  - Typed.js

## Features

- **Responsive Design:** Optimized for desktop, tablet, and mobile devices
- **Animations:** Smooth transitions and animations throughout the site
- **Project Showcase:** Interactive display of projects with descriptions and links
- **Experience Timeline:** Visual representation of work experience
- **Skills Visualization:** Visual representation of technical skills
- **Contact Form:** Easy way for visitors to get in touch
- **Superhero Theme:** Themed design with superhero elements

## Project Structure

```
├── app.py                 # Main Flask application file
├── requirements.txt       # Python dependencies
├── static/                # Static files
│   ├── css/               # CSS stylesheets
│   ├── js/                # JavaScript files
│   └── images/            # Image files
└── templates/             # HTML templates
    ├── layout.html        # Base template
    ├── index.html         # Home page
    ├── about.html         # About page
    ├── experience.html    # Experience page
    ├── projects.html      # Projects page
    ├── skills.html        # Skills page
    ├── honors.html        # Honors & Achievements page
    └── contact.html       # Contact page
```

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/portfolio-website.git
   cd portfolio-website
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

## Deployment

This application can be deployed to various platforms:

### Heroku

1. Create a Heroku account and install the Heroku CLI
2. Create a Procfile with the content: `web: gunicorn app:app`
3. Deploy using the Heroku CLI:
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

### PythonAnywhere

1. Create a PythonAnywhere account
2. Upload the project files
3. Set up a web app using the Flask framework
4. Configure the WSGI file to point to your app

## Customization

To customize this portfolio for your own use:

1. Replace the personal information with your own in the HTML templates
2. Update the project details in `projects.html`
3. Modify the experience information in `experience.html`
4. Update the skills in `skills.html`
5. Change the background and project images in the `static/images` directory
6. Adjust the color scheme in `static/css/style.css`

## License

This project is available for personal use. Please provide attribution if you use substantial portions of the code.

## Credits

- Superhero images and icons are used for demonstration purposes
- Background images from Unsplash
- Fonts from Google Fonts
- Icons from Font Awesome