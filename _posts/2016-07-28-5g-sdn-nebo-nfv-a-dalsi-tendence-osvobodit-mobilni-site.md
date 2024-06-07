---
ID: 3098
title: '5G: SDN nebo NFV a&nbsp;další tendence osvobodit mobilní sítě'
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/5g-sdn-nebo-nfv-a-dalsi-tendence-osvobodit-mobilni-site
published: true
post_date: 2016-07-28 20:46:59
---
<p>Kolem sítí páté generace se objevuje celá řada nových architektonických a konstrukčních přístupů. Dnešní malý náhled bude na dva významné přístupy, které se mají podílet na poklesu cen infrastruktury a do jisté míry i na “laicizaci” - tedy zjednodušení síťové infrastruktury tak, aby byla snáze obsluhovatelná. Tlak je tedy jak na capex, tak na provozní výdaje opex - to z pohledu velkého operátora. Z pohledu menších operátorů by mohlo dojít k tomu, že infrastruktura 5G jimi bude použitelná.</p>


<!--more-->

<p>Tohle je ostatně zajímavý postřeh, který výrobcům infrastruktury přinesl střet 3G s WiFi, jenž 3G sítě málem neustály. Ukázalo se totiž krátce po přelomu tisíciletí, že běžní zákazníci sice chtějí “data vždy a všude”, ale nejsou ochotni si za to příliš připlácet (existovalo důvodné podezření, že si nejsou ochotni připlácet vůbec).Pokud se tedy v počátku rozjezdu 3G operátoři domnívali, že vznikne tlačenka na právo připlatit si padesát euro za datové tarify kolem 400 Kb/s, které první 3G nabízelo, byli operátoři záhy vyvedeni z omylu. Starší skupina zákazníků prostě mobilní datovou technologii adaptovala pomalu (či vůbec a drze používala notebooky s WiFi), mladší dokonce vyvinula nepředpokládané substituční řešení, kdy namísto videokonferencí a dalších drahých polo-datových 3G služeb začala zhusta používat texting, navíc formou zkrácených akronymů, které v jazyce zastupovaly roli kompresního algoritmu. S rozvojem mobilních IM služeb, kde operátorská Wireless Village projela boj bez boje, se v první polovině prvního desetiletí ukazuje, že s mobilními daty to nebude tak žhavé. A tím mine příležitost splatit investice do 3G a prodat hromady železa.</p>

<p>Pak přišel Apple s prasáckou myšlenkou, dát do mobilu WiFi. Chápejte, dát něco, co může být používáno zdarma, do posvátného chrámu operátorského výdělku. To je z pohledu operátora jako stoupnout si s pořádnou náloží pod Asuánskou přehradu a těšit se na sprchu. Svinstvo, terorismus, příležitost vysmát se tomu naivkovi Jobsovi ještě před tím, než půjde pod ochranu paragrafu jedenáct. Zbytek je historie: WiFi bylo přesně to, co zákazníci chtěli, z počátku téměř 90% datových přenosů natočili na svých mobilech právě přes něj. Apple se vykoupalo ve zlatě a dodnes se v něm koupe, operátoři čučeli na vypuštěnou přehradu jako puci a ostatní výrobci hromadně naskakovali na vlnu datového multimediálního centra v kapse nadšeného uživatele. Někteří úspěšně, zejména ti čínští, jimž byl osud a názor euro-amerických operátorů poněkud ukradený, jiné lpění na dogmatech ohrazené zahrádky stáhlo pod vodu, Nokia byla zářný příklad. Tím vlastně zmizely všechny dosud dominantní evropské mobilní značky.</p>

<p>Ponaučení? Když nedáte zákazníkovi to, co chce, za nějakou dobu si stejně cestu najde a vy budete stát opodál. Proto se při rozvoji standardu 5G klade důraz na to, aby všechny moderní komunikační technologie do něj byly zapojené. Výrobci infrastruktury tak budou moci nabídnout i drobným zákazníkům technologie na bázi 5G za levný peníz. Zda to vyjde, k tomu ještě dáme příležitostně menší rozpravu, neboť tu vzniká problém levného kanónu na vrabce.</p>

