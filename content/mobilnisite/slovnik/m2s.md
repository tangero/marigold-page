---
slug: "m2s"
url: "/mobilnisite/slovnik/m2s/"
type: "slovnik"
title: "M2S – Motion to Sound"
date: 2025-01-01
abbr: "M2S"
fullName: "Motion to Sound"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/m2s/"
summary: "M2S je služba 3GPP umožňující převod dat z pohybových senzorů na zvukové signály pro aplikace zvyšující přístupnost. Umožňuje uživatelům, zejména se zrakovým postižením, vnímat pohyb nebo gesta prostř"
---

M2S je služba 3GPP, která převádí data z pohybových senzorů na zvukové signály za účelem zvýšení přístupnosti pro uživatele, zejména pro osoby se zrakovým postižením.

## Popis

Motion to Sound (M2S) je standardizovaná funkce služby v rámci 3GPP, primárně v kontextu přístupnosti a obohacení médií. Definuje mechanismy pro překlad pohybových dat – zachycených ze senzorů zařízení, jako jsou akcelerometry, gyroskopy nebo kamery – na odpovídající zvukové reprezentace nebo zvukové signály. Architektonický model zahrnuje zdrojovou komponentu generující pohybová data (např. gesto ruky uživatele zachycené smartphonem), zpracovatelskou funkci, která tato data interpretuje na základě předdefinovaných mapovacích pravidel, a engine pro vykreslování zvuku, který vytváří výstupní zvuk. Tato služba je často implementována v rámci aplikačních frameworků nebo middleware, který zpracovává senzorová data a přehrávání zvuku.

Fungování M2S zahrnuje několik technických kroků. Nejprve jsou získávána nezpracovaná pohybová data ze senzorů při určité vzorkovací frekvenci. Tato data jsou následně zpracována, což může zahrnovat filtrování, extrakci příznaků (např. detekci vzorů gest, rychlosti nebo směru) a normalizaci. Zpracované pohybové parametry jsou namapovány na zvukové parametry podle konfigurovatelného profilu. Například rychlost mávnutí rukou může ovládat výšku tónu, zatímco trajektorie pohybu může panoramovat zvuk mezi stereo kanály. Syntéza zvuku může sahat od jednoduchých pípnutí a tónů po složitější auditorní ikony nebo earcony. Výstup je doručován prostřednictvím zvukového subsystému zařízení do sluchátek nebo reproduktorů, čímž poskytuje auditorní zpětnou vazbu v reálném čase nebo téměř v reálném čase.

Klíčové komponenty v systému M2S zahrnují Správce senzorů pro sběr dat, Engine pro mapování pohybu na zvuk, který aplikuje transformační pravidla, a Vykreslovač zvuku. Služba může také zahrnovat funkci správy profilů, která umožňuje přizpůsobení pro různé uživatelské potřeby nebo aplikační scénáře. Její role v síti je primárně na aplikační vrstvě, kde zlepšuje uživatelský zážitek a přístupnost pro služby jako hraní her, virtuální/rozšířená realita, navigační pomůcky nebo asistenční technologie. Ačkoli se nejedná o protokol jádra sítě, její standardizace zajišťuje interoperabilitu napříč zařízeními a platformami, což umožňuje konzistentní funkce přístupnosti v ekosystémech podporujících 3GPP.

## K čemu slouží

M2S byla vytvořena za účelem řešení výzev v oblasti přístupnosti, zejména pro uživatele se zrakovým postižením, tím, že poskytuje alternativní senzorický kanál pro vnímání informací založených na pohybu. V moderních mobilních a IoT zařízeních jsou pohybové senzory všudypřítomné a umožňují bohaté interakce prostřednictvím gest, tyto interakce jsou však převážně vizuální. To vytváří bariéru pro uživatele se zrakovým postižením, kteří nemohou těžit z rozhraní ovládaných gesty nebo pohybové zpětné vazby v aplikacích, jako jsou hry, fitness trackery nebo [AR](/mobilnisite/slovnik/ar/)/VR. Omezení předchozích přístupů spočívalo v nedostatku standardizovaných metod pro převod pohybu na nevizuální zpětnou vazbu, což vedlo k fragmentovaným, na aplikaci specifickým řešením, která nebyla interoperabilní.

Tato technologie řeší problém zpřístupnění aplikací zaměřených na pohyb tím, že poskytuje standardizovaný framework pro generování auditorních podnětů z pohybových dat. To umožňuje vývojářům implementovat konzistentní, multiplatformní funkce přístupnosti bez nutnosti znovuvynalézat kolo pro každou aplikaci. Umožňuje uživatelům interagovat s aplikacemi citlivými na pohyb prostřednictvím zvuku, čímž zvyšuje jejich nezávislost a uživatelský zážitek. Historický kontext zahrnuje rostoucí regulatorní a společenský důraz na digitální přístupnost, který vede normalizační orgány jako 3GPP k začleňování funkcí podporujících inkluzivní design.

Její motivace vychází z širšího trendu obohacování multimediálních služeb a zajišťování rovného přístupu k technologiím. Standardizací M2S umožňuje 3GPP poskytovatelům služeb a výrobcům zařízení efektivně nasazovat funkce přístupnosti, což podporuje inovace v oblasti asistenčních technologií a inkluzivních uživatelských rozhraní v rámci mobilního ekosystému.

## Klíčové vlastnosti

- Převádí data z pohybových senzorů (např. akcelerometr, gyroskop) na zvukové signály
- Podporuje konfigurovatelné mapovací profily pro přizpůsobitelnou zvukovou zpětnou vazbu
- Umožňuje auditorní reprezentaci gest a pohybů v reálném čase
- Zvyšuje přístupnost pro uživatele se zrakovým postižením
- Umožňuje využití v aplikacích jako hraní her, navigace a AR/VR
- Poskytuje standardizovanou interoperabilitu napříč zařízeními a platformami

## Definující specifikace

- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP

---

📖 **Anglický originál a plná specifikace:** [M2S na 3GPP Explorer](https://3gpp-explorer.com/glossary/m2s/)
