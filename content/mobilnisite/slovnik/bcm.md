---
slug: "bcm"
url: "/mobilnisite/slovnik/bcm/"
type: "slovnik"
title: "BCM – Bearer Control Mode"
date: 2025-01-01
abbr: "BCM"
fullName: "Bearer Control Mode"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bcm/"
summary: "Bearer Control Mode (BCM) je síťově řízený mechanismus pro vytváření a správu kontextů Packet Data Protocol (PDP) nebo připojení Packet Data Network (PDN) v systémech 3GPP. Určuje, zda UE nebo síť ini"
---

BCM je síťově řízený mechanismus pro vytváření a správu PDP kontextů nebo PDN připojení, který určuje, zda UE nebo síť iniciuje modifikace přenosových kanálů, aby centralizoval řízení QoS.

## Popis

Bearer Control Mode (BCM) je základní koncept v architektuře paketového jádra 3GPP, konkrétně definovaný v kontextu [GPRS](/mobilnisite/slovnik/gprs/) Tunnelling Protocol ([GTP](/mobilnisite/slovnik/gtp/)) pro rozhraní S5/S8 a S4/S11 a v rámci Evolved Packet Core (EPC) pro rozhraní S5/S8 používající GTPv2. Je to parametr vyjednaný během vytváření [PDP](/mobilnisite/slovnik/pdp/) kontextu v 2G/3G GPRS nebo [PDN](/mobilnisite/slovnik/pdn/) připojení v systémech 4G EPS a 5G. Hodnota BCM určuje, která entita – User Equipment (UE) nebo síť (konkrétně Packet Data Network Gateway, [PGW](/mobilnisite/slovnik/pgw/), v EPS, nebo Gateway GPRS Support Node, GGSN, v GPRS) – je oprávněna iniciovat procedury pro změnu charakteristik přenosového kanálu, jako jsou jeho parametry Quality of Service (QoS). K tomuto vyjednávání dochází v rámci zpráv Create Session Request/Response nebo Activate PDP Context Request/Response.

Architektonicky je BCM atribut řídicí roviny spravovaný rámcem policy and charging control ([PCC](/mobilnisite/slovnik/pcc/)) v síťovém jádře. PGW/GGSN, fungující jako Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)), přijímá autorizovanou QoS od Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)). Nastavení BCM určuje, jak jsou tyto autorizované změny QoS provedeny směrem k UE a přístupové rádiové síti. Když má síť kontrolu (specifická hodnota BCM), může PGW/GGSN proaktivně iniciovat proceduru Bearer Resource Modification pro zvýšení nebo snížení QoS přenosového kanálu na základě rozhodnutí PCRF, požadavků aplikací nebo stavu sítě. To je signalizováno UE přes Mobility Management Entity (MME) nebo Serving GPRS Support Node (SGSN).

Při provozu, pokud je BCM nastaven do režimu 'pouze UE', musí UE jakoukoli změnu QoS požádat prostřednictvím Bearer Resource Modification Request. Síť tento požadavek následně vyhodnotí vůči svým pravidlům. V režimech řízených sítí může PGW/GGSN modifikace spustit samostatně. Tím se centralizují klíčová rozhodnutí o QoS a pravidlech v doméně síťového operátora, což zajišťuje konzistentní uplatňování obchodních pravidel, politik směrování provozu a účtovacích pravidel. Zabrání tak tomu, aby UE svévolně požadovalo prostředky s vysokou QoS, což je klíčové pro prevenci podvodů, správu kongescí a zajištění spravedlivého využití prostředků mezi všemi účastníky.

Role BCM je nedílnou součástí dynamického vynucování pravidel a správy relací. Spolupracuje s parametry jako QoS Class Identifier (QCI), Allocation and Retention Priority (ARP) a dalšími parametry na úrovni přenosového kanálu. Tím, že řídí iniciační bod pro modifikaci přenosového kanálu, umožňuje BCM sofistikované služby řízené sítí, jako jsou sponzorovaná data, zvýšení QoS na vyžádání pro video streaming nebo plynulé přizpůsobení QoS během předávání spojení. Je klíčovým prvkem pro schopnost sítě poskytovat diferencované služby a implementovat pokročilé scénáře PCC definované ve specifikacích 3GPP.

## K čemu slouží

Bearer Control Mode byl vytvořen, aby řešil potřebu síťových operátorů udržovat autoritativní kontrolu nad alokací a modifikací prostředků přenosových kanálů, které jsou přímo spojeny s kvalitou služby (QoS), kapacitou sítě a výnosy. V raných systémech mobilních dat představovalo poskytnutí nekontrolované možnosti UE žádat přenosové kanály s vysokou QoS významná rizika, včetně možného vyčerpání síťových prostředků, QoS podvodů (kdy UE neoprávněně požaduje prémiovou QoS) a problémů při uplatňování konzistentních pravidel a účtování. BCM poskytuje standardizovaný mechanismus pro určení místa kontrolního bodu, čímž tyto provozní a obchodní problémy řeší.

Historicky, jak se služby vyvíjely od jednoduchého best-effort přístupu k internetu k multimediálním a latenci citlivým aplikacím, se stala kritickou potřeba dynamického, na relaci zaměřeného řízení QoS. Zavedení architektury PCC v 3GPP Release 7 formalizovalo oddělení řízení pravidel od správy přenosových kanálů. BCM je logickou součástí této architektury, která zajišťuje, že entita vynucující pravidla (PCEF v PGW/GGSN) má také procedurální pravomoc upravovat přenosové kanály tak, aby odpovídaly těmto pravidlům. To byl významný pokrok oproti statické, předem konfigurované QoS přenosových kanálů.

Vytvoření BCM bylo motivováno omezeními dřívějších, více statických přístupů ke správě přenosových kanálů. Umožňuje síti být proaktivní a inteligentní. Například IMS hovor vyžaduje vyhrazený přenosový kanál se zaručenou přenosovou rychlostí. Při síťově řízeném BCM může PCRF nařídit PCEF, aby tento kanál automaticky vytvořil při zřizování hovoru, aniž by se spoléhalo na žádost UE, což zajišťuje rychlejší a spolehlivější zřízení služby. Síť také umožňuje snížit QoS během přetížení na základě úrovně účastníka nebo typu služby, čímž optimalizuje zážitek pro všechny uživatele.

## Klíčové vlastnosti

- Definuje oprávněnou entitu (UE nebo Síť) pro iniciaci modifikace QoS přenosového kanálu
- Centralizuje vynucování pravidel tím, že umožňuje síťově řízené aktualizace přenosových kanálů
- Zabraňuje neautorizovaným požadavkům na QoS od uživatelského zařízení (UE)
- Umožňuje dynamickou adaptaci služeb na základě rozhodnutí PCRF a spouštěčů z aplikačních funkcí
- Spolupracuje s architekturou Policy and Charging Control (PCC)
- Parametr vyjednaný během aktivace PDP kontextu nebo vytváření PDN připojení

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System

---

📖 **Anglický originál a plná specifikace:** [BCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/bcm/)
