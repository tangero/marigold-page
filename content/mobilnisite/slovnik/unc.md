---
slug: "unc"
url: "/mobilnisite/slovnik/unc/"
type: "slovnik"
title: "UNC – Unbalanced Operation Normal Response Mode Class"
date: 2025-01-01
abbr: "UNC"
fullName: "Unbalanced Operation Normal Response Mode Class"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/unc/"
summary: "UNC je třída protokolu v rámci nevyváženého provozu v normálním režimu odpovědí (NRM), používaná v komunikacích na linkové vrstvě. Definuje specifický vztah typu master-slave pro řízení přenosu dat, z"
---

UNC je třída protokolu linkové vrstvy pro nevyvážený provoz, která definuje vztah typu master-slave pro řízení uspořádaného přenosu dat mezi primární a sekundární stanicí.

## Popis

Unbalanced Operation Normal Response Mode Class (UNC) je specifická provozní třída v rámci protokolového rámce linkové vrstvy, často spojovaná se standardy jako [HDLC](/mobilnisite/slovnik/hdlc/) (High-Level Data Link Control) a jeho adaptacemi v telekomunikacích. Definuje komunikační režim pro nevyvážené konfigurace, kde je jedna stanice určena jako primární a jedna či více stanic jako sekundární. V normálním režimu odpovědí ([NRM](/mobilnisite/slovnik/nrm/)) mohou sekundární stanice vysílat pouze tehdy, když jsou k tomu explicitně vyzvány (polled) primární stanicí. Označení 'Class' (UNC) specifikuje konkrétní soubor procedur, typů rámců a kódování řídicích polí, které řídí tento nevyvážený provoz v NRM. To zahrnuje pravidla pro navazování a zrušení logických spojů, sekvencování rámců a potvrzování pomocí čítačů N(R) a N(S), procedury pro obnovu po chybě jako [REJ](/mobilnisite/slovnik/rej/) (Reject) a [SREJ](/mobilnisite/slovnik/srej/) (Selective Reject) a zacházení s různými dozorovými (S) a nečíslovanými (U) rámci. V kontextu 3GPP se takové protokoly linkové vrstvy používají pro signalizaci v řídicí rovině a přenos uživatelských dat přes různá rozhraní, jako je rozhraní Abis v GSM nebo některá managementová rozhraní. Protokol zajišťuje spolehlivé sekvenční doručování rámců přes potenciálně šumový fyzický kanál. Řídí řízení toku a opravu chyb na linkové vrstvě, čímž poskytuje stabilní základnu pro síťové protokoly vyšších vrstev.

## K čemu slouží

Třída protokolu UNC existuje za účelem poskytnutí standardizované, spolehlivé metody pro řízení linkové vrstvy v topologiích sítě typu point-to-multipoint nebo master-slave, běžných v telekomunikační infrastruktuře. Řeší problém koordinace komunikace mezi centrální řídicí entitou (jako Base Station Controller nebo [RNC](/mobilnisite/slovnik/rnc/)) a více vzdálenými entitami (jako základnové stanice) přes sdílený nebo vyhrazený spoj. Před zavedením takových standardizovaných procedur linkové vrstvy vedly proprietární řešení k problémům s interoperabilitou. UNC jako součást širší sady protokolů, jako je [LAPD](/mobilnisite/slovnik/lapd/) (Link Access Procedure on the D-channel) nebo jeho deriváty, zajišťuje, že více sekundárních stanic nevysílá současně a nezpůsobuje kolize, poskytuje mechanismy pro detekci chyb a retransmisi a efektivně spravuje logická spojení. Její vznik byl motivován potřebou robustní, na dodavateli nezávislé signalizace a přenosu dat v digitálních telekomunikačních sítích, čímž tvoří kritickou nižší vrstvu v protokolovém zásobníku pro komunikaci v řídicí a managementové rovině.

## Klíčové vlastnosti

- Definuje vztah primární-sekundární stanice pro nevyváženou konfiguraci
- Funguje v normálním režimu odpovědí (NRM), kde sekundární stanice vysílají pouze na vyžádání (poll)
- Specifikuje procedury pro potvrzování rámců pomocí sekvenčních čísel
- Zahrnuje mechanismy pro obnovu po chybě, jako REJ a SREJ
- Spravuje navázání, udržování a uvolnění logického spoje
- Používá standardizované formáty řídicích polí pro dozorové a nečíslované příkazy/odpovědi

## Související pojmy

- [HDLC – High Level Data Link Control](/mobilnisite/slovnik/hdlc/)
- [LAPD – Link Access Procedure on the D-channel](/mobilnisite/slovnik/lapd/)
- [NRM – Network Resource Model](/mobilnisite/slovnik/nrm/)

## Definující specifikace

- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [UNC na 3GPP Explorer](https://3gpp-explorer.com/glossary/unc/)