<p>Zpět z motivační okliky. Má-li hardware být levný, je potřeba, aby byl pokud možno co nejsnáze modifikovatelný. Hodilo by se tedy použít několik přístupů známých ze světa PC: co nejvíce funkcí vytvořit pomocí software, aby bylo možné funkce přizpůsobovat aktualizací software a ne výměnou hardware. To za prvé. Za druhé možnost řetězení těchto funkcí v rámci jednoho hardware. A za třetí, modularitou jednotlivých hardwarových částí tak, aby se potřebné hardwarové podpory oněm softwarovým funkcím dostávalo výměnou či dokoupením kousků hardware asi tak, jako když si ke svému PC dokoupíte DVD mechaniku.</p>

<p>V řeči buzzwordů se zrodily tyto pojmy:</p>

<ul>
<li>SDN - Software Defined Networking, softwarově definované síťování.</li>
<li>NFV - Network Functions Virtualization - virtualizace síťových funkcí</li>
</ul>
<p>Pojmy vypadají zaměnitelně, ale nejsou - jsou spíše komplementární.</p>

<p><strong>SDN</strong> obnáší oddělení "řídící části" od samotné “výkonové” části sítě. Pod pojmem výkonová část sítě si představte optické koncentrátory, antény, vysílače a další propojovací technologii, zatímco samotné zpracování těchto signálů se vyčleňuje jako prvek SDN. Povýšení takové sítě či změna “technologie” v ní nabízené se tedy může udát “pouhým” upgrade software v té síti, díky čemuž síť nabídne nové funkce. Nedá se tedy říci, že by se SDN týkala jen někdejšího Core Network (či spíše EPC v 4G) nebo naopak RAN/E-UTRAN, týká se čehokoliv, co takto může být vyjmuto a převedeno do software.</p>

<p><img title="/obrazek/fnc-sdn1.PNG" src="/obrazek/fnc-sdn1.png" alt="schéma" width="600" height="267" border="0" /></p>

<p><strong>NFV</strong> oproti tomu bere síťové služby, které byly dříve provozovány na samostatných síťových prvcích, jako je cache, DNS atd - a převádí je jako čistý software. Tím se na první pohled kryje s SDN, jenže zatímco v případě SDN jde o rozdělení hardware sítě na část obsluhovatelnou softwarově a na to, co musí zůstat jako samostatný hardware, v případě NFV jde o úsporu místa i provozních starostí tím, že se dříve samostatné služby převádějí na společnou platformu, na běžné servery. V obojím případě je to tlak na cenu. SDN odděluje relativně drahý specializovaný hardware s jiným životním a investičním cyklem od komoditního serveru, na němž běží to, co na něm běžet může. NFV omezuje potřebu hromady specializovaných serverů pro síťové služby a vše převádí na standardní komoditní servery. Někde tady můžete zároveň hledat decentralizaci a <a href="http://www.lupa.cz/clanky/edge-computing-a-fog-computing-o-vyhodach-mlznych-siti/">odbočku k mlžným sítím, edge computingu</a>.</p>


<p><img src="/obrazek/nfv-diagram.jpg" alt="schéma" width="600" border="0" /></p>


<p><br />S ohledem na to je podstatou SDN především nízkoúrovňové API propojující software a komponenty, zatímco podstatou vyjadřující NFV je orchestrace prvků NFV, protože jednotlivé služby v NFV jsou samostatně kompletní a jde jen o to, poskládat jejich součinnost tak, aby výsledek byl ten očekávaný a správný.</p>

<h3>SDN a NFV: přínosy</h3>
<p>Nyní pojďme od analýzy změn v sítích 5G k syntéze přínosů. Tu lze vnímat v celé řadě úrovní.</p>

<h4>Cenový tlak</h4>
<p>Tak především snížení pořizovacích nákladů na síť komodizací použitého hardware, kdy jen málo hardware bude speciální, většinou bude možné použít běžné komerční servery, protože výkon jejich hardware dnes poskytuje značnou flexibilitu užití. Půjde například o anténní pole, nezapomínejme na to, že antény používají směřování signálu vůči mnoha uživatelům, massive multiple-in multiple-out beamforming. Nebo rádiové TX/RX prvky.</p>

