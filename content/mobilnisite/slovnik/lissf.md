---
slug: "lissf"
url: "/mobilnisite/slovnik/lissf/"
type: "slovnik"
title: "LISSF – Lawful Interception State Storage Function"
date: 2025-01-01
abbr: "LISSF"
fullName: "Lawful Interception State Storage Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lissf/"
summary: "Standardizovaná funkce pro ukládání a správu stavových informací vyžadovaných pro operace zákonného odposlechu (LI) v sítích 3GPP. Zajišťuje, že data související s odposlechem, jako jsou identity cílů"
---

LISSF je standardizovaná funkce 3GPP, která trvale ukládá a spravuje stavové informace, jako jsou identity cílů a aktivní žádosti o odposlech, aby podporovala operace zákonného odposlechu a soulad s předpisy v celé síti.

## Popis

Funkce pro ukládání stavu zákonného odposlechu (LISSF) je klíčovou součástí architektury zákonného odposlechu ([LI](/mobilnisite/slovnik/li/)) v rámci 3GPP, konkrétně definovanou od vydání 16. Funguje jako centralizované úložiště stavu, které odděluje ukládání stavových informací souvisejících s LI od jednotlivých síťových funkcí, které odposlech provádějí, jako je Funkce zákonného odposlechu ([LIF](/mobilnisite/slovnik/lif/)) nebo různé Aplikační funkce ([AF](/mobilnisite/slovnik/af/)). Toto architektonické oddělení je klíčovým principem moderního, cloud-nativního návrhu sítě. LISSF ukládá kritická data včetně identit cílů podléhajících odposlechu (např. [IMSI](/mobilnisite/slovnik/imsi/), SUPI, [MSISDN](/mobilnisite/slovnik/msisdn/)), podrobností o povolených soudních příkazech k odposlechu, aktuálního stavu aktivace odposlechů a přidružených metadat potřebných pro korelaci relací a doručování dat do monitorovacího zařízení orgánů činných v trestním řízení ([LEMF](/mobilnisite/slovnik/lemf/)).

Z funkční perspektivy poskytuje LISSF standardizovanou službu správy stavu ostatním entitám LI. Když je přijato nové povolení k zákonnému odposlechu, příslušná administrativní funkce (např. Administrativní funkce, [ADMF](/mobilnisite/slovnik/admf/)) zapíše informace o cíli a soudním příkazu do LISSF. Následně síťové funkce, jako je Přístupová síť, Síť jádra nebo platformy pro poskytování služeb, dotazují LISSF, aby zjistily, zda konkrétní uživatelská relace nebo datová jednotka služby podléhá odposlechu. Tento mechanismus dotaz-odpověď umožňuje odposlouchávacím funkcím aplikovat správná pravidla odposlechu, aniž by samy musely udržovat složitý, distribuovaný stav. LISSF zajišťuje konzistenci a trvalost tohoto stavu, což je zásadní pro kontinuitu odposlechu během mobility uživatele, předávání hovorů nebo výpadků síťových funkcí.

Její role je nedílnou součástí dosažení spolehlivého a kompatibilního LI v systému 5G (5GS) a vyvinutých sítích. Tím, že poskytuje jediný zdroj pravdy pro stav odposlechu, zjednodušuje implementaci schopností LI v disagregovaném a virtualizovaném síťovém prostředí. Podporuje rozhraní definovaná v 3GPP TS 33.127 a TS 33.128, čímž zajišťuje interoperabilitu mezi implementacemi různých dodavatelů. LISSF je základním prvkem pro umožnění zákonného přístupu způsobem, který je v souladu s principy bezstavovosti síťových funkcí, kde jsou výpočetní prostředky (odposlouchávací funkce) a stav (LISSF) odděleny za účelem lepší škálovatelnosti, odolnosti a provozní flexibility.

## K čemu slouží

LISSF byla zavedena, aby řešila výzvy implementace zákonného odposlechu v moderních, cloud-nativních sítích 5G založených na architekturách typu service-based (SBA). Předchozí vydání 3GPP spoléhala na integrovanou správu stavu [LI](/mobilnisite/slovnik/li/) v rámci jednotlivých síťových prvků, což se v disagregovaném prostředí s bezstavovými síťovými funkcemi stalo složitým a neefektivním. Posun směrem k mikroslužbám a kontejnerizovaným funkcím, kde mohou být instance dynamicky vytvářeny a ničeny, si vyžádal centralizovaný, externí mechanismus pro ukládání stavu, aby se zajistilo, že relace odposlechu nebudou ztraceny během škálování nebo výpadků.

Její vytvoření bylo motivováno potřebou standardizovaného, odolného a škálovatelného přístupu ke správě stavu LI. Bez LISSF by každá síťová funkce musela implementovat vlastní trvalé úložiště a synchronizační mechanismy pro data LI, což by vedlo k duplikaci, potenciálním nekonzistencím a zvýšené režii vývoje. LISSF to řeší poskytnutím společné služby, která zjednodušuje logiku LI uvnitř odposlouchávacích funkcí a zajišťuje, že stav aktivního odposlechu je udržován nezávisle na životním cyklu jakékoli konkrétní instance síťové funkce. To je klíčové pro splnění regulačních povinností, které vyžadují spolehlivé a nepřerušované schopnosti odposlechu, a to i když se základní síťová infrastruktura stává více softwarově definovanou a elastickou.

## Klíčové vlastnosti

- Centralizované úložiště pro stav zákonného odposlechu (ID cílů, informace o soudním příkazu, stav aktivace)
- Odděluje trvalost stavu od bezstavových odposlouchávacích síťových funkcí
- Poskytuje standardizované dotazovací rozhraní pro síťové funkce ke kontrole stavu odposlechu
- Zajišťuje kontinuitu odposlechu během mobility uživatele a výpadků síťových funkcí
- Podporuje cloud-nativní principy architektury typu service-based u 5G
- Umožňuje zjednodušenou implementaci a ověřování souladu pro LI

## Definující specifikace

- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [LISSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lissf/)
