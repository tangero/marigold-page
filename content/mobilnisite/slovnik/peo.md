---
slug: "peo"
url: "/mobilnisite/slovnik/peo/"
type: "slovnik"
title: "PEO – Power Efficient Operation"
date: 2025-01-01
abbr: "PEO"
fullName: "Power Efficient Operation"
category: "IoT"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/peo/"
summary: "Soubor funkcí v GSM/EDGE Radio Access Network (GERAN) navržených k prodloužení výdrže baterie zařízení IoT. Snižuje spotřebu energie optimalizací procedur pagingu a signalizace, což umožňuje zařízením"
---

PEO je soubor funkcí GERAN navržených k prodloužení výdrže baterie zařízení IoT optimalizací procedur pagingu a signalizace, aby umožnily delší spánkové periody.

## Popis

Power Efficient Operation (PEO) je soubor mechanismů standardizovaných v 3GPP pro GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)) za účelem minimalizace spotřeby energie uživatelského zařízení (UE), zejména zařízení určených pro Machine-Type Communication ([MTC](/mobilnisite/slovnik/mtc/)) a aplikace Internetu věcí (IoT). Funguje na principu zásadní změny chování zařízení v režimu nečinnosti (idle mode), tedy ve stavu, kdy je zařízení registrováno v síti, ale aktivně nepřenáší ani nepřijímá uživatelská data. Základním principem je prodloužení spánkových cyklů zařízení, během nichž je většina jeho rádiových obvodů vypnuta, čímž se drasticky snižuje průměrný odběr energie.

Architektura pro PEO zahrnuje vylepšení jak na straně sítě, tak na straně UE. Síť, konkrétně Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) a Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)), podporuje prodloužené cykly přerušovaného příjmu (eDRX) v režimu nečinnosti a režim úspory energie ([PSM](/mobilnisite/slovnik/psm/)). UE implementuje odpovídající protokoly pro vyjednání a využití těchto prodloužených časovačů. Mezi klíčové komponenty patří prodloužený cyklus [DRX](/mobilnisite/slovnik/drx/), který umožňuje UE probouzet se méně často ke kontrole pagingových zpráv ze sítě, a Aktivní časovač (Active Timer), který definuje, jak dlouho zůstává UE dosažitelné pro mobilně-terminované služby po přenosu dat, než přejde do hlubšího spánkového stavu.

Provoz PEO je řízen signalizací mezi UE a sítí během procedur, jako je Attach, aktualizace směrovací oblasti (Routing Area Update), nebo prostřednictvím specifických zpráv Device Properties. UE indikuje svou podporu PEO a může požadovat konkrétní hodnoty časovačů. Síť tyto požadavky autorizuje na základě předplatitelských dat a síťových politik. Po nakonfigurování UE následuje vyjednaný cyklus: probudí se v určeném pagingovém okamžiku, naslouchá případným pagingovým zprávám, a pokud žádné nejsou, vrátí se do spánku. Pro mobilně-iniciovanou komunikaci může UE zahájit přenos kdykoli, ale její dosažitelnost pro příchozí data je omezena na její aktivní okna, což obětuje latenci ve prospěch obrovské úspory energie. To činí z PEO základní technologii pro hromadná nasazení IoT, kde je klíčovým požadavkem výdrž baterie zařízení přes 10 let.

## K čemu slouží

Power Efficient Operation byl vytvořen, aby řešil kritickou výzvu výdrže baterie v celulárních zařízeních IoT. Před jeho zavedením byly standardní procedury GSM/GPRS/EDGE optimalizovány pro komunikaci orientovanou na člověka, kde se očekává, že zařízení budou často dosažitelná a mají pravidelné možnosti nabíjení. Pro IoT senzory a měřiče nasazené na odlehlých nebo těžko přístupných místech tyto procedury vedly k nepřijatelně krátké výdrži baterie, často pouze v řádu měsíců, což činilo rozsáhlá nasazení ekonomicky a logisticky neproveditelnými.

Primární problém, který PEO řeší, je vysoká spotřeba energie v režimu nečinnosti. Konvenční zařízení se musí probouzet často (např. každých několik sekund), aby naslouchala pagingovým zprávám, což v čase spotřebovává značnou energii. PEO bylo motivováno potřebou umožnit nové případy užití MTC s nízkou propustností a tolerancí k zpoždění, definované v 3GPP, jako je chytré měření, sledování majetku a monitorování životního prostředí. Přímo cílí na cíl 3GPP podporovat zařízení s výdrží baterie až 10 let a více.

Zavedením prodloužených cyklů DRX a PSM umožňuje PEO zařízením spát minuty, hodiny nebo dokonce dny, což dramaticky snižuje pracovní cyklus rádiového rozhraní. Tím se vyřešila omezení předchozích přístupů, které nabízely pouze základní DRX, což pro ultra dlouhou výdrž baterie nestačilo. PEO spolu s podobnými funkcemi v LTE-M a NB-IoT (jako eDRX a PSM) tvoří základní kámen strategie celulárního IoT 3GPP, což umožnilo sítím GSM zůstat životaschopnými pro nasazení IoT s nízkou spotřebou a širokou oblastí pokrytí.

## Klíčové vlastnosti

- Prodloužené cykly přerušovaného příjmu (eDRX) pro režim nečinnosti
- Režim úspory energie (PSM) pro hluboké spánkové stavy
- Vyjednávání parametrů PEO prostřednictvím procedur Attach a aktualizace směrovací oblasti (Routing Area Update)
- Podpora mobilně-iniciovaných dat kdykoli
- Konfigurovatelný Aktivní časovač (Active Timer) pro dosažitelnost po přenosu dat
- Zpětná kompatibilita se staršími sítěmi GSM a UE

## Související pojmy

- [PSM – Protocol State Machine](/mobilnisite/slovnik/psm/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PEO na 3GPP Explorer](https://3gpp-explorer.com/glossary/peo/)
