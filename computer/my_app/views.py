from django.shortcuts import render

# Create your views here.

names = {
"Murodjon": {"id":1,"surname":"Tohirov", "age":26, "profession":"Mentor", "about":"Murodjon (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is the wealthiest person in the world, with an estimated net worth of US$232 billion as of December 2023, according to the Bloomberg Billionaires Index, and $254 billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX.["},
"Boburjon": {"id":2,"surname":"G'ulomov", "age":25, "profession":"Student", "about":"Boburjon (born October 28, 1955) is an American businessman, investor, philanthropist, and writer best known for co-founding the software giant Microsoft, along with his childhood friend Paul Allen. During his career at Microsoft, Gates held the positions of chairman, chief executive officer (CEO), president, and chief software architect, while also being its largest individual shareholder until May 2014.[2][a] He was a prominent pioneer of the microcomputer revolution of the 1970s and 1980s."},
"Ikromjon": {"id":3,"surname":"Odiljonov", "age":23, "profession":"Teacher", "about":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"},
"Javohir": {"id":4,"surname":"Tarichi", "age":19, "profession":"Unemployed", "about":"Galikarnasslik Gerodot — (qadimgi yunoncha: Ἡρόδοτος Ἁλικαρνᾱσσεύς, taxminan mil. avv. 484—425 yillar.) — qadimgi yunon tarixchisi, yunon-fors urushlari va oʻz davrining koʻplab xalqlarini urf-odatlarini taʼriflagan, birinchi toʻliq tarixiy traktat — „Tarix“ning muallifi. Gerodotning asarlari antik madaniyat uchun katta ahamiyatga ega boʻlgan. Sitseron uni, hayotligidayoq „tarix otasi“ deb ataydi."}
}



def index(request):
    return render(request, "my_app/index.html", context={"names":names})

def main(request):
    return render(request, "my_app/main.html")


def about(request,id):
    for key,value in names.items():
        if value["id"]==id:
            return render(request, 'my_app/about.html', context={"value":value})
            
    return render(request, 'my_app/about.html')