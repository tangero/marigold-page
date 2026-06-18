---
slug: "pbu"
url: "/mobilnisite/slovnik/pbu/"
type: "slovnik"
title: "PBU – Proxy Binding Update"
date: 2025-01-01
abbr: "PBU"
fullName: "Proxy Binding Update"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pbu/"
summary: "Proxy Binding Update (PBU) je klíčová signalizační zpráva v Proxy Mobile IPv6 (PMIPv6), odesílaná Mobile Access Gateway (MAG) k Local Mobility Anchor (LMA). Vytváří nebo aktualizuje vazbu mezi domovsk"
---

PBU je klíčová signalizační zpráva v Proxy Mobile IPv6, odesílaná Mobile Access Gateway k Local Mobility Anchor za účelem vytvoření nebo aktualizace vazby pro mobilní uzel, což umožňuje mobilitu založenou na síti.

## Popis

Proxy Binding Update (PBU) je zpráva řídicí roviny definovaná v protokolu Proxy Mobile IPv6 (PMIPv6), specifikovaném v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 5213 a přijatém 3GPP pro správu mobility založenou na síti. Je to základní zpráva odesílaná z Mobile Access Gateway ([MAG](/mobilnisite/slovnik/mag/)), což je síťová entita obsluhující mobilní uzel ([MN](/mobilnisite/slovnik/mn/)), k Local Mobility Anchor ([LMA](/mobilnisite/slovnik/lma/)), což je domovský agent pro mobilní relaci MN. Zpráva PBU slouží k registraci aktuálního bodu připojení MN a k žádosti o vytvoření nebo aktualizaci záznamu vazby v cache LMA.

Z architektonického hlediska, když se mobilní uzel připojí k doméně PMIPv6 (např. k síti LTE nebo 5G), MAG detekuje toto připojení. MAG, který vystupuje jako proxy za MN, sestaví a odešle zprávu PBU k LMA. Tato zpráva obsahuje klíčové informace, jako je identifikátor MN (např. jeho Network Access Identifier nebo [NAI](/mobilnisite/slovnik/nai/)), domovský síťový prefix(y) přidělený MN, vlastní IP adresa MAG (Proxy-CoA) a požadovaná životnost vazby. MAG tyto informace odvozuje z lokální politiky a autentizační výměny s infrastrukturou [AAA](/mobilnisite/slovnik/aaa/).

Po přijetí platné PBU ji LMA zpracuje, aby vytvořil nebo aktualizoval záznam vazby v cache. Tento záznam mapuje domovský síťový prefix MN na Proxy-CoA (adresu MAG). LMA následně odpoví zprávou Proxy Binding Acknowledgement ([PBA](/mobilnisite/slovnik/pba/)). Pokud je operace úspěšná, LMA také vytvoří obousměrný tunel s MAG. Všechny pakety určené pro domovskou adresu MN jsou směrovány na LMA, který je zapouzdří a přepošle přes tunel k MAG. MAG pakety de-encapsuluje a doručí je MN. Podobně jsou vzestupné pakety od MN odeslány k MAG, který je zapouzdří a pošle je k LMA pro směrování do externí sítě.

Zpráva PBU je spuštěna nejen při počátečním připojení, ale také při předávání spojení (handover) mezi MAG. Když se MN přesune k novému MAG, nový MAG odešle PBU, což způsobí, že LMA aktualizuje vazbu na nový Proxy-CoA. Stará vazba je následně vyčištěna. Tento proces umožňuje plynulou IP mobilitu bez nutnosti, aby se sám MN účastnil jakékoli signalizace mobility – odtud termín 'mobilita založená na síti'. Zprávy PBU jsou zabezpečeny pomocí IPsec bezpečnostních asociací vytvořených mezi MAG a LMA.

## K čemu slouží

Zpráva PBU a protokol PMIPv6 byly vytvořeny, aby poskytly škálovatelné řešení mobility založené na síti, které řeší omezení hostitelsky orientovaných protokolů mobility, jako je Mobile IPv6 (MIPv6). V MIPv6 je samotný mobilní uzel zodpovědný za odesílání aktualizací vazeb svému domovskému agentovi, což může být neefektivní pro zařízení s omezenými zdroji (jako senzory IoT) a přidává složitost softwaru zařízení. PMIPv6, a tím i PBU, přesouvá tuto zodpovědnost na síťovou infrastrukturu.

Řeší problém zajištění plynulé IP mobility pro velký počet zařízení bez nutnosti úprav jejich IP zásobníků. To je zvláště klíčové pro sítě 3GPP, které obsluhují různorodá zařízení od chytrých telefonů po jednoduché M2M moduly. Síť (MAG) detekuje pohyb a spravuje signalizaci mobility transparentně. To operátorům umožňuje spravovat mobilitu jako síťovou službu.

Historická motivace vychází z potřeby efektivního řízení mobility v sítích Evolved Packet Core (EPC) pro LTE a později v 5G Core. V architekturách 3GPP je funkce MAG často umístěna společně s přístupovým uzlem (např. Serving Gateway v EPC) a LMA je umístěno společně s Packet Data Network Gateway (PGW) nebo jeho ekvivalentem. Výměna PBU/PBA je klíčový mechanismus, který umožňuje PGW sledovat obslužnou bránu (Serving Gateway) UE, což umožňuje kontinuitu relace během předávání spojení. Podporuje různé přístupové technologie (3GPP i non-3GPP) pod společným IP kotvícím bodem, což zjednodušuje návrh jádra sítě a umožňuje konvergenci pevných a mobilních sítí.

## Klíčové vlastnosti

- Iniciována sítí (MAG) jménem mobilního uzlu
- Vytváří nebo aktualizuje vazbu mezi domovským prefixem a Proxy-CoA na LMA
- Spouští vytvoření obousměrného tunelu mezi LMA a MAG
- Podporuje předání spojení (handover) tím, že umožňuje aktualizace vazeb od nových MAG
- Přenáší parametry mobilní relace, jako je životnost a domovský síťový prefix
- Zabezpečena pomocí IPsec mezi MAG a LMA

## Související pojmy

- [PMIP – Proxy Mobile Internet Protocol version 6](/mobilnisite/slovnik/pmip/)
- [LMA – Local Mobility Anchor](/mobilnisite/slovnik/lma/)
- [MAG – Mobility Access Gateway](/mobilnisite/slovnik/mag/)

## Definující specifikace

- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 29.275** (Rel-19) — PMIPv6 Mobility & Tunnelling Protocols Stage 3

---

📖 **Anglický originál a plná specifikace:** [PBU na 3GPP Explorer](https://3gpp-explorer.com/glossary/pbu/)
