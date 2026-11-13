
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>My Educational Blog</title>
</head>
<body>

    <h1>Welcome to My Web Blog</h1>

    <h2>Introduction</h2>
    <p>This is my first educational web blog.</p>

    <h2>Anchor Tag</h2>
    <a href="https://www.google.com">Visit Google</a>

    <h2>Heading Tags</h2>
    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <h3>Heading 3</h3>

    <h2>Image Tag</h2>
    <img src="https://via.placeholder.com/200"
    alt="Sample Image">

    <h2>Ordered List</h2>
    <ol>
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
    </ol>

    <h2>Unordered List</h2>
    <ul>
        <li>Web Design</li>
        <li>WordPress</li>
        <li>Web Development</li>
    </ul>

    <h2>Conclusion</h2>
    <p>HTML is used to create web pages.</p>

</body>
</html>
"""

file = open("blog.html", "w")
file.write(html_code)
file.close()

print("Web Blog Created Successfully!")
print("Open blog.html in your browser.")
