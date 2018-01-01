# Purpose

Companion script to a hazel workflow to publish a Pelican blog.

# Functionality (Status 2018-01-01)

- Puts date prefix ('/images/{year}/{month}/') in front of image references.

# Usage

- Use `sys.argv[1]` to refer to the file being processed by Hazel
	- NOTE: sys needs to be imported;
	- `sys.argv[1]` returns file incl. full path
- Hazel command: `python /path/to/script/blog_date-prefix.py "$1"` (with the /bin/bash shell)

# Relevant Sources:

- Date matching: https://stackoverflow.com/questions/3276180/extracting-date-from-a-string-in-python, https://www.tutorialspoint.com/python/string_startswith.htm
- File handling: https://stackoverflow.com/a/17141572
- Search and replace: https://www.tutorialspoint.com/python/string_replace.htm, https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3
- Encoding: https://stackoverflow.com/a/24265848