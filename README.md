Project URL: [https://roadmap.sh/projects/url-shortener](https://roadmap.sh/projects/url-shortener)
https://github.com/prashundwivedi1128/Flask-URL-Shortener

# URL Shortener - Backend Project

This project is a functional URL Shortener built as part of the roadmap.sh backend challenges.

### Project Link
Project URL: https://roadmap.sh/projects/url-shortener

### Tech Stack
- **Backend:** Python (Flask)
- **Database:** SQLite
- **Logic:** Base62 Encoding for short code generation

### How it Works
1. User provides a long URL.
2. The system generates a unique 6-character short code.
3. Both are stored in the SQLite database.
4. When the short URL is accessed, the system redirects to the original long URL.
