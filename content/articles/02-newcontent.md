Title: First Static Test
Date: 2010-12-03 10:20
Category: Review
Summary: This is the Summary Test

Cehcking out display.  
[Gunship](https://www.gunshipmusic.com/) is a *retro synthwave* artist out of the UK.

[Revel in Your Time](https://www.youtube.com/watch?v=uYRZV8dV10w), 
[Tech Noir](https://www.youtube.com/watch?v=-nC5TBv3sfU), 
[Fly for Your Life](https://www.youtube.com/watch?v=Jv1ZN8c4_Gs) 
and 
[The Mountain](https://www.youtube.com/watch?v=-HYRTJr8EyA) 
are all quality songs by Gunship. Check out those amazing music videos!   
  
    #!python
    from xml.etree.ElementTree import parse
    doc = parse('rt22.xml')
    for bus in doc.findall('bus'):   #sort according to bus
        lat = float(bus.findtext('lat'))  #check lat field in bus  
  
![Alt Text]({static ../images/test.jpeg thumb="128x_"}) 

There are two ways to specify the identifier:

    :::python
    print("The triple-colon syntax will *not* show line numbers.")

To display line numbers, use a path-less shebang instead of colons:

    #!python
    print("The path-less shebang syntax *will* show line numbers.")
  


Also take a look at other retro synthwave artists such as
[Trevor Something](https://trevorsomething.bandcamp.com/), 
[Droid Bishop](https://droidbishop.bandcamp.com/),
[FM-84](https://fm84.bandcamp.com/)
and 
[Daniel Deluxe](https://danieldeluxe.bandcamp.com/)
