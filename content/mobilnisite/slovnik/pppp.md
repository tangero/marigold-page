---
slug: "pppp"
url: "/mobilnisite/slovnik/pppp/"
type: "slovnik"
title: "PPPP – ProSe Per-Packet Priority"
date: 2025-01-01
abbr: "PPPP"
fullName: "ProSe Per-Packet Priority"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pppp/"
summary: "ProSe Per-Packet Priority je QoS mechanismus pro služby na základě blízkosti (ProSe), který přiděluje jednotlivým datovým paketům prioritu pro komunikaci mezi zařízeními (D2D). Zajišťuje, že kritická"
---

PPPP je QoS mechanismus ProSe, který přiděluje jednotlivým D2D paketům prioritu, aby zajistil, že kritická data (např. provoz pro veřejnou bezpečnost) jsou přenesena s vyšší precedencí než méně urgentní provoz na sidelinku.

## Popis

[ProSe](/mobilnisite/slovnik/prose/) Per-Packet Priority (PPPP) je základní parametr kvality služeb (QoS) definovaný v architektuře 3GPP pro služby na základě blízkosti (ProSe), konkrétně pro sidelinkovou komunikaci (např. na rozhraní PC5). Funguje tak, že přiděluje každému jednotlivému datovému paketu generovanému ProSe-enabled uživatelským zařízením (UE) pro přímou komunikaci s jiným UE číselnou hodnotu priority. Tato hodnota priority je celé číslo, typicky v rozsahu od 1 (nejvyšší priorita) do 8 (nejnižší priorita) podle příslušných specifikací, a je zahrnuta v protokolové datové jednotce paketu.

Hodnota PPPP je klíčovým vstupem pro procedury plánování a výběru prostředků na Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) vrstvě na sidelinku. V obou režimách alokace prostředků – řízené síťou (mode 1) a autonomní na UE (mode 2) – PPPP ovlivňuje, jak UE soutěží o a využívá sidelinkové prostředky. Paket s vyšší prioritou (nižší číslo PPPP) bude naplánován k přenosu před pakety s nižší prioritou. Toto ovlivňuje proces prioritizace logických kanálů, reportování stavu bufferu a výběr příslušného fondu prostředků nakonfigurovaného pro daný rozsah priorit. Síť může předkonfigurovat fondy prostředků, které jsou mapované na specifické PPPP úrovně, což zajistí, že provoz s vysokou prioritou využívá prostředky s příznivějšími charakteristikami, jako nižší latence nebo vyšší spolehlivost.

Architektonicky je PPPP asociované s profilem ProSe Per-Packet Priority Profile, který je nakonfigurován v UE, často prostřednictvím provisioning nebo policy control. Aplikační vrstva nebo ProSe funkce v UE přiděluje PPPP na základě charakteru služby (např. hlas, video nebo data pro veřejnou bezpečnost). Tento mechanismus je oddělený od tradiční QoS na základě EPS bearerů, protože sidelinková komunikace může probíhat mimo dosah síťového pokrytí. Role PPPP je kritická při zvládání kongescí v hustých [D2D](/mobilnisite/slovnik/d2d/) scénářích, jako operace pro veřejnou bezpečnost nebo vozidlové platooning ([V2X](/mobilnisite/slovnik/v2x/)), kde zajistí, že životně kritické alerty nebo řídicí zprávy nejsou zdrženy méně důležitým datovým provozem na pozadí.

## K čemu slouží

PPPP bylo zavedeno, aby řešilo specifické QoS nároky přímé komunikace mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)), které tradiční QoS modely v mobilních sítích (na základě EPS bearerů mezi UE a síťou) nemohly adekvátně podporovat. Před [ProSe](/mobilnisite/slovnik/prose/) bylo QoS řízeno end-to-end prostřednictvím core networku. Pro sidelinkovou komunikaci, zejména mimo pokrytí nebo na jeho hranici, byl nezbytný distribuovaný mechanismus prioritizace na jednotlivé pakety. Primární problém, který řeší, je deterministická prioritizace provozu v decentralizovaném radio prostředí, kde více UE soutěží o sdílený fond sidelinkových prostředků.

Jeho vytvoření bylo silně motivováno nároky komunikace pro veřejnou bezpečnost a kritické mise, které byly klíčovým hnacím motorem standardizace ProSe. V katastrofických scénářích, kdy síťová infrastruktura může být narušena, potřebují první respondenti používající D2D režimy garantovaný přenos pro emergency alerty a řídicí komunikaci. PPPP toto poskytuje tím, že zajistí, že 'lifeline' hlasový paket od hasiče je vždy považován za důležitější než neurgentní datová update z jiného zařízení. Podporuje také evoluci [V2X](/mobilnisite/slovnik/v2x/) služeb, kde zpráva o brzdění od auta musí mít absolutní prioritu nad periodickou beacon zprávou, aby se zabránilo nehodám. PPPP tedy umožňuje diferenciaci služeb na čistě peer-to-peer radio linku, což byla schopnost, která nebyla dostupná v LTE před Release 13.

## Klíčové vlastnosti

- Prioritizace na jednotlivé pakety pro QoS na sidelinku (rozhraní PC5)
- 8úrovňová škála priority (1=nejvyšší, 8=nejnižší) pro diferenciaci provozu
- Přímý vliv na plánování na MAC vrstvě a výběr prostředků v UE
- Mapování na specifické fondy sidelinkových prostředků pro izolaci a garantovaný výkon
- Funguje v scénářích s pokrytím síťou (mode 1) i mimo pokrytí (mode, 2)
- Nezávislé na tradiční QoS na základě EPS bearerů, uzpůsobené pro přímou D2D komunikaci

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 24.385** (Rel-19) — V2X Communication Provisioning Management Object
- **TS 24.386** (Rel-19) — V2X Communication Protocols and Procedures
- **TS 24.481** (Rel-19) — Mission Critical Services (MCS) group management
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR

---

📖 **Anglický originál a plná specifikace:** [PPPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pppp/)
