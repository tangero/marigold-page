---
slug: "rp"
url: "/mobilnisite/slovnik/rp/"
type: "slovnik"
title: "RP – Reference Point"
date: 2025-01-01
abbr: "RP"
fullName: "Reference Point"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rp/"
summary: "Referenční bod (RP) je konceptuální bod v síťové architektuře představující standardizované rozhraní mezi dvěma odlišnými funkčními entitami. Definuje protokoly, procedury a vyměňované informace, čímž"
---

RP je konceptuální bod v architektuře sítě 3GPP představující standardizované rozhraní mezi dvěma funkčními entitami za účelem zajištění interoperability.

## Popis

V systémové architektuře 3GPP je Referenční bod (RP) základním architektonickým konceptem definujícím logický spojovací bod mezi dvěma odlišnými funkčními entitami nebo skupinami entit. Jedná se o specifikační bod, který abstrahuje komunikační rozhraní a podrobně popisuje protokoly, procedury, primitiva a toky informací, které musí být podporovány pro interoperabilitu. Na rozdíl od fyzického rozhraní je RP konceptuální specifikace; jeho fyzická realizace může být implementována přes různé přenosové sítě (např. IP, [ATM](/mobilnisite/slovnik/atm/), [TDM](/mobilnisite/slovnik/tdm/)) a v reálném nasazení se může mapovat na jedno nebo více fyzických rozhraní.

RP je v architektonických diagramech typicky znázorněn jako čára spojující dva bloky (funkční entity) a označen názvem (např. Rx, Gx, [N2](/mobilnisite/slovnik/n2/)). Specifikace RP je obsažena v technických specifikacích 3GPP (TS) a často zahrnuje více vrstev protokolů. Například referenční bod Rx mezi Application Function ([AF](/mobilnisite/slovnik/af/)) a Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) používá protokol Diameter. Definice zahrnuje servisní primitiva (požadavky, odpovědi, příkazy), přesné informační elementy ([AVP](/mobilnisite/slovnik/avp/) v Diameter), které mají být vyměněny, sekvenci zpráv a očekávané chování každé entity.

Jak to funguje: Když funkční entita (např. [P-CSCF](/mobilnisite/slovnik/p-cscf/)) potřebuje komunikovat s jinou entitou (např. PCRF), činí tak podle procedur definovaných pro konkrétní RP (v tomto případě rozhraní Rx). Entita vytvoří protokolové zprávy podle specifikace RP, vyplní povinné informační elementy a odešle je přes podkladovou přenosovou síť. Přijímající entita interpretuje zprávy na základě stejné definice RP, vykoná příslušnou logiku a může odeslat odpověď. Tím je zajištěno, že i když jsou obě entity dodány různými výrobci, mohou úspěšně interagovat, protože se obě řídí stejnou specifikací RP. RP jsou stavebními kameny, které umožňují dekompozici sítě 3GPP na standardizované, interoperabilní funkční komponenty, což umožňuje flexibilní síťový design, vývoj a nasazení od více dodavatelů.

## K čemu slouží

Koncept Referenčního bodu existuje k vyřešení kritického problému interoperability v komplexních telekomunikačních sítích s více dodavateli. V počátcích celulárních systémů vedly proprietární rozhraní mezi síťovými elementy k závislosti na jediném dodavateli, potlačovaly inovace a zvyšovaly náklady operátorů. Standardizační orgán 3GPP přijal funkční, dekomponovanou architekturu, kde je síť popsána jako soubor interagujících funkčních entit.

RP je nástroj, který formálně definuje *jak* tyto entity interagují. Jeho účelem je poskytnout úplnou, jednoznačnou specifikaci pro komunikaci mezi libovolnými dvěma standardizovanými funkcemi. To umožňuje síťovým operátorům vybírat nejlepší komponenty od různých dodavatelů s jistotou, že budou spolupracovat. Umožňuje také nezávislý vývoj síťových funkcí; pokud zachovávají shodu se specifikací RP, lze zavádět nové funkce. Historicky byl tento přístup, založený na dobře definovaných RP, klíčový pro úspěch a globální přijetí technologií 3GPP (GSM, UMTS, LTE, 5G), podporoval konkurenční ekosystém a urychloval technologický pokrok. RP řeší omezení monolitických proprietárních systémů tím, že umožňují modulární, flexibilní a budoucím vývojem ovlivnitelné síťové architektury.

## Klíčové vlastnosti

- Konceptuální bod definující interoperabilitu mezi funkčními entitami
- Specifikuje protokoly, sekvence zpráv a informační elementy (např. AVP v Diameter)
- Umožňuje nasazení od více dodavatelů a zabraňuje závislosti na jediném dodavateli
- Abstrahuje logickou komunikaci od podkladového fyzického přenosu
- Základní stavební kámen dekomponované síťové architektury 3GPP
- Zdokumentováno v technických specifikacích 3GPP (řada TS)

## Související pojmy

- [SAE – System Architecture Evolution](/mobilnisite/slovnik/sae/)

## Definující specifikace

- **TS 22.895** (Rel-12) — 3GPP SSO Framework Integration Study
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 29.338** (Rel-19) — Diameter protocols for SMS in MME/5GS
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 33.804** (Rel-12) — Non-UICC SSO using SIP Digest credentials
- **TR 33.924** (Rel-19) — GBA-OpenID Interworking Specification
- **TR 33.995** (Rel-19) — Study on SSO Security Integration with 3GPP Networks
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [RP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rp/)
