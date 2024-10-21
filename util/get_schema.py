def get_schema():
    return """\
0|title|TEXT 
1|artist|TEXT  
2|top genre|TEXT 
3|year|TEXT
4|beats.per.minute|INT 
5|energy|TEXT 
6|danceability|TEXT 
7|loudness.dB|TEXT 
8|liveness|TEXT
9|valance|TEXT
10|length|TEXT
11|acousticness|TEXT
12|speechiness|TEXT
13|popularity|TEXT
"""

def get_schema_altered():
        return """\
0|title|TEXT 
1|artist|TEXT  
2|top genre|TEXT Use square brackets for this column in the SQL (since it has spaces between words)
3|year|TEXT
4|beats.per.minute|INT Use square brackets for this column in the SQL (since it has characters between words)
5|energy|TEXT 
6|danceability|TEXT 
7|loudness.dB|TEXT  Use square brackets for this column in the SQL (since it has characters between words)
8|liveness|TEXT
9|valance|TEXT
10|length|TEXT
11|acousticness|TEXT
12|speechiness|TEXT
13|popularity|TEXT
"""
    