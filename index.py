import jinja2
import markdown
import frontmatter
from os import listdir
files = listdir("pages/.")
html = {}
links = []
counter = 1
for file in files:
    with open(f"pages/{file}","r") as input_file:

        post = frontmatter.Frontmatter.read_file(f"pages/{file}")
    html[counter] = {"filename": f"{file.rstrip(".md")}.html", "html": markdown.markdown(post['body'])}
    links.append(f"{file.rstrip(".md")}.html")
    counter+=1

environment = jinja2.Environment(loader=jinja2.FileSystemLoader("./templates"))
template = environment.get_template("base.html")
        
for page_info in html.values():
    content ={
        "page" :page_info["html"],
        "links" :links
    } 
    with open(f"HTML/{page_info["filename"]}",mode="w",encoding="utf-8") as message:
        message.write(template.render(content))
        print(f"... wrote {page_info["filename"]}")