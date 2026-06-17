---
slug: "ist"
url: "/mobilnisite/slovnik/ist/"
type: "slovnik"
title: "IST – Immediate Service Termination"
date: 2025-01-01
abbr: "IST"
fullName: "Immediate Service Termination"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ist/"
summary: "Immediate Service Termination (IST) je síťová funkce umožňující okamžité a vynucené ukončení služeb účastníka, typicky z administrativních, bezpečnostních nebo fakturačních důvodů. Jedná se o klíčový"
---

IST je síťová funkce umožňující okamžité a vynucené ukončení služeb účastníka z administrativních, bezpečnostních nebo fakturačních důvodů.

## Popis

Immediate Service Termination (IST) je standardizovaná síťová funkce definovaná ve specifikacích 3GPP, která poskytuje mechanismus pro okamžité a úplné přerušení všech telekomunikačních služeb pro konkrétního účastníka na straně operátora. Proces je iniciován operátorem, obvykle prostřednictvím administrativního nebo operačního podpůrného systému ([OSS](/mobilnisite/slovnik/oss/)), který odešle příkaz příslušným síťovým uzlům, jako je Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Po přijetí příkazu IST tyto základní síťové entity okamžitě aktualizují profil účastníka do stavu 'blokováno' nebo 'ukončeno', čímž zabrání jakémukoliv novému zřizování relací, volání nebo příjmu hovorů. Stávající aktivní relace, jako hlasové hovory nebo datová připojení, jsou také vynuceně uvolněny. Signalizace pro IST je navržena jako vysokoprioritní a neodkladná, aby bylo zajištěno co nejrychlejší provedení ukončení v celé síti, často během několika sekund. Mezi klíčové zapojené komponenty patří HLR/HSS pro správu dat účastníka, Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) pro řízení relací a Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) nebo Packet Data Network Gateway (PGW) pro správu datových relací. IST hraje zásadní roli v síťových operacích, reakci na bezpečnostní incidenty a plnění požadavků zákonného odposlechu nebo regulatorních požadavků tím, že poskytuje jednoznačné a okamžité přerušení služby.

## K čemu slouží

IST byl vytvořen pro uspokojení kritické potřeby provozovatelů sítí mít okamžitou a definitivní metodu pro pozastavení přístupu účastníka ke všem síťovým službám. Před jeho standardizací mohly mechanismy pozastavení služeb zahrnovat manuální procesy nebo pomalejší hromadné aktualizace, které byly nedostatečné pro naléhavé scénáře, jako je podezření na podvod, bezpečnostní narušení, nezaplacení faktur vedoucí ke zneužívání služeb nebo plnění požadavků orgánů činných v trestním řízení. Tato technologie řeší problém opožděné reakce v situacích s vysokými riziky, kde pokračující přístup k síti mohl vést k finanční ztrátě, bezpečnostním kompromisům nebo právním odpovědnostem. Jeho vznik byl motivován rostoucí komplexitou mobilních sítí a potřebou robustních, standardizovaných operačních postupů, které lze spolehlivě provádět napříč zařízeními různých dodavatelů a generacemi sítí, od okruhově přepínaných domén 2G/3G až po paketově přepínané jádro 4G/5G.

## Klíčové vlastnosti

- Vynucené a okamžité ukončení všech aktivních hlasových a datových relací
- Administrativní spuštění z OSS/BSS systémů operátora
- Aktualizace stavu účastníka na 'blokováno' v HLR/HSS
- Vysokoprioritní signalizace pro zajištění rychlého provedení v celé síti
- Použitelnost napříč okruhově přepínanými a paketově přepínanými doménami
- Podpora scénářů pro plnění zákonných a regulatorních požadavků

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TS 22.031** (Rel-19) — Fraud Information Gathering System (FIGS) Stage 1
- **TS 22.032** (Rel-19) — Immediate Service Termination (IST) Service
- **TS 23.035** (Rel-19) — Immediate Service Termination (IST) Stage 2
- **TS 41.031** (Rel-19) — Fraud Information Gathering System (FIGS) Requirements

---

📖 **Anglický originál a plná specifikace:** [IST na 3GPP Explorer](https://3gpp-explorer.com/glossary/ist/)
