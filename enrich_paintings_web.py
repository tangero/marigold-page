#!/usr/bin/env python3
"""
Enrich painting articles with information from web search and structured data.
Uses a simple approach with known art history facts.
"""
import os
import re
from pathlib import Path

# Comprehensive painting database
PAINTINGS_DATA = {
    "Venus de Milo": {
        "rok": "cca 150-125 př. n. l.",
        "styl": "helénistické sochařství",
        "autor": "Neznámý",
        "autor_narozen": "neznámo",
        "uvod": "Venuše Milská je jednou z nejslavnějších antických soch, která ztělesňuje ideál ženské krásy. Socha byla objevena v roce 1820 na řeckém ostrově Mílos a přestože jí chybí obě paže, její elegance a proporce uchvátily celý svět umění.",
        "kde_videt": "Louvre, Paříž, Francie",
        "autor_fakta": [
            "🗿 Socha byla objevena v roce 1820 na ostrově Mílos",
            "🏛️ Představuje pravděpodobně bohyni Afrodítu (Venuši)",
            "📏 Výška sochy je přibližně 203 cm",
            "🎭 Paže byly pravděpodobně ztraceny při objevení nebo krátce poté"
        ],
        "o_obraze": [
            "socha zobrazuje ženu v kontrapostu s bohatě řasenou drapérií",
            "detailní zpracování tkaniny a lidského těla ukazuje mistrovství helénistického sochařství",
            "záhada chybějících paží vedla k mnoha teoriím o původní póze sochy",
            "socha spojuje klasickou harmonii s helénistickou expresivitou"
        ],
        "detaily": {
            "styl_popis": "Helénistické sochařství kombinující klasickou krásu s naturalistickým zpracováním",
            "perspektiva": "Socha byla navržena ke zhlédnutí z mírně levého úhlu, dynamická kompozice",
            "inspirace": "Klasické řecké sochařství 5. a 4. století př. n. l.",
            "nalada": "Božská elegance a nadčasová krása"
        },
        "historicky_kontext": "Socha vznikla v období helénismu, kdy se řecká kultura šířila po celém Středomoří po výbojích Alexandra Velikého. V této době umělci kombinovali klasické ideály s větším naturalismem a expresivitou.",
        "srovnani": [
            "🏛️ **Praxitelés** - klasický řecký sochař, autor Afrodity Knidské",
            "🗿 **Nike ze Samothráky** - další slavná helénistická socha v Louvru",
            "⚡ **Laokoón a jeho synové** - dramatičtější helénistické dílo"
        ]
    },
    "Nike of Samothrace": {
        "rok": "cca 200-190 př. n. l.",
        "styl": "helénistické sochařství",
        "autor": "Neznámý",
        "autor_narozen": "neznámo",
        "uvod": "Nike ze Samothráky, známá také jako Vítězná Nike, je monumentální helénistická socha oslavující vítězství v námořní bitvě. Socha byla objevena v roce 1863 na ostrově Samothráké a stala se jedním z nejdynamičtějších děl antického umění.",
        "kde_videt": "Louvre, Paříž, Francie - umístěna na vrcholu Schodiště Daru",
        "autor_fakta": [
            "🏺 Objevena v roce 1863 archeologem Charlesem Champoisem",
            "⛵ Původně stála na přídi lodi vytesané z kamene",
            "🌊 Pravděpodobně oslavovala námořní vítězství",
            "👤 Chybí jí hlava a paže, ale dynamika pohybu je zachována"
        ],
        "o_obraze": [
            "socha zachycuje bohyni vítězství Nike v okamžiku přistání na lodi",
            "mistrně zpracované řasení šatu vytváří dojem pohybu větru",
            "křídla jsou rozpjata v dramatickém gestu",
            "kompozice vyjadřuje triumf a dynamickou energii"
        ],
        "detaily": {
            "styl_popis": "Helénistické sochařství s důrazem na dramatický pohyb a expresivitu",
            "perspektiva": "Navržena k pohledu zespodu vzhůru, monumentální dojem",
            "inspirace": "Oslavy námořních vítězství a bohyně Nike jako symbol triumfu",
            "nalada": "Dynamický triumf a vítězství nad živly"
        },
        "historicky_kontext": "Socha pravděpodobně vznikla jako votivní dar oslavující námořní vítězství, možná bitvu u Salamíny na Kypru. Helénistické období se vyznačovalo dramatičností a dynamikou v umění.",
        "srovnani": [
            "🗿 **Venuše Milská** - další slavná helénistická socha v Louvru",
            "⚡ **Laokoón** - podobně dramatické dílo helénistického sochařství",
            "🏛️ **Parthenonské frízy** - klasičtější přístup k pohybu v řeckém umění"
        ]
    },
    "Mona Lisa": {
        "rok": "1503-1519",
        "styl": "vrcholná renesance",
        "autor": "Leonardo da Vinci",
        "autor_narozen": "1452-1519",
        "uvod": "Mona Lisa je nejslavnějším obrazem na světě, mistrovské dílo Leonarda da Vinciho zachycující ženu s enigmatickým úsměvem. Obraz fascinuje diváky již více než 500 let svou psychologickou hloubkou a revoluční malířskou technikou sfumato.",
        "kde_videt": "Louvre, Paříž, Francie",
        "autor_fakta": [
            "🎨 Všestranný génius - malíř, vynálezce, vědec, anatomik",
            "📚 Zanechal tisíce stran poznámek a skic v zrcadlovém písmu",
            "✈️ Navrhl koncepty helikoptér, tanků a dalších vynálezů století před jejich realizací",
            "🔬 Prováděl detailní anatomické studie pitvou lidských těl"
        ],
        "o_obraze": [
            "zobrazuje pravděpodobně Lisu Gherardini, manželku florentského obchodníka",
            "Leonardo pracoval na obraze mnoho let a nikdy jej nepovažoval za dokončený",
            "revoluční technika sfumato vytváří jemné přechody bez viditelných tahů štětcem",
            "záhadný úsměv se zdá měnit podle úhlu pohledu díky optickému efektu",
            "krajina v pozadí je fantastická a atmosférická, vytvořená vzdušnou perspektivou"
        ],
        "detaily": {
            "styl_popis": "Leonardo používá techniku sfumato (jemné kouřové přechody) a vzdušnou perspektivu k vytvoření iluze hloubky",
            "perspektiva": "Pyramidová kompozice s Lisou v popředí a snovou krajinou v pozadí",
            "inspirace": "Leonardovy anatomické studie a zájem o optiku a lidskou psychologii",
            "nalada": "Záhadná, kontemplativní, nadčasová"
        },
        "historicky_kontext": "Obraz vznikl během vrcholné renesance ve Florencii a Miláně. Leonardo jej nosil s sebou po celý život a nakonec jej prodal francouzskému králi Františku I. Od té doby zůstal ve francouzském vlastnictví.",
        "srovnani": [
            "🖼️ **Raphael** - Madona se stehlíčkem, podobná pyramidová kompozice",
            "🎨 **Jan van Eyck** - Portrait Arnolfini, detailní portrétní technika",
            "👤 **Sandro Botticelli** - Portrét mladé ženy, florentský portrét téže doby"
        ]
    },
    "The Last Supper": {
        "rok": "1495-1498",
        "styl": "vrcholná renesance",
        "autor": "Leonardo da Vinci",
        "autor_narozen": "1452-1519",
        "uvod": "Poslední večeře je monumentální nástěnná malba zachycující dramatický okamžik, kdy Ježíš oznamuje svým učedníkům, že jeden z nich ho zradí. Leonardo revolucionalizoval zobrazení této scény psychologickým vhledem a mistrovskou kompozicí.",
        "kde_videt": "Klášter Santa Maria delle Grazie, Milán, Itálie",
        "autor_fakta": [
            "🎨 Všestranný génius renesance",
            "🔬 Studoval lidskou anatomii pitvou více než 30 těl",
            "📐 Mistr perspektivy a matematických proporcí",
            "✍️ Psal zrcadlovým písmem zprava doleva"
        ],
        "o_obraze": [
            "zachycuje okamžik oznámení zrady v dramatických reakcích všech apoštolů",
            "každý z dvanácti apoštolů má jedinečnou psychologickou reakci",
            "Kristus je umístěn v geometrickém středu kompozice s trojúhelníkovou siluetou",
            "perspektiva směřuje k Ježíšově hlavě jako mizícímu bodu",
            "Leonardo experimentoval s novou technikou místo tradiční fresky, což vedlo k pozdějšímu poškození"
        ],
        "detaily": {
            "styl_popis": "Renesanční mistr perspektivy a lidské anatomie s revolučním psychologickým přístupem",
            "perspektiva": "Lineární perspektiva s mizícím bodem za Kristovou hlavou",
            "inspirace": "Biblický příběh Poslední večeře, Leonardovy anatomické studie",
            "nalada": "Dramatické napětí a psychologická intenzita"
        },
        "historicky_kontext": "Dílo bylo vytvořeno na zakázku vévody Lodovica Sforzy pro refektář dominikánského kláštera v Miláně během vrcholné renesance. Bohužel Leonardova experimentální technika vedla k rychlému poškození díla.",
        "srovnani": [
            "🎨 **Tintoretto** - Poslední večeře, dynamičtější manýristická verze",
            "🖼️ **Andrea del Castagno** - Poslední večeře, dřívější florentská verze",
            "👤 **Michelangelo** - Sixtinská kaple, monumentální biblické scény"
        ]
    },
    "Starry Night": {
        "rok": "1889",
        "styl": "postimpresionismus",
        "autor": "Vincent van Gogh",
        "autor_narozen": "1853-1890",
        "uvod": "Hvězdná noc je ikonickým dílem Vincenta van Gogha, které zachycuje noční oblohu nad Saint-Rémy-de-Provence s bouřlivými víry a zářícími hvězdami. Obraz vznikl během umělcova pobytu v psychiatrické léčebně a stal se symbolem expresivní síly umění.",
        "kde_videt": "Museum of Modern Art (MoMA), New York, USA",
        "autor_fakta": [
            "🎨 Za svého života prodal pouze jeden obraz",
            "✉️ Psal stovky dopisů svému bratrovi Theovi, které dokumentují jeho život",
            "🌻 Namaloval během svého života více než 2000 děl za pouhých 10 let",
            "🏥 Trpěl duševní nemocí a dobrovolně se nechal hospitalizovat v Saint-Rémy"
        ],
        "o_obraze": [
            "malováno z okna jeho pokoje v psychiatrické léčebně, i když krajina je částečně imaginární",
            "charakteristické víry a spirály vyjadřují vnitřní emocionální stav",
            "cypřiš v popředí připomíná plamen dosahující k nebesům",
            "vesnice dole kontrastuje s dramatickou oblohou, představující klid a řád",
            "hvězdy a měsíc září s nadpřirozenou intenzitou"
        ],
        "detaily": {
            "styl_popis": "Postimpresionismus s expresivními, vírovými tahy štětcem a intenzivními barvami",
            "perspektiva": "Pohled z výšky na vesnici s dramatickou oblohou dominující kompozici",
            "inspirace": "Skutečný pohled z okna léčebny, japonské dřevotisky, vlastní emocionální stav",
            "nalada": "Bouřlivá, transcendentní, plná emocionální energie"
        },
        "historicky_kontext": "Obraz vznikl v červnu 1889 během van Goghova dobrovolného pobytu v psychiatrické léčebně v Saint-Rémy-de-Provence. Trpěl psychickými krizemi, ale pokračoval v produktivní tvorbě. Zemřel o rok později.",
        "srovnani": [
            "🌊 **Edvard Munch** - Výkřik, podobně expresivní zobrazení vnitřního stavu",
            "🎨 **Paul Gauguin** - syntetické barvy a emocionální expresivita",
            "🖌️ **Henri de Toulouse-Lautrec** - další postimpresionista stejné generace"
        ]
    },
    "The Scream": {
        "rok": "1893",
        "styl": "expresionismus",
        "autor": "Edvard Munch",
        "autor_narozen": "1863-1944",
        "uvod": "Výkřik je jedním z nejrozpoznatelnějších obrazů všech dob, zachycující křičící postavu na mostě v Oslo. Munch vytvořil tento obraz jako vyjádření existenciální úzkosti a moderní alienace, která rezonuje s diváky dodnes.",
        "kde_videt": "Národní galerie v Oslo, Norsko (existuje několik verzí)",
        "autor_fakta": [
            "🎨 Norský malíř, průkopník expresionismu",
            "💔 Ztratil matku a sestru v dětství na tuberkulózu, což ovlivnilo jeho tvorbu",
            "🖼️ Vytvořil čtyři verze Výkřiku různými technikami",
            "😷 Trpěl depresemi a úzkostí, které byly tématem jeho díla"
        ],
        "o_obraze": [
            "inspirováno skutečnou zkušeností při procházce, kdy Munch viděl krvavě červenou oblohu",
            "postava v popředí není zdrojem výkřiku, ale reaguje na děsivý výkřik přírody",
            "vlnivé linie krajiny a oblohy vyjadřují úzkost a nestabilitu",
            "zjednodušené tvary a intenzivní barvy posilují emocionální účinek",
            "most v pozadí je skutečný most Ekeberg v Oslo"
        ],
        "detaily": {
            "styl_popis": "Raný expresionismus s vlnitými liniemi a intenzivními, nerealistickými barvami",
            "perspektiva": "Diagonální kompozice s postavou v popředí a mostem vedoucím do pozadí",
            "inspirace": "Munchova osobní zkušenost úzkosti při západu slunce",
            "nalada": "Existenciální úzkost, osamění, psychologické napětí"
        },
        "historicky_kontext": "Obraz vznikl na konci 19. století, kdy se v umění objevoval symbolismus a raný expresionismus. Munch vytvořil dílo jako reakci na moderní život a rostoucí pocit alienace v industrializované společnosti.",
        "srovnani": [
            "🌟 **Vincent van Gogh** - Hvězdná noc, podobně expresivní zobrazení emocionálního stavu",
            "🎨 **James Ensor** - expresivní, groteskní figury",
            "🖼️ **Egon Schiele** - expresionistické portréty plné napětí"
        ]
    }
}

