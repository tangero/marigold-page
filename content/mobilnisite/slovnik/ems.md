---
slug: "ems"
url: "/mobilnisite/slovnik/ems/"
type: "slovnik"
title: "EMS – Enhanced Messaging Service"
date: 2025-01-01
abbr: "EMS"
fullName: "Enhanced Messaging Service"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ems/"
summary: "Standardizovaná služba zasílání zpráv v sítích 3GPP, která jde nad rámec základní SMS. Umožňuje výměnu rozsáhlého obsahu, jako jsou obrázky, zvuk, video a formátovaný text, mezi uživateli a aplikacemi"
---

EMS je rozšířená, standardizovaná služba zasílání zpráv podle 3GPP, která rozšiřuje základní SMS o možnost výměny multimediálního obsahu, jako jsou obrázky, zvuk, video a formátovaný text.

## Popis

Enhanced Messaging Service (EMS) je standardizovaná služba 3GPP, která definuje možnosti pro odesílání a přijímání zpráv obsahujících multimediální obsah přes mobilní sítě. Funguje jako rozšíření služby Short Message Service ([SMS](/mobilnisite/slovnik/sms/)), využívá stejné základní transportní mechanismy, ale rozšiřuje User Data Header ([UDH](/mobilnisite/slovnik/udh/)) a datovou část pro podporu bohatších typů médií. Architektura zahrnuje mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) pro vytváření a zobrazování zpráv, prvky jádra sítě (jako [MSC](/mobilnisite/slovnik/msc/), [SMSC](/mobilnisite/slovnik/smsc/)) pro směrování a případně externí servery ([MMS](/mobilnisite/slovnik/mms/) Relay/Server) pro pokročilejší zpracování MMS. Zprávy EMS jsou strukturovány jako zřetězené SMS zprávy se specifickými hlavičkami označujícími přítomnost formátovaného textu, obrázků, melodií nebo animací.

Technicky EMS funguje tak, že kóduje mediální objekty do definovaného binárního formátu a zabalí je do transportního protokolu SMS. Standard definuje sadu předdefinovaných mediálních objektů (např. černobílé obrázky, vyzváněcí tóny ve formátu iMelody) a jejich kódování. Když uživatel odešle zprávu EMS, software mobilního zařízení sestaví obsah, použije správné kódování EMS a odešle jej jako jedno nebo více SMS podání do sítě. Přijímající zařízení po detekci specifických indikátorů EMS v UDH zprávu znovu sestaví a interpretuje mediální prvky pro zobrazení nebo přehrání.

Její role v síti je jako základní vrstva služby zasílání zpráv. Ačkoli byla z pohledu spotřebitele z velké části nahrazena plnohodnotnou službou Multimedia Messaging Service (MMS), specifikace EMS poskytly klíčový evoluční krok a technický rámec. Mezi klíčové komponenty definované ve specifikacích EMS patří struktura zprávy, definice mediálních objektů a aplikační protokoly pro podání, doručení a oznámení. Zajišťovala interoperabilitu mezi zařízeními a sítěmi různých výrobců pro základní multimediální zprávy předtím, než se všudypřítomným stal plně IP-based MMS.

## K čemu slouží

EMS byla vytvořena, aby řešila významné omezení [SMS](/mobilnisite/slovnik/sms/), která byla omezena na prostý text velmi omezené délky (160 znaků). Hnací motivací bylo umožnit expresivnější a poutavější komunikaci přímo z mobilních telefonů podporou základních multimédií. Tím byla uspokojena rostoucí uživatelská poptávka po sdílení více než jen textu, jako jsou jednoduchá grafika (např. emotikony, obrázky) a vyzváněcí tóny, což bylo populární na konci 90. let a počátku 21. století.

Historicky existovala proprietární řešení specifická pro výrobce pro odesílání obrázků nebo zvuků, ale postrádala interoperabilitu. EMS poskytla standardizovaný, interoperabilní rámec v rámci ekosystému 3GPP. Vyřešila problém fragmentace definováním společné metody kódování a přenosu, kterou mohly podporovat všechny kompatibilní sítě a zařízení, což zajišťovalo, že uživatel může odeslat obrázkovou zprávu jakémukoli jinému uživateli na jakékoli kompatibilní síti.

Vytvoření EMS bylo strategickým krokem k plnohodnotné multimediální službě zasílání zpráv ([MMS](/mobilnisite/slovnik/mms/)). Umožnilo operátorům a výrobcům mobilních zařízení zavádět bohatší funkce zasílání zpráv postupně, s využitím stávající, všudypřítomné a spolehlivé infrastruktury SMS. To snížilo vstupní bariéru pro multimediální zprávy a připravilo cestu pro přijetí trhem a technickou evoluci, která vyvrcholila standardy IP-based MMS.

## Klíčové vlastnosti

- Podpora formátovaného textu (tučné, kurzíva, zarovnání)
- Schopnost zahrnout předdefinované bitmapové obrázky (např. emotikony, obrázky)
- Podpora předdefinovaných zvukových melodií (formát iMelody)
- Podpora animací pro jednoduché sekvence bitmap
- Zřetězení zpráv pro obsah větší než jeden segment SMS
- Standardizovaná rozšíření User Data Header (UDH) pro identifikaci médií

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TS 22.242** (Rel-19) — DRM Service Requirements
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.822** (Rel-9) — EMS Maintenance Functions Study over Itf-N
- **TS 32.826** (Rel-10) — Study on Energy Savings Management in LTE/SAE Networks
- **TS 32.854** (Rel-11) — FMC Federated Network Information Model
- **TS 32.861** (Rel-13) — IRP Subset Selection for Network Management
- **TS 32.880** (Rel-15) — Simplified Itf-N IRP Solution Sets Study
- **TR 38.882** (Rel-18) — Technical Report on UE Location Service

---

📖 **Anglický originál a plná specifikace:** [EMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ems/)
