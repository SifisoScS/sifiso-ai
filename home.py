import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Sifiso AI | Learn AI in Your Language")
root.geometry("1000x700")  # Set initial window size

# Header Frame (Sticky at the top)
header = tk.Frame(root, bg="#ffffff")  # bg-white
header.pack(side="top", fill="x")

# Logo
logo = tk.Label(header, text="Sifiso AI", font=("Montserrat", 24, "bold"), fg="#D97706", bg="#ffffff")  # text-yellow-600
logo.pack(side="left", padx=20, pady=8)

# Navigation Links
nav_links = ["Learn", "Community", "Tools", "About", "Contact"]
section_frames = {}  # To store section frames for scrolling

def scroll_to_section(section):
    """Scroll the canvas to the specified section."""
    if section in section_frames:
        frame = section_frames[section]
        root.update_idletasks()  # Ensure layout is updated
        y = frame.winfo_y()
        total_height = canvas.bbox("all")[3]  # Bottom y-coordinate of content
        fraction = y / total_height
        canvas.yview_moveto(fraction)

# Add navigation labels
for link in nav_links:
    lbl = tk.Label(header, text=link, font=("Open Sans", 12, "bold"), fg="#374151", bg="#ffffff", cursor="hand2")  # text-gray-700
    lbl.pack(side="left", padx=10)
    lbl.bind("<Button-1>", lambda event, s=link: scroll_to_section(s))

# Canvas and Scrollbar for scrollable content
canvas = tk.Canvas(root, bg="#ffffff")
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# Content Frame inside Canvas
content_frame = tk.Frame(canvas, bg="#ffffff")
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Hero Section (Welcome)
hero_section = tk.Frame(content_frame, bg="#D97706", pady=50)  # Approx yellow-500
hero_section.pack(fill="x")

tk.Label(hero_section, text="Welcome to Sifiso AI", font=("Montserrat", 48, "bold"), fg="white", bg="#D97706").pack()
tk.Label(hero_section, text="Desire to Learn, Power to Build", font=("Open Sans", 24), fg="white", bg="#D97706").pack()
tk.Label(hero_section, text="Learn AI and digital skills in your language: From Mdantsane to eThekwini & from eThekwini to Soweto. Unlock your potential with community-powered AI tutoring and startup tools.", font=("Open Sans", 16), fg="white", bg="#D97706", wraplength=600).pack(pady=20)
tk.Button(hero_section, text="Get Started", font=("Open Sans", 16, "bold"), bg="white", fg="#B45309", relief="flat", command=lambda: scroll_to_section("Learn")).pack()  # text-yellow-700

# Learn Section
learn_section = tk.Frame(content_frame, bg="#ffffff", pady=40)
learn_section.pack(fill="x")
section_frames["Learn"] = learn_section

tk.Label(learn_section, text="Learn AI in Your Language", font=("Montserrat", 32, "bold"), fg="#D97706", bg="#ffffff").pack()

articles = [
    {"title": "Mdantsane AI Classroom", "desc": "Interactive AI lessons tailored for the Mdantsane community, focusing on practical skills and local language support.", "image": "mdantsane.jpg"},
    {"title": "eThekwini AI Workshop", "desc": "Hands-on AI workshops in eThekwini designed to empower learners with coding and machine learning skills.", "image": "ethekwini.jpg"},
    {"title": "Soweto AI Community Meetup", "desc": "Monthly meetups in Soweto to share AI knowledge, collaborate on projects, and build a supportive network.", "image": "soweto.jpg"}
]

article_grid = tk.Frame(learn_section, bg="#ffffff")
article_grid.pack()

