#
# texto inadequado pode ser:
#     - contem palavras que são xingamentos (procura em lista)
#       (procura com REGEX)
#     - textos agressivos ou ofensivos (sera colocado futuramente
#        no escopo com analise de sentimentos com NLTK)
#     - conteudos que contenham payloads que produzam erros no sistema
#       (sera colocado futuramente no escopo com analise da entropia do texto)
#

def naLista(palavra):
    return palavra in listaPalavrasInadequadas

def palavraInadequada(palavra):
    return palavra.lower() in listaPalavrasInadequadas

def preparaTexto(texto):
    texto_lower = texto.lower()
    texto_split = texto_lower.split()
    return texto_split


def textoInadequado(texto):
	#
	# retorna o percentual de palavras inadequadas no texto
	#
    texto_split = preparaTexto(texto)
    ocorrencias = 0
    for palavra in texto_split:
        if palavra in listaPalavrasInadequadas:
            ocorrencias += 1
    return ocorrencias / len(texto_split)

def textoInadequadoRapido(texto):
	#
	# retorna o percentual de palavras inadequadas no texto
	#  para assim que encontra uma palavra inadequada
    texto_split = preparaTexto(texto)
    ocorrencias = 0
    for palavra in texto_split:
        if palavra in listaPalavrasInadequadas:
            ocorrencias += 1
            break
    return ocorrencias / len(texto_split)

