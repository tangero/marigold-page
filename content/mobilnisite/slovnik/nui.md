---
slug: "nui"
url: "/mobilnisite/slovnik/nui/"
type: "slovnik"
title: "NUI – National User Identifier / USIM Identifier"
date: 2025-01-01
abbr: "NUI"
fullName: "National User Identifier / USIM Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nui/"
summary: "Národní uživatelský identifikátor (NUI) je jedinečný identifikátor uložený na kartě USIM, používaný primárně pro účely zákonného odposlechu a národní bezpečnosti v rámci konkrétní země. Umožňuje národ"
---

NUI je jedinečný identifikátor uložený na kartě USIM, který umožňuje národním orgánům identifikovat účastníka v rámci konkrétní země pro účely zákonného odposlechu a bezpečnosti.

## Popis

Národní uživatelský identifikátor (NUI), označovaný také jako [USIM](/mobilnisite/slovnik/usim/) Identifier, je parametr identity účastníka definovaný ve specifikacích 3GPP. Je uložen v rámci aplikace Universal Subscriber Identity Module (USIM) na [SIM](/mobilnisite/slovnik/sim/) kartě uživatele. NUI slouží jako národně významný identifikátor, což znamená, že je jedinečný a smysluplný v kontextu regulatorního rámce jedné země. Jeho primární technickou rolí je poskytnout jednoznačnou referenci pro účastníka, která je oddělena od mezinárodně roamingu schopného [IMSI](/mobilnisite/slovnik/imsi/) (International Mobile Subscriber Identity).

Z architektonického hlediska se NUI nachází v souborovém systému USIM, typicky v elementárním souboru [EF](/mobilnisite/slovnik/ef/)(NUI). Na USIM je zřízen operátorem mobilní sítě, často v souladu s národními regulacemi. Když je vyžadován pro účely, jako je zákonný odposlech, může síť požádat o NUI od UE (konkrétně z USIM) během procedur, jako je aktualizace polohy, nebo při zahájení volání iniciovaného mobilním zařízením. Síťová entita provádějící odposlech (jako je Lawful Interception Gateway) používá tento identifikátor ke korelaci zachycené komunikace s konkrétním národním záznamem účastníka.

Princip jeho činnosti je spojen se specifickými síťově spouštěnými příkazy. Síť může odeslat příkaz 'REQ NUI' do mobilního zařízení. Tento příkaz je předán aplikaci USIM, která načte hodnotu NUI ze své zabezpečené paměti a vrátí ji síti prostřednictvím mobilního zařízení. Proces je definován v rámci aplikačního toolkitu USIM a souvisejících protokolů. NUI se nepoužívá v rutinních procedurách mobility nebo správy relací; jeho použití je specializované a spouštěno pouze pro funkce regulatorní shody.

Jeho role v síti je vysoce specifická pro domény bezpečnosti a regulace. Funguje jako klíč, který spojuje síťovou aktivitu (volání, zprávy, datové relace) s uživatelskou identitou definovanou národními orgány. To je zásadní pro vyšetřování a sledovací operace prováděné na základě zákonných mandátů. Oddělení od IMSI je záměrné; IMSI se používá pro mezinárodní roaming a směrování v jádrové síti, zatímco NUI je zachováno pro domácí regulatorní účely, což poskytuje vrstvu administrativního oddělení.

## K čemu slouží

NUI bylo vytvořeno primárně k řešení národních regulatorních požadavků na identifikaci účastníka, konkrétně pro zákonný odposlech ([LI](/mobilnisite/slovnik/li/)) a účely národní bezpečnosti. Různé země mají právní rámce, které ukládají telekomunikačním operátorům povinnost poskytnout vládním orgánům možnost identifikovat a monitorovat komunikaci konkrétních účastníků. Před zavedením NUI orgány spoléhaly na [IMSI](/mobilnisite/slovnik/imsi/) nebo [MSISDN](/mobilnisite/slovnik/msisdn/) (telefonní číslo), ale ty mohly být změněny nebo mít mezinárodní implikace.

Historický kontext zahrnuje vývoj sítí GSM a 3G v kritickou národní infrastrukturu. Regulátoři hledali standardizovaný, proti manipulaci odolný identifikátor, který byl trvale spojen s předplatným a pod národní kontrolou. IMSI, ačkoli jedinečné, je přidělováno operátorem a následuje mezinárodní číslovací plán ([MCC](/mobilnisite/slovnik/mcc/), MNC), což jej činí méně vhodným jako čistě národní administrativní údaj. NUI tento problém řeší tím, že je identifikátor přidělený operátorem, který je definován a používán výhradně v národním kontextu, jak je specifikováno v národních přílohách specifikací 3GPP.

Řeší problém poskytnutí spolehlivého, sítí získatelného identifikátoru pro účastníka, který je nezávislý na komerčních identifikátorech používaných pro směrování a fakturaci. To umožňuje systémům zákonného odposlechu fungovat na základě stabilního ID, které je méně pravděpodobné, že bude změněno nebo zastřeno. Motivací bylo vytvořit harmonizovanou, 3GPP-standardizovanou metodu pro splnění těchto regulatorních povinností, zajišťující interoperabilitu mezi řešeními odposlechu různých dodavatelů a USIM kartami napříč různými operátory v rámci země.

## Klíčové vlastnosti

- Uložen bezpečně v aplikaci USIM
- Jednoznačně identifikuje účastníka v rámci národní jurisdikce
- Získán sítí prostřednictvím specifického příkazu USIM (REQ NUI)
- Používán primárně pro zákonný odposlech a národní bezpečnost
- Nezávislý na mezinárodních identifikátorech, jako je IMSI nebo MSISDN
- Definován v 3GPP TS 22.975 (požadavky na zákonný odposlech) a TS 21.905 (slovníček)

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements

---

📖 **Anglický originál a plná specifikace:** [NUI na 3GPP Explorer](https://3gpp-explorer.com/glossary/nui/)