# Add more paintings data here...
# For brevity, I'll add a few more key ones

PAINTINGS_DATA.update({
    "David": {
        "rok": "1501-1504",
        "styl": "vrcholná renesance",
        "autor": "Michelangelo Buonarroti",
        "autor_narozen": "1475-1564",
        "uvod": "David je monumentální mramorová socha vytvořená Michelangelem, která představuje biblického hrdinu před jeho bojem s Goliášem. S výškou přes 5 metrů je tato socha považována za vrchol renesančního sochařství a symbol florentské republiky.",
        "kde_videt": "Galleria dell'Accademia, Florencie, Itálie",
        "autor_fakta": [
            "🗿 Jeden z největších sochařů všech dob",
            "🎨 Také malíř Sixtinské kaple",
            "📐 Studoval lidskou anatomii pitvou těl",
            "💪 Vytesal Davida z jediného kusu mramoru, který ostatní umělci odmítli"
        ],
        "o_obraze": [
            "na rozdíl od předchozích zobrazení ukazuje Davida před bitvou, v okamžiku soustředění",
            "detailní anatomie odhaluje Michelangelovo mistrovské znalosti lidského těla",
            "pravá ruka je záměrně větší, zdůrazňující sílu",
            "pohled směřuje k nepříteli, vyjadřující odhodlání",
            "contrapposto póza vytváří dynamický, přirozený postoj"
        ],
        "detaily": {
            "styl_popis": "Vrcholně renesanční naturalistická socha s důrazem na anatomii a kontrapost",
            "perspektiva": "Socha byla původně určena pro umístění vysoko na katedrále, odtud mírně zvětšené proporce hlavy a rukou",
            "inspirace": "Antické řecké a římské sochařství, biblický příběh",
            "nalada": "Napětí před bojem, odhodlání, heroismus"
        },
        "historicky_kontext": "Socha byla vytvořena pro Florentskou republiku jako symbol občanské svobody a obrany proti tyranům. David symbolizuje malou, ale odvážnou Florencii proti větším nepřátelům.",
        "srovnani": [
            "🏛️ **Donatello** - David (1440), dřívější bronzová verze",
            "⚔️ **Bernini** - David (1623), barokní dynamická verze zachycující akci",
            "🗿 **Antické řecké sochy** - Doryphoros, klasický ideál"
        ]
    },
    "Girl with a Pearl Earring": {
        "rok": "cca 1665",
        "styl": "nizozemský zlatý věk, barok",
        "autor": "Johannes Vermeer",
        "autor_narozen": "1632-1675",
        "uvod": "Dívka s perlou je nádherný portrét mladé ženy s exotickým turbanem a velkou perlovou náušnicí. Vermeerovo mistrovské zacházení se světlem a stínem vytváří intimní, nadčasový okamžik, díky kterému je tento obraz často nazýván 'nizozemskou Monou Lisou'.",
        "kde_videt": "Mauritshuis, Haag, Nizozemsko",
        "autor_fakta": [
            "🎨 Jeden z nejvýznamnějších malířů nizozemského zlatého věku",
            "💡 Mistr v zachycení světla a intimních domácích scén",
            "🖼️ Za života vytvořil pouze asi 45 obrazů",
            "🔍 Možná používal camera obscura jako pomůcku při malování"
        ],
        "o_obraze": [
            "nejedná se o tradiční portrét, ale o 'tronie' - studii hlavy nebo výrazu",
            "identita dívky zůstává záhadou, mohla být modelkou nebo dcerou umělce",
            "perla na náušnici je namalována pouze dvěma tahy štětce, ale vypadá realisticky",
            "tmavé pozadí činí dívku ještě zářivější",
            "otevřená ústa dívky a její pohled vytváří intimní spojení s divákem"
        ],
        "detaily": {
            "styl_popis": "Vermeerovo charakteristické jemné zacházení se světlem, hladký štětec a zářivé barvy",
            "perspektiva": "Jednoduchá kompozice se zaměřením na tvář a rám dívky",
            "inspirace": "Orientální móda (turban), nizozemský zájem o exotiku",
            "nalada": "Intimní, záhadná, tichá krása"
        },
        "historicky_kontext": "Obraz vznikl během nizozemského zlatého věku, období prosperity a kulturního rozkvětu v Nizozemsku. Vermeer pracoval pomalu a pečlivě, vytvářel pouze několik obrazů ročně.",
        "srovnani": [
            "🖼️ **Leonardo da Vinci** - Mona Lisa, podobná záhada identity a výrazu",
            "🎨 **Rembrandt van Rijn** - nizozemský mistr světla stejné doby",
            "👤 **Frans Hals** - expresivní portréty nizozemského zlatého věku"
        ]
    },
    "Guernica": {
        "rok": "1937",
        "styl": "kubismus, surrealismus",
        "autor": "Pablo Picasso",
        "autor_narozen": "1881-1973",
        "uvod": "Guernica je monumentální protiválečné dílo Pabla Picassa, které zachycuje hrůzu bombardování baskického města Guernica během španělské občanské války. Tento černobílý obraz se stal univerzálním symbolem proti válečným atrocitám.",
        "kde_videt": "Museo Reina Sofía, Madrid, Španělsko",
        "autor_fakta": [
            "🎨 Jeden z nejvlivnějších umělců 20. století, spoluzakladatel kubismu",
            "🌍 Vytvořil více než 50 000 uměleckých děl během svého života",
            "🇪🇸 Španělského původu, většinu života strávil ve Francii",
            "🕊️ Guernica byla jeho nejsilnější politické prohlášení"
        ],
        "o_obraze": [
            "zachycuje chaos a utrpení způsobené bombardováním civilního města",
            "fragmentované kubistické formy vyjadřují rozbitý a zničený svět",
            "symbolické postavy zahrnují křičící ženu, mrtvé dítě, umírajícího koně a býka",
            "černobílé provedení zdůrazňuje novinový, dokumentární charakter",
            "světlo žárovky nahoře symbolizuje moderní technologii použitou ke zničení"
        ],
        "detaily": {
            "styl_popis": "Kubismus kombinovaný s expresivní, surrealistickou symbolikou",
            "perspektiva": "Zploštělá, fragmentovaná kompozice bez tradiční perspektivy",
            "inspirace": "Bombardování Guernicy nacistickými letouny 26. dubna 1937",
            "nalada": "Chaos, hrůza, zoufalství, protiválečný protest"
        },
        "historicky_kontext": "Obraz byl vytvořen jako reakce na bombardování Guernicy během španělské občanské války. Picasso jej namaloval během několika týdnů pro světovou výstavu v Paříži 1937. Stal se ikonou proti fašismu a válce.",
        "srovnani": [
            "🎨 **Otto Dix** - Válka, expresionistické zobrazení hrůz první světové války",
            "🖼️ **Goya** - Třetí května 1808, dřívější španělské protiválečné dílo",
            "💥 **Anselm Kiefer** - moderní zpracování válečné tematiky"
        ]
    }
})


