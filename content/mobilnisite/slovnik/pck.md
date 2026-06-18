---
slug: "pck"
url: "/mobilnisite/slovnik/pck/"
type: "slovnik"
title: "PCK – Personalisation Control Key"
date: 2026-01-01
abbr: "PCK"
fullName: "Personalisation Control Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pck/"
summary: "Tajný klíč používaný v UICC/USIM k řízení personalizace ME (mobilního zařízení) v sítích 3GPP. Umožňuje síťovým operátorům nebo výrobcům uzamknout zařízení na konkrétní síť, značku nebo poskytovatele"
---

PCK je tajný klíč používaný v UICC nebo USIM k uzamčení mobilního zařízení na konkrétní síť, značku nebo poskytovatele služeb, čímž vynucuje komerční dohody.

## Popis

Personalisation Control Key (PCK) je bezpečnostní funkce definovaná v rámci aplikačního toolkitu UICC (Universal Integrated Circuit Card) a [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module) standardu 3GPP. Jedná se o tajný kryptografický klíč, typicky o délce 128 bitů, který je bezpečně uložen v chráněném souboru ([EF](/mobilnisite/slovnik/ef/)_PCK) na UICC. Primární funkcí PCK je umožnit síťovou, provozovatelskou nebo korporátní personalizaci mobilního zařízení ([ME](/mobilnisite/slovnik/me/)). Personalizace označuje schopnost omezit provoz ME tak, aby fungovalo pouze s konkrétní UICC, sítí nebo sadou služeb. Mechanismus je vyvolán příkazem "PERSONALISE" z UICC do ME, který zahrnuje výzva-odpověď autentizační protokol využívající PCK.

Technický proces funguje následovně: Když je personalizované ME zapnuto s UICC, ME načte personalizační data z UICC. Pokud je personalizace aktivní, ME odešle náhodnou výzvu ([RAND](/mobilnisite/slovnik/rand/)) do UICC. UICC použije uložený PCK a kryptografický algoritmus (jako je MILENAGE) k výpočtu odpovědi ([RES](/mobilnisite/slovnik/res/)) a očekávané odpovědi ([XRES](/mobilnisite/slovnik/xres/)). RES je odeslána zpět do ME. ME, které také disponuje PCK (naprogramovaným do jeho nevolatilní paměti během procesu personalizace), nezávisle vypočítá XRES pomocí stejného RAND a algoritmu. Pokud se RES shoduje s XRES, kontrola personalizace projde a ME funguje normálně. Pokud kontrola selže, ME může odepřít službu, omezit funkčnost nebo zobrazit zprávu v závislosti na kategorii personalizace (např. síť, poskytovatel služeb, korporátní).

Architektura zahrnuje několik komponent: personalizační rámec ME, USIM aplikaci na UICC se souborem PCK a platformu pro správu na dálku ([OTA](/mobilnisite/slovnik/ota/)) používanou k provizionování nebo aktualizaci PCK na UICC. PCK je odlišný od autentizačních klíčů (Ki/K) používaných pro přístup k síti; slouží výhradně k uzamčení zařízení. Jeho role je klíčová pro vynucování komerčních politik. Například dotovaný telefon prodaný Operátorem A je personalizován PCK Operátora A, což zabraňuje jeho použití se [SIM](/mobilnisite/slovnik/sim/) kartou konkurenta, dokud není odemčen. Specifikace podrobně popisují více kategorií personalizace (Network, Network Subset, Service Provider, Corporate), z nichž každá může mít svůj vlastní PCK, což umožňuje podrobnou kontrolu. Příkazy pro správu umožňují deaktivovat personalizaci (odemčení), pokud je poskytnut správný PCK.

## K čemu slouží

PCK byl zaveden, aby řešil komerční potřebu síťových operátorů a výrobců mobilních zařízení kontrolovat prostředí používání mobilních zařízení, zejména na trzích, kde jsou zařízení výrazně dotována. Bez takového mechanismu by mohlo být dotované zařízení okamžitě použito se SIM kartou konkurenta, což by podkopalo obchodní model návratnosti dotovaných nákladů prostřednictvím výnosů ze služeb. Před standardizovanou personalizací existovala proprietární řešení uzamčení, což vedlo k fragmentaci a problémům s interoperabilitou. PCK, standardizovaný od Release 4, poskytl univerzální, bezpečnou metodu pro personalizaci napříč všemi zařízeními a UICC kompatibilními se standardem 3GPP. Řeší problém uzamčení zařízení kryptograficky bezpečným způsobem, který brání snadnému obejití. Jeho vytvoření bylo motivováno snahou chránit investice operátorů, spravovat flotily zařízení pro korporátní zákazníky a umožnit nabídky značkových služeb, při zachování standardizovaného bezpečnostního rámce, který je interoperabilní mezi různými výrobci ME a UICC.

## Klíčové vlastnosti

- Tajný kryptografický klíč (např. 128bitový) uložený v souboru EF_PCK na UICC/USIM.
- Používá se ve výzva-odpověď protokolu k ověření ME vůči UICC pro kontroly personalizace.
- Podporuje více kategorií personalizace: Network, Network Subset, Service Provider a Corporate.
- Umožňuje omezit provoz ME na základě přihlašovacích údajů vložené UICC.
- Lze jej bezpečně provizionovat a spravovat prostřednictvím OTA platforem.
- Odlišný od síťových autentizačních klíčů (Ki/K), je určen výhradně pro řízení uzamčení zařízení/služeb.

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [OTA – Over The Air](/mobilnisite/slovnik/ota/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G
- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.581** (Rel-19) — MCVideo Media Plane Control Protocol Specification
- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols
- **TS 29.380** (Rel-19) — MCPTT-LMR Interworking Media Plane Control
- **TS 29.582** (Rel-19) — MCData Interworking with LMR Systems
- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.879** (Rel-13) — MCPTT Security Study
- **TS 33.880** (Rel-15) — Security Study for Enhanced Mission Critical Services
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G

---

📖 **Anglický originál a plná specifikace:** [PCK na 3GPP Explorer](https://3gpp-explorer.com/glossary/pck/)
