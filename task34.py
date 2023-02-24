def rhyme(phrase):
    val = phrase.lower().split()
    func = lambda x: sum(1 for i in x if i in 'аеиоуыэюя')
    temp = func(val[0])
    if all([func(i) == temp for i in val]):
        print('Парам пам-пам')
    else:
        print('Пам парам')
 
rhyme('пара-ра-рам рам-пам-папам па-ра-па-дам')
rhyme(input())