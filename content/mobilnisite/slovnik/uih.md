---
slug: "uih"
url: "/mobilnisite/slovnik/uih/"
type: "slovnik"
title: "UIH – Unnumbered Information with Header Check"
date: 2025-01-01
abbr: "UIH"
fullName: "Unnumbered Information with Header Check"
category: "Protocol"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/uih/"
summary: "Typ rámce v multiplexním protokolu 3GPP 27.010 používaný pro přenos dat mezi terminálním zařízením (TE) a mobilním zakončením (MT). Přenáší uživatelská data s kontrolovanou hlavičkou a poskytuje spole"
---

UIH je typ rámce v multiplexním protokolu 3GPP 27.010 používaný pro spolehlivý přenos dat mezi terminálním zařízením (Terminal Equipment) a mobilním zakončením (Mobile Termination), který přenáší uživatelská data s kontrolovanou hlavičkou.

## Popis

Unnumbered Information with Header Check (UIH) je specifický příkazový/response rámec definovaný v protokolu 3GPP TS 27.010 s názvem "[Multiplexing](/mobilnisite/slovnik/multiplexing/) protocol for mobile equipment interfaces." Tento protokol funguje přes sériový rozhraní, historicky RS-232 nebo [USB](/mobilnisite/slovnik/usb/) sériovou emulaci, mezi terminálním zařízením ([TE](/mobilnisite/slovnik/te/)), jako laptop nebo [PDA](/mobilnisite/slovnik/pda/), a mobilním zakončením ([MT](/mobilnisite/slovnik/mt/)), jako mobilní telefon nebo datová karta. Rámec UIH je jedním z několika typů rámců používaných k vytvoření a správě více logických datových kanálů (virtuálních okruhů) přes jediný fyzický sériový spoj. Rámec UIH se primárně používá pro přenos uživatelských dat. Jeho struktura obsahuje pole Adresa (identifikující koncový bod spojení datového spoje), pole Řízení (specifikující typ rámce jako UIH), volitelný délkový indikátor, uživatelskou datovou část a sekvenci kontroly hlavičky ([HCS](/mobilnisite/slovnik/hcs/)). HCS je [CRC](/mobilnisite/slovnik/crc/) vypočítané přes pole hlavičky (Adresa a Řízení) pro ochranu proti chybám v těchto kritických částích rámce, což zajistí, že data jsou směrována na správný logický kanál. Na rozdíl od jiných typů rámců, jako [SABM](/mobilnisite/slovnik/sabm/) (Set Asynchronous Balanced Mode) používaný pro zřízení spoje, rámce UIH nevyžadují potvrzení na úrovni datového spoje; jsou vysílány v nečíslovaném formátu, což znamená, že nemají čísla sekvencí. Díky tomu jsou efektivní pro proudová data. Protokol používá tyto rámce pro multiplexování různých protokolů vyšších vrstev (např. kanál AT příkazů, PPP pro IP data, řízení hlasového volání) současně přes jeden sériový port. Příjemce kontroluje HCS; pokud kontrola selže, rámec je zahozen.

## K čemu slouží

Rámec UIH a multiplexní protokol TS 27.010 byly vytvořeny k řešení problému podpory více současných služeb přes jediné, omezené sériové rozhraní dostupné na raných mobilních zařízeních. Před multiplexováním zařízení typicky mohlo zpracovat pouze jeden logický spoj v daném momentu – například buď session AT příkazů nebo PPP datovou session, ale ne obě současně. To bylo hlavní omezení pro aplikace vyžadující simultánní hlas a data nebo více datových kanálů. Protokol 27.010, inspirovaný standardy ITU-T V.42bis / LAPM, zaváděl multiplexer datové vrstvy. Rámec UIH specificky poskytuje efektivní mechanismus pro přenos uživatelských dat pro zřízené logické kanály. Jeho účelem je nabídnout lehkou, potvrzenou (via HCS pro integritu hlavičky) ale ne sekvenčně řízenou službu přenosu dat, minimalizující režii při zachování základní integrity adresování rámce. Tím byla řešena potřeba spolehlivého oddělení kanálů a přenosu dat pro pomocné služby jako fax, okruhově přepínaná data a řízení doplňkových služeb vedle primárního datového spojení, což umožnilo pokročilejší funkce mobilní stanice v období GSM a UMTS.

## Klíčové vlastnosti

- Rámec datové vrstvy spoje pro přenos uživatelských dat v multiplexování TS 27.010
- Obsahuje sekvenci kontroly hlavičky (HCS) pro detekci chyb v hlavičce rámce
- Funguje v nečíslovaném režimu (bez čísel sekvencí pro řízení toku)
- Používá se pro data na zřízených logických kanálech mezi TE a MT
- Podporuje multiplexování více protokolů přes jediné sériové rozhraní
- Umožňuje současné služby jako hlas, data a AT příkazy na jediném portu

## Definující specifikace

- **TS 27.010** (Rel-19) — Multiplexing Protocol for UE-TE Interface

---

📖 **Anglický originál a plná specifikace:** [UIH na 3GPP Explorer](https://3gpp-explorer.com/glossary/uih/)
