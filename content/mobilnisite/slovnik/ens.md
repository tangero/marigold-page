---
slug: "ens"
url: "/mobilnisite/slovnik/ens/"
type: "slovnik"
title: "ENS – Edge Notification Server"
date: 2026-01-01
abbr: "ENS"
fullName: "Edge Notification Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ens/"
summary: "Edge Notification Server (ENS) je síťová funkce zavedená v 5G-Advanced, která poskytuje obecnou službu doručování notifikací. Umožňuje aplikacím vyžádat si a přijímat asynchronní notifikace o událoste"
---

ENS (Edge Notification Server) je síťová funkce 5G-Advanced, která poskytuje obecnou službu umožňující aplikacím vyžádat si a přijímat asynchronní notifikace o událostech pro skupiny uživatelských zařízení (UE), čímž snižuje potřebu jejich neustálého dotazování (polling).

## Popis

Edge Notification Server (ENS) je servisní schopnost definovaná v rámci architektury systému 5G počínaje 3GPP Release 18. Je součástí širšího rámce Edge Computingu a vystavování služeb (service exposure). Je navržen jako aplikační server, který poskytuje obecný a efektivní mechanismus pro doručování asynchronních notifikací externím aplikačním funkcím (AFs). ENS funguje jako prostředník, který spravuje žádosti o odběr (subscription) od AFs pro konkrétní události související s uživatelskými zařízeními (UEs) a následně zasílá odpovídající notifikace při výskytu těchto událostí, aniž by [AF](/mobilnisite/slovnik/af/) musela síť neustále dotazovat (polling).

Architektonicky je ENS logická funkce, kterou lze nasadit uvnitř operátorovy sítě, potenciálně na jejím okraji (edge) pro nízké zpoždění. Interaguje s funkcí pro vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) 5G jádra (5G Core) nebo přímo s dalšími síťovými funkcemi (NFs), jako je Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), aby si přihlásila odběr a přijímala interní síťové události. Primárním rozhraním pro spotřebitele služby je aplikační rozhraní ENS, přes které AFs zakládají odběry. Žádost o odběr obsahuje parametry jako cílová skupina UE (identifikovaná pomocí [GPSI](/mobilnisite/slovnik/gpsi/), skupinového ID nebo geografické oblasti), typ události (např. změna dosažitelnosti UE, hlášení polohy, ztráta připojení) a cílové callback URI pro notifikace.

Jak to funguje: Jedná se o průběžný proces monitorování a párování. Po přijetí platného odběru ENS přeloží aplikační požadavek do odpovídajícího odběru událostí na síťové úrovni prostřednictvím NEF nebo jiných NFs. Když síť detekuje přihlášenou událost (např. když UE z cílové skupiny vstoupí do určité oblasti), příslušná [NF](/mobilnisite/slovnik/nf/) pošle hlášení o události (event report) do ENS. ENS toto hlášení zpracuje, případně agreguje nebo filtruje události podle kritérií odběru, a nakonec doručí strukturovanou notifikaci (např. ve formátu [JSON](/mobilnisite/slovnik/json/)) na callback URI poskytnuté AF prostřednictvím protokolu [HTTP](/mobilnisite/slovnik/http/)/2. Tento model je vysoce efektivní pro scénáře založené na skupinách, jako je upozornění serveru pro správu vozového parku, když se jakékoli vozidlo z flotily stane dostupné, nebo upozornění sítě pro doručování obsahu (CDN), když kritické množství uživatelů vstoupí do oblasti stadionu.

## K čemu slouží

ENS byl vytvořen, aby řešil neefektivitu modelu dotazování (polling), který aplikace běžně používají ke kontrole změn stavu UE nebo síťových událostí. Před zavedením ENS musela AF periodicky zasílat dotazy (např. přes NEF) do sítě, což spotřebovává signalizační prostředky, zvyšuje latenci pro aplikaci a může způsobit přehlédnutí přechodných událostí mezi jednotlivými dotazy. To je obzvláště problematické pro aplikace řízené událostmi (event-driven), které obsluhují velké skupiny UE, jako jsou služby IoT, vozidlové komunikace nebo immersivní média.

Motivace vychází z vize 5G-Advanced umožňující efektivní nativní edge aplikace a síťovou automatizaci. Existovala jasná potřeba standardizované, síťově asistované notifikační služby, která by ulehčila aplikacím monitorování událostí a poskytovala spolehlivé, včasné aktualizace na principu push. ENS to zajišťuje tím, že využívá přirozenou schopnost sítě sledovat stav a polohu UE. Řeší problém škálovatelného distribuce událostí pro služby založené na skupinách, snižuje redundantní signalizaci a umožňuje nízko latence reaktivní aplikace na síťovém okraji (edge). Jeho zavedení je součástí probíhající evoluce směřující k větší programovatelnosti a servisnímu povědomí 5G sítí, což usnadňuje nové případy užití pro vertikální segmenty.

## Klíčové vlastnosti

- Poskytuje obecnou službu asynchronního doručování notifikací externím aplikačním funkcím (AFs).
- Podporuje odběr (subscription) událostí pro skupinu uživatelských zařízení (UEs) (identifikovaných seznamem, skupinovým ID nebo geografickou oblastí).
- Typy událostí zahrnují dosažitelnost UE, ztrátu připojení, hlášení polohy a selhání komunikace.
- Spolupracuje se síťovými funkcemi (NFs) 5G jádra (jako je NEF, UDM) za účelem získávání síťově spouštěných událostí.
- Doručuje notifikace prostřednictvím HTTP/2 callbacků na URI poskytnuté odběratelskou AF.
- Umožňuje efektivní komunikační model založený na push, čímž odstraňuje potřebu dotazování (polling) ze strany aplikace.

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer

---

📖 **Anglický originál a plná specifikace:** [ENS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ens/)
