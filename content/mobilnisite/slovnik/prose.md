---
slug: "prose"
url: "/mobilnisite/slovnik/prose/"
type: "slovnik"
title: "ProSe – Proximity-based Services"
date: 2026-01-01
abbr: "ProSe"
fullName: "Proximity-based Services"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/prose/"
summary: "Soubor schopností 3GPP, které umožňují zařízením vzájemně se objevovat a komunikovat přímo, když jsou v těsné blízkosti, bez směrování dat přes síťovou infrastrukturu. Podporuje veřejnou bezpečnost, k"
---

ProSe je soubor schopností 3GPP, které umožňují zařízením vzájemně se objevovat a komunikovat přímo, když jsou v těsné blízkosti, bez směrování dat přes síťovou infrastrukturu.

## Popis

Služby založené na blízkosti (ProSe) představují komplexní architekturu 3GPP definovanou v řadě technických specifikací (např. TS 22.278, 23.280, 23.281), která umožňuje přímé objevování zařízení (Device-to-Device, [D2D](/mobilnisite/slovnik/d2d/)) a přímou komunikaci. Umožňuje uživatelskému zařízení (UE), jako jsou chytré telefony nebo IoT zařízení, detekovat přítomnost jiných zařízení s podporou ProSe v těsné geografické blízkosti a navázat přímou datovou cestu, a to buď s využitím licencovaného spektra (pod kontrolou sítě), nebo nezávisle na síťovém pokrytí. Architektura zahrnuje několik klíčových síťových funkcí, včetně funkce ProSe v jádru sítě, která spravuje autorizaci, provisioning a asistenci při objevování, a aplikačního serveru ProSe, který podporuje operace na úrovni služeb.

ProSe funguje prostřednictvím dvou hlavních procedur: přímého objevování ProSe a přímé komunikace ProSe. Při přímém objevování může UE oznamovat svou přítomnost nebo naslouchat oznámením od jiných zařízení s využitím předdefinovaných kódů. To může být síťově asistované, kdy síť pomáhá přiřazovat zdroje pro objevování a ověřovat oprávnění, nebo autonomní, kdy zařízení využívají přednastavené zdroje. Přímá komunikace navazuje datové spojení mezi zařízeními typu jeden k jednomu nebo jeden k mnoha. Pro scénáře v pokrytí přiděluje [E-UTRAN](/mobilnisite/slovnik/e-utran/) nebo NG-RAN rádiové zdroje pro přímý spoj, čímž zajišťuje efektivní využití spektra a minimální rušení s konvenčním buněčným provozem. Pro scénáře mimo pokrytí nebo s částečným pokrytím, jako jsou operace veřejné bezpečnosti, mohou zařízení využívat předem přidělené zdroje k přímé komunikaci a vytvářet tak ad-hoc sítě.

Technologie využívá podkladové rádiové přístupové sítě LTE nebo 5G NR, ale zavádí nová boční rozhraní (např. rozhraní PC5 pro přímou komunikaci mezi UE). Funkce ProSe autentizuje uživatele pro služby ProSe, poskytuje jim potřebné parametry (jako jsou kódy pro objevování nebo konfigurace rádiových zdrojů) a může přeposílat žádosti o objevování. Pro komunikaci datová rovina obchází uživatelskou rovinu jádra sítě, čímž snižuje latenci a zatížení přenosové trasy. ProSe je nedílnou součástí pro umožnění kritických služeb, jako je komunikace pro veřejnou bezpečnost při výpadcích sítě, komerčních aplikací, jako je objevování pro sociální sítě, a vozidlové komunikace (která se později vyvinula ve služby [V2X](/mobilnisite/slovnik/v2x/)), což představuje posun od čistě infrastrukturně centrického k distribuovanějšímu, zařízením centrickému modelu konektivity.

## K čemu slouží

ProSe bylo vytvořeno za účelem řešení několika klíčových omezení tradiční buněčné architektury, kde je veškerá komunikace směrována přes základnové stanice a uzly jádra sítě. Tento model zavádí latenci, spotřebovává zdroje přenosové trasy a zcela selhává, když je síťová infrastruktura poškozena nebo nedostupná. Primární motivací byla podpora komunikace pro veřejnou bezpečnost s misně kritickým významem, kdy si první respondenti potřebují vzájemně komunikovat přímo během katastrof. Před zavedením ProSe se veřejná bezpečnost spoléhala na samostatné, vyhrazené systémy pozemní mobilní rádiové komunikace, kterým chyběly vysoké datové rychlosti a bohaté služby buněčných sítí.

Dalším hnacím účelem bylo umožnit nové komerční a sociální aplikace založené na blízkosti, jako je objevování zařízení pro sociální média, místní sdílení souborů nebo cílená reklama. To vytvořilo příležitosti pro síťové operátory nabízet nové služby a odlehčovat provoz z jádra sítě, čímž se zlepšila celková kapacita a efektivita. Technologie také položila základy pro pokročilejší paradigma přímé komunikace, nejvýznamněji komunikaci Vozidlo-se-vším ([V2X](/mobilnisite/slovnik/v2x/)), která je klíčová pro autonomní řízení a inteligentní dopravní systémy.

Zavedení ve vydání 14 představovalo významný vývoj oproti dřívějším konceptům [D2D](/mobilnisite/slovnik/d2d/) studovaným ve vydáních 12 a 13, neboť poskytlo plně standardizovanou servisní vrstvu a síťovou architekturu. Vyřešilo problém, jak integrovat přímou komunikaci zařízení do prostředí licencovaného spektra spravovaného operátorem, a zajistit tak kontrolu, zabezpečení a fakturační schopnosti. ProSe tak překlenuje propast mezi spolehlivostí a řiditelností buněčných sítí a flexibilitou a odolností ad-hoc peer-to-peer sítí.

## Klíčové vlastnosti

- Přímá komunikace zařízení (D2D) přes rozhraní PC5
- Objevování na základě blízkosti (síťově asistovaný a autonomní režim)
- Provoz ve scénářích v pokrytí, mimo pokrytí a s částečným pokrytím
- Podpora aplikací pro veřejnou bezpečnost a komerčních aplikací
- Síťově řízené přidělování zdrojů pro správu rušení
- Integrace s bočním přenosem LTE a 5G NR

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 22.278** (Rel-19) — Evolved Packet System Service Requirements
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.281** (Rel-20) — MCVideo Functional Architecture and Flows
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 38.423** (Rel-19) — Xn Application Protocol (XnAP) specification

---

📖 **Anglický originál a plná specifikace:** [ProSe na 3GPP Explorer](https://3gpp-explorer.com/glossary/prose/)
