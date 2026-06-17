---
slug: "nl"
url: "/mobilnisite/slovnik/nl/"
type: "slovnik"
title: "NL – No support of multiple Languages"
date: 2025-01-01
abbr: "NL"
fullName: "No support of multiple Languages"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nl/"
summary: "Konfigurační parametr v rámci správy sítě 3GPP, který udává, že síťový prvek nebo služba nepodporuje více lidských jazyků pro své uživatelské rozhraní nebo oznámení. Je klíčový pro definování schopnos"
---

NL je parametr správy sítě 3GPP, který udává, že síťový prvek nebo služba nepodporuje více jazyků pro své uživatelské rozhraní nebo oznámení.

## Popis

V rámci architektury správy sítě 3GPP je NL (No support of multiple Languages – bez podpory více jazyků) specifický atribut schopností definovaný v třídách spravovaných objektů ([MO](/mobilnisite/slovnik/mo/)). Jedná se o booleovský nebo výčtový parametr, který explicitně uvádí, zda spravovaná síťová funkce, jako je NodeB, eNodeB, gNB nebo prvek jádra sítě, může poskytovat své rozhraní pro správu, popisy alarmů, výkonnostní měření nebo konfigurační data ve více než jednom lidském jazyce. Pokud je nastaven na hodnotu 'true' nebo její ekvivalent, znamená to, že prvek podporuje pouze jeden předdefinovaný jazyk (často angličtinu jako výchozí technický jazyk). Tento parametr je nedílnou součástí konceptu internacionalizace a lokalizace v rámci modelu správy FCAPS (Fault, Configuration, Accounting, Performance, and Security – správa poruch, konfigurace, účtování, výkonu a zabezpečení).

Parametr je definován v řadě technických specifikací 3GPP (TS), především v rámci série 32 (Telecommunication management – správa telekomunikací). Tyto specifikace, jako jsou TS 32.305 (Performance Management – správa výkonu), TS 32.371 (Generic Network Resource Model – obecný model síťových zdrojů) a TS 32.415 (Performance measurements Evolved Universal Terrestrial Radio Access Network – výkonnostní měření Evolved UTRAN), detailně popisují informační službu ([IS](/mobilnisite/slovnik/is/)) a přidružený model spravovaných objektů. V tomto modelu je NL atributem konkrétních tříd MO, které reprezentují spravovatelné zdroje. Jeho hodnota je zpřístupněna řídicímu systému, typicky systému pro podporu provozu ([OSS](/mobilnisite/slovnik/oss/)) nebo systému správy prvků ([EMS](/mobilnisite/slovnik/ems/)), prostřednictvím rozhraní Itf-N nebo jiných rozhraní pro správu.

Z provozní perspektivy parametr NL řídí chování řídicího systému. Pokud OSS zjistí, že síťový prvek má nastaven NL, nepokusí se u tohoto prvku vyžadovat lokalizované řetězce ani přepínat jazykový kontext. Tím se zjednodušuje datový model správy a snižuje se složitost OSS při obsluze prvků, které nevyžadují vícejazyčnou podporu. To je obzvláště relevantní pro prvky s minimálním přímým rozhraním člověk-stroj ([HMI](/mobilnisite/slovnik/hmi/)), kde je správa primárně mezi stroji (M2M) s použitím standardizovaných, na jazyku nezávislých identifikátorů objektů a hodnot.

Role NL se rozšiřuje i na oznámení a hlášení alarmů, jak je definováno ve specifikacích jako TS 32.111 (Fault Management – správa poruch) a TS 32.332 (Alarm Integration Reference Point – referenční bod integrace alarmů). Texty alarmů a další informace čitelné pro člověka, generované prvkem s povoleným NL, budou v jediném jazyce. Tím je zajištěna konzistence pro operátory sítě a vyhnutí se složitosti správy vícejazyčných knihoven alarmů pro jednoduché nebo starší síťové komponenty. Jedná se o základní atribut pro zajištění předvídatelného a spravovatelného chování systému napříč rozsáhlými sítěmi s více dodavateli.

