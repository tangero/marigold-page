---
slug: "e-stn-sr"
url: "/mobilnisite/slovnik/e-stn-sr/"
type: "slovnik"
title: "E-STN-SR – Emergency Call Session Transfer Number – Single Radio"
date: 2025-01-01
abbr: "E-STN-SR"
fullName: "Emergency Call Session Transfer Number – Single Radio"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/e-stn-sr/"
summary: "Vyhrazené telefonní číslo používané k přenosu relace nouzového volání z okruhově spínané (CS) domény do paketově spínané (PS) domény pro UE s jedním rádiovým modulem. Umožňuje kontinuitu nouzových slu"
---

E-STN-SR je vyhrazené telefonní číslo používané k přenosu relace nouzového volání z okruhově spínané domény do paketově spínané domény pro zařízení s jedním rádiovým modulem, což zajišťuje kontinuitu služby během předávání spojení.

## Popis

E-STN-SR je klíčový funkční prvek v architektuře nouzového volání IP multimediální podsystému (IMS) definované 3GPP. Jedná se o globálně směrovatelné číslo E.164, odlišné od běžného telefonního čísla, které je předkonfigurováno v síti a asociováno se specifickými aplikačními servery IMS odpovědnými za nouzové relace. Když uživatelské zařízení (UE) s jedním rádiovým modulem – což znamená, že nemůže současně vysílat/přijímat na LTE a starších rádiových modulech 2G/3G – podstoupí předání spojení z [PS](/mobilnisite/slovnik/ps/) přístupu jako LTE do [CS](/mobilnisite/slovnik/cs/) přístupu jako [GERAN](/mobilnisite/slovnik/geran/) nebo [UTRAN](/mobilnisite/slovnik/utran/) pro probíhající nouzové volání, síť použije E-STN-SR. Tento mechanismus je součástí procedur kontinuity služeb IMS. Během předání spojení [MSC](/mobilnisite/slovnik/msc/) Server v CS síti obdrží indikaci přenosu nouzové relace. Iniciuje přenos relace uskutečněním nového volání na číslo E-STN-SR. Toto volání je směrováno přes síť [PSTN](/mobilnisite/slovnik/pstn/)/CS do sítě IMS, konkrétně k aplikačnímu serveru IMS (např. funkci řízení nouzových relací nebo vyhrazenému aplikačnímu serveru centralizace a kontinuity služeb). Tento server koreluje příchozí CS volání s existující IMS nouzovou relací pomocí identifikátorů relace a propojí mediální cesty, čímž přenese větev volání UE z PS přenosu na CS přenos bez přerušení hovoru. Architektura zajišťuje, že centrum nouzových služeb (Public Safety Answering Point) zůstane s uživatelem spojeno po celou dobu přechodu. Mezi klíčové zapojené komponenty patří UE, [E-UTRAN](/mobilnisite/slovnik/e-utran/), MSC Server, jádro IMS ([P-CSCF](/mobilnisite/slovnik/p-cscf/), I-CSCF, S-CSCF) a příslušný aplikační server IMS. Jeho úlohou je poskytnout standardizovaný, sítí řízený bod ukotvení pro mobilitu nouzových relací, což zajišťuje splnění regulatorních požadavků na spolehlivost nouzového volání i v případě, kdy se uživatel pohybuje mimo pokrytí LTE.

## K čemu slouží

E-STN-SR byl vytvořen k řešení kritického problému udržení aktivního nouzového volání, když zařízení s jedním rádiovým modulem provede předání spojení z nouzového volání Voice over LTE (VoLTE) nebo založeného na IMS do starší okruhově spínané sítě. Před nouzovými službami založenými na IMS byla nouzová volání nativní pro přístupovou síť (např. CS volání v 2G/3G). Se zavedením LTE jako čistě paketového přístupu byla nouzová volání definována pro směrování přes IMS. Nicméně raná nasazení LTE často měla mezery v pokrytí, což vyžadovalo předávání spojení do všudypřítomných CS sítí 2G/3G. Bez standardizovaného mechanismu přenosu by se nouzové volání během takového předání spojení přerušilo, což by vytvořilo vážné riziko pro veřejnou bezpečnost. E-STN-SR poskytuje nezbytnou signalizační adresu (telefonní číslo), která umožňuje CS síti 'zavolat zpět' do ekosystému IMS a získat kontext existující nouzové relace. Tím se vyřešilo omezení starších nouzových služeb bez IMS, které neměly koncept kontinuity relace mezi zásadně odlišnými síťovými doménami (PS a CS). Jeho vytvoření bylo motivováno regulatorními požadavky na spolehlivé nouzové služby a praktickou potřebou plynulé přechodové fáze během dlouhodobé migrace z CS na plně IP sítě.

## Klíčové vlastnosti

- Globálně unikátní číslo E.164 pro směrování přenosu nouzové relace
- Umožňuje kontinuitu hlasového volání s jedním rádiovým modulem (SRVCC) pro nouzové relace
- Sítí spouštěný přenos relace z domény IMS/PS do CS domény
- Zajišťuje kontinuitu hovoru bez přerušení služby pro uživatele
- Integruje se s procedurami kontinuity služeb IMS a aplikačními servery
- Podporuje shodu s regulatorními požadavky na spolehlivost nouzových služeb během mobility

## Související pojmy

- [SR-VCC – Single Radio Voice Call Continuity](/mobilnisite/slovnik/sr-vcc/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)

## Definující specifikace

- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 23.870** (Rel-9) — SRVCC for IMS Emergency Calls Study
- **TS 24.237** (Rel-19) — IMS Service Continuity Protocol Details

---

📖 **Anglický originál a plná specifikace:** [E-STN-SR na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-stn-sr/)
