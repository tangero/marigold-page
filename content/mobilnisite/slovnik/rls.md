---
slug: "rls"
url: "/mobilnisite/slovnik/rls/"
type: "slovnik"
title: "RLS – Radio Location Service"
date: 2025-01-01
abbr: "RLS"
fullName: "Radio Location Service"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rls/"
summary: "Služba určující geografickou polohu mobilního zařízení pomocí měření v rádiové síti. Je klíčová pro tísňové služby (E911/E112), služby založené na poloze a optimalizaci sítě, což operátorům umožňuje p"
---

RLS je služba, která určuje geografickou polohu mobilního zařízení pomocí měření v rádiové síti.

## Popis

Radio Location Service (RLS) je standardizovaná sada funkcí v sítích 3GPP navržená k určení geografické polohy uživatelského zařízení (UE). Funguje na základě využití měření z rádiové přístupové sítě, která mohou zahrnovat časová měření (jako Round Trip Time nebo Observed Time Difference of Arrival), měření síly signálu a data o úhlu příchodu signálu. Architektura zahrnuje síťové prvky, jako je Serving Mobile Location Center ([SMLC](/mobilnisite/slovnik/smlc/)) v GSM/[WCDMA](/mobilnisite/slovnik/wcdma/) nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) a Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5GC, které koordinují s základnovými stanicemi (NodeBs, eNBs, gNBs) sběr potřebných rádiových dat. Samotné UE se může na lokalizačním procesu také podílet, například měřením sousedních buněk nebo využitím vlastních schopností globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)), přičemž síť tato data asistuje nebo vyžaduje.

Určení polohy může probíhat několika metodami, které se obecně dělí na síťové, UE-bázi nebo hybridní. U síťových metod provádí měření a výpočty síťová infrastruktura bez nutnosti speciálních schopností ze strany UE. UE-bázi metody spoléhají na UE (často s integrovaným GNSS), aby vypočítalo svou vlastní polohu, případně s pomocí asistenčních dat ze sítě pro zlepšení rychlosti a přesnosti. Hybridní metody kombinují měření ze sítě i z UE. Vypočtený odhad polohy je poté doručen klientské aplikaci, kterou může být síť tísňových služeb (pro volání E911/E112), poskytovatel komerčních služeb založených na poloze nebo vlastní systémy síťového operátora pro funkce jako detekce podvodů nebo analýza provozu.

RLS je integrována do servisní architektury jádra sítě prostřednictvím standardizovaných rozhraní. V systémech 5G komunikuje LMF s gNB pomocí protokolu NRPPa přes rozhraní [NG](/mobilnisite/slovnik/ng/) a s UE pomocí LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) přenášeného v [NAS](/mobilnisite/slovnik/nas/) signalizaci. To umožňuje přesnou koordinaci napříč doménami rádiové sítě a jádra sítě. Služba podporuje více parametrů Quality of Service (QoS), včetně přesnosti, doby odezvy (latence) a spolehlivosti, které lze přizpůsobit potřebám vyžadující aplikace. Její role je klíčová nejen pro služby pro koncové uživatele, ale také pro správu sítě, což operátorům umožňuje porozumět distribuci uživatelů, plánovat nasazení buněk a optimalizovat přidělování rádiových zdrojů na základě dat o poloze v reálném čase.

## K čemu slouží

RLS byla vytvořena za účelem splnění přísných regulatorních požadavků, primárně pro lokalizaci tísňových volajících. Vlády po celém světě, počínaje požadavky FCC na E911 ve Spojených státech, nařídily, že operátoři mobilních sítí musí být schopni poskytnout polohu volajícího, který uskuteční tísňové volání. To byl zásadní posun od pevné telefonie, kde byla adresa známá, k mobilní telefonii, kde se volající mohl nacházet kdekoli. 3GPP standardizovala RLS, aby poskytla konzistentní, interoperabilní metodu pro všechny buněčné technologie (GSM, UMTS, LTE, NR) k naplnění těchto zákonných povinností.

Mimo tísňové služby vytvořila proliferace chytrých telefonů a mobilních dat masivní trh pro komerční služby založené na poloze (LBS). Aplikace pro navigaci, místní vyhledávání, sociální sítě a cílenou reklamu všechny vyžadují spolehlivou lokalizaci zařízení. RLS poskytuje síťovou infrastrukturu pro podporu těchto služeb, zejména ve scénářích, kde je satelitní GPS/GNSS nedostupná (např. uvnitř budov, v městských kaňonech). Řeší problém poskytnutí všudypřítomné, vždy dostupné lokalizační schopnosti, která doplňuje, ale není výhradně závislá na GNSS integrovaném v UE.

Z pohledu síťového operátora řeší RLS také provozní a optimalizační výzvy. Znalost míst, kde jsou uživatelé koncentrováni, umožňuje lepší plánování rádiové sítě, správu kapacity a optimalizaci předávání hovorů. Lze ji také využít pro zákonné odposlechy, detekci podvodů (identifikace neobvyklých vzorců polohy) a poskytování služeb s přidanou hodnotou podnikovým zákazníkům. RLS se tak vyvinula z nástroje pro regulatorní shodu v klíčovou síťovou službu umožňující bezpečnost, komerční inovace a provozní inteligenci.

## Klíčové vlastnosti

- Podpora více lokalizačních metod (např. OTDOA, E-CID, A-GNSS, UTDOA)
- Architektonická podpora pro síťové, UE-bázi a UE-asistované/hybridní režimy
- Standardizované protokoly jako LPP (LTE Positioning Protocol) a NRPPa (NG-RAN Positioning Protocol A)
- Parametry Quality of Service (QoS) pro přesnost polohy, dobu odezvy a spolehlivost
- Integrace s frameworky tísňových služeb (např. E911, E112)
- Spolupráce napříč generacemi 3GPP (GSM, UMTS, LTE, 5G NR) a s nepřístupem 3GPP

## Související pojmy

- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.841** (Rel-6) — Presence Service IP Multimedia Subsystem
- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 38.807** (Rel-16) — NR beyond 52.6 GHz Study

---

📖 **Anglický originál a plná specifikace:** [RLS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rls/)
