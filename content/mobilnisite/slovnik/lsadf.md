---
slug: "lsadf"
url: "/mobilnisite/slovnik/lsadf/"
type: "slovnik"
title: "LSADF – Location System Assistance Data Function"
date: 2025-01-01
abbr: "LSADF"
fullName: "Location System Assistance Data Function"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lsadf/"
summary: "Síťová funkce, která poskytuje pomocná data uživatelskému zařízení (UE) za účelem zlepšení rychlosti, přesnosti a efektivity metod satelitního určování polohy, jako je GPS. Dodává informace o oběžných"
---

LSADF je síťová funkce, která poskytuje uživatelskému zařízení (UE) pomocná data o oběžných drahách satelitů a časování, aby se zvýšila rychlost, přesnost a efektivita satelitního určování polohy.

## Popis

Funkce pomocných dat polohového systému (Location System Assistance Data Function – LSADF) je klíčovou součástí architektury Secure User Plane Location (SUPL) v rámci 3GPP, konkrétně definovanou pro UMTS. Jejím hlavním úkolem je generovat a poskytovat pomocná data terminálům s podporou SUPL (SUPL Enabled Terminals – SET), což jsou uživatelská zařízení (UE) s možností určování polohy. Tato pomocná data jsou zásadní pro zlepšení výkonu systémů satelitního určování polohy, především Globálního polohového systému ([GPS](/mobilnisite/slovnik/gps/)). LSADF se typicky nachází v síti, často společně s platformou SUPL Location Platform (SLP) nebo jako její součást. Čerpá nezpracovaná data o efemeridách, almanachu a časování satelitů z referenčních přijímačů nebo jiných externích zdrojů.

LSADF funguje tak, že tato nezpracovaná data převede do kompaktního standardizovaného formátu vhodného pro přenos přes mobilní síť k uživatelskému zařízení. Když uživatelské zařízení zahájí polohovací relaci (např. pro požadavek na službu založenou na poloze), může SLP vyvolat LSADF, aby poskytla potřebná pomocná data. Tato data jsou následně odeslána uživatelskému zařízení přes uživatelskou rovinu (např. přes IP). Pomocná data výrazně snižují čas do prvního určení polohy (Time To First Fix – TTFF) pro GPS přijímač uživatelského zařízení. Bez pomoci provádí GPS přijímač tzv. studený start, který zahrnuje hledání všech možných satelitů a stahování jejich efemeridních dat přímo ze satelitů – proces, který může trvat několik minut a spotřebovává značné množství energie baterie.

Poskytnutím přesných informací o tom, které satelity jsou viditelné a jaké jsou jejich očekávané parametry, umožňuje LSADF uživatelskému zařízení provést tzv. asistovaný start. GPS přijímač uživatelského zařízení se může okamžitě zaměřit na příjem signálů od konkrétních satelitů, což dramaticky snižuje TTFF na několik sekund. LSADF může poskytovat různé typy pomocných dat, včetně asistence pro příjem (Acquisition Assistance – [AA](/mobilnisite/slovnik/aa/)), která poskytuje odhady kódové fáze a Dopplerova posuvu; asistence pro citlivost (Sensitivity Assistance – SA) pro podmínky se slabým signálem; a informací o integritě v reálném čase (Real-Time Integrity – RTI). Funkce je definována tak, aby pracovala pod kontrolou SLP, což zajišťuje, že doručování pomocných dat je bezpečné, efektivní a v souladu s požadavky na soukromí uživatele a služby.

## K čemu slouží

LSADF byla zavedena za účelem překonání významných omezení spotřebitelských [GPS](/mobilnisite/slovnik/gps/) přijímačů integrovaných do mobilních telefonů, zejména jejich špatného výkonu z hlediska času do určení polohy a spotřeby energie. Rané mobilní polohové služby byly brzděny dlouhými prodlevami (často přes minutu) při získávání GPS polohy, zejména ze studeného startu nebo v náročných prostředích, jako jsou městské kaňony. Tato špatná uživatelská zkušenost ohrožovala životaschopnost služeb založených na poloze v reálném čase. Hlavním problémem, který LSADF řeší, je tento výkonnostní rozdíl.

Její vytvoření bylo motivováno potřebou učinit satelitní určování polohy proveditelným pro hromadně rozšířená zařízení s omezenou kapacitou baterie. Přesunutím výpočetně náročného úkolu shromažďování a zpracování nezpracovaných satelitních dat na výkonný, stále připojený síťový server (LSADF) se výrazně sníží zátěž na mobilním zařízení. Tento síťově asistovaný přístup, standardizovaný jako součást SUPL v rámci 3GPP, řešil klíčová úzká místa: rychlost, přesnost při slabých signálech a výdrž baterie. Umožnil rozšířené přijetí navigace s pokyny, vyhledávání na základě polohy a nouzových polohových služeb (jako je E911) na mobilních zařízeních, čímž vytvořil základní technologii pro moderní mobilní ekosystém.

## Klíčové vlastnosti

- Generuje a poskytuje pomocná data pro GPS (a další GNSS) mobilním zařízením
- Významně snižuje čas do prvního určení polohy (TTFF) pro satelitní určování polohy
- Umožňuje fungování v podmínkách se slabým signálem (např. uvnitř budov, v městských kaňonech)
- Snižuje spotřebu energie uživatelského zařízení během určování polohy
- Funguje v rámci architektury SUPL pod kontrolou platformy SUPL Location Platform
- Poskytuje typy dat včetně asistence pro příjem, asistence pro citlivost a efemeridních dat

## Související pojmy

- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [LSADF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lsadf/)
