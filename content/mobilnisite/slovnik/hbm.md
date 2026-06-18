---
slug: "hbm"
url: "/mobilnisite/slovnik/hbm/"
type: "slovnik"
title: "HBM – Host Based Mobility"
date: 2025-01-01
abbr: "HBM"
fullName: "Host Based Mobility"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hbm/"
summary: "Síťový protokol pro správu mobility, v němž signalizaci mobility a správu IP adres zajišťuje kotva mobility v síti, nikoli samotné mobilní zařízení. Zařízení používá stabilní domácí adresu (HoA), zatí"
---

HBM je síťový mobilní protokol, v němž síťová kotva spravuje signalizaci a IP adresy, což hostitelskému zařízení umožňuje používat stabilní domácí adresu, zatímco síť zajišťuje směrování prostřednictvím dočasné adresy.

## Popis

Host Based Mobility (HBM) je základní paradigma správy mobility definované v architektuře 3GPP Evolved Packet Core (EPC), konkrétně pro ne-3GPP přístupové sítě jako Wi-Fi. V HBM jsou inteligence a signalizace potřebné pro udržení kontinuity IP relace při pohybu uživatelského zařízení (UE) primárně umístěny v síťové infrastruktuře, nikoli na samotném UE. Klíčovou síťovou entitou umožňující HBM je Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v EPC, která funguje jako kotva mobility a domácí agent ([HA](/mobilnisite/slovnik/ha/)). UE je přidělena stabilní, trvalá IP adresa známá jako domácí adresa (HoA) z jeho domovské sítě. Když se UE připojí prostřednictvím ne-3GPP přístupové sítě (např. důvěryhodné [WLAN](/mobilnisite/slovnik/wlan/)), síť mu přidělí lokální topologicky správnou IP adresu zvanou dočasná adresa (CoA).

Hlavním protokolem implementujícím HBM pro propojení s 3GPP je Proxy Mobile IPv6 (PMIPv6), specifikovaný v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 5213 a přijatý 3GPP. V PMIPv6 je správa mobility zprostředkována síťovými entitami zvanými Mobile Access Gateway ([MAG](/mobilnisite/slovnik/mag/)) a Local Mobility Anchor ([LMA](/mobilnisite/slovnik/lma/)). V kontextu 3GPP se funkce MAG nachází v Trusted WLAN Access Gateway ([TWAG](/mobilnisite/slovnik/twag/)) pro důvěryhodný WLAN přístup a funkce LMA sídlí v PGW. MAG detekuje připojení a pohyb UE a jménem UE zaregistruje jeho CoA u LMA. LMA pak udržuje vazbu mezi HoA UE (nebo jeho síťovou předponou) a jeho aktuální CoA. Všechny datové pakety určené pro HoA UE jsou zachyceny LMA, zapouzdřeny v IP-in-IP tunelu (s použitím CoA jako cílové adresy) a přeposlány na MAG, který je dekapuluje a doručí UE. Vzestupný provoz z UE je typicky směrován přímo nebo přes MAG na LMA.

Tato architektura zcela odstíní UE od signalizace mobility. UE není vyžadováno, aby implementovalo mobilního klienta; jednoduše používá svou HoA jako svou IP adresu a síť zajišťuje, že tato adresa zůstává dosažitelná bez ohledu na změny bodu připojení v rámci důvěryhodné ne-3GPP domény. HBM prostřednictvím PMIPv6 je klíčovým prvkem pro bezproblémovou mobilitu a přesměrování provozu mezi 3GPP (LTE) a důvěryhodnými ne-3GPP přístupy, tvoří část referenčních bodů S2a a S2b v EPC. Poskytuje síťově řízenou mobilitu s nižší složitostí a spotřebou energie na UE ve srovnání s řešeními založenými na klientovi, jako je Dual-Stack MIPv6 (DSMIPv6).

## K čemu slouží

HBM byl vyvinut, aby poskytoval bezproblémovou správu IP mobility pro zařízení, kterým může chybět sofistikovaný software mobilního klienta, nebo kde je prioritou optimalizace životnosti baterie a složitosti UE. Protokoly mobility založené na klientovi, jako je MIPv6, vyžadují aktivní účast UE na signalizaci – detekci pohybu, získání CoA a odesílání aktualizací vazby svému domácímu agentovi. To zvyšuje režii zpracování, spotřebu energie a implementační složitost UE, což je nežádoucí pro jednoduchá IoT zařízení nebo masově rozšířené mobilní telefony.

3GPP přijalo HBM, konkrétně PMIPv6, aby umožnilo integraci ne-3GPP přístupových sítí (primárně WLAN) do EPC způsobem, který je pro UE transparentní. Hlavní problém, který řeší, je poskytnutí kontinuity relace a konzistentní aplikace politik pro UE pohybující se mezi LTE a důvěryhodnou WLAN bez nutnosti změn v IP zásobníku UE. Síťový operátor má plnou kontrolu nad procesem mobility a přidělováním IP adres, což umožňuje centralizovanou aplikaci politik, účtování a kvality služeb (QoS). Tento přístup usnadnil propojení 3GPP-WLAN (IFOM, MAPCON) a pozdější funkce směrování, přepínání a rozdělování přístupového provozu (ATSSS) definované v pozdějších vydáních.

## Klíčové vlastnosti

- Signalizace mobility založená na síti (Proxy Mobile IPv6)
- UE používá stabilní domácí adresu (HoA) přidělenou síťovou kotvou (PGW/LMA)
- Mobilita je pro UE transparentní; není vyžadován žádný mobilní klient
- Mobilita je spravována zprostředkujícími entitami: Mobile Access Gateway (MAG) a Local Mobility Anchor (LMA)
- Podporuje bezproblémový přechod mezi 3GPP a důvěryhodnými ne-3GPP přístupy (např. WLAN)
- Umožňuje síťově řízené uplatňování politik a účtování pro ne-3GPP přístup

## Definující specifikace

- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO

---

📖 **Anglický originál a plná specifikace:** [HBM na 3GPP Explorer](https://3gpp-explorer.com/glossary/hbm/)
