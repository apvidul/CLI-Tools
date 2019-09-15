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
        click.echo((str(count)+" "+item["volumeInfo"]["title"]))
        
        count+=1
        
    option = raw_input("choose you option")
    
    url_format = 'https://www.googleapis.com/books/v1/volumes/{}'
   
    response = requests.get(url_format.format(mapper[option]))
    
    metadata = ["previewLink","subtitle","description","authors","publishedDate"]
    dic= response.json()["volumeInfo"]
    for info in metadata:
        
        if info in dic.keys():
            click.echo(info)
            click.echo(dic[info])
            click.echo()
            
    

if __name__ == "__main__":
    main()
