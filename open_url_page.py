import webbrowser

query = raw_input("enter the query:")
url = "https://www.google.co.in/search?dcr=0&source=hp&ei=gWJ5WpKVMcrS0gKw4K2gAg&q=drogba&oq={0}&gs_l=psy-ab.3..0l10.2229.3374.0.3475.6.5.0.1.1.0.135.556.1j4.5.0....0...1c.1.64.psy-ab..0.6.571...0i131k1.0.TOs995qf-bQ".format(query)

webbrowser.open_new(url)