def get_painting_files(directory):
    """Get all markdown files from directory."""
    files = []
    for file in Path(directory).glob('*.md'):
        if 'bar-ve-folies' not in file.name:
            files.append(str(file))
    return sorted(files)


def extract_frontmatter(content):
    """Extract frontmatter from markdown content."""
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        body = match.group(2)
        fm_dict = {}
        for line in frontmatter.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                fm_dict[key.strip()] = value.strip().strip('"')
        return fm_dict, body
    return {}, content


def create_enriched_article(filepath, data):
    """Create enriched markdown article from data."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm, body = extract_frontmatter(content)

    # Update frontmatter
    fm['namalovano'] = data['rok']
    fm['styl'] = data['styl']

    # Create new content
    new_body = f"\n\n{data['uvod']}\n\n"
    new_body += f"## 🖼️ Kde dílo vidět\n{data['kde_videt']}\n\n"
    new_body += f"## {fm['autor']}\n"
    new_body += f"- 🗓️ **Narozen/a:** {data['autor_narozen']}\n"

    for fact in data['autor_fakta']:
        new_body += f"- {fact}\n"

    new_body += f"\n![{fm['obraz']}]({fm['urlobrazu']})\n\n"
    new_body += f"## 🎨 O obraze {fm['obraz']}\n\n"

    for detail in data['o_obraze']:
        new_body += f"- {detail}\n"

    new_body += "\n## Pár detailů k obrazu\n\n"
    new_body += f"- 🖋️ **Styl:** {data['detaily']['styl_popis']}\n"
    new_body += f"- 🪞 **Perspektiva:** {data['detaily']['perspektiva']}\n"
    new_body += f"- 🎭 **Inspirace:** {data['detaily']['inspirace']}\n"
    new_body += f"- 🌃 **Nálada:** {data['detaily']['nalada']}\n\n"
    new_body += f"## Historický kontext\n\n{data['historicky_kontext']}\n\n"
    new_body += "## Srovnání s dalšími umělci\n\n"

    for comparison in data['srovnani']:
        new_body += f"- {comparison}\n"

    # Reconstruct file
    new_content = "---\n"
    for key, value in fm.items():
        if value:
            if ' ' in str(value) or ':' in str(value) or ',' in str(value):
                new_content += f'{key}: "{value}"\n'
            else:
                new_content += f'{key}: {value}\n'
        else:
            new_content += f'{key}:\n'
    new_content += "---"
    new_content += new_body

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✓ Enriched {os.path.basename(filepath)}")


if __name__ == '__main__':
    directory = '/Users/imac/Github/zastupitelstvo/_obrazy'
    files = get_painting_files(directory)

    print(f"Found {len(files)} painting files")
    enriched_count = 0

    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        fm, _ = extract_frontmatter(content)
        artwork = fm.get('obraz', '')

        if artwork in PAINTINGS_DATA:
            print(f"\nProcessing: {artwork}")
            create_enriched_article(filepath, PAINTINGS_DATA[artwork])
            enriched_count += 1
        else:
            print(f"  Skipping {artwork} (no data available)")

    print(f"\n✅ Done! Enriched {enriched_count} paintings.")
    print(f"📝 You can add more paintings to PAINTINGS_DATA dictionary to enrich more articles.")
