# -*- coding: utf-8 -*-
import click
import requests

@click.group()
def main():
    
    """
    Simple CLI for querying books on Google Books 
    """
    pass

@main.command()
@click.argument('query')
def search(query):
    """This search and return results corresponding to the given query from Google Books"""
    url_format = 'https://www.googleapis.com/books/v1/volumes'
    query = "+".join(query.split())

    query_params = {
        'q': query
    }

    response = requests.get(url_format, params=query_params)
    
    


    items = response.json()["items"] 
    
    mapper={}
    count = 1
    for item in items:
        mapper[str(count)] = item["id"]
        click.echo(str(str(count)+" "+item["volumeInfo"]["title"]))
        
        count+=1
        
    option = raw_input("choose you option")
    
    url_format = 'https://www.googleapis.com/books/v1/volumes/{}'
   
    response = requests.get(url_format.format(mapper[option]))
    dic= response.json()["volumeInfo"]
    link =dic["previewLink"]
    title = dic["subtitle"]
    desc = dic["description"]
    
    click.echo("About")
    click.echo(title)
    click.echo("Description")
    click.echo(desc)
    click.echo("Open the link to preview the book")
    click.echo(link)
    
    
if __name__ == "__main__":
    main()