<h4>Mikrooperátoři</h4>
<p>Za druhé bude možné integrovat jednotlivé přístupové technologie, například právě WiFi do ekosystému 5G. To se doposud šilo hodně horkou jehlou. V zásadě nejjednoduší bývalo integraci nedělat, WiFi síť nechat otevřenou či s heslem napsaným na kandelábru a brát to jako ulehčení vlastní síti. Nově je tu možnost, že WiFi operátoři použijí relevantní levné části 5G infrastruktury jednak k orchestraci (to je pojem, co!) svých přístupových bodů, ale také k tomu, aby partnerům nabídli možnost pronájmu svého WiFi jejich klientům. Po virtuálních operátorech, kteří nemají infrastrukturu, ale mají klienty, se tak mají zrodit i mikrooperátoři, kteří naopak mají infrastrukturu, do které se tlačí klienti. Tady je třeba upomenout se na dlouhodobé problémy, s nimiž se potýkala autentizační a autorizační architektura AKA v rámci 3G založená na U/SIM, jež znemožňovala klienta věrohodně přehodit do WiFi se znalostí jeho totožnosti a autorizace do služeb. Odbočku k tomu, jak to bude 5G řešit, si necháme napříště (zájemci o samostudium googlují 5G ENSURE a AAA).</p>

<p>Mikrooperátoři by z drobných ISP učinili vážené obchodní partnery, zatímco dneska jsou obtížným hmyzem. Mikrooperátor by se staral o výstavbu, lokální support, investice a mobilní operátor by si bral spravedlivý díl ve výši, na kterou by měl odvahu si shrábnout. Na druhou stranu by tu byla očekávána určitá flexibilita, protože stejně by si mohli počínat i virtuální operátoři, kteří by zajišťovali výběr prostředků a “pouhou” integraci nezávislých sítí. Započítejte další faktory. Především sílící podporu VoWiFi, kdy hlas se přenáší přes nelicenované spektrum a na budoucí rozvoj LTE-U, tedy přístupové technologie LTE v nelicencovaném pásmu. A také malý vliv mobilních operátorů na to, co je a co není integrováno v mobilních telefonech. Už to nejsou devadesátá léta, kdy tam bylo a nebylo, co chtěli. Z toho nám vyjde, že celkově role vazby koncového klienta na mobilního operátora se může zásadně snižovat, čímž stojíme před bojem o digitální identitu. Tou byla doposud SIM karta, telefonní číslo a PIN. Nově to bude co? Login Google/Apple ID? Ten čas je ještě před námi, ale moudří už zbrojí.</p>

<h4>Rychlejší reakce na změny na trhu a v technologiích</h4>
<p>Za třetí by SDN mělo umožnit rychlejší a snadnější upgrade, tedy větší přizpůsobení uživateli. Což je ovšem navázáno na vůli provozovatele sítě, která nemusí být vysoká i s ohledem na to, že náklady vysoké nebudou. Neslibujte si od toho mnoho.</p>

<h4>Nižší cena, vyšší bezpečnost a tlak na čínské copycaty</h4>
<p>Do čtvrtice jde o zajímavé oddělení výroby komodizovaného hardware od intelektuálního vlastnictví a software s vyšší přidanou hodnotou. Ve výrobě hardware v posledních (mnoha) letech vedou čínské firmy, problém bylo zpřístupňovat jim intelektuální práva a ani jejich implementační schopnosti nebývaly vysoké. Nyní se to může hezky oddělit. Číňanům zůstane výroba krabic, vývoj software a patenty pak těm, kdo to budou schopni zvládat. Nezanedbatelný bude i pátý aspekt, bezpečnostní. Odstíněním Číny od samotného software se dá důvěryhodněji kontrolovat, co ten software dělá a nedělá, mohlo by to umenšit obavy, že v čínských síťových prvcích jsou backdoory atd. Přijde vám to nejasné? Podívejte se na projekt OpenCellular od Facebooku - s tím zřejmě ještě bude dost legrace.</p>

<p>Hodilo by se sem teď dát nějaké schéma. Jenže jak SDN, tak NFV nejsou zatím standardizované ani ustálené záležitosti a názory na to, jak se budou implementovat, jak hluboce a jak povinně, se zatím dosti různí. Snad si to umíte představit alespoň z toho popisu. </p>

<p>Tak, to je pro zatím všechno. Přiznám se, že úplně původně jsem na začátku tohohle článku chtěl popsat, jak bude vypadat architektura sítě 5G (oproti třeba 3.99 či 4G), jen mi rychle došlo, že v těch nových zkratkách bude potřeba se zorientovat.</p>

<p>Dneska jsme si prosvištěli SDN, NFV a mikrooperátory (no, to není architektura). Příště se podíváme dále, dá-li Bůh a ITU. </p>
