---
slug: "seid"
url: "/mobilnisite/slovnik/seid/"
type: "slovnik"
title: "SEID – Session Endpoint Identifier"
date: 2025-01-01
abbr: "SEID"
fullName: "Session Endpoint Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/seid/"
summary: "Jedinečný identifikátor používaný v Packet Forwarding Control Protocol (PFCP) mezi řídicí a uživatelskou rovinou v 5G Core. Identifikuje konkrétní PFCP relaci, která odpovídá PDU relaci uživatele nebo"
---

SEID je jedinečný identifikátor PFCP relace používaný mezi řídicí a uživatelskou rovinou v 5G Core pro asociaci řídicích zpráv s konkrétní PDU relací uživatele nebo kontextem přenosu provozu.

## Popis

Session Endpoint Identifier (SEID) je základním parametrem v Packet Forwarding Control Protocol ([PFCP](/mobilnisite/slovnik/pfcp/)), což je protokol používaný pro komunikaci mezi řídicí a uživatelskou rovinou v síti 3GPP 5G Core (5GC) a v rozšířeném EPC. Konkrétně PFCP funguje mezi Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5GC a mezi Control Plane [PGW](/mobilnisite/slovnik/pgw/) ([PGW-C](/mobilnisite/slovnik/pgw-c/)) a User Plane PGW ([PGW-U](/mobilnisite/slovnik/pgw-u/)) v EPC. SEID je 64bitové celé číslo bez znaménka, které jednoznačně identifikuje PFCP relaci na konkrétním uzlu (buď uzlu řídicí roviny, nebo uzlu uživatelské roviny).

PFCP relace je zřízena pro správu pravidel přenosu uživatelské roviny pro datovou relaci uživatele, známou jako [PDU](/mobilnisite/slovnik/pdu/) relace v 5G. Když SMF potřebuje instruovat UPF, jak zacházet s provozem uživatele (např. které QoS toky mapovat na které tunely, jaké politiky uplatnit), zahájí PFCP Session Establishment Request. Tato žádost obsahuje lokální SEID SMF pro tuto relaci. UPF po přijetí vytvoří svůj vlastní lokální kontext relace a odpoví svým vlastním SEID. Následně všechny PFCP zprávy související s touto relací (modifikace, odstranění, hlášení) musí obsahovat jak SEID odesílatele, tak tam, kde je to relevantní, SEID protistrany. Tím vzniká obousměrná asociace.

SEID funguje ve spojení s [F-SEID](/mobilnisite/slovnik/f-seid/) (Fully Qualified SEID), který zahrnuje jak hodnotu SEID, tak IP adresu uzlu, který jej přidělil. To umožňuje jednoznačnou identifikaci v sítích s více uzly. SEID je lokálně významný pro uzel, který jej přiděluje, což znamená, že stejnou číselnou hodnotu mohou různé SMF nebo UPF používat pro různé relace bez konfliktu. Protokol tyto identifikátory používá ke korelaci požadavků a odpovědí a k efektivní správě stavu potenciálně milionů simultánních uživatelských relací.

Architektonicky je SEID klíčovým prvkem umožňujícím separaci řídicí a uživatelské roviny (CUPS) a architekturu založenou na službách v 5GC. Umožňuje bezestavovým řídicím funkcím (jako je SMF) spravovat stavové uživatelské funkce (UPF), aniž by musely samy uchovávat podrobný stav přeposílání paketů. SEID poskytuje úchop, pomocí kterého může SMF vzdáleně programovat přenosové cesty UPF, vynucování QoS, účtování a funkce hlášení provozu pro každou jednotlivou uživatelskou relaci.

## K čemu slouží

SEID byl vytvořen k uspokojení potřeby škálovatelného a efektivního identifikátoru relace v protokolu řídícím architekturu separované řídicí a uživatelské roviny (CUPS). Před zavedením CUPS, v monolitických branách jako SGSN nebo GGSN, byl stav relace spravován interně v rámci jediného uzlu. Se separací zavedenou v EPC a plně realizovanou v 5GC byl potřebný standardizovaný protokol (PFCP), aby řídicí entita mohla vzdáleně spravovat entitu uživatelské roviny. Tento protokol vyžadoval způsob, jak jednoznačně odkazovat na každý kontext relace na obou koncích.

Problém, který řeší, je jednoznačná korelace řídicích zpráv se správným stavem uživatelské relace na uzlu uživatelské roviny. Bez jedinečného identifikátoru relace, jako je SEID, by UPF neměl efektivní způsob, jak rozlišit, na kterou sadu pravidel detekce paketů (PDR), pravidel přenosových akcí (FAR) a pravidel vynucování QoS (QER) se daná PFCP zpráva vztahuje, zejména při zpracování provozu pro miliony současných uživatelů. SEID poskytuje tento přímý vyhledávací klíč.

Historicky byl SEID zaveden s protokolem PFCP v 3GPP Release 14 jako součást architektury CUPS pro EPC. Ještě kritičtější se stal v Release 15 s 5G Core, kde architektura založená na službách a dekompozice síťových funkcí učinily dynamické, relaci specifické řízení uživatelské roviny ústředním principem návrhu. SEID je základním prvkem, který umožňuje flexibilitu, škálovatelnost a možnosti síťového řezání moderních 5G sítí tím, že poskytuje jednoduchý, ale výkonný úchop pro správu relací napříč distribuovanými síťovými funkcemi.

## Klíčové vlastnosti

- 64bitový lokálně jedinečný identifikátor pro PFCP relaci
- Přidělen nezávisle každým uzlem (řídicí rovinou a uživatelskou rovinou)
- Obsažen ve všech PFCP zprávách souvisejících s relací pro korelaci
- Součást F-SEID pro globální jedinečnost v celé síti
- Umožňuje škálovatelnou správu stavu při separaci řídicí a uživatelské roviny
- Základní pro správu PDU relací v 5G Core

## Související pojmy

- [PFCP – Packet Forwarding Control Protocol](/mobilnisite/slovnik/pfcp/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation

---

📖 **Anglický originál a plná specifikace:** [SEID na 3GPP Explorer](https://3gpp-explorer.com/glossary/seid/)
