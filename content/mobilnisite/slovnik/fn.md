---
slug: "fn"
url: "/mobilnisite/slovnik/fn/"
type: "slovnik"
title: "FN – Fixed Network"
date: 2025-01-01
abbr: "FN"
fullName: "Fixed Network"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fn/"
summary: "Pevná síť (Fixed Network, FN) označuje nemobilní, pevnou telekomunikační infrastrukturu v ekosystému 3GPP. Zahrnuje páteřní a přístupové sítě poskytující služby jako širokopásmový přístup, PSTN a kabe"
---

FN je nemobilní, pevná telekomunikační infrastruktura v ekosystému 3GPP, zahrnující páteřní a přístupové sítě poskytující služby jako širokopásmový přístup a PSTN.

## Popis

Pevná síť (Fixed Network, FN) v kontextu 3GPP je architektonická a funkční doména představující tradiční pevnou telekomunikační infrastrukturu. Nejde o jedinou síť, ale o konceptuální seskupení zahrnující různé technologie pevného přístupu (jako [DSL](/mobilnisite/slovnik/dsl/), optická vlákna a kabel), přenosové sítě a prvky páteřní sítě, jako jsou ústředny pro pevné linky a brány širokopásmových sítí ([BNG](/mobilnisite/slovnik/bng/)). FN tvoří základ pro služby, jako je rezidenční širokopásmový internet, hlas přes IP (VoIP) a IP televize ([IPTV](/mobilnisite/slovnik/iptv/)). Její začlenění do specifikací 3GPP, počínaje Release 99, uznává potřebu standardů usnadňujících vzájemnou spolupráci a konvergenci mezi mobilními sítěmi (jako UMTS a později LTE/5G) a těmito zavedenými pevnými sítěmi.

Architektonicky FN rozhraní s mobilní páteřní sítí prostřednictvím definovaných referenčních bodů. Specifikace jako TS 25.423 a TS 25.931 detailně popisují rozhraní Iu-Flex a Iur-F pro připojení řadičů rádiové sítě (RNC) v UMTS k uzlům páteřní sítě, s ohledem na scénáře, kde mohou být tyto uzly obsluhovány pevnými přenosovými sítěmi. FN poskytuje spolehlivou, vysokokapacitní přenosovou a backhaulovou konektivitu nezbytnou pro mobilní provoz, zejména s rostoucími požadavky na data. Funguje jako 'potrubí' spojující lokality rádiové přístupové sítě (Node B, eNodeB, gNB) s prvky páteřní sítě, jako jsou [MSC](/mobilnisite/slovnik/msc/), SGSN a později [MME](/mobilnisite/slovnik/mme/)/[AMF](/mobilnisite/slovnik/amf/).

Její role se vyvinula od samostatného přenosového média k integrální součásti celkové architektury poskytování služeb. V kontextech správy (definovaných v TS 32.833) je FN považována za spravovanou doménu s vlastními požadavky na správu výkonu a poruch, oddělenou od, ale koordinovanou se správou mobilní sítě. Důležitost FN spočívá v její kapacitě a všudypřítomnosti; často tvoří ekonomickou páteř pro přenos mobilního provozu, zejména v hustě obydlených městských oblastech a na místech agregace sítě. Tento koncept je základem konvergence pevných a mobilních sítí ([FMC](/mobilnisite/slovnik/fmc/)), kde jsou služby poskytovány bezproblémově napříč oběma typy sítí.

## K čemu slouží

Koncept FN byl do 3GPP zaveden, aby formálně uznal a standardizoval interakci mezi vznikajícími mobilními sítěmi 3. generace a všudypřítomnou stávající pevnou telekomunikační infrastrukturou. Před prací 3GPP se mobilní a pevné sítě často vyvíjely nezávisle s proprietárními nebo ad-hoc řešeními vzájemné spolupráce. Hlavním řešeným problémem byla potřeba efektivního, standardizovaného přenosu a propojení. Mobilní sítě, zejména při přechodu na paketově orientované architektury s UMTS, vyžadovaly vysokokapacitní, spolehlivé backhaulové spoje pro připojení základnových stanic k řadičům a bránám páteřní sítě – roli, kterou přirozeně plní pevné sítě (např. pronajaté okruhy, optická vlákna, [DSL](/mobilnisite/slovnik/dsl/)).

Dalším klíčovým motivem bylo umožnění konvergence pevných a mobilních sítí na síťové úrovni. Definováním FN jako domény v rámci systémové architektury 3GPP se umožnilo specifikovat společné postupy správy (poruchy, konfigurace, účtování, výkon, zabezpečení - FCAPS), mapování kvality služeb (QoS) napříč doménami a bezproblémovou kontinuitu služeb. To bylo klíčové pro operátory vlastnící jak pevné, tak mobilní sítě, což jim umožnilo optimalizovat infrastrukturu a nabízet balíčkované služby. Zařazení v Release 99 připravilo půdu pro pozdější inovace, jako je IP Multimedia Subsystem (IMS), který je nezávislý na přístupu a spoléhá se na pevnou i mobilní IP konektivitu pro poskytování multimediálních služeb.

## Klíčové vlastnosti

- Poskytuje standardizovaný přenos a backhaul pro uzly RAN 3G/4G/5G k páteřní síti
- Umožňuje konvergenci pevných a mobilních sítí (FMC) na architektonické a správní úrovni
- Definuje rozhraní (např. Iu, Iur přes pevný přenos) pro propojení s mobilní páteřní sítí
- Zahrnuje definice domén správy pro integrovanou správu, údržbu a provoz (OAM) kombinovaných sítí
- Podporuje mapování QoS a vynucování politik napříč pevnými a mobilními doménami
- Slouží jako základ pro širokopásmový rezidenční přístup v konvergovaných scénářích

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 32.833** (Rel-11) — Converged OSS End-to-End Management Study

---

📖 **Anglický originál a plná specifikace:** [FN na 3GPP Explorer](https://3gpp-explorer.com/glossary/fn/)
