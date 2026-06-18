---
slug: "smt"
url: "/mobilnisite/slovnik/smt/"
type: "slovnik"
title: "SMT – Short Message Terminal"
date: 2025-01-01
abbr: "SMT"
fullName: "Short Message Terminal"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/smt/"
summary: "Funkční entita v architektuře 3GPP, která generuje, ukončuje a zpracovává provoz služby krátkých textových zpráv (SMS). Jedná se o klíčovou komponentu pro zajištění služeb textového zasílání zpráv v m"
---

SMT je funkční entita v architektuře 3GPP, která generuje, ukončuje a zpracovává SMS provoz pro mobilní sítě.

## Popis

Short Message Terminal (SMT) je síťový prvek definovaný v rámci servisní architektury 3GPP pro službu krátkých textových zpráv ([SMS](/mobilnisite/slovnik/sms/)). Funguje jako koncový bod pro zpracování SMS zpráv. V architektonickém modelu může SMT sídlit v uživatelském zařízení (UE), síťovém serveru nebo externím aplikačním serveru. Jeho primární funkcí je odeslat (vygenerovat) nebo přijmout (ukončit) krátké zprávy. Při generování zprávy SMT formátuje obsah zprávy a řídicí informace do protokolové datové jednotky vyhovující standardům jako 3GPP TS 23.040. Následně komunikuje se střediskem služby krátkých zpráv (SM-SC) prostřednictvím příslušných servisních rozhraní, jako je cesta Mobile Originated ([MO](/mobilnisite/slovnik/mo/)). Pro ukončení zprávy SMT přijímá zprávu od SM-SC, zpracovává relevantní instrukce (jako doba platnosti nebo indikátory priority) a předává zprávu koncovému uživateli nebo aplikaci. SMT je zodpovědný za protokolovou adaptaci, zajišťuje, aby zpráva vyhovovala požadavkům transportní vrstvy, což může zahrnovat interakce s podsoubory správy mobility ([MM](/mobilnisite/slovnik/mm/)) a správy spojení ([CM](/mobilnisite/slovnik/cm/)) v UE nebo síti. Dále zvládá lokální funkce, jako je ukládání zpráv, pokud je příjemce dočasně nedostupný, a generuje hlášení o doručení. V síťových implementacích, jako je SMS brána nebo [IP-SM-GW](/mobilnisite/slovnik/ip-sm-gw/), SMT usnadňuje spolupráci s jinými zprávovacími systémy a hraje klíčovou roli v řetězci od konce ke konci pro doručování SMS.

## K čemu slouží

SMT byl zaveden za účelem standardizace funkčního chování koncových bodů v ekosystému [SMS](/mobilnisite/slovnik/sms/), což je základní služba 2G (GSM) a následujících mobilních generací. Před formální standardizací mohly být implementace SMS proprietární, což vedlo k problémům s interoperabilitou mezi různými terminály a síťovým vybavením. Definice SMT vytvořila jasný architektonický referenční bod, který odděluje servisní logiku od transportních mechanismů. To umožnilo konzistentní implementaci funkcí SMS napříč různými zařízeními a síťovými infrastrukturami a zajišťuje spolehlivé a všudypřítomné textové zasílání zpráv. Specifikace SMT vyřešila problém, jak má zprávová entita (ať už telefon, server nebo stroj) správně formátovat, odesílat a potvrzovat zprávy v rámci složitého signalizačního rámce mobilní sítě. Jeho vznik byl motivován explozivním růstem využívání SMS, což si vyžádalo robustní, škálovatelný a dobře definovaný model pro podporu jak komunikace mezi osobami, tak mezi aplikací a osobou, což se stalo klíčovým pro uživatelskou komunikaci a nadstavbové služby.

## Klíčové vlastnosti

- Generuje a ukončuje SMS zprávy podle protokolů 3GPP
- Komunikuje se střediskem služby krátkých zpráv (SM-SC) pro směrování zpráv
- Zajišťuje formátování zpráv a adaptaci na protokoly transportní vrstvy
- Spravuje odesílání zpráv a hlášení o doručení
- Podporuje ukládání zpráv pro pozdější doručení, pokud je příjemce nedostupný
- Může být implementován v uživatelském zařízení (UE), síťových serverech nebo externích aplikačních platformách

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [IP-SM-GW – IP Short Message Gateway](/mobilnisite/slovnik/ip-sm-gw/)

## Definující specifikace

- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download

---

📖 **Anglický originál a plná specifikace:** [SMT na 3GPP Explorer](https://3gpp-explorer.com/glossary/smt/)
