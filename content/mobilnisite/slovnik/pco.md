---
slug: "pco"
url: "/mobilnisite/slovnik/pco/"
type: "slovnik"
title: "PCO – Processing Cross-check Organization"
date: 2025-01-01
abbr: "PCO"
fullName: "Processing Cross-check Organization"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pco/"
summary: "Rámec pro ověřování správnosti síťových zpracovatelských funkcí, zejména pro zákonné odposlechy. Zajišťuje, že odposlechnutá data jsou zpracována přesně a spolehlivě v souladu s právními a technickými"
---

PCO je rámec pro ověřování správnosti síťových zpracovatelských funkcí, zejména pro zákonné odposlechy, který zajišťuje přesné a spolehlivé zacházení s daty pro soulad s předpisy a možnost auditu.

## Popis

Processing Cross-check Organization (PCO) je konceptuální a architektonický rámec definovaný ve specifikacích 3GPP, který zajišťuje integritu a správnost zpracovatelských funkcí, s primární aplikací v systémech zákonného odposlechu (Lawful Interception, [LI](/mobilnisite/slovnik/li/)). Funguje tak, že zavádí mechanismy pro ověření, že zpracování odposlechnutého komunikačního obsahu a souvisejících informací o odposlechu (Interception-Related Information, [IRI](/mobilnisite/slovnik/iri/)) probíhá přesně a bez poškození nebo neoprávněné modifikace. To zahrnuje vzájemné porovnávání výstupů zpracovatelských funkcí s očekávanými výsledky nebo použití redundantních zpracovatelských cest k detekci chyb nebo nesrovnalostí.

Architektonicky rámec PCO spolupracuje s klíčovými funkčními entitami LI, jako je Intercepting Control Element ([ICE](/mobilnisite/slovnik/ice/)), který provádí vlastní odposlech v síti, a Delivery Functions ([DF2](/mobilnisite/slovnik/df2/) a [DF3](/mobilnisite/slovnik/df3/)), které zajišťují přenos odposlechnutých dat do zařízení orgánů činných v trestním řízení (Law Enforcement Monitoring Facility, [LEMF](/mobilnisite/slovnik/lemf/)). PCO může využívat techniky jako kontrolní součty (checksums), pořadová čísla, kryptografickou ochranu integrity nebo porovnávání s duplicitními zpracovatelskými datovými toky, aby ověřilo, že data byla správně zpracována od bodu odposlechu až po doručení.

Jeho role v síti je především záruční a týká se souladu s předpisy. Poskytnutím ověřitelné stopy a validací zpracovatelských kroků pomáhá PCO síťovým operátorům a orgánům prokázat, že odposlechnutá data jsou věrnou a přesnou reprezentací komunikace cíle, což je základním právním požadavkem pro zákonný odposlech. Řeší rizika spojená s chybami softwaru, závadami hardwaru nebo škodlivými zásahy v infrastruktuře odposlechu.

## K čemu slouží

PCO bylo zavedeno, aby řešilo kritickou potřebu ověřitelné přesnosti a spolehlivosti v systémech zákonného odposlechu. Jak se telekomunikační sítě stávaly složitějšími a digitálními, zajištění toho, aby odposlechnutá data zůstala během zpracování nezměněna a nepoškozena, se stalo významnou technickou i právní výzvou. Právní rámce po celém světě vyžadují, aby odposlechnutý důkaz byl autentický a spolehlivý, aby mohl být připuštěn u soudu, což si žádá technické mechanismy pro prokázání integrity procesu odposlechu.

Před formalizovanými koncepty, jako je PCO, se spoléhalo na méně systematické metody zajišťování integrity zpracování, které nemusely stačit pro přísný právní dohled. Vytvoření rámce PCO ve standardech 3GPP poskytlo strukturovaný, standardizovaný přístup k tomuto problému. Definuje konkrétní požadavky a možné metody pro vzájemné ověřování, což umožňuje výrobcům zařízení a síťovým operátorům implementovat řešení splňující přísné požadavky na soulad s předpisy. Jeho vývoj byl motivován vývojem regulatorního prostředí a potřebou mezinárodních technických standardů pro podporu zákonného odposlechu napříč různými jurisdikcemi a síťovými technologiemi.

## Klíčové vlastnosti

- Rámec pro ověřování integrity zpracování v zákonném odposlechu
- Zajišťuje přesnost informací souvisejících s odposlechem (IRI) a obsahu komunikace (CC)
- Poskytuje mechanismy pro detekci chyb v řetězcích zpracování
- Podporuje soulad s právními a regulatorními požadavky na připustnost důkazů
- Spolupracuje se standardními funkčními entitami zákonného odposlechu (ICE, DF2, DF3)
- Může využívat techniky jako kontrolní součty, ověřování pořadí nebo redundantní zpracování

## Související pojmy

- [IRI – Intercept Related Information](/mobilnisite/slovnik/iri/)

## Definující specifikace

- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TR 23.981** (Rel-19) — IPv4 IMS Interworking and Migration Study
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.244** (Rel-19) — Wireless LAN Control Plane Protocol
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TR 26.996** (Rel-19) — ISAR Split Rendering Audio Characterization
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 29.806** (Rel-12) — P-CSCF Restoration Analysis & Solutions
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN
- **TR 33.739** (Rel-18) — Study on security enhancement of support for
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [PCO na 3GPP Explorer](https://3gpp-explorer.com/glossary/pco/)
