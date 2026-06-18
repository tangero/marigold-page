---
slug: "sd-rsrp"
url: "/mobilnisite/slovnik/sd-rsrp/"
type: "slovnik"
title: "SD-RSRP – Sidelink Discovery Reference Signal Received Power"
date: 2026-01-01
abbr: "SD-RSRP"
fullName: "Sidelink Discovery Reference Signal Received Power"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sd-rsrp/"
summary: "Měření úrovně přijímaného výkonu referenčního signálu pro objevování na postranním spoji (Sidelink Discovery Reference Signal) v LTE a NR ProSe. Zařízení jej používají k vyhodnocení kvality potenciáln"
---

SD-RSRP je měření úrovně přijímaného výkonu referenčního signálu pro objevování na postranním spoji (Sidelink Discovery Reference Signal), které zařízení používají k vyhodnocení kvality potenciálního přímého komunikačního spoje pro služby založené na blízkosti.

## Popis

Sidelink Discovery Reference Signal Received Power (SD-RSRP) je klíčové měření na fyzické vrstvě v rámci architektury Device-to-Device ([D2D](/mobilnisite/slovnik/d2d/)) a Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)) podle 3GPP, použitelné pro postranní spoj (sidelink) v LTE (od Rel-12) i v NR (od Rel-16). Kvantifikuje úroveň výkonu přijímaného referenčního signálu pro objevování (Discovery Reference Signal, [DRS](/mobilnisite/slovnik/drs/)), který vysílá blízké UE na rozhraní postranního spoje (PC5). Na rozdíl od [RSRP](/mobilnisite/slovnik/rsrp/) pro buňkový downlink, které měří signály ze základnové stanice (eNodeB/gNB), SD-RSRP měří signály z protějškových zařízení, což umožňuje přímé objevování a odhad kvality spoje. Měření provádí fyzická vrstva UE na nakonfigurovaných zdrojích pro objevování v rámci nosné pro ProSe objevování.

Technický postup zahrnuje vysílající UE, které rozesílá zprávu pro objevování (Discovery Message) obsahující přidružené referenční signály pro objevování. Tyto signály mají známou strukturu a sekvenci, což přijímajícím UE umožňuje je detekovat a měřit jejich přijímaný výkon. Měření SD-RSRP je definováno jako lineární průměr přes příspěvky výkonu z prvků zdroje (resource elements), které nesou specifické referenční signály pro objevování v rámci měřicí šířky pásma. Vyšší vrstvy UE ([RRC](/mobilnisite/slovnik/rrc/)) konfigurují kritéria měření a hlášení, která mohou být spouštěna událostí nebo periodická. Naměřená hodnota SD-RSRP je pak použita protokolovou sadou ProSe nebo aplikační vrstvou UE k rozhodování, například zda oznámit objevení jiného zařízení nebo vybrat nejvhodnějšího protějška pro potenciální přímý komunikační spoj.

SD-RSRP hraje klíčovou roli v procesu objevování na postranním spoji, který funguje ve dvou hlavních modelech: Model A (oznámení typu "jsem tady") a Model B (dotazy "kdo je tam?" / "jsi tam?" a odpovědi). V obou modelech lze naměřené SD-RSRP použít jako kritérium pro filtrování objevů – za platná nebo relevantní mohou být považována pouze zařízení s SD-RSRP nad určitou prahovou hodnotou. Tím se zabrání zahlcení UE vzdálenými nebo slabými signály a zajistí se spolehlivé objevování pouze v požadovaném dosahu. Jde o základní metriku pro síťově řízený nebo autonomní výběr zdrojů, řízení výkonu a správu mobility v komunikaci na postranním spoji, která přímo ovlivňuje výkon a spolehlivost služeb, jako jsou komunikace pro veřejnou bezpečnost, komunikace mezi vozidlem a čímkoli ([V2X](/mobilnisite/slovnik/v2x/)) a komerční ProSe.

## K čemu slouží

SD-RSRP bylo vytvořeno, aby řešilo základní potřebu standardizované, kvantitativní míry síly signálu pro objevování na postranním spoji v LTE a NR [ProSe](/mobilnisite/slovnik/prose/). Před standardizací ProSe chyběla pro přímé objevování a komunikaci zařízení jednotná metoda, jak zařízení vyhodnotit kvalitu a životaschopnost přímého rádiového spoje. Zavedení ProSe v LTE Rel-12 pro případy užití veřejné bezpečnosti a komerční sféry vyžadovalo mechanismus, aby se zařízení mohla autonomně nebo s pomocí sítě vzájemně objevovat a odhadnout kvalitu spoje ještě před navázáním komunikace.

Vývoj SD-RSRP byl motivován omezeními jednoduchého binárního objevování (detekováno/nedetekováno). Měření založené na výkonu umožňuje odhad blízkosti, predikci kvality spoje a inteligentní filtrování objevů. Řeší problém určení, zda je objevené zařízení v užitečném komunikačním dosahu, což je zásadní pro efektivní využití zdrojů a spolehlivost služby. V síťově řízených scénářích může základnová stanice použít nahlášená měření SD-RSRP ke správě zdrojů pro objevování a interference. V autonomních scénářích zařízení používají SD-RSRP k nezávislému rozhodování o objevení protějšku a zahájení spojení, což umožňuje robustní přímou komunikaci v situacích bez pokrytí nebo s částečným pokrytím, klíčových pro aplikace veřejné bezpečnosti a [V2X](/mobilnisite/slovnik/v2x/).

## Klíčové vlastnosti

- Měří přijímaný výkon referenčních signálů pro objevování na postranním spoji (Sidelink Discovery Reference Signals) na rozhraní PC5
- Podporuje operace ProSe pro postranní spoj (SL) v LTE i v NR
- Používá se jako kritérium pro filtrování a validaci objevů založených na blízkosti
- Informuje o výběru zdrojů pro postranní spoj, řízení výkonu a rozhodnutích o mobilitě
- Lze konfigurovat pro hlášení spouštěné událostí nebo periodické hlášení síti
- Základní pro síťově řízené a autonomní modely objevování (Model A a B)

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [SL-RSRP – Sidelink Reference Signal Received Power](/mobilnisite/slovnik/sl-rsrp/)

## Definující specifikace

- **TS 23.289** (Rel-20) — Mission Critical services over 5G System
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SD-RSRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sd-rsrp/)
