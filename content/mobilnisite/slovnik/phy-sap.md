---
slug: "phy-sap"
url: "/mobilnisite/slovnik/phy-sap/"
type: "slovnik"
title: "PHY-SAP – Physical Service Access Point"
date: 2025-01-01
abbr: "PHY-SAP"
fullName: "Physical Service Access Point"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/phy-sap/"
summary: "Physical Service Access Point (PHY-SAP) je konceptuální servisní rozhraní mezi fyzickou vrstvou (PHY) a vrstvou řízení přístupu k médiu (MAC) v protokolovém zásobníku 3GPP. Definuje primitiva a vyměňo"
---

PHY-SAP je konceptuální servisní rozhraní mezi fyzickou vrstvou a vrstvou řízení přístupu k médiu, které definuje primitiva a vyměňované datové jednotky, jako jsou přenosové bloky.

## Popis

Physical Service Access Point (PHY-SAP) je standardizované servisní rozhraní, bod, kde vrstva řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) přistupuje ke službám poskytovaným fyzickou vrstvou ([PHY](/mobilnisite/slovnik/phy/)). Nejde o fyzický konektor, ale o logický referenční bod definovaný ve specifikacích 3GPP (primárně TS 25.321 pro MAC a TS 25.212 pro PHY v [UTRA](/mobilnisite/slovnik/utra/), s ekvivalenty v LTE a NR). [SAP](/mobilnisite/slovnik/sap/) definuje sadu primitiv – abstraktních, na implementaci nezávislých zpráv – které proudí mezi vrstvami. Tato primitiva reprezentují požadavky, indikace, odpovědi a potvrzení pro konkrétní služby.

Fungování PHY-SAP zahrnuje výměnu konkrétních datových jednotek a řídicích informací. Primárními datovými jednotkami jsou přenosové bloky ([TB](/mobilnisite/slovnik/tb/)). Vrstva MAC doručuje jeden nebo více přenosových bloků do PHY prostřednictvím PHY-SAP pro přenos na konkrétním přenosovém kanálu (např. [DCH](/mobilnisite/slovnik/dch/), [HS-DSCH](/mobilnisite/slovnik/hs-dsch/), [RACH](/mobilnisite/slovnik/rach/)). Každý TB obsahuje datovou část a přidružené řídicí informace z MAC, jako je přenosový formát (TF), který specifikuje velikost bloku, modulaci a kódovací schéma. Naopak, PHY doručuje přijaté přenosové bloky nahoru do vrstvy MAC přes stejný SAP. Dále PHY-SAP přenáší potvrzení hybridního automatického opakování požadavku (HARQ) (ACK/NACK) pro řízení opakování paketů a měřicí hlášení (např. indikátor kvality kanálu – CQI) z PHY do MAC, aby pomohla při rozhodování o plánování.

Klíčovými komponentami PHY-SAP jsou definovaná primitiva a jejich parametry. Mezi běžná primitiva patří PHY-DATA-REQ (žádost o přenos TB), PHY-DATA-IND (indikace přijatého TB), PHY-STATUS-IND (pro hlášení měření nebo chyb) a primitiva pro řízení procedur náhodného přístupu. Jeho úlohou v síti je zajistit čisté, standardizované oddělení odpovědností mezi vrstvami MAC a PHY. To umožňuje nezávislý vývoj, testování a optimalizaci každé vrstvy. Například dodavatel základnové stanice může navrhnout sofistikovanou implementaci PHY (s pokročilými anténami) při dodržení SAP, což zajišťuje její funkčnost se standardním plánovačem MAC od jiného dodavatele. Zapouzdřuje složitost procesu rádiového přenosu a příjmu a představuje vrstvě MAC jednodušší službu přenosu dat.

## K čemu slouží

PHY-SAP existuje, aby formalizoval interakci mezi vrstvami MAC a PHY, podporuje modularitu a interoperabilitu v bezdrátových komunikačních systémech. Řeší problém těsně provázaných proprietárních implementací, kde jsou MAC a PHY navrženy jako jediná, neoddělitelná jednotka. Toto těsné propojení by brzdilo inovace, komplikovalo testování a ztěžovalo kombinaci komponent od různých dodavatelů v prostředí sítě s více výrobci.

Historická motivace vychází ze strukturovaného, vrstveného přístupu návrhu komunikačních protokolů (jako je model OSI). Definováním přesného servisního rozhraní zajišťuje 3GPP jasné vymezení funkčních odpovědností každé vrstvy. Vrstva MAC se zabývá multiplexováním logických kanálů, plánováním a řízením priorit, zatímco PHY se zabývá přenosem nezpracovaného signálu. SAP tuto hranici jasně vymezuje. To bylo obzvláště důležité s vývojem systémů 3GPP pro podporu více technologií rádiového přístupu (RAT) a agregace nosných, kde jedna vrstva MAC může potřebovat komunikovat s různými instancemi PHY (např. LTE a NR).

Řeší omezení ad-hoc rozhraní, která by se mohla měnit s každou technologickou verzí a způsobovat problémy s kompatibilitou. PHY-SAP poskytuje stabilní abstrakci. I když se základní PHY technologie dramaticky vyvíjela od WCDMA přes LTE založené na OFDMA až po flexibilní NR, základní koncept SAP – výměna přenosových bloků a řídicích informací – zůstal, což umožnilo vyšším vrstvám protokolů se vyvíjet jiným tempem. Jeho vytvoření bylo motivováno potřebou škálovatelné, do budoucna připravené architektury, která by mohla pojmout nové funkce fyzické vrstvy (jako nové numerologie nebo massive MIMO) bez nutnosti překreslení celého protokolového zásobníku, čímž se sníží čas a náklady na vývoj pro výrobce zařízení.

## Klíčové vlastnosti

- Definuje abstraktní servisní primitiva pro přenos dat mezi MAC a PHY
- Specifikuje přenosový blok (TB) jako základní jednotku pro výměnu dat
- Přenáší řídicí informace, jako je přenosový formát (TF) pro konfiguraci přenosu
- Přenáší HARQ zpětnou vazbu (ACK/NACK) pro řízení opakování
- Doručuje měření fyzické vrstvy (např. CQI, RSRP) plánovači MAC
- Umožňuje nezávislost vrstev a interoperabilitu mezi více dodavateli

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [SAP – Service Access Point](/mobilnisite/slovnik/sap/)

## Definující specifikace

- **TS 25.411** (Rel-19) — Iu Interface Layer 1 Specification

---

📖 **Anglický originál a plná specifikace:** [PHY-SAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/phy-sap/)
