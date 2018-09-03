from itertools import permutations

# Unit 6: Fun with Words

"""
A portmanteau word is a blend of two or more words, like 'mathelete',
which comes from 'math' and 'athelete'.  You will write a function to
find the 'best' portmanteau word from a list of dictionary words.
Because 'portmanteau' is so easy to misspell, we will call our
function 'natalie' instead:

    natalie(['word', ...]) == 'portmanteauword' 

In this exercise the rules are: a portmanteau must be composed of
three non-empty pieces, start+mid+end, where both start+mid and
mid+end are among the list of words passed in.  For example,
'adolescented' comes from 'adolescent' and 'scented', with
start+mid+end='adole'+'scent'+'ed'. A portmanteau must be composed
of two different words (not the same word twice).

That defines an allowable combination, but which is best? Intuitively,
a longer word is better, and a word is well-balanced if the mid is
about half the total length while start and end are about 1/4 each.
To make that specific, the score for a word w is the number of letters
in w minus the difference between the actual and ideal lengths of
start, mid, and end. (For the example word w='adole'+'scent'+'ed', the
start,mid,end lengths are 5,5,2 and the total length is 12.  The ideal
start,mid,end lengths are 12/4,12/2,12/4 = 3,6,3. So the final score
is

    12 - abs(5-3) - abs(5-6) - abs(2-3) = 8.

yielding a score of 12 - abs(5-(12/4)) - abs(5-(12/2)) -
abs(2-(12/4)) = 8.

The output of natalie(words) should be the best portmanteau, or None
if there is none. 

"""


def natalie(words):
    "Find the best Portmanteau word formed from any two of the list of words."
    words = set(x for x in words if x)
    if len(words) < 2:
        return None

    pairs = permutations(words, 2)

    def getTails(s):
        return {s[i:] for i in range(1, len(s))}

    def getPres(s):
        return {s[:i] for i in range(1, len(s))}

    def trans(pair):
        a, b = pair
        tails, pres = getTails(a), getPres(b)
        maxScore = -1
        maxWord = None
        for common in tails & pres:
            commonLength = len(common)
            pre, mid, end = len(a) - commonLength, commonLength, len(b) - commonLength
            word = (a + b).replace(common, '', 1)
            l = len(word)
            score = l - sum(map(abs, [pre - l / 4, mid - l / 2, end - l /4]))
            if score > maxScore:
                maxScore = score
                maxWord = word
        return maxScore, maxWord

    result = max(map(trans, pairs), key=lambda x: x[0])
    score, word = result
    return word

def test_natalie():
    "Some test cases for natalie"
    assert (natalie(['eskimo', 'escort', 'kimchee', 'kimono', 'cheese'])
            == 'eskimono')
    assert (natalie(['kimono', 'kimchee', 'cheese', 'serious', 'us', 'usage'])
            == 'kimcheese')
    assert (natalie(['circus', 'elephant', 'lion', 'opera', 'phantom'])
            == 'elephantom')
    assert (natalie(['adolescent', 'scented', 'centennial', 'always',
                    'ado', 'centipede'])
            in ( 'adolescented', 'adolescentennial', 'adolescentipede'))
    assert (natalie(['programmer', 'coder', 'partying', 'merrymaking'])
            == 'programmerrymaking')
    assert (natalie(['int', 'intimate', 'hinter', 'hint', 'winter'])
            == 'hintimate')
    assert (natalie(['morass', 'moral', 'assassination'])
            == 'morassassination')
    assert (natalie(['entrepreneur', 'academic', 'doctor',
                     'neuropsychologist', 'neurotoxin', 'scientist', 'gist'])
            in ('entrepreneuropsychologist', 'entrepreneurotoxin'))
    assert (natalie(['perspicacity', 'cityslicker', 'capability', 'capable'])
            == 'perspicacityslicker')
    assert (natalie(['backfire', 'fireproof', 'backflow', 'flowchart',
                     'background', 'groundhog'])
            == 'backgroundhog')
    assert (natalie(['streaker', 'nudist', 'hippie', 'protestor',
                     'disturbance', 'cops'])
            == 'nudisturbance')
    assert (natalie(['night', 'day']) == None)
    assert (natalie(['dog', 'dogs']) == None)
    assert (natalie(['test']) == None)
    assert (natalie(['']) ==  None)
    assert (natalie(['ABC', '123']) == None)
    assert (natalie([]) == None)
    assert (natalie(['pedestrian', 'pedigree', 'green', 'greenery'])
            == 'pedigreenery')
    assert (natalie(['armageddon', 'pharma', 'karma', 'donald', 'donut'])
            == 'pharmageddon')
    assert (natalie(['lagniappe', 'appendectomy', 'append', 'lapin'])
            == 'lagniappendectomy')
    assert (natalie(['angler', 'fisherman', 'boomerang', 'frisbee', 'rangler',
                     'ranger', 'rangefinder'])
            in ('boomerangler', 'boomerangefinder'))
    assert (natalie(['freud', 'raelian', 'dianetics', 'jonestown', 'moonies'])
            == 'freudianetics')
    assert (natalie(['atheist', 'math', 'athlete', 'psychopath'])
            in ('psychopatheist', 'psychopathlete'))
    assert (natalie(['hippo', 'hippodrome', 'potato', 'dromedary'])
            == 'hippodromedary')
    assert (natalie(['taxi', 'taxicab', 'cabinet', 'cabin',
                     'cabriolet', 'axe'])
            in ('taxicabinet', 'taxicabriolet'))
    assert (natalie(['pocketbook', 'bookmark', 'bookkeeper', 'goalkeeper'])
            in ('pocketbookmark', 'pocketbookkeeper'))
    assert (natalie(['athlete', 'psychopath', 'athletic', 'axmurderer'])
            in ('psychopathlete', 'psychopathletic'))
    assert (natalie(['info', 'foibles', 'follicles'])
            == 'infoibles')
    assert (natalie(['moribund', 'bundlers', 'bundt'])
            == 'moribundlers')

print(test_natalie())
