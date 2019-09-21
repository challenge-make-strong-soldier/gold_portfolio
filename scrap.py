try:
    hist = yf.download("SPY ^GSPC TLT GLD GDX ^FVX,^TNX,^TYX", start=start, end=end) # GC=F
    f = open('data/history.pkl', 'wb')
    pickle.dump(hist, f)
    f.close()
except:
    pass