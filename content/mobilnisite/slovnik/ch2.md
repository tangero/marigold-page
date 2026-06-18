---
slug: "ch2"
url: "/mobilnisite/slovnik/ch2/"
type: "slovnik"
title: "CH2 – CTS Random Challenge Value of the CTS-MS"
date: 2025-01-01
abbr: "CH2"
fullName: "CTS Random Challenge Value of the CTS-MS"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ch2/"
summary: "CH2 je náhodná výzva používaná v systému bezšňůrové telefonie (CTS) pro autentizaci mezi mobilní stanicí (CTS-MS) a sítí. Slouží jako klíčový bezpečnostní parametr v autentizačním mechanismu výzva-odp"
---

CH2 je náhodná výzva (challenge value) používaná v systému bezšňůrové telefonie (Cordless Telephony System, CTS) k ověření mobilní stanice pomocí kryptografického mechanismu výzva-odpověď.

## Popis

CH2 je základní bezpečnostní parametr definovaný ve specifikacích systému bezšňůrové telefonie ([CTS](/mobilnisite/slovnik/cts/)), konkrétně v 3GPP TS 43.020. Funguje jako náhodná výzva generovaná sítí a přenášená k mobilní stanici bezšňůrové telefonie ([CTS-MS](/mobilnisite/slovnik/cts-ms/)) během autentizační procedury. Tato hodnota je zásadní pro implementaci bezpečného autentizačního protokolu výzva-odpověď, kde mobilní stanice musí prokázat znalost sdíleného tajného klíče výpočtem platné odpovědi na základě přijaté výzvy.

Autentizační proces začíná, když síť vygeneruje CH2 jako kryptograficky bezpečné náhodné číslo. Tato výzva je následně odeslána CTS-MS jako součást autentizační výzvy. Po přijetí CH2 použije mobilní stanice tuto hodnotu jako vstup do autentizačního algoritmu ([A3](/mobilnisite/slovnik/a3/)) spolu se sdíleným tajným klíčem (Ki) uloženým v modulu [SIM](/mobilnisite/slovnik/sim/) zařízení nebo v ekvivalentním bezpečnostním prvku. Algoritmus vypočítá podepsanou odpověď ([SRES](/mobilnisite/slovnik/sres/)), která je vrácena síti k ověření.

Síť provede stejný výpočet nezávisle pomocí své kopie sdíleného tajného klíče a původní hodnoty CH2. Porovnáním SRES přijaté od mobilní stanice s vlastní vypočtenou hodnotou může síť zařízení ověřit. Pokud se hodnoty shodují, je prokázáno, že mobilní stanice disponuje správným tajným klíčem, a je jí udělen přístup k CTS službám. Tento mechanismus brání neoprávněnému přístupu, i když jsou autentizační zprávy zachyceny, protože útočník nemůže bez znalosti tajného klíče vypočítat správnou odpověď.

Náhodnost CH2 je klíčová pro bezpečnost systému. Každý pokus o autentizaci by měl použít novou, nepředvídatelnou hodnotu CH2, aby se zabránilo útokům opakováním (replay attacks), při kterých by útočník mohl znovu použít dříve zachycené autentizační výměny. Délka a kvalita generování náhodného čísla přímo ovlivňují odolnost systému vůči kryptografickým útokům. V architektuře CTS funguje CH2 spolu s dalšími bezpečnostními parametry, jako je šifrovací klíč (Kc) a konfigurace autentizačního algoritmu, a poskytuje tak komplexní zabezpečení přístupu pro služby bezšňůrové telefonie.

## K čemu slouží

CH2 byl vytvořen k řešení základního bezpečnostního požadavku na ověřování mobilních zařízení v systémech bezšňůrové telefonie. Před standardizovanými autentizačními mechanismy trpěly rané bezšňůrové telefony významnými bezpečnostními slabinami, včetně snadného odposlechu a neoprávněného přístupu prostřednictvím prostého skenování nebo klonování. Systém výzva-odpověď založený na CH2 poskytl kryptografické řešení pro ověření, že se zařízení pokoušející se připojit k síti k tomu skutečně má oprávnění.

Primární problém, který CH2 řeší, je ověření identity v bezdrátové komunikaci. Vyžadováním, aby mobilní stanice prokázala znalost tajného klíče výpočtem na náhodné výzvě, systém zajišťuje, že k síťovým službám mají přístup pouze zařízení s legitimními přihlašovacími údaji. Tím se zabrání neoprávněným uživatelům v uskutečňování hovorů prostřednictvím systému nebo v přístupu ke službám jiných účastníků. Náhodná povaha CH2 konkrétně řeší útoky opakováním, při kterých by útočník mohl nahrát a znovu vyslat úspěšné autentizační zprávy.

Historicky byl CH2 zaveden jako součást širšího bezpečnostního rámce [CTS](/mobilnisite/slovnik/cts/), který se vyvinul z dřívějších analogových bezšňůrových systémů s minimálním zabezpečením. Implementace autentizace založené na CH2 představovala významný pokrok v zabezpečení bezšňůrové telefonie, přinášejíc autentizační mechanismy na úrovni mobilních sítí do rezidenčních a podnikových bezšňůrových systémů. Řešila omezení předchozích přístupů, které spoléhaly na pevné kódy nebo jednoduché identifikátory, které mohly být snadno zachyceny a replikovány neoprávněnými zařízeními.

## Klíčové vlastnosti

- Generování náhodné výzvy pro autentizaci
- Vstup pro výpočet autentizačního algoritmu A3
- Prevence útoků opakováním prostřednictvím jedinečnosti
- Kryptografické ověření identity zařízení
- Integrace s úložištěm tajného klíče založeným na SIM
- Standardizovaná délka a formát podle specifikací 3GPP

## Související pojmy

- [CTS-MS – Cordless Telephony System - Mobile Station](/mobilnisite/slovnik/cts-ms/)

## Definující specifikace

- **TS 43.020** (Rel-19) — Security Procedures for GSM

---

📖 **Anglický originál a plná specifikace:** [CH2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/ch2/)
