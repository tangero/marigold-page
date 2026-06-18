---
slug: "h-pcef"
url: "/mobilnisite/slovnik/h-pcef/"
type: "slovnik"
title: "H-PCEF – Home Policy and Charging Enforcement Function"
date: 2025-01-01
abbr: "H-PCEF"
fullName: "Home Policy and Charging Enforcement Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/h-pcef/"
summary: "Funkce vynucování pravidel a účtování v domovské síti (H-PCEF) je funkce vynucování pravidel a účtování (PCEF) umístěná v domovské veřejné pozemní mobilní síti (HPLMN) účastníka. Je klíčovou součástí"
---

H-PCEF je funkce vynucování pravidel a účtování (Policy and Charging Enforcement Function) v domovské síti účastníka, která vynucuje pravidla kvality služeb (QoS) a účtování, zejména při roamingu, aby zajistila konzistentní službu a fakturaci.

## Popis

Funkce vynucování pravidel a účtování v domovské síti (H-PCEF) je specializovaná instance [PCEF](/mobilnisite/slovnik/pcef/), která funguje v rámci domovské veřejné pozemní mobilní sítě ([HPLMN](/mobilnisite/slovnik/hplmn/)) účastníka. Zavedená ve specifikaci 3GPP Release 7 jako součást architektury řízení pravidel a účtování ([PCC](/mobilnisite/slovnik/pcc/)) nabývá role H-PCEF zvláštního významu v roamingových scénářích, konkrétně v architektuře roamingu s trasováním do domovské sítě (Home Routed). V této architektuře je datový provoz uživatele směrován zpět do HPLMN a H-PCEF je entita, která aplikuje pravidla pro politiky a účtování. Typicky je umístěna společně s nebo je sama uzlem GGSN (Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node) v 3G nebo bránou [PGW](/mobilnisite/slovnik/pgw/) (Packet Data Network Gateway) v 4G/5G v rámci domovské sítě. H-PCEF komunikuje s funkcí [H-PCRF](/mobilnisite/slovnik/h-pcrf/) (Home Policy and Charging Rules Function) přes referenční bod Gx. H-PCRF jí poskytuje PCC pravidla obsahující instrukce pro řízení přenosového kanálu (např. parametry QoS jako garantovaný přenosový výkon), řízení propustnosti (povolování/blokování paketů) a řízení účtování (identifikaci účtovacích klíčů a metod měření). H-PCEF tato pravidla vynucuje v reálném čase na uživatelské rovině provozu. Provádí hlubokou kontrolu paketů (DPI) pro detekci toků služebních dat, aplikuje odpovídající QoS (např. nastavuje hodnoty DiffServ Code Points) a komunikuje s online účtovacím systémem ([OCS](/mobilnisite/slovnik/ocs/)) přes rozhraní Gy pro správu kreditu nebo s offline účtovacím systémem ([OFCS](/mobilnisite/slovnik/ofcs/)) přes rozhraní Gz pro generování záznamů o účtovaných datech (CDR). Když je uživatel v roamingu, může navštívenou síťovou funkci V-PCEF (Visited PCEF) zpracovávat provoz s místním průnikem (local breakout), ale pro provoz směrovaný do domovské sítě je H-PCEF konečným bodem vynucování pravidel, který zajišťuje konzistentní aplikaci služebních a účtovacích politik domovského operátora.

## K čemu slouží

H-PCEF byla vyvinuta proto, aby umožnila operátorům domovských sítí udržovat přímou kontrolu nad kvalitou služeb, účtováním a vynucováním politik pro své účastníky, i když tito účastníci využívají rádiové přístupové sítě roamingových partnerů. Před zavedením PCC a jasnou definicí H-PCEF bylo vynucování politik v roamingových scénářích méně podrobné a často ponecháno na navštívené síti, což mohlo vést k nekonzistentnímu poskytování služeb a složitým zúčtovacím procesům. H-PCEF jako součást modelu roamingu s trasováním do domovské sítě (Home Routed) tento problém řeší tím, že zajišťuje věrné provedení profilu služeb účastníka, definovaného a řízeného v HPLMN. To umožňuje domovskému operátorovi nabízet služby v různých úrovních, implementovat politiky spravedlivého používání a aplikovat přesné účtování na základě vlastních obchodních pravidel bez ohledu na navštívenou síť. Její vznik byl motivován potřebou sofistikovanější diferenciace služeb, růstem využívání mobilních dat a požadavkem na standardizovanou architekturu podporující složitá mezioděratelská zúčtování za datové služby. Tvoří vynucovací páteř pro zpoplatnění datových služeb a zajištění využívání síťových zdrojů v souladu s dohodami s účastníky.

## Klíčové vlastnosti

- Bod vynucování PCC pravidel (QoS, řízení propustnosti, účtování) v HPLMN
- Kritická role v architektuře roamingu s trasováním do domovské sítě (Home Routed) pro datové relace
- Hluboká kontrola paketů (DPI) pro detekci a klasifikaci toků služeb
- Interakce s OCS (Online Charging System) pro řízení kreditu v reálném čase
- Interakce s OFCS (Offline Charging System) pro generování záznamů o účtovaných datech (CDR)
- Vazba na přenosový kanál a vynucování parametrů QoS na uživatelské rovině

## Související pojmy

- [V-PCEF – Visited Policy and Charging Enforcement Function](/mobilnisite/slovnik/v-pcef/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)

## Definující specifikace

- **TS 23.203** (Rel-19) — Policy and charging control architecture

---

📖 **Anglický originál a plná specifikace:** [H-PCEF na 3GPP Explorer](https://3gpp-explorer.com/glossary/h-pcef/)