## K čemu slouží

Parametr NL byl zaveden, aby formálně a jednoznačně definoval schopnosti lokalizace spravovaného síťového prvku v rámci architektury správy 3GPP. Před takovou formalizací byla jazyková podpora síťových prvků často nedokumentovanou vlastností nebo vlastností specifickou pro dodavatele, což vedlo k nekonzistencím v interakcích systémů pro podporu provozu ([OSS](/mobilnisite/slovnik/oss/)) s různými síťovými prvky. OSS mohlo nesprávně předpokládat vícejazyčnou podporu a pokusit se vyžadovat lokalizované řetězce, což vedlo k chybám nebo přechodu do výchozího, potenciálně matoucího stavu.

Jeho vytvoření bylo motivováno potřebou standardizované správy sítě, což je základní princip 3GPP. Jak sítě rostly na složitosti a začleňovaly zařízení od více dodavatelů, stala se společná architektura správy nezbytnou. Definice atributů jako NL umožňuje automatizované zjišťování a konfiguraci chování systému správy. Řeší problém nepředvídatelného výstupu rozhraní člověk-stroj ([HMI](/mobilnisite/slovnik/hmi/)) a zjednodušuje návrh softwaru OSS tím, že poskytuje jasný, strojově čitelný ukazatel jazykových schopností prvku.

Historicky, jak se správa 3GPP vyvíjela od jednoduché správy prvků k sofistikovanějším modelům síťových zdrojů (NRM) a referenčním bodům integrace ([IRP](/mobilnisite/slovnik/irp/)), se stala nutnou definice takto přesných atributů. NL řeší omezení ad-hoc, implicitní jazykové podpory. Zajišťuje, že u prvků, kde vícejazyčná podpora není vyžadována ani implementována (často z důvodu nákladů, složitosti nebo zastaralosti), zůstanou interakce správy efektivní a bezchybné, zaměřené na standardizovanou, na jazyku neutrální výměnu dat, která je páteří správy FCAPS.

## Klíčové vlastnosti

- Booleovský nebo výčtový atribut v třídách spravovaných objektů (MO)
- Explicitně deklaruje schopnost podpory jediného jazyka
- Definován napříč více specifikacemi správy 3GPP (série 32)
- Ovlivňuje výstup alarmů a oznámení čitelný pro člověka
- Řídí chování OSS/EMS při žádostech o lokalizaci
- Zjednodušuje správu starších a jednoduchých síťových prvků

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 32.111** (Rel-19) — Fault Management Requirements
- **TS 32.305** (Rel-9) — Notification IRP XML Definitions for CM
- **TS 32.306** (Rel-19) — Configuration Management Notification IRP Solution Set
- **TS 32.325** (Rel-9) — Test Management IRP XML Definitions
- **TS 32.326** (Rel-19) — Test Management IRP Solution Set Definitions
- **TS 32.332** (Rel-19) — Notification Log IRP Information Service
- **TS 32.335** (Rel-9) — Notification Log IRP XML Definitions
- **TS 32.336** (Rel-19) — Notification Log IRP Solution Set Definitions
- **TS 32.337** (Rel-9) — Notification Log IRP SOAP Solution Set
- **TS 32.345** (Rel-9) — XML Definitions for File Transfer IRP
- **TS 32.346** (Rel-19) — File Transfer IRP Solution Set Definitions
- **TS 32.355** (Rel-9) — Communication Surveillance IRP XML Definitions
- **TS 32.356** (Rel-19) — Communication Surveillance IRP Solution Set
- **TS 32.365** (Rel-9) — EP IRP XML Definitions for 3GPP Management
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [NL na 3GPP Explorer](https://3gpp-explorer.com/glossary/nl/)
