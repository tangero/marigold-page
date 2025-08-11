---
author: Patrick Zandl
audio: true
categories:
  - AI
  - Netscape
  - Internet
layout: post
post excerpt: Přinese AI svobodu lidem? Nikoliv nutně. Kvůli architektuře, jíž jsou nutně stavěné internetové služby, je internet decentralizovaný technologicky, ale v oblasti služeb ostře centralizuje. A to bude s AI jen horší a horší. Proč tomu tak je, jaké jsou důsledky a jaká jsou východiska z této situace?
summary points:
  - Internet je technologicky decentralizovaný, ale služby jsou stále více centralizované.
  - Zásada stejného původu (SOP) brání snadnému sdílení dat mezi službami a posiluje centralizaci.
  - Přenos dat mezi službami je pro uživatele složitý a nekomfortní.
  - AI bude centralizaci služeb ještě více prohlubovat, protože potřebuje osobní data.
  - Velké firmy těží z datové dominance a uživatelské báze, což ztěžuje konkurenci.
  - Existují snahy o decentralizaci dat (Solid, IPFS, HAT), ale zatím se neprosadily.
  - Alternativou jsou šifrovaná data s vlastními pravidly přístupu (sticky policies) a technologie TEE.
title: Dědictví Netscape tlačí internetové služby k centralizaci
thumbnail: https://www.marigold.cz/assets/netscape.png
---


Přinese AI svobodu lidem? Nikoliv nutně. Kvůli architektuře, jíž jsou nutně stavěné internetové služby, je internet decentralizovaný technologicky, ale v oblasti služeb ostře centralizuje. A to bude s AI jen horší a horší. Proč tomu tak je, jaké jsou důsledky a jaká jsou východiska z této situace?

S každou novou službou jsou velké internetové služby ještě většími a je stále obtížnější opustit je. A každá nová open source služba slibuje, že to změní. Nezmění, nikdy. Centralizace služeb je nativní součástí jinak decentralizovaného internetu. A s AI to bude ještě horší.

