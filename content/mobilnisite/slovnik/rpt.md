---
slug: "rpt"
url: "/mobilnisite/slovnik/rpt/"
type: "slovnik"
title: "RPT – Radio Planning Tool"
date: 2025-01-01
abbr: "RPT"
fullName: "Radio Planning Tool"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/rpt/"
summary: "Softwarový nástroj používaný operátory sítí k plánování, návrhu a optimalizaci nasazení prvků rádiové přístupové sítě (RAN), jako jsou základnové stanice. Využívá propagční modely, předpovědi provozu"
---

RPT je softwarový nástroj používaný k plánování, návrhu a optimalizaci nasazení rádiové přístupové sítě predikcí pokrytí, kapacity a interference pomocí propagčních modelů a geografických dat.

## Popis

Radio Planning Tool (RPT) je komplexní softwarový balík klíčový pro proces řízení životního cyklu sítě definovaný ve specifikacích 3GPP pro management a orchestraci, konkrétně TS 28.667 a TS 28.668. Není to jediný protokol, ale třída aplikací operačního podpůrného systému ([OSS](/mobilnisite/slovnik/oss/)). Architektura nástroje typicky integruje geografický informační systém (GIS), pokročilé modely šíření rádiového signálu (např. Okumura-Hata, ray-tracing), moduly modelování provozu a databázi charakteristik zařízení (vyzařovací diagramy antén, vysílací výkon, citlivost přijímače). Základní pracovní postup zahrnuje import podrobných dat o terénu a překážkách (budovy, vegetace) pro cílovou oblast. Plánovač sítě následně definuje návrhové požadavky, jako je cílové pokrytí, typy služeb (např. enhanced Mobile Broadband), prahové hodnoty kvality služeb a požadavky na kapacitu. RPT simuluje rádiové frekvenční ([RF](/mobilnisite/slovnik/rf/)) prostředí výpočtem predikované síly signálu ([RSRP](/mobilnisite/slovnik/rsrp/)), poměru signálu k šumu a interferenci ([SINR](/mobilnisite/slovnik/sinr/)) a propustnosti pro navrhované lokace a konfigurace základnových stanic. Provádí iterativní analýzu za účelem optimalizace parametrů, jako je umístění stanoviště, výška antény, sklon (mechanický a elektrický), azimut a vysílací výkon, aby byly splněny cíle pokrytí a kapacity při minimalizaci kapitálových výdajů ([CAPEX](/mobilnisite/slovnik/capex/)) a provozních výdajů ([OPEX](/mobilnisite/slovnik/opex/)) způsobených interferencí a nadbytečným dimenzováním. V kontextu samo-organizujících se sítí ([SON](/mobilnisite/slovnik/son/)) podle 3GPP mohou RPT poskytovat vstupní data pro samokonfiguraci a jsou používány offline pro podrobné úlohy optimalizace kapacity a pokrytí ([CCO](/mobilnisite/slovnik/cco/)).

## K čemu slouží

Účelem nástroje pro plánování rádiové sítě je umožnit vědecké, daty řízené plánování mobilních sítí, které překračuje heuristický nebo manuální výběr lokalit. Před existencí sofistikovaných RPT bylo nasazování sítí více experimentální a reaktivní, což vedlo k neoptimálnímu pokrytí, vyšší interferenci a zvýšeným nákladům kvůli zbytečným instalacím stanic nebo špatnému využití zdrojů. RPT řeší základní problém efektivního převodu požadavků na služby a obchodních cílů na fyzický návrh sítě. Řeší složité optimalizační problémy s mnoha proměnnými zahrnujícími terén, fyziku šíření rádiového signálu, distribuci uživatelů a omezení zařízení. Formalizace požadavků na takové nástroje ve specifikacích managementu 3GPP, počínaje Release 12, byla motivována rostoucí složitostí sítí (od 2G přes 3G, 4G až po 5G), omezenou dostupností a vysokou cenou nových lokalit pro buňky a potřebou interoperability mezi plánovacími nástroji a systémy správy sítě (NMS) pro automatizovanou provizi a optimalizaci.

## Klíčové vlastnosti

- Geografické modelování s integrací dat o terénu a budovách
- Pokročilá predikce šíření RF signálu a simulace pokrytí
- Předpověď poptávky po provozu a plánování kapacity
- Automatické plánování buněk (ACP) pro návrh umístění stanic a parametrů
- Analýza interference a optimalizace pro plánování kmitočtů/kanálů
- Podpora plánování více rádiových přístupových technologií (multi-RAT) a vícevrstvých sítí

## Související pojmy

- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)

## Definující specifikace

- **TS 28.667** (Rel-19) — RPTA IRP Requirements
- **TS 28.668** (Rel-19) — RPTA Integration Reference Point Requirements

---

📖 **Anglický originál a plná specifikace:** [RPT na 3GPP Explorer](https://3gpp-explorer.com/glossary/rpt/)
