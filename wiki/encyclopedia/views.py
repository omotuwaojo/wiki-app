


import random
from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe
import markdown 
from django.contrib import messages
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        # If entry doesn't exist, render a custom 404 page (assuming it's in Markdown)
        content = markdown.markdown(util.get_entry("404"))
        return render(request, "encyclopedia/entry.html",
                      {'title': "404 - Page Not Found", 'content':  mark_safe(content)} )

    # If entry exists, render its content
    content = markdown.markdown(content)
    return render(request, "encyclopedia/entry.html", 
                  {'title': title, 'content': mark_safe(content)})


      
def search(request,):
    query = request.GET.get('q')
    if query:
        # Search for entries that contain the query as a substring
     entry_titles = util.list_entries()  # Fetch all entries using your utility function
     matching_entries = [title for title in entry_titles if query.lower() in title.lower()]
     if query.lower() in [title.lower() for title in entry_titles]:
            return redirect('wiki_entry', title=query)
     else:
            return render(request, 'encyclopedia/search_results.html', {'entries': matching_entries})
    else:
     return redirect( request, 'encyclopedia/no_results.html')  # Redirect to homepage if no quer

    
    

    
def  new_entry(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

         #Check if an entry with the provided title already exists
        if util.get_entry(title):
            messages.error(request, 'an entry with this title already exists')
            return redirect('new_entry')
        
        # Save the new entry
        util.save_entry(title, content)
        return redirect('wiki_entry', title=title)
    else:
        return render(request, 'encyclopedia/create_new_entry.html')
    

def edit_entry(request, title,):
    if request.method == 'POST':
        content = request.POST.get('content')
        # Update the content of the entry
        util.save_entry(title, content)
        return redirect('wiki_entry', title=title)
    else:
        content=util.get_entry(title)
        return render(request, 'encyclopedia/edit_entry.html', {'title': title,'content':content })


def random_entry(request):
    all_titles = util.list_entries() # Fetch all entry titles
      # Use your utility function to fetch a random entry
    if all_titles:
        random_title = random.choice(all_titles)  # Choose a random entry title
        return redirect('wiki_entry', title=random_title)
    else:
         # Handle if no random entry is found
        return redirect(request,'index')  # Redirect to the homepage or handle as needed    
     