listaPalavrasInadequadas = [
	'acefal',
	'anal',
	'ana!',
	'ant',
	'anus',
	'arombad',
	'baba-ovo',
	'babaca',
	'babaq',
	'babaovo',
	'bacanal',
	'bacana!',
	'bacura',
	'bagos',
	'baitol',
	'ba!tol',
	'baito!',
	'ba!to!',
	'bct',
	'bebum'
	'bicha',
	'bichinha',
	'bisca',
	'bixa',
	'bixinha',
	'boazuda',
	'bocet',
	'boiola',
	'boiolinha',
	'bo!ola',
	'bo!olinha',
	'bolagto',
	'bo!agto',
	'boquet',
	'bolcat',
	'bo!cat',
	'boset',
	'bosta',
	'bqt',
	'brioco',
	'br!oco',
	'bronha',
	'bucet',
	'bunda',
	'bunduda',
	'bur'
	'burinh'
	'buset',
	'cachora',
	'cadel',
	'cade!',
	'cacet',
	'caga',
	'cagado',
	'cagona',
	'canalha',
	'cana!ha',
	'caralh',
	'cara!h',
	'caseta',
	'casete',
	'caseto',
	'casetu',
	'chana',
	'chaninh',
	'chavasc',
	'chavask',
	'chavasquinh',
	'chavasqu!nh',
	'chechec',
	'chechek',
	'chechequinh',
	'chechequ!nh',
	'cherec',
	'cherek',
	'cherequinh',
	'cherequ!nh',
	'chererec',
	'chererek',
	'chererequinh',
	'chererequ!nh',
	'chibiu',
	'ch!biu',
	'chib!u',
	'ch!b!u',
	'chibumb',
	'ch!bumb',
	'chifrud',
	'ch!frud',
	'chota',
	'chotinh',
	'chot!nh',
	'chupa',
	'chupe',
	'clitoris',
	'cl!toris',
	'clitor!s',
	'cl!tor!s',
	'corna',
	'corninh',
	'corn!nh',
	'corno',
	'cornud',
	'crl',
	'cretin',
	'cret!n',
	'cruzcredo'
	'cruz-credo'
	'cusa',
	'cusinho',
	'cus!nho',
	'cusud',
	'curalho',
	'cura!ho',
	'cuza',
	'cuzinho',
	'cuz!nho',
	'cuzud',
	'debil',
	'debei',
	'demonio',
	'diabo',
	'diabinh',
	'dick',
	'doid',
	'doidinh',		
	'egua',
	'escrot',
	'esporad',
	'estupid',
	'estup!d',
	'fdp',
	'fedid',
	'fedor',
	'feia',
	'feio',
	'feinh',
	'fdm'
	'foda',
	'fode',
	'fodid',
	'fod!d',
	'fodinha',
	'fod!nha',
	'fodona',
	'fornica',
	'forn!ca',
	'fuck',
	'fude',
	'fudendo',
	'fudecao',
	'fudid',
	'fud!d',
	'furnica',
	'furn!ca',
	'gay',
	'gonore',
	'gosma',
	'gosment',
	'grelinho',
	'gre!inho',
	'grel!nho',
	'grelo',
	'goza',
	'gozo',
	'gozinh',
	'idiota',
	'!diota',
	'id!ota',
	'!d!ota',
	'idiotice',
	'!diotice',
	'id!otice',
	'idiot!ce',
	'!d!otice',
	'!diot!ce',
	'!d!ot!ce',
	'imbecil',
	'!mbecil',
	'imbec!l',
	'imbeci!',
	'!mbec!l',
	'!mbeci!',
	'iscrot',
	'!scrot',
	'kadel',
	'kade!',
	'kacet',
	'kaga',
	'kagado',
	'kagona',
	'kanalha',
	'kana!ha',
	'karalh',
	'kara!h',
	'kaseta',
	'kasete',
	'korna',
	'korninh',
	'korn!nh',
	'korno',
	'kornud',
	'krl',
	'kr!',
	'kretin',
	'kret!n',
	'kuralh',
	'kura!h',
	'kusa',
	'kusinho',
	'kus!nho',
	'kusudo',
	'kuza',
	'kuzinho',
	'kuz!nho',
	'kuzud',
	'ladra',
	'!adra',
	'ladroeira',
	'!adroeira',
	'ladroe!ra',
	'!adroe!ra',
	'ladrona',
	'!adrona',
	'lepros',
	'!epros',
	'lesbica',
	'!esbica',
	'lesb!ca',
	'!esb!ca',
	'loli',
	'!oli',
	'lo!i',
	'lol!',
	'!o!i',
	'!ol!',
	'macac',
	'machona',
	'machora',
	'manguaca',
	'masturba',
	'melec',
	'merda',
	'merdinha',
	'mija',
	'm!ja',
	'mije',
	'm!je',
	'mijo',
	'm!jo',
	'mocorong',
	'mocrea',
	'mocreia',
	'mocre!a',
	'mondrong',
	'mongol',
	'nadega',
	'nazi',
	'ninfeta',
	'n!nfeta',
	'nojeira',
	'noje!ra',
	'nojent',
	'nojo',
	'olhota',
	'orgia',
	'org!a',
	'otari',
	'otar!',
	'paca',
	'paspalh',
	'pauzao',
	'pauzaum',
	'pauzinho',
	'pauz!nho',
	'peida',
	'pe!da',
	'peide',
	'pe!de',
	'peidi',
	'peid!',
	'pe!di',
	'pe!d!',
	'peido',
	'pe!do',
	'pemba',
	'penian',
	'pen!an',
	'penis',
	'pen!s',
	'pentelh',
	'pente!h',
	'pepeca',
	'pepeka',
	'pepeq',
	'pererec',
	'pererek',
	'perereq',
	'peroc',
	'perok',
	'peroq',
	'peru',
	'pintudo',
	'p!ntudo',
	'pintao',
	'p!ntao',
	'pintaum',
	'p!ntaum',
	'pintaso',
	'p!ntaso',
	'pintinh',
	'p!ntinh',
	'pint!nh',
	'p!nt!nh',
	'piranha',
	'p!ranha',
	'piriguet',
	'p!riguet',
	'pir!guet',
	'p!r!guet',
	'piroc',
	'p!roc',
	'pirok',
	'p!rok',
	'piroq',
	'p!roq',
	'pora',
	'porinh',
	'porno',
	'ppk',
	'ppquinh',
	'pqp',
	'prostibulo',
	'prost!bulo',
	'prostibu!o',
	'prost!bu!o',
	'prostitut',
	'prost!tut',
	'punheta',
	'pupunha',
	'pustula',
	'pustu!a',
	'pusy',
	'puta',
	'putinh',
	'put!nh',
	'puto',
	'puxasaco',
	'puxa-saco',

	'rabao',
	'rabaum',
	'rabo',
	'rabud',
	'racha',
	'retardad',
	'ridicul',
	'rid!cul',
	'r!dicul',
	'r!d!cul',
	'rola',
	'ro!a',
	'rolinha',
	'ro!inha',
	'rol!nha',
	'rolud',
	'rosca',

	'sacana',
	'safad',
	'sapata',
	'sapataum',
	'sifili',
	's!fili',
	'sif!li',
	'sifi!i',
	'sifil!',
	's!f!li',
	's!fi!i',
	's!fil!',
	'sif!l!',
	's!f!l!',
	'siriric',
	's!riric',
	'sir!ric',
	'sirir!c',
	's!r!ric',
	's!rir!c',
	'sir!r!c',
	's!r!r!c',

	'tarad',
	'tesao',
	'testuda',
	'tesud',
	'tezao',
	'tezaum',
	'tezud',
	'transa',
	'transo',
	'trocha',
	'troucha',
	'trolha',
	'tro!ha',
	'troucha',
	'trouxa',
	'troxa',
	'vaca',
	'vadia',
	'vad!a',
	'vadio',
	'vad!o',
	'vagabund',
	'vagina',
	'vag!na',
	'vead',
	'viad',
	'v!ad',
	'vibrador',
	'v!brador',
	'vsf',
	'vtnc',
	'verme',
	'verminoid',
	'vomit',
	'xavasc',
	'xavask',
	'xavasquinh',
	'xavasqu!nh',
	'xerec',
	'xerek',
	'xerequinh',
	'xerequ!nh',
	'xererec',
	'xererek',
	'xererequinh',
	'xererequ!nh',
	'xexec',
	'xexek',
	'xexequinh',
	'xexequ!nh',
	'xibiu',
	'x!biu',
	'xib!u',
	'x!b!u',
	'xibumb',
	'x!bumb',
	'xifrud',
	'x!frud',
	'xota',
	'xotinh',
	'xot!nh',
	'xana',
	'xaninh',
	'xan!nh',
	'xupa',
	'xupe',
	'xupo'] 