Tomuto problému se v počítačové hantýrce říká „zásada stejného původu“ - anglicky _[same-origin policy](https://en.wikipedia.org/wiki/Same-origin_policy)_ [(SOP).](https://en.wikipedia.org/wiki/Same-origin_policy) A vzniklo to, jako řada podobných velmi důležitých věcí, náhodou. V roce 1995 přišli vývojáři tehdejšího prohlížeče Netscape s JavaScriptem, jenže hned po uvedení verze 2.0 vznikly pochybnosti, zda JavaScript nemůže být nebezpečný tím, že by mohl předávat data od uživatele někam do pryč. A protože bylo situaci potřeba rychle vyřešit, vyřešila se přes noc tím nejjednodušším způsobem - zakázalo se předávání dat do „jiného původu“ - tedy na jiné servery. JavaScript tak nemůže vzít vaše data a předat je jinému serveru, než z jakého byl spuštěn.

Je to velmi důležitá zásada. Například, pokud byste se neodhlásili ze svojí bankovní aplikace a přešli na stránku, na níž by byl podvodný script, mohl by tento script použít snadno vaše přihlášení a dělat cokoliv, co by na bankovním webu mohl dělat přihlášený uživatel. Díky SOP je to podvodnému scriptu málo platné, musí použít mnohem sofistikovanější taktiky.

Tento přístup se mimochodem liší od zásad, která jinak na internetu pamatují. Obrázek z cizího serveru můžete do stránky vnořit, taktéž HTML kód. Obojí se ve stránce zobrazí. JavaScript? Ten sice do cizí stránky můžete vnořit, ale nemá přístup k datům té vaší stránky, jen k datům z vlastního serveru.

Až potud je přínos jasný a byl to ostatně důvod, proč inženýři Netscape toto pravidlo zavedli. Jenže SOP je také důvod, proč jsou internetové služby tlačeny k centralizaci. O datech nerozhoduje uživatel, ale provozovatel služby.

Je to jednoduché. Pokud si své fotografie nahrajete do služby společnosti Google, není žádná kloudná cesta, jak je přenést do jiné služby, než je všechny stáhnout a uploadovat znovu. Pokud se zaregistrujete na sociální síť Facebook, nemůžete to samé přihlášení, natož ta samá data použít v jiné sociální síti. Pokud to dotyčný původce nějak implicitně nepovolí, což je to, co dělá Facebook, když (z pro sebe dobrého důvodu) dovolí přihlášení k jiným službám (ano, tím monitoruje váš provoz jinde, což by jinak nemohl).

Říkám tomu gravitace internetových služeb. Je moc hezké, že vymyslíte nový úžasný fotoeditor, jenže uživatelé si do něj musí své fotky stáhnout a uploadovat. Budou to dělat a udělají to dost rychle na to, aby služba nabrala dostatečnou uživatelskou základnu, než Google či Apple stihne okopírovat její službu a zaintegrovat ji do té svojí? Zkušenost ukazuje, že spíše ne.

Služba s největším množstvím dat může poskytovat největší hodnotu, tím přitahuje více uživatelů a ti přinášejí více dat. A do tohoto gravitačního zákona je těžké vstupovat, protože i kdybyste nakrásně vyvinuli dostatečně zajímavou službu, aby obstála nabídkou funkcí vůči těm etablovaným, proč by do ní přecházeli uživatelé se svými daty? A jak by to zvládli?

Nic v tom nehledejme. Není to žádné spiknutí, je to jen gravitační zákon vyplývající z jednoho rutinního rozhodnutí v roce 1995.

#### Jak se SOP projeví v AI?

Mohli bychom dlouze pohovořit o tom, jak SOP pomohl spoluvytvořit dominanci firem jako Google, Apple, Microsoft, Amazon a Facebook. Ale to si nechme na jindy. Jaký problém SOP přináší pro AI?

Vlastně ten stejný. Aby pro vás AI dobře fungovala, potřebuje kontext, tedy vaše osobní data. Jenže k nim nemá přístup, má jen ta, co jste jí dali. Pokud začnete používat ChatGPT nebo Claude přes webové rozhraní (či mobilní aplikaci), obě AI o vás záhy nasbírají hromadu vašich preferencí. A za rok už nebude jednoduché přejít jinam, protože byste musel všechen tento kontext mít jak přenést. Ano, dneska to jde - můžete jít do Personalizace v ChatGPT a Claude a tam textově vidíte kontext, který o vás ví.

Jenže co takový Google nebo Meta? Na společnosti Google je vidět, jak pomalejší rozjezd nemusí nutně vadit, pokud včas naberete rychlost a máte data i uživatelskou bázi. Google o vás ví první i poslední, stačí vám trochu projít emaily, dokumenty nebo fotky a zvláště, když používáte Android (ano, i proto mám služby Proton). A jeho AI vás okouzlí, když mu dáte odkaz na video z Youtube a poprosíte ho, aby vám udělal jeho souhrn. Integrace nad takovou datovou hegemonií je průlomová. Copak budete odcházet někam jinam, když to bude TAK POHODLNÉ?

Něco podobného by mohla mít i Meta - její Facebook a WhatsApp je studnicí dat. Jenže Meta se zatím nepoprala s tím, aby nabídla konkurenceschopnou AI. Teď do této trhliny valí miliardy dolarů, aby je zacelila.

Pokud bude SOP pokračovat, bude AI velmi výrazným důvodem, proč se vláda korporací nad našimi daty bude jen více centralizovat a prohlubovat.

### Jak se zbavit SOP?

To není vůbec lehké. SOP je do technologického světa zakořeněná velmi pevně a z dobrého důvodu. SOP umožňuje pracovat s citlivými údaji, přistupovat k síti a používat nedůvěryhodný software. Tedy, abychom byli přesnější, umožňuje používat dva ze tří těchto přístupů najednou.

Již v roce 1995 bylo několik možností, jak problém vyřešit - jenže všechny vyžadovaly více programování a Netscape potřeboval opravu okamžitě. Microsoft později použil pro ActiveX systém digitálních podpisů. Servery mohly posílat speciální HTTP hlavičky určující, které domény mohou přistupovat k jejich obsahu. Tento přístup by předešel CORS (Cross-Origin Resource Sharing), který přišel až mnohem později. Servery by generovaly jednorázové tokeny pro cross-domain požadavky, které by musely být validovány před každým přístupem. Atd.

Je příznačné, že problém uchopil autor WWW protokolu Tim Berners Lee. V roce 2016 představil [projekt Solid](https://solidproject.org/), který umožňuje uživatelům svá data ukládat do takzvaných Podů a rozhodovat o tom, kdo k nim získá jaký přístup. Jak se asi dalo čekat, za osm let velkého rozšíření nedošly. Po pravdě řečeno, když to tehdy vzniklo, tak jsem vůbec nepochopil, co se tím myslí. Po osmi letech už zhruba tuším, že by to bylo dobré. V Británii to například používají (nebo chtějí) k ukládání zdravotních dat, abyste nebyli závislí na provozovateli systému a mohli jste si je kdykoliv uvolnit do jiného systému. Jo, k tomu to má být! Lee momentálně pracuje na tom, [aby se Solid stal součástí W3C standardu](https://www.euronews.com/next/2024/12/26/world-wide-web-creator-sir-tim-berners-lees-hopes-for-2025-data-rights-and-a-social-media-).

To je jeden přístup, který má řadu podmnožin. Existuje několik projektů z kryptosvěta (Filecoin, IPFS, Storj, Sia), která se snaží vytvořit decentralizované úložiště, ale nejsou vhodná pro strukturovaná data jsou to spíše decentralizované cloudy. Nebo britský projekt HAT (Hub of All Things), to je zase mikroserverová služba, již aplikace žádají o přístup k datům a uživatel vlastní svůj mikroserver podobně, jako v Solidu svůj Pod.

Pak je tu druhý přístup. Data jsou zašifrovaná a „nesou si sebou vlastní pravidla“. Říká se tomu _sticky policies_. Například fotku lze vytisknout, ale nelze ji zobrazit. Nebo obráceně. Rozhoduje majitel dat - a může se rozhodnout svá pravidla změnit a přes server pravidel tuto aktualizaci vynutit. Je to zajímavé, vyžaduje to také celou řadu infrastruktury, ale pomalu to vzniká. Například to vyžaduje TEE, tedy _Trusted Execution Environment_ (Důvěryhodné prostředí pro vykonávání kódu) - česky bychom mohli říct "bezpečná enkláva" nebo "izolované výpočetní prostředí". TEE je bezpečná, izolovaná oblast uvnitř procesoru. Běží specifický kód a zpracovává citlivá data způsobem, který je chráněn před zbytkem systému, včetně operačního systému, hypervisorů a administrátorů cloudu. Díky ní se s vaším souborem nestane nic, co nechcete. Startup projekty v této oblasti

-   Oasis Network - blockchain s TEE pro soukromé smart contracts
-   Secret Network - šifrované smart contracts s TEE
-   Phala Network - confidential computing cloud
    

### Jaké jsou možnosti změny?

Čili možnosti jsou. Až sem je to méně kontroverzní. Jenže, jak by mělo probíhat prosazení takových technologií?

První možnost je „neviditelná revoluce“, tedy způsob, jakým se drobnější technologie prosazují. Technologie se potichu implementuje, hledá si své užití, není kolem ní rozruch a za deset let je fundamentem. Takhle zvítězil SIP (nevíte, co to je, ale všichni to používají při telefonování). Skvěle to funguje pro podkladové technologie, které je těžké marketovat.

Druhou možností je Trh - když to budou lidé chtít, tak se to bude vyrábět, protože z toho budou peníze a tím víc se to bude tlqčit.

Třetí možnost je Změna myšlení. Lidé to budou chtít proto, že to budou vnímat jako užitečné pro sebe.

Čtvrtá možnost je působení regulátorů, tedy regulace. To dnes vnímáme jako čistě EU záležitost, nic není ale tak daleko od pravdy. EU je Privacy lídr. USA tlačí Národní bezpečnost. Čína a její Digitální suverenita. Každý má svou vizi, do které tohle nějak může zapadat.

Nejúspěšnější bude postupná, nenásilná integrace, kde:

-   Uživatelé získají výhody bez nutnosti měnit chování
-   Firmy ušetří peníze a sníží rizika
-   Regulátoři podpoří, ne vynutí změnu
-   Technologie bude "nudně fungující" infrastruktura
    

Takhle nějak se HTTPS stalo standardem. Ne proto, že to regulátoři nařídili, ale proto, že Google začal upřednostňovat HTTPS stránky ve vyhledávání... (takže vlastně monopolní rozhodnutí jedné firmy).

> _Za dalších dvacet let buďto bude způsob, jakým pracujeme s daty, diametrálně odlišný, nebo budeme ještě více závislí na velkých korporacích a jejich online službách..._