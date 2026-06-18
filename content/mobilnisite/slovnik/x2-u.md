---
slug: "x2-u"
url: "/mobilnisite/slovnik/x2-u/"
type: "slovnik"
title: "X2-U – X2-User Plane"
date: 2025-01-01
abbr: "X2-U"
fullName: "X2-User Plane"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/x2-u/"
summary: "Uživatelská rovina rozhraní mezi eNodeB v LTE a 5G NR, používaná k přeposílání paketů uživatelských dat během předávání spojení mezi základnovými stanicemi. Vytváří GTP-U tunely, aby bylo zajištěno, ž"
---

X2-U je uživatelská rovina rozhraní mezi základnovými stanicemi v LTE a 5G NR, které přeposílá uživatelská data prostřednictvím GTP-U tunelů během předávání spojení, aby umožnilo plynulou mobilitu.

## Popis

Rozhraní X2-U je protějškem na uživatelské rovině k rozhraní [X2-C](/mobilnisite/slovnik/x2-c/) a tvoří cestu pro přeposílání dat mezi dvěma eNodeB (nebo gNB v 5G NR) v architektuře LTE/5G RAN. Jeho primární a nejkritičtější úlohou je podpora přeposílání dat během předávání spojení mezi eNodeB. Když se UE pohybuje ze zdrojové buňky do cílové buňky, mohou být pakety dat směrované směrem k UE (downlink) již na cestě nebo uložené ve frontě ve zdrojovém eNodeB. Rozhraní X2-U poskytuje přímý tunel pro přeposlání těchto paketů ze zdrojového do cílového eNodeB, čímž zabraňuje ztrátě paketů a zajišťuje kontinuitu služby.

Technicky rozhraní X2-U používá pro uživatelskou rovinu protokol [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol ([GTP-U](/mobilnisite/slovnik/gtp-u/)) nad transportní vrstvou [UDP](/mobilnisite/slovnik/udp/)/IP. Během předávání spojení zdrojový eNodeB zřídí jeden nebo více GTP-U tunelů k cílovému eNodeB. Každý tunel odpovídá jednomu EPS přenosovému kanálu (nebo [DRB](/mobilnisite/slovnik/drb/) v 5G). Zdrojový eNodeB přeposílá všechny downlink pakety, které ještě nepřenesl na UE, stejně jako všechny nové pakety, které přijímá od Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)), prostřednictvím těchto tunelů. Cílový eNodeB tyto přeposlané pakety ukládá do fronty a doručí je UE, jakmile je předání spojení dokončeno a je navázáno nové rádiové spojení. Tento proces je často označován jako "bezztrátové" nebo "plynulé" předání spojení pro určité přenosové kanály se zaručenou přenosovou rychlostí.

Provoz X2-U je úzce řízen signalizací X2-C. Zpráva X2AP Handover Preparation obsahuje nezbytné informace pro cílový eNodeB, aby mohl nastavit koncové body GTP-U tunelů ([TEID](/mobilnisite/slovnik/teid/)). Zdrojový eNodeB začíná přeposílat data, jakmile odešle cílovému eNodeB zprávu [SN](/mobilnisite/slovnik/sn/) Status Transfer, která synchronizuje čísla sekvencí PDCP. Přeposílání pokračuje, dokud není dokončeno přepnutí cesty v jádru sítě a SGW nezačne odesílat downlink data přímo cílovému eNodeB. Zatímco jeho nejvýznamnější použití je během předávání spojení, rozhraní X2-U může být také využito ve scénářích duální konektivity pro rozdělení toků dat uživatelské roviny mezi hlavním a sekundárním uzlem. Rozhraní je navrženo pro vysokou propustnost a nízkou latenci, aby se minimalizoval čas přerušení během předávání spojení, což je klíčový ukazatel výkonu mobilních sítí.

## K čemu slouží

Rozhraní X2-U bylo vytvořeno, aby vyřešilo zásadní problém ztráty dat a přerušení služby během předávání spojení v paketově orientované mobilní síti. V před-LTE systémech 3G bylo přeposílání dat během předávání spojení řízeno RNC. S plochou architekturou LTE, která RNC eliminovala, bylo třeba tuto funkci distribuovat na eNodeB. Bez přímého spoje na uživatelské rovině, jako je X2-U, by musela být všechna uživatelská data směrována přes jádro sítě (SGW), což by drasticky zvýšilo latenci předávání spojení a riziko ztráty paketů, pokud by se stará cesta zrušila dříve, než by byla nová připravena.

X2-U umožňuje schopnost typu "nejdřív vytvoř, potom zruš" pro uživatelskou rovinu. Umožňuje zdrojovému eNodeB pokračovat v příjmu dat z jádra a současně je přeposílat cílovému eNodeB, čímž vytváří dočasný přímý most. To zajišťuje, že data na cestě nejsou ztracena a že UE zažívá minimální přerušení, což je zásadní pro aplikace v reálném čase, jako je hlas a video. Motivací bylo dosáhnout doby přerušení při předání spojení pod 50 ms, což je požadavek pro podporu VoIP a dalších služeb citlivých na latenci v LTE. Díky lokalizaci cesty pro přeposílání dat na okraji RAN snižuje X2-U zatížení přenosu v jádru sítě a umožňuje rychlejší a spolehlivější mobilitu, což je jeden ze základních kamenů uživatelského zážitku v LTE a 5G.

## Klíčové vlastnosti

- Poskytuje tunely založené na GTP-U pro přeposílání uživatelských dat během předávání spojení
- Zabraňuje ztrátě paketů a zajišťuje kontinuitu služby pro aktivní UE
- Funguje pod řízením signalizace X2-C (procedury X2AP)
- Používá pro transport UDP/IP, optimalizováno pro vysokorychlostní přenos dat
- Podporuje simultánní přeposílání pro více přenosových kanálů (EPS bearers/DRB)
- Umožňuje přepínání datových cest s nízkou latencí na lokalizované úrovni, nezávisle na jádru sítě

## Související pojmy

- [X2-C – X2-Control Plane](/mobilnisite/slovnik/x2-c/)
- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)
- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services

---

📖 **Anglický originál a plná specifikace:** [X2-U na 3GPP Explorer](https://3gpp-explorer.com/glossary/x2-u/)
