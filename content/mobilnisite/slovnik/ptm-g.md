---
slug: "ptm-g"
url: "/mobilnisite/slovnik/ptm-g/"
type: "slovnik"
title: "PTM-G – Point to Multipoint – Group Call"
date: 2025-01-01
abbr: "PTM-G"
fullName: "Point to Multipoint – Group Call"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ptm-g/"
summary: "PTM-G je specifický režim služby PTM pro skupinové hlasové nebo datové hovory, umožňující komunikaci mezi předem definovanou skupinou uživatelů. Je klíčový pro služby push-to-talk a komunikace s klíčo"
---

PTM-G je služební režim typu point-to-multipoint pro efektivní skupinové hlasové nebo datové hovory mezi předem definovanou skupinou uživatelů, klíčový pro služby push-to-talk a komunikace s klíčovým významem (mission-critical) v celulárních sítích.

## Popis

Point to Multipoint – Group Call (PTM-G) je služební režim v rámci širšího rámce [PTM](/mobilnisite/slovnik/ptm/), speciálně navržený pro navazování hlasových nebo datových komunikačních relací mezi definovanou skupinou účastníků. Je klíčovou součástí specifikací 3GPP pro služby skupinové komunikace, zejména pro Push-to-talk over Cellular (PoC) a Mission Critical Push-to-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)). Architektura využívá infrastrukturu PTM, ale přidává specifické řídicí mechanismy pro správu skupiny, řízení práva k mluvení (floor control) a dynamické členství ve skupině.

Provozně je relace PTM-G zahájena uživatelem, který požádá o slovo (floor request) pro předem definovanou skupinu. Síť, často s vyhrazeným aplikačním serverem pro skupinové hovory (Group Call application server), žádost ověří, naváže multicastový přenosový kanál pomocí principů PTM a distribuuje média všem aktuálně připojeným a autorizovaným členům skupiny. Radiová síť k doručení médií využívá efektivní multicastové přenosové kanály. Mezi klíčové protokoly patří [SIP](/mobilnisite/slovnik/sip/) pro řízení relace, [RTP](/mobilnisite/slovnik/rtp/) pro přenos médií a specifické protokoly pro řízení práva k mluvení (floor control). [BM-SC](/mobilnisite/slovnik/bm-sc/) nebo vyhrazený Group Communication System Application Server (GCS [AS](/mobilnisite/slovnik/as/)) spravuje členství ve skupině, autorizaci služby a účtování.

Úlohou PTM-G je poskytovat doručování médií skupině s nízkou latencí a současně, což je klíčové pro koordinované činnosti v oblasti veřejné bezpečnosti, dopravy a podnikových prostředí. Zajišťuje, že všichni členové skupiny obdrží stejné informace prakticky ve stejný čas, což podporuje spolupráci v reálném čase. Služba zahrnuje funkce jako dynamické připojování/opouštění skupiny, identifikaci mluvčího a prioritu nouzových hovorů, což z ní činí robustní řešení pro profesionální skupinovou komunikaci.

## K čemu slouží

PTM-G byl vyvinut pro uspokojení poptávky po efektivních, okamžitých službách skupinové komunikace v celulárních sítích, aby konkuroval tradičním systémům obousměrného radiového spojení. Před jeho standardizací byly skupinové hovory v mobilních sítích neefektivní, často simulované prostřednictvím konferenčních můstků využívajících více jednosměrných (unicast) spojů, což spotřebovávalo nadměrné zdroje a zvyšovalo latenci.

Primární problém, který PTM-G řeší, je poskytnutí standardizované, síťově optimalizované metody pro vysílací služby typu jeden-vůči-mnohým (one-to-many) pro hlas a data. Umožňuje komerční služby Push-to-Talk a, což je klíčové, tvoří základ pro služby s klíčovým významem (Mission Critical) standardizované 3GPP pro organizace veřejné bezpečnosti. Tito uživatelé vyžadují spolehlivou, okamžitou skupinovou komunikaci s funkcemi jako vysoká dostupnost, priorita a možnost přerušení.

Využitím základního [PTM](/mobilnisite/slovnik/ptm/) přenosu dosahuje PTM-G ve srovnání s více jednosměrnými (unicast) hovory vyšší spektrální účinnosti a sníženého zatížení sítě. Jeho vznik byl motivován potřebou integrovat schopnosti profesionální mobilní rádiové komunikace (PMR) do hlavního proudu sítí 3GPP, což umožňuje úspory z rozsahu a pokročilé funkce. Řeší omezení dřívějších proprietárních řešení tím, že poskytuje interoperabilní, operátorský standard.

## Klíčové vlastnosti

- Optimalizováno pro skupinovou komunikaci hlasem/daty s nízkou latencí
- Dynamická správa členství ve skupině a autorizace služby
- Mechanismus řízení práva k mluvení (floor control) pro správu práv mluvčího
- Podpora funkcí pro komunikaci s klíčovým významem (mission-critical), jako je priorita a možnost přerušení
- Efektivní využití multicastových rádiových přenosových kanálů pro distribuci médií
- Integrace s IMS pro řízení relací a služebními podpůrnými funkcemi

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description

---

📖 **Anglický originál a plná specifikace:** [PTM-G na 3GPP Explorer](https://3gpp-explorer.com/glossary/ptm-g/)
