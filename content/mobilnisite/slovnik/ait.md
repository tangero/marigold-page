---
slug: "ait"
url: "/mobilnisite/slovnik/ait/"
type: "slovnik"
title: "AIT – Application Information Table"
date: 2025-01-01
abbr: "AIT"
fullName: "Application Information Table"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ait/"
summary: "AIT (Application Information Table, tabulka informací o aplikaci) je standardizovaná datová struktura definovaná organizací 3GPP pro správu a doručování informací souvisejících s aplikacemi přes vysíl"
---

AIT je standardizovaná datová struktura definovaná organizací 3GPP pro správu a doručování informací souvisejících s aplikacemi přes vysílací (broadcast) sítě, která umožňuje přijímačům tyto přidružené aplikace objevovat a spouštět.

## Popis

AIT (Application Information Table, tabulka informací o aplikaci) je základní komponenta v ekosystému služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a její evoluované verze (eMBMS) podle 3GPP, podrobně specifikovaná v dokumentu TS 26.953. Funguje jako signalizační tabulka, analogická k Program Map Table ([PMT](/mobilnisite/slovnik/pmt/)) v tradičních [MPEG-2](/mobilnisite/slovnik/mpeg-2/) transportních proudech, ale speciálně navržená pro signalizaci aplikací v rámci IP-based vysílacích přenosových frameworků, jako je [FLUTE](/mobilnisite/slovnik/flute/)/[ALC](/mobilnisite/slovnik/alc/). AIT je přenášena jako soubor v rámci session File Delivery over Unidirectional Transport (FLUTE), což umožňuje její spolehlivé doručení všem přijímačům ve vysílacím pokrytí.

Z architektonického hlediska se AIT nachází v aplikační vrstvě vysílacího protokolového stacku. Je generována poskytovatelem služby nebo vysílacím aplikačním serverem a je multiplexována do vysílacího transportního proudu společně s audio, video a dalšími datovými karusely. Samotná tabulka je strukturována pomocí [XML](/mobilnisite/slovnik/xml/) nebo binárních formátů dle specifikace a obsahuje seznam deskriptorů aplikací. Každý deskriptor poskytuje komplexní metadata pro jednu aplikaci včetně globálně unikátního identifikátoru aplikace, informací o verzi, priority, ovládání viditelnosti a především transportních parametrů potřebných pro získání samotné aplikace. Tyto parametry specifikují FLUTE session (pomocí Source IP, Destination IP a Transport Session Identifier - [TSI](/mobilnisite/slovnik/tsi/)) a soubor (pomocí Transport Object Identifier - [TOI](/mobilnisite/slovnik/toi/)), kde se nachází spustitelný kód nebo zdroje aplikace.

Když přijímač (User Equipment - UE) naladí vysílací službu, nejprve získá informace o oznámení služby (service announcement), které odkazují na FLUTE session nesoucí AIT. Po přijetí a zpracování AIT může middleware nebo správce aplikací v UE identifikovat všechny aplikace přidružené k aktuální službě. UE poté vyhodnotí deskriptory aplikací na základě svých schopností, uživatelských preferencí a bezpečnostních politik. Pokud je aplikace shledána vhodnou a autorizovanou, UE použije transportní parametry z AIT k připojení k příslušné FLUTE session a stažení souborů aplikace. AIT také řídí životní cyklus aplikace, specifikuje, zda má být aplikace spuštěna automaticky, předstižena pro pozdější použití, nebo pouze uvedena jako dostupná. Tento mechanismus umožňuje bezproblémový, deklarativní model pro doručování aplikací, který odděluje proces objevování služeb od logiky získání a spuštění aplikace.

Role AIT je klíčová pro umožnění přidaných služeb nad rámec čistého audio/video vysílání. Mění pasivní vysílací kanál na interaktivní aplikační platformu. Například v mobilní televizní službě založené na eMBMS může AIT signalizovat přidruženou hlasovací aplikaci, doprovodný informační portál nebo cílový reklamní engine. V implementacích systému veřejného varování (Public Warning System - PWS) může AIT signalizovat doručení multimediální aplikace pro nouzové výstrahy obsahující mapy, evakuační trasy nebo pokyny v několika jazycích. Standardizovaný formát zajišťuje interoperabilitu mezi vysílacím síťovým vybavením různých výrobců a přijímači různých značek, což je nezbytné pro široké nasazení interaktivních vysílacích služeb.

## K čemu slouží

AIT byla vytvořena, aby vyřešila základní problém, jak dynamicky a standardizovaně, efektivně a na přijímači nezávislým způsobem přidružovat a doručovat spustitelné aplikace k lineárnímu vysílanému obsahu. Před její standardizací se používaly proprietární metody nebo omezené signalizační mechanismy (jako jednoduché triggery), což vedlo k fragmentaci, zvýšené složitosti přijímačů a bránilo rozvoji bohatého ekosystému pro vysílací aplikace. AIT poskytuje sjednocený, deklarativní framework, který přijímači přesně říká, jaké aplikace jsou dostupné, jak je získat a co s nimi dělat.

Historicky tlak na vznik AIT vzrostl s vývojem MBMS od 3GPP směrem k bohatším multimediálním zkušenostem a integrací vysílání s IP sítěmi (což vedlo k eMBMS). Jak se vysílací služby vyvíjely za hranice jednoduchých audio a video streamů směrem k interaktivním prvkům, doprovodnému obsahu a personalizovaným komponentám, vznikla jasná potřeba robustního signalizačního protokolu. AIT řeší nedostatky předchozích ad-hoc přístupů tím, že nabízí strukturované, pro síť efektivní řešení. Umožňuje síti signalizovat informace o aplikacích jednou masivnímu publiku, využívaje vysílací povahu přenosu, namísto toho, aby každé zařízení muselo individuálně dotazovat aplikační server (což by přetížilo buněčné unicastové sítě).

Navíc AIT umožňuje správu životního cyklu služby a aplikací ze strany sítě. Poskytovatelé služeb mohou aplikace přidružené k živé vysílací službě aktualizovat, přidávat nebo odebírat pouhou aktualizací souboru AIT ve vysílacím karuselu. To dává vysílatelům dynamickou kontrolu nad uživatelskou zkušeností. Vznik AIT byl také motivován potřebou zabezpečení a důvěry; tabulka může obsahovat informace o původu aplikace a podpisy, což umožňuje přijímači ověřit autenticitu před spuštěním. AIT v konečném důsledku existuje proto, aby odemkla komerční a funkční potenciál vysílacích sítí tím, že z nich učiní platformu pro nasazovatelný, interaktivní software, čímž překlenuje propast mezi tradičním lineárním vysíláním a světem moderních digitálních služeb, který je založen na službách na vyžádání a aplikacích.

## Klíčové vlastnosti

- Standardizovaný XML/binární formát pro signalizaci aplikací definovaný v 3GPP TS 26.953
- Deklarativní model deskriptoru aplikace zahrnující ID, verzi, prioritu a ovládání viditelnosti
- Integrovaná transportní signalizace využívající parametry FLUTE/ALC session (Source IP, Dest IP, TSI, TOI)
- Podporuje správu životního cyklu aplikace (automatické spuštění, předstižení, příkazy k ukončení)
- Umožňuje síťově řízené přidružení aplikací k lineárním vysílacím službám
- Usnadňuje zabezpečené doručení aplikací začleněním informací o podpisu a původu

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)

## Definující specifikace

- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download

---

📖 **Anglický originál a plná specifikace:** [AIT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ait/)
