---
slug: "cntr"
url: "/mobilnisite/slovnik/cntr/"
type: "slovnik"
title: "CNTR – Counter"
date: 2024-01-01
abbr: "CNTR"
fullName: "Counter"
category: "Management"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/cntr/"
summary: "CNTR je řídicí parametr definovaný v 3GPP TS 31.213 pro aplikace na UICC, který představuje hodnotu čítače. Používá se ke sledování a omezení počtu, kolikrát může nastat konkrétní operace nebo událost"
---

CNTR je řídicí parametr pro aplikace na UICC, který představuje hodnotu čítače používaného ke sledování a omezení počtu, kolikrát může nastat konkrétní operace nebo událost, čímž zajišťuje bezpečnost a provozní integritu.

## Popis

CNTR (Counter, čítač) je základní datový objekt definovaný v technické specifikaci 3GPP TS 31.213, která specifikuje aplikační programové rozhraní ([API](/mobilnisite/slovnik/api/)) pro Java Card™ na UICC. Jedná se o trvalou celočíselnou proměnnou uloženou v nevolatilní paměti UICC (neboli [SIM](/mobilnisite/slovnik/sim/)/[USIM](/mobilnisite/slovnik/usim/) karty). Hlavní architektonickou rolí CNTR je fungovat jako stavový monotónní čítač, který mohou autorizované aplikace (typicky pod kontrolou bezpečnostní domény) zvýšit, snížit nebo resetovat. Operuje v rámci prostředí Java Card Runtime Environment ([JCRE](/mobilnisite/slovnik/jcre/)), kde je k němu přistupováno pomocí standardizovaných metod třídy `javacard.framework.Util` nebo podobných aplikací specifických rozhraní definovaných vydavatelem karty.

Fungování CNTR je neodmyslitelně spojeno s bezpečností a správou životního cyklu aplikací na UICC. Když aplikace potřebuje vynutit limit – například počet neúspěšných pokusů o ověření osobního identifikačního čísla ([PIN](/mobilnisite/slovnik/pin/)) před jeho zablokováním – přečte aktuální hodnotu určeného CNTR. Po každém neúspěšném pokusu aplikační logika instruuje JCRE, aby čítač zvýšil. Aplikace poté porovná aktualizovanou hodnotu CNTR s předdefinovaným prahem uloženým v souborovém systému karty (např. v souboru [EF](/mobilnisite/slovnik/ef/)_UST). Pokud je práh dosažen, aplikace spustí bezpečnostní akci, jako je uzamčení PINu nebo deaktivace služby. Hodnota čítače je zachována i po vypnutí a zapnutí karty díky uložení v nevolatilní paměti, což zajišťuje trvalé sledování stavu.

Klíčové komponenty zapojené do správy CNTR zahrnují souborový systém UICC (pro ukládání hodnoty čítače a jeho přidruženého prahu), apletu Java Card implementující obchodní logiku a bezpečnostní rámec řídící přístupová oprávnění. Čítače jsou často spojeny s konkrétními elementárními soubory (EF) definovanými ve struktuře karty. Například čítač pokusů o zadání PINu je přímo spravován operačním systémem karty ve spolupráci s referenčními daty PINu. Role CNTR v síti je nepřímá, ale kritická; jde o základní prvek pro zabezpečení autentizace účastníka, řízení poskytování služeb a prevenci podvodů na samotné hraně sítě – na zabezpečeném hardwarovém tokenu uživatele. Jeho spolehlivá činnost je základem důvěry v mechanismy, jako je blokování PINu, které chrání před neoprávněným použitím SIM karty.

## K čemu slouží

Koncept CNTR existuje proto, aby poskytl standardizovaný a spolehlivý mechanismus pro stavové počítání událostí v omezeném a zabezpečeném prostředí UICC. Před zavedením standardizovaných [API](/mobilnisite/slovnik/api/) museli vývojáři aplikací implementovat vlastní mechanismy čítačů, což vedlo k fragmentaci, potenciálním bezpečnostním slabinám a zvýšené složitosti testování pro síťové operátory a výrobce karet. Formální definice CNTR v TS 31.213 řeší problém, jak trvale sledovat výskyty událostí (jako jsou bezpečnostní selhání nebo milníky ve využití) způsobem, který je interoperabilní napříč různými výrobci karet a implementacemi platformy Java Card.

Historicky, jak se UICC vyvíjely z jednoduchých autentizačních modulů na platformy pro více aplikací (jako platby, identita nebo doprava), rostla potřeba robustní správy stavu aplikací. Čítač je základním, ale nezbytným stavebním kamenem pro implementaci bezpečnostních politik (např. omezení opakovaných pokusů) a obchodní logiky (např. sledování věrnostních bodů nebo počtu datových relací). Jeho vytvoření bylo motivováno požadavkem na překročení pevně zakódovaných, na operační systém specifických řešení směrem k přenositelnému přístupu standardizovanému pro Java Card. To umožňuje síťovým operátorům vyvíjet a nasazovat zabezpečené aplety s předvídatelným chováním s vědomím, že integrita a trvalost čítače jsou spravovány podkladovou, certifikovanou platformou Java Card.

Mezi omezení, která řeší, patří absence garantovaného API pro trvalé ukládání stavu aplikace v raných systémech čipových karet a riziko manipulace s čítačem, pokud není řádně zabezpečen. Definováním operací s CNTR v zabezpečeném kontextu apletu Java Card a bezpečnostních domén karty zajistilo 3GPP, že tyto kritické hodnoty jsou odolné vůči neoprávněným zásahům a mohou je měnit pouze autorizované entity, čímž se zvyšuje celková bezpečnostní úroveň modulu identity účastníka v mobilní síti.

## Klíčové vlastnosti

- Trvalé celočíselné úložiště v nevolatilní paměti UICC
- Standardizovaný přístup prostřednictvím 3GPP TS 31.213 a Java Card API
- Používá se k vynucování bezpečnostních limitů (např. pokusů o zadání PINu)
- Monotónní funkce (typicky pouze zvyšování hodnoty pro bezpečnostní události)
- Spravován v kontextu zabezpečené aplikace nebo bezpečnostní domény
- Zásadní pro správu stavu a životního cyklu aplikace

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [PIN – Personal Identification Number](/mobilnisite/slovnik/pin/)

## Definující specifikace

- **TS 31.213** (Rel-18) — Test specification for (U)SIM

---

📖 **Anglický originál a plná specifikace:** [CNTR na 3GPP Explorer](https://3gpp-explorer.com/glossary/cntr/)
