---
slug: "r-uim"
url: "/mobilnisite/slovnik/r-uim/"
type: "slovnik"
title: "R-UIM – Removable User Identity Module"
date: 2025-01-01
abbr: "R-UIM"
fullName: "Removable User Identity Module"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/r-uim/"
summary: "Čipová karta definovaná standardizačním orgánem 3GPP2 pro sítě CDMA2000, funkčně podobná kartě SIM v GSM/UMTS. Bezpečně ukládá identitu účastníka (IMSI), autentizační klíče a aplikace, což umožňuje mo"
---

R-UIM je výměnná čipová karta pro sítě CDMA2000, která bezpečně ukládá identifikační a autentizační data účastníka a funkčně odpovídá kartě SIM v GSM, což umožňuje mobilitu uživatele mezi zařízeními.

## Popis

Removable User Identity Module (R-UIM) je fyzická čipová karta standardizovaná organizací 3GPP2 určená pro použití v sítích CDMA2000 a příbuzných mobilních sítích. Jejím hlavním účelem je bezpečné uložení dat specifických pro účastníka, tedy oddělení identity uživatele a jeho služebního profilu od mobilního telefonu. Fyzicky i elektricky je kompatibilní s formátem karty [SIM](/mobilnisite/slovnik/sim/), což umožňuje její vložení do slotu v mobilním zařízení. R-UIM obsahuje mikroprocesor a paměť, ve které uchovává klíčové informace, jako je International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), Authentication Key (A-Key), preferred roaming list ([PRL](/mobilnisite/slovnik/prl/)), a může také hostovat aplikace (například SIM toolkit pro [CDMA](/mobilnisite/slovnik/cdma/)).

Z architektonického hlediska R-UIM komunikuje s mobilním zařízením ([ME](/mobilnisite/slovnik/me/)) prostřednictvím standardizovaného rozhraní. Když se zařízení s R-UIM zapne, ME z karty přečte IMSI a další potřebná data. Pro přístup k síti a autentizaci v CDMA síti zařízení použije A-Key uložený na R-UIM spolu s algoritmem CAVE k vygenerování autentizačních podpisů. R-UIM také umožňuje funkce jako personalizace, kdy mohou být kontakty a zprávy uživatele uloženy na kartě, což usnadňuje jejich přenos mezi zařízeními. Ve vícemódových zařízeních podporujících jak technologie 3GPP (GSM/UMTS/LTE), tak 3GPP2 (CDMA), může R-UIM (nebo jeho vývojová forma CSIM) koexistovat s kartou SIM/[USIM](/mobilnisite/slovnik/usim/), přičemž zařízení směruje autentizaci do příslušné sítě.

Její role v síti je klíčová pro mobilitu účastníka a zabezpečení v ekosystému CDMA. Oddělením identity účastníka od telefonu umožňuje uživatelům měnit telefony pouhým přesunutím karty R-UIM při zachování jejich čísla a nastavení služeb. Pro síťové operátory představuje zabezpečený, proti manipulaci odolný prvek pro ukládání autentizačních přihlašovacích údajů, což je zásadní pro prevenci podvodů. Zatímco primárním ekvivalentem v 3GPP je SIM/USIM, specifikace 3GPP odkazují na R-UIM v kontextech týkajících se propojování sítí GSM/UMTS/LTE a CDMA nebo ve specifikacích definujících požadavky na vícemódová uživatelská zařízení, která musí podporovat identifikační moduly od obou standardizačních orgánů.

## K čemu slouží

R-UIM byl vytvořen, aby přinesl funkčnost podobnou kartě [SIM](/mobilnisite/slovnik/sim/) do rodiny sítí CDMA2000, které původně používaly síťový autentizační model, kde byla identita účastníka vázána na telefon (identifikovaný Electronic Serial Number - [ESN](/mobilnisite/slovnik/esn/)). Tento model orientovaný na telefon omezoval mobilitu a flexibilitu uživatele. Motivací pro R-UIM bylo tuto limitaci odstranit zavedením výměnného, zabezpečeného tokenu, který může uchovávat identitu a autentizační data uživatele, což umožňuje účastníkům CDMA snadno měnit zařízení při zachování své služební identity – funkce, která byla hlavní konkurenční výhodou sítí GSM.

Její vývoj pod záštitou 3GPP2 vyřešil několik klíčových problémů: zvýšil uživatelský komfort, umožnil operátorům nabízet flexibilnější tarify a poskytl robustnější platformu pro zabezpečenou autentizaci a přidané služby (prostřednictvím aplikací na R-UIM). Dále usnadnil vývoj globálních vícemódových zařízení schopných pracovat v sítích GSM i CDMA tím, že poskytl standardizovaný formát a logické rozhraní pro přihlašovací údaje CDMA. To bylo obzvláště důležité na trzích, kde obě technologie koexistovaly. Zatímco základní specifikace 3GPP se zaměřují na SIM/USIM, zahrnutí R-UIM do některých dokumentů 3GPP (např. o bezpečnostních aspektech a charakteristikách terminálů) uznává potřebu interoperability a definuje, jak by se mělo zařízení vyhovující 3GPP chovat k této komponentě definované 3GPP2, pokud je přítomna.

## Klíčové vlastnosti

- Zabezpečená čipová karta pro identitu a autentizaci účastníka v CDMA2000
- Ukládá IMSI, Authentication Key (A-Key) a Preferred Roaming List (PRL)
- Fyzicky kompatibilní s formátem karty SIM (ID-1, plug-in)
- Umožňuje mobilitu účastníka mezi telefony CDMA
- Podporuje aplikační toolkit pro přidané služby
- Je zmíněna v dokumentech 3GPP v souvislosti s požadavky na propojování vícemódových zařízení

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [SIM – Subscriber Identity Module / Universal Subscriber Identity Module](/mobilnisite/slovnik/sim/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TR 22.936** (Rel-19) — Multi-system terminal behavior study
- **TS 33.203** (Rel-19) — IMS Security Specification

---

📖 **Anglický originál a plná specifikace:** [R-UIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/r-uim/)