for i, article in enumerate(articles):
    frame = tk.Frame(article_grid, bg="#ffffff", bd=1, relief="solid")
    frame.grid(row=0, column=i, padx=10, pady=10)
    
    img = Image.open(f"images/{article['image']}").resize((400, 250), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    tk.Label(frame, image=photo, bg="#ffffff").pack()
    frame.image = photo  # Keep reference
    
    tk.Label(frame, text=article["title"], font=("Open Sans", 18, "bold"), fg="#374151", bg="#ffffff").pack(pady=5)
    tk.Label(frame, text=article["desc"], font=("Open Sans", 14), fg="#4B5563", bg="#ffffff", wraplength=380).pack()

# Community Section
community_section = tk.Frame(content_frame, bg="#FFF7ED", pady=40)  # bg-yellow-50
community_section.pack(fill="x")
section_frames["Community"] = community_section

tk.Label(community_section, text="Community Powered AI Tutoring", font=("Montserrat", 32, "bold"), fg="#B45309", bg="#FFF7ED").pack()  # text-yellow-700

comm_content = tk.Frame(community_section, bg="#FFF7ED")
comm_content.pack()

img = Image.open("images/community.jpg").resize((600, 400), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
tk.Label(comm_content, image=photo, bg="#FFF7ED").grid(row=0, column=0, padx=20)
comm_content.image = photo

text_frame = tk.Frame(comm_content, bg="#FFF7ED")
text_frame.grid(row=0, column=1, padx=20)

tk.Label(text_frame, text="Our community-powered AI tutoring connects learners with experienced mentors who speak your language and understand your context. Get personalized guidance, ask questions, and build your AI skills with support every step of the way.", font=("Open Sans", 16), fg="#4B5563", bg="#FFF7ED", wraplength=500).pack(pady=10)

features = [
    "Live tutoring sessions in multiple South African languages",
    "Peer-to-peer learning groups",
    "Access to curated AI learning resources",
    "Supportive and inclusive community environment"
]
for feature in features:
    tk.Label(text_frame, text=f"• {feature}", font=("Open Sans", 14), fg="#4B5563", bg="#FFF7ED").pack(anchor="w")

# Tools Section
tools_section = tk.Frame(content_frame, bg="#ffffff", pady=40)
tools_section.pack(fill="x")
section_frames["Tools"] = tools_section

tk.Label(tools_section, text="Startup Tools for AI Builders", font=("Montserrat", 32, "bold"), fg="#D97706", bg="#ffffff").pack()

tools_grid = tk.Frame(tools_section, bg="#ffffff")
tools_grid.pack()

tools = [
    {"title": "AI Code Editor", "desc": "Write, test, and debug AI code with smart suggestions and real-time error checking.", "image": "code_editor.jpg"},
    {"title": "Data Visualization Tool", "desc": "Create interactive charts and graphs to better understand your AI datasets.", "image": "data_viz.jpg"},
    {"title": "Model Training Dashboard", "desc": "Monitor and optimize your AI models with detailed training insights and metrics.", "image": "model_dashboard.jpg"}
]

for i, tool in enumerate(tools):
    frame = tk.Frame(tools_grid, bg="#ffffff", bd=1, relief="solid")
    frame.grid(row=0, column=i, padx=10, pady=10)
    
    img = Image.open(f"images/{tool['image']}").resize((120, 120), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    tk.Label(frame, image=photo, bg="#ffffff").pack()
    frame.image = photo
    
    tk.Label(frame, text=tool["title"], font=("Open Sans", 18, "bold"), fg="#374151", bg="#ffffff").pack(pady=5)
    tk.Label(frame, text=tool["desc"], font=("Open Sans", 14), fg="#4B5563", bg="#ffffff", wraplength=380).pack()

# About Section
about_section = tk.Frame(content_frame, bg="#FFF7ED", pady=40)
about_section.pack(fill="x")
section_frames["About"] = about_section

tk.Label(about_section, text="About Sifiso AI", font=("Montserrat", 32, "bold"), fg="#B45309", bg="#FFF7ED").pack()
tk.Label(about_section, text="Sifiso AI is dedicated to democratizing AI education across South Africa by providing accessible, language-inclusive learning experiences. We believe that everyone, regardless of background or location, should have the opportunity to learn and build with AI.", font=("Open Sans", 16), fg="#4B5563", bg="#FFF7ED", wraplength=800).pack(pady=10)

img = Image.open("images/team.jpg").resize((800, 400), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
tk.Label(about_section, image=photo, bg="#FFF7ED").pack()
about_section.image = photo

# Contact Section
contact_section = tk.Frame(content_frame, bg="#ffffff", pady=40)
contact_section.pack(fill="x")
section_frames["Contact"] = contact_section

tk.Label(contact_section, text="Contact Us", font=("Montserrat", 32, "bold"), fg="#D97706", bg="#ffffff").pack()

form_frame = tk.Frame(contact_section, bg="#ffffff", bd=1, relief="solid", padx=20, pady=20)
form_frame.pack()

tk.Label(form_frame, text="Name", font=("Open Sans", 14), fg="#374151", bg="#ffffff").grid(row=0, column=0, sticky="w")
tk.Entry(form_frame, font=("Open Sans", 14), width=30).grid(row=0, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Email", font=("Open Sans", 14), fg="#374151", bg="#ffffff").grid(row=1, column=0, sticky="w")
tk.Entry(form_frame, font=("Open Sans", 14), width=30).grid(row=1, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Message", font=("Open Sans", 14), fg="#374151", bg="#ffffff").grid(row=2, column=0, sticky="w")
tk.Text(form_frame, font=("Open Sans", 14), width=30, height=5).grid(row=2, column=1, padx=10, pady=5)

tk.Button(form_frame, text="Send Message", font=("Open Sans", 14, "bold"), bg="#D97706", fg="white", relief="flat").grid(row=3, column=1, pady=10)

# Footer
footer = tk.Frame(content_frame, bg="#D97706", pady=20)
footer.pack(fill="x")

tk.Label(footer, text="© 2024 Sifiso AI. All rights reserved.", font=("Open Sans", 12), fg="white", bg="#D97706").pack(side="left", padx=20)

social_icons = ["facebook", "twitter", "linkedin", "instagram"]
for icon in social_icons:
    img = Image.open(f"images/{icon}.png").resize((24, 24), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    tk.Label(footer, image=photo, bg="#D97706").pack(side="right", padx=10)
    footer.image_refs = getattr(footer, "image_refs", []) + [photo]  # Keep references

# Configure Scrolling
def update_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

content_frame.bind("<Configure>", update_scrollregion)

# Start the application
root.mainloop()