# this file for custom tags
from django import template
from ..models import Post
from django.db.models import Count
# these two lines below for custom filters
from django.utils.safestring import mark_safe
import markdown

register = template.Library()
'''
Each module that contains template tags needs to define a variable called 
register to be a valid tag library. This variable is an instance of template.Library, 
and it's used to register your own template tags and filters.
'''


@register.simple_tag
def total_posts():  # return the number of post published
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')   # you should create a file to handle the way the returned
# data will be displayed
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
        ).order_by('-total_comments')[:count]


'''
After adding a new template tags module, you will need to restart 
the Django development server in order to use the new tags and 
filters in templates.
'''

'''
custom tags types :
1-simple_tag: Processes the data and returns a string
2-inclusion_tag: Processes the data and returns a rendered template
'''

'''
to use custom tags in html files just load the file by {% load blog_tags %} at the top of the file
to call any function inside html file just use {% functionName %}  anywhere in the html file
if the function have parameters you can call it by {% functionName param1 param2 %} and so on
'''


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))