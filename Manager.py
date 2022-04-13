def exist( postIndex, authorId ):
    line1 = open("./posts.txt", "r").read()
    lines = line1.split("\n")
    for line in lines:
        index = ""
        idd = ""
        indexing = True
        idding = False
        for ch in line:
            if indexing == True:
                if ch != " ":
                    index = index + ch
                else:
                    indexing = False
                    idding = True
                    continue
            elif idding == True:
                if ch != " ":
                    idd = idd + ch
                else:
                    break
    
        if( int(postIndex) == int(index) ):
            if( int(idd) == int(authorId) ):
                return 1
                break
            else:
                return 0
                break
    return -1

def addPost( content, authorId ):
    line1 = open("./posts.txt", "r").read()
    lines = line1.split("\n")
    for line in lines:
        index = ""
        indexing = True
        idding = False
        for ch in line:
            if indexing == True:
                if ch != " ":
                    index = index + ch
                else:
                    indexing = False
                    idding = True
                    continue
            elif idding == True:
                if ch == " ":
                    break
    line1 = open("./posts.txt", "a")
    line1.write(f"\n{int(index)+1} {authorId}")
    for cont in content:
        line1.write(f" {cont}")
    line1.write(" ")
    return str(int(index)+1)

def getPostContent( postIndex ):
    line1 = open("./posts.txt", "r").read()
    lines = line1.split("\n")
    line2 = ""
    spaces = 0
    content = []
    con = ""
    for line in lines:
        index = ""
        idd = ""
        indexing = True
        idding = False
        for ch in line:
            if indexing == True:
                if ch != " ":
                    index = index + ch
                else:
                    indexing = False
                    idding = True
                    continue
            elif idding == True:
                if ch != " ":
                    idd = idd + ch
                else:
                    break
    
        if( int(postIndex) == int(index) ):
            line2 = line
    for ch in line2:
        if( ch == " " ):
            spaces+=1
            if( spaces >= 3 ):
                content.append(int(con.replace(" ", "")))
                con = ""
        if( spaces >= 2 ):
            con = con + ch
        
    return content

def getAuthorId(postIndex):
    line1 = open("./posts.txt", "r").read()
    lines = line1.split("\n")
    for line in lines:
        index = ""
        idd = ""
        indexing = True
        idding = False
        for ch in line:
            if indexing == True:
                if ch != " ":
                    index = index + ch
                else:
                    indexing = False
                    idding = True
                    continue
            elif idding == True:
                if ch != " ":
                    idd = idd + ch
                else:
                    break
    
        if( int(postIndex) == int(index) ):
            return idd

def deletePost(postIndex):
    content = " ".join(map(str, getPostContent(postIndex)))
    f = open("./posts.txt", "r+")
    d = f.readlines()
    with open("./posts.txt", "w") as new_f:
        for line in d:  
            if line != f"{postIndex} {getAuthorId(postIndex)} {content} ":      
                new_f.write(line)
    f.truncate()
    f.close()
