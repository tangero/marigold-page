---
slug: "sat"
url: "/mobilnisite/slovnik/sat/"
type: "slovnik"
title: "SAT – SIM Application Toolkit"
date: 2025-01-01
abbr: "SAT"
fullName: "SIM Application Toolkit"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sat/"
summary: "Standard, který umožňuje modulu identifikace účastníka (SIM) iniciovat akce a komunikovat s mobilní sítí a telefonem. Umožňuje přidané služby, jako je přizpůsobení nabídky, proaktivní příkazy SIM a za"
---

SAT je standard, který umožňuje SIM kartě iniciovat akce a komunikovat s mobilní sítí a telefonem pro přidané služby, jako je přizpůsobení nabídky, proaktivní příkazy a zabezpečené transakce.

## Popis

[SIM](/mobilnisite/slovnik/sim/) Application Toolkit (SAT) je soubor příkazů a procedur, které umožňují aplikaci na UICC (Universal Integrated Circuit Card, běžně známé jako SIM karta) proaktivně fungovat v mobilním prostředí. Mění SIM kartu z pasivního autentizačního modulu na aktivního účastníka, který může ovládat aspekty mobilního zařízení ([ME](/mobilnisite/slovnik/me/) neboli telefonu) a komunikovat se sítí. Architektura je založena na modelu klient-server, kde SIM je klientská aplikace (SAT klient) a vyhrazený síťový server, SAT Server nebo Proactive SIM Server, funguje jako vzdálená entita. Komunikace probíhá přes standardizované rozhraní mezi UICC a ME, přičemž síťové zprávy jsou přenášeny přes existující signalizační kanály (jako [SMS](/mobilnisite/slovnik/sms/) nebo Bearer Independent Protocol).

Toolkit funguje tak, že definuje 'proaktivní příkazy', které může SIM vydat směrem k ME. Tyto příkazy instruují ME k provedení akcí, jako je zobrazení nabídky, přehrání tónu, odeslání SMS, uskutečnění hovoru nebo poskytnutí informace o poloze. ME příkaz vykoná a vrátí terminálovou odpověď zpět na SIM. Pro interakci se sítí může SIM odeslat data na předdefinovaný SAT server pomocí SMS paketu nebo datového kanálu. Server pak může odpovědět příkazy, které SIM interpretuje a podle nich jedná. Tento mechanismus je klíčový pro služby jako bankovnictví založené na SIM, mobilní vstupenky nebo dálková ([OTA](/mobilnisite/slovnik/ota/)) správa SIM.

Klíčové součásti zahrnují SAT aplikaci rezidentní na UICC, proaktivní příkazy SAT a obálky definované ve specifikacích 3GPP, software pro obsluhu SAT v ME a síťový SAT server. Jeho role v síti je poskytovat zabezpečenou, na SIM centrickou platformu pro poskytování služeb. Protože SIM je odolný hardwarový prvek vůči neoprávněné manipulaci, služby využívající SAT těží z její vnitřní bezpečnosti, což ji činí ideální pro důvěryhodné transakce. SAT se vyvinul do komplexnějšího [USIM](/mobilnisite/slovnik/usim/) Application Toolkit ([USAT](/mobilnisite/slovnik/usat/)) pro 3G/4G/5G, ale základní proaktivní koncept zůstává, což zajišťuje zpětnou kompatibilitu a dlouhodobý ekosystém pro služby založené na SIM.

## K čemu slouží

SAT byl vytvořen, aby odemkl potenciál [SIM](/mobilnisite/slovnik/sim/) karty nad její původní účel autentizace účastníka a úložiště klíčů. V rané éře GSM ([R99](/mobilnisite/slovnik/r99/)) sítě a poskytovatelé služeb hledali způsoby, jak nasadit přizpůsobené, interaktivní služby přímo spojené s identitou účastníka bezpečným způsobem. Problém byl, že software telefonu byl různorodý a nebyl pod kontrolou operátora, zatímco SIM byla standardizovaná, bezpečná, operátorem vydávaná komponenta. SAT to vyřešil tím, že změnil SIM na programovatelnou platformu, což operátorům umožnilo nasazovat služby, které budou konzistentně fungovat na různých modelech telefonů.

Motivace vycházela z touhy po přidaných službách (VAS), jako jsou informační služby, mobilní bankovnictví (m-banking) a dálková (OTA) správa dat SIM. Před SAT musela být jakákoli interaktivní služba implementována výhradně v softwaru telefonu, což vedlo k fragmentaci a bezpečnostním obavám. SAT poskytl standardizovaný, na síť centrický přístup. Vyřešil omezení SIM jako pasivní komponenty definováním jasného protokolu, aby mohla 'převzít iniciativu.' To umožnilo operátorům udržet kontrolu nad uživatelským zážitkem ze služby a bezpečností, protože kritická logika a přihlašovací údaje sídlily na zabezpečené SIM. Jeho vytvoření umožnilo první vlnu mobilních datových služeb a připravilo cestu pro moderní správu eSIM a provizionování zařízení IoT.

## Klíčové vlastnosti

- Proaktivní příkazy SIM pro ovládání telefonu
- Zabezpečený komunikační kanál přes SMS nebo BIP
- Zobrazení a výběr z nabídky na displeji telefonu
- Podpora přidaných služeb centrických na SIM
- Dálková (OTA) správa aplikací a dat
- Prostředí pro provádění odolné vůči neoprávněné manipulaci na UICC

## Související pojmy

- [USAT – Universal Subscriber Identity Module Application Toolkit](/mobilnisite/slovnik/usat/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.038** (Rel-19) — USIM Application Toolkit (USAT) Stage 1
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.228** (Rel-19) — IP Multimedia Service Requirements
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 29.198** (Rel-9) — OSA API Overview Specification

---

📖 **Anglický originál a plná specifikace:** [SAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/sat/)
