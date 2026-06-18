---
slug: "nt-rlc"
url: "/mobilnisite/slovnik/nt-rlc/"
type: "slovnik"
title: "NT-RLC – RLC Non-Transparent Mode"
date: 2020-01-01
abbr: "NT-RLC"
fullName: "RLC Non-Transparent Mode"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nt-rlc/"
summary: "Provozní režim protokolu řízení rádiového spoje (RLC) v sítích GSM/EDGE, kde vrstva RLC poskytuje omezenou opravu chyb, primárně pro potvrzovaný přenos dat. Je navržen pro služby ne-reálného času, kde"
---

NT-RLC je provozní režim vrstvy RLC v sítích GSM/EDGE, který poskytuje omezenou opravu chyb pro potvrzovaný přenos dat v ne-reálném čase, vyvažuje spolehlivost a složitost tím, že připouští přijatelné zpoždění pro opakované vysílání.

## Popis

Netransparentní režim [RLC](/mobilnisite/slovnik/rlc/) (NT-RLC) je jeden ze tří provozních režimů vrstvy řízení rádiového spoje v rádiových přístupových sítích GSM a [EDGE](/mobilnisite/slovnik/edge/), standardizovaný v 3GPP TS 44.060. Vrstva RLC se nachází nad vrstvou řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) a je zodpovědná za segmentaci, zpětné sestavení a doručování datových jednotek ve správném pořadí, stejně jako za opravu chyb pomocí opakovaného vysílání. NT-RLC se konkrétně používá pro služby paketových dat, především pro [GPRS](/mobilnisite/slovnik/gprs/) a EDGE.

V NT-RLC protokol pracuje v potvrzovaném režimu ([AM](/mobilnisite/slovnik/am/)). To znamená, že implementuje mechanismus automatického požadavku na opakování ([ARQ](/mobilnisite/slovnik/arq/)) pro zajištění spolehlivého doručení dat. Když vysílající entita (např. [BSS](/mobilnisite/slovnik/bss/)) odešle blok dat, čeká na potvrzení ([ACK](/mobilnisite/slovnik/ack/)) od přijímače. Pokud není potvrzení přijato v rámci časového limitu, nebo je přijato záporné potvrzení (NACK), je blok znovu vyslán. Tento proces pokračuje až do úspěšného doručení nebo do dosažení maximálního limitu opakování. Hlavička RLC obsahuje pořadová čísla, řídicí bity pro dotazování a stavové informace pro správu tohoto ARQ procesu.

Architektura zahrnuje entity RLC jak na mobilní stanici (MS), tak v podsystému základnové stanice (BSS). Tyto entity spravují vysílací a přijímací okna, udržují stavové proměnné pro pořadová čísla a zajišťují vytváření a interpretaci hlaviček bloků RLC/MAC. NT-RLC spolupracuje s nadřazenou vrstvou řízení logického spoje (LLC), která poskytuje koncové spolehlivosti mezi MS a SGSN. Spolehlivost NT-RLC je tedy po jednotlivých skocích (přes rozhraní vzduchu), zatímco LLC poskytuje dodatečné zabezpečení a potvrzování na koncích.

Jeho úlohou je poskytnout spolehlivý rádiový přenos pro služby paketově přepínaných dat přes rozhraní Um. Maskuje chyby vlastní bezdrátovému médiu před vyššími vrstvami, zajišťuje, že datové pakety jsou doručeny správně a ve správném pořadí přes rádiový spoj. To je klíčové pro aplikace jako e-mail, prohlížení webu a přenos souborů přes GPRS/EDGE, kde je důležitá integrita dat, ale nejsou vyžadována striktní časová omezení reálného času. Představuje složitější, ale robustnější alternativu k transparentnímu režimu (používanému pro hlas) a nepotvrzovanému režimu.

## K čemu slouží

NT-RLC byl vyvinut pro podporu zavedení služeb paketově přepínaných dat v sítích GSM, konkrétně služby General Packet Radio Service (GPRS) a později Enhanced Data rates for GSM Evolution (EDGE). Před GPRS GSM primárně podporovalo okruhově přepínaný hlas a nízkorychlostní data pomocí transparentního režimu RLC, který nabízel dopřednou opravu chyb, ale žádné opakované vysílání, což jej činilo nevhodným pro spolehlivý přenos datových paketů, kde by chyby bitů mohly poškodit celé datové bloky.

Problém, který řešil, bylo, jak poskytnout dostatečně spolehlivý datový spoj přes náchylný k chybám bezdrátový kanál pro aplikace ne-reálného času. Transparentní režim byl pro data nevhodný, protože nemohl obnovit ztracené nebo poškozené rámce. NT-RLC s jeho ARQ mechanismem byl vytvořen, aby tuto mezeru zaplnil. Byl motivován potřebou umožnit efektivní služby založené na IP v mobilních sítích, což vyžadovalo spojový protokol, který mohl garantovat doručení bez trvalé alokace prostředků okruhově přepínaného spojení.

Odstranil omezení existujících režimů zavedením schopnosti selektivního opakovaného vysílání. To umožnilo síti vyměnit zvýšenou latenci (způsobenou opakovaným vysíláním) za dramaticky zlepšenou spolehlivost, což bylo přijatelné pro rané aplikace mobilních dat. NT-RLC se stal základem pro přerušovaný, efektivní přenos paketových dat, který definoval GPRS a EDGE, a umožnil tak první rozšířené zkušenosti s mobilním internetem.

## Klíčové vlastnosti

- Pracuje v potvrzovaném režimu RLC (AM) s ARQ
- Poskytuje spolehlivý přenos dat pomocí selektivního opakovaného vysílání
- Používá pořadová čísla pro doručování ve správném pořadí a detekci duplicit
- Obsahuje mechanismus dotazování pro stavové hlášení přijímače
- Spravuje vysílací a přijímací okna pro řízení toku
- Spolupracuje s vrstvou LLC pro koncovou spolehlivost

## Související pojmy

- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [ARQ – Automatic Repeat Request](/mobilnisite/slovnik/arq/)
- [LLC – SM Low Layer Source Specific Multicast (address)](/mobilnisite/slovnik/llc/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [NT-RLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/nt-rlc/)
