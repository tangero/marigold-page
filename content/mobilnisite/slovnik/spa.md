---
slug: "spa"
url: "/mobilnisite/slovnik/spa/"
type: "slovnik"
title: "SPA – Simple Power Analysis"
date: 2025-01-01
abbr: "SPA"
fullName: "Simple Power Analysis"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/spa/"
summary: "Technika útoku vedlejším kanálem, která extrahuje tajné informace (např. kryptografické klíče) z zařízení analýzou vzorců jeho spotřeby energie během výpočtu. V 3GPP je považována za model hrozby pro"
---

SPA je útok vedlejším kanálem, který extrahuje tajné informace z zařízení (např. z UICC) analýzou jeho vzorců spotřeby energie během výpočtu.

## Popis

Simple Power Analysis (SPA) je kryptografická metoda útoku relevantní pro zabezpečení 3GPP, na kterou odkazují specifikace jako 35.205 (MILENAGE), 35.234 ([GEA](/mobilnisite/slovnik/gea/)) a 29.198 (Open Service Access). Spadá do širší kategorie útoků vedlejším kanálem (SCA), které zneužívají fyzikální charakteristiky implementace kryptografického systému spíše než matematické slabosti samotného algoritmu. SPA zahrnuje přímé pozorování časového průběhu spotřeby energie zařízení během provádění kryptografické operace, jako je modulární umocňování v [RSA](/mobilnisite/slovnik/rsa/) nebo sekvence operací v [AES](/mobilnisite/slovnik/aes/). Odchylky v odběru energie silně korelují s prováděnou sekvencí instrukcí a zpracovávanými daty.

V kontextu sítě 3GPP jsou primárními cíli SPA vestavěné bezpečnostní prvky, jako je univerzální integrovaný obvodová karta (UICC) hostující aplikaci [USIM](/mobilnisite/slovnik/usim/), autentizační servery ([AUC](/mobilnisite/slovnik/auc/)) nebo hardwarové bezpečnostní moduly provádějící klíčové kryptografické funkce. Například během procedury [AKA](/mobilnisite/slovnik/aka/) (Authentication and Key Agreement) používá USIM dlouhodobý tajný klíč (K) a algoritmus MILENAGE k výpočtu odpovědi ([RES](/mobilnisite/slovnik/res/)) a šifrovacích/integritních klíčů ([CK](/mobilnisite/slovnik/ck/)/IK). Pokud implementace MILENAGE nebo základní AES primitivu není odolná vůči SPA, může útočník s fyzickým přístupem ke kartě měřit její spotřebu energie během těchto výpočtů. Analýzou průběhu, zejména hledáním vzorců, které se liší při zpracování bitu '0' versus bitu '1' tajného klíče nebo mezihodnoty, může útočník statisticky odvodit tajný klíč.

Technický proces zahrnuje sběr velkého množství průběhů spotřeby energie (možná tisíců) pro známé nebo zvolené vstupní výzvy (hodnoty RAND v AKA). Na tyto průběhy jsou následně aplikovány sofistikované metody zpracování signálu a statistické analýzy k identifikaci datově závislých variací v odběru energie. SPA je považována za 'jednoduchou', protože často vyžaduje pouze jeden nebo několik průběhů, pokud implementace jasně prozrazuje informace prostřednictvím svého energetického profilu, například podmíněnými větvemi (např. příkazy if-else), jejichž prováděná cesta závisí na tajných datech. Specifikace zabezpečení 3GPP tuto hrozbu uznávají a nařizují nebo doporučují použití implementací odolných vůči útokům vedlejším kanálem pro kryptografické algoritmy používané v citlivých síťových prvcích, což ovlivňuje návrh a testování bezpečnostních funkcí.

## K čemu slouží

Simple Power Analysis, jakožto zdokumentovaná hrozba ve standardech 3GPP, existuje k vyzdvihnutí a zmírnění kritické zranitelnosti ve fyzické implementaci bezpečnostních protokolů. Primární problém, který řeší, je mezera mezi teoretickou kryptografickou silou a praktickým, reálným zabezpečením. Šifra jako AES-128 je matematicky bezpečná proti útokům hrubou silou, ale naivní softwarová nebo hardwarová implementace může prozradit klíč prostřednictvím spotřeby energie během sekund, což činí matematické zabezpečení irelevantním. Motivace pro zahrnutí ohledů na SPA v 3GPP vychází z potřeby chránit dlouhodobou identitu účastníka (IMSI) a kořenový tajný klíč (K) uložený na UICC, který je základem autentizace a důvěrnosti v mobilní síti.

Historicky, jak se mobilní zařízení stávala výkonnějšími a všudypřítomnými, stala se také cíli s vysokou hodnotou pro útočníky. Přechod na programovatelné UICC a složitější aplikace USIM zvýšil plochu pro útok. 3GPP ve spolupráci s ETSI SCP a dalšími orgány začalo formalizovat odolnost vůči útokům vedlejším kanálem jako požadavek pro bezpečnostně kritické komponenty, zejména od vydání 8 s vylepšeným bezpečnostním rámcem pro LTE. Specifikace SPA jako modelu hrozby vede návrháře algoritmů (např. MILENAGE) a implementátory (výrobce čipů) k používání protiopatření. Mezi ně patří algoritmy s konstantním časem provádění (eliminující datově závislé větvení), logické styly vyvažující spotřebu energie a maskovací techniky náhodňující mezidata. Tímto 3GPP zajišťuje, že zabezpečení celého mobilního ekosystému je robustní nejen teoreticky, ale také proti praktickým fyzickým útokům, které může provést odhodlaný protivník s fyzickým přístupem k zařízení nebo síťové kartě.

## Klíčové vlastnosti

- Zneužívá datově závislé odchylky v okamžité spotřebě energie zařízení
- Cílí na kryptografické implementace v UICC/USIM a síťových funkcích
- Potenciálně může extrahovat tajné klíče pomocí jednoho nebo několika měřených průběhů
- Je zohledněna v modelech hrozeb pro 3GPP autentizační algoritmy (např. MILENAGE)
- Podmiňuje požadavky na provádění s konstantním časem a další hardwarová/softwarová protiopatření
- Základní typ útoku v rámci širší disciplíny analýzy vedlejším kanálem (SCA)

## Související pojmy

- [DPA – Differential Power Analysis](/mobilnisite/slovnik/dpa/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming
- **TS 29.198** (Rel-9) — OSA API Overview Specification
- **TS 35.205** (Rel-19) — MILENAGE Algorithm Set: General Overview
- **TS 35.234** (Rel-19) — MILENAGE-256 Algorithm Set Specification
- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report
- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen
- **TR 35.937** (Rel-19) — MILENAGE-256 Algorithm Set Specification

---

📖 **Anglický originál a plná specifikace:** [SPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/spa/)
