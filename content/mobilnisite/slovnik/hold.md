---
slug: "hold"
url: "/mobilnisite/slovnik/hold/"
type: "slovnik"
title: "HOLD – Communication session Hold"
date: 2026-01-01
abbr: "HOLD"
fullName: "Communication session Hold"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hold/"
summary: "Doplňková služba, která umožňuje účastníkovi hovoru (hlasového nebo multimediálního) dočasně pozastavit přenos a příjem médií, čímž převede protistranu do stavu držení (hold). Signalizační spojení zůs"
---

HOLD je doplňková služba, která umožňuje účastníkovi hovoru dočasně pozastavit přenos a příjem médií, čímž převede protistranu do stavu držení (hold) při zachování signalizačního spojení pro pozdější obnovení.

## Popis

Služba HOLD je telekomunikační doplňková služba, která uživateli v aktivním hovoru (v přepojování okruhů nebo založeném na IP Multimedia Subsystem) umožňuje dočasně pozastavit obousměrnou výměnu médií bez ukončení relace hovoru. Při aktivaci služba převede protistranu do stavu 'držení (hold)', čímž pozastaví přenos audio a/nebo video mediálních proudů od místního uživatele k protiuserovi. Signalizační cesta, řízená protokoly jako [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) v IMS nebo [ISUP](/mobilnisite/slovnik/isup/)/BICC v [CS](/mobilnisite/slovnik/cs/), zůstává neporušená, aby udržovala stav a řízení hovoru. Držená strana typicky obdrží indikaci, jako je tón držení, hudba-on-hold nebo oznamovací zpráva, a čeká na obnovení hovoru.

Technická implementace se liší mezi síťovými doménami. V IMS je služba implementována pomocí metod signalizace SIP. Terminál uživatele (UE) nebo aplikační server ([AS](/mobilnisite/slovnik/as/)) jednající jeho jménem odešle požadavek SIP re-INVITE nebo UPDATE směrem k protistraně. Tento požadavek obsahuje nabídku Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)), která upravuje mediální relaci. Pro převedení hovoru do držení nabídka typicky nastaví adresu pro spojení mediálního proudu ('c=' řádek v SDP) na '0.0.0.0' nebo zahrne atribut 'a=sendonly' či 'a=inactive' pro místní směr, čímž indikuje dočasné zastavení odesílání médií. Síť může také připojit mediální cestu držené strany k Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)), která přehrává oznámení nebo hudbu. Obnovení hovoru se provede odesláním nové nabídky SIP re-INVITE/UPDATE s normální SDP nabídkou znovu nastavující obousměrný ('sendrecv') přenos médií.

V architektuře Core Network může logika služby HOLD sídlit v terminálu uživatele, v síťové servisní platformě (jako IMS Application Server) nebo v Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) pro hovory s přepojováním okruhů. Pro IMS je definována jako součást sady služeb Multimedia Telephony. Služba interaguje s dalšími doplňkovými službami, jako je Call Waiting a Multiparty hovory. Jejím účelem je zvýšit uživatelský dohled a flexibilitu během komunikační relace, což umožňuje akce jako přijetí druhého příchozího hovoru, soukromou konzultaci nebo pozastavení konverzace bez rozpojení. Síť zajišťuje, že zdroje držené strany jsou odpovídajícím způsobem udržovány a že aktivace služby nezpůsobí nechtěné ukončení hovoru.

## K čemu slouží

Služba HOLD existuje za účelem replikace a vylepšení známé funkce 'držení' z tradiční pevné telefonie v mobilních a IP komunikačních systémech. Řeší praktický problém správy více souběžných komunikačních úkolů nebo potřebu dočasné pauzy během hovoru. Bez ní by uživatel, který potřebuje soukromě hovořit s někým jiným nebo vyhledat informace, musel hovor ukončit, což je rušivé a může vést k neúspěšným pokusům o opětovné spojení. Služba poskytuje řízený, standardizovaný způsob pozastavení médií při zachování signalizační relace, čímž zajišťuje, že hovor lze rychle a spolehlivě obnovit.

Její vytvoření a standardizace byly motivovány potřebou parity funkcí mezi staršími sítěmi s přepojováním okruhů (jako GSM) a síťmi nové generace založenými na IP (jako IMS). Když 3GPP definovalo IMS ve Release 5, bylo klíčové zajistit, aby všechny základní a doplňkové služby ze sítí [CS](/mobilnisite/slovnik/cs/) mohly být podporovány, což garantuje přijetí uživateli a hladkou migraci. Specifikace služby HOLD zajistila interoperabilitu mezi zařízeními různých dodavatelů a přes síťové hranice (např. mezi IMS a CS). V následujících releasech byla její definice upřesněna pro zpracování složitějších multimediálních relací (video, text) a pro bezproblémovou integraci s dalšími IMS službami, čímž si udržela svou roli základního uživatelského očekávání pro kompletní telefonní službu.

## Klíčové vlastnosti

- Dočasně pozastaví obousměrné mediální proudy (audio/video) při zachování signalizačního spojení
- Poskytuje indikaci držené straně prostřednictvím sítí generovaného tónu, hudby nebo zprávy
- Pro implementaci v IMS využívá SIP re-INVITE/UPDATE s upraveným SDP
- Možnosti implementace služby: síťová nebo terminálová
- Integruje se s dalšími službami, jako je Call Waiting, Consultation Hold a Multiparty hovory
- Standardizována pro sítě s přepojováním okruhů (GSM, UMTS) i pro sítě založené na IMS

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.196** (Rel-19) — Enhanced Calling Name (eCNAM) Stage 3 Protocol
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.416** (Rel-7) — Malicious Call Identification Service
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.606** (Rel-19) — MWI Service Protocol Description
- **TS 24.615** (Rel-19) — Communication Waiting (CW) Service Protocol
- **TS 24.642** (Rel-19) — CCBS/CCNR/CCNL SIP Protocol Specification
- **TS 24.647** (Rel-19) — Advice of Charge (AOC) service protocol
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.364** (Rel-19) — IMS AS Service Data Descriptions
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [HOLD na 3GPP Explorer](https://3gpp-explorer.com/glossary/hold/)
