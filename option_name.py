import pickle



bolly_movies_list=pickle.load(open('bolly_movies.pkl','rb'))
# def name(l):
for x in bolly_movies_list.original_title:
    print("<option>"+x+"</option>")

try:
    if(2==5):
        print('they are equal')
except:
    print('unequal')